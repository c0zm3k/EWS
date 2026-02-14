import os
import pandas as pd
import joblib
from flask import Flask, render_template, request, redirect, url_for, send_from_directory
import numpy as np

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'e:/EWS/data/uploads'
app.config['STATIC_DATA_FOLDER'] = 'e:/EWS/data/static'
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

# Load models and features
LR_MODEL = joblib.load('e:/EWS/models/logistic_regression.pkl')
DT_MODEL = joblib.load('e:/EWS/models/decision_tree.pkl')
FEATURES = joblib.load('e:/EWS/models/features.pkl')

def generate_explanation(row):
    reasons = []
    if row['Attendance'] < 75:
        reasons.append("Low attendance (< 75%)")
    if row['Midterm_Score'] < 50:
        reasons.append("Poor midterm performance")
    if row['Previous_CGPA'] < 2.5:
        reasons.append("Weak academic background")
    
    if not reasons:
        return "Combined marginal factors"
    return "Check: " + " & ".join(reasons)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/download_demo')
def download_demo():
    return send_from_directory(app.config['STATIC_DATA_FOLDER'], 'demo_students.xlsx', as_attachment=True)

@app.route('/predict', methods=['POST'])
def predict():
    if 'file' not in request.files:
        return redirect(request.url)
    
    file = request.files['file']
    if file.filename == '':
        return redirect(request.url)

    if file:
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(filepath)
        
        # Process CSV or Excel
        if filepath.endswith('.csv'):
            df = pd.read_csv(filepath)
        elif filepath.endswith(('.xls', '.xlsx')):
            df = pd.read_excel(filepath)
        else:
            return "Unsupported file format", 400
        
        # Ensure Student_ID exists or generate it
        if 'Student_ID' not in df.columns:
            df['Student_ID'] = [f'AUTO_{i}' for i in range(len(df))]
        
        # Select features for prediction
        X = df[FEATURES]
        
        # Predictions (using LR for probabilities, DT for show)
        # Handle cases where model might error due to data types
        try:
            probs = LR_MODEL.predict_proba(X)[:, 0] # Probability of Class 0 (At Risk)
            preds = LR_MODEL.predict(X)
        except Exception as e:
            return f"Error during prediction: {str(e)}", 500
        
        df['Probability'] = probs
        df['Status'] = preds
        df['Explanation'] = df.apply(generate_explanation, axis=1)
        
        results = df.to_dict('records')
        
        # Summary stats
        at_risk_count = int(np.sum(preds == 0))
        safe_count = int(np.sum(preds == 1))
        
        summary = {
            'total': len(df),
            'at_risk': at_risk_count,
            'safe': safe_count,
            'chart_data': {
                'at_risk': at_risk_count,
                'safe': safe_count
            }
        }
        
        return render_template('dashboard.html', results=results, summary=summary)

if __name__ == '__main__':
    app.run(debug=True, port=3300)
