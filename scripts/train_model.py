import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, classification_report
import joblib
import os

def train_models():
    # Load data
    data_path = 'e:/EWS/data/students.csv'
    if not os.path.exists(data_path):
        print("Data file not found. Run generate_data.py first.")
        return

    df = pd.read_csv(data_path)
    
    # Features and Target
    X = df[['Attendance', 'Midterm_Score', 'Assignment_Score', 'Previous_CGPA', 'Participation_Score']]
    y = df['Status']
    
    # Split data
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # 1. Logistic Regression
    lr_model = LogisticRegression()
    lr_model.fit(X_train, y_train)
    y_pred_lr = lr_model.predict(X_test)
    
    print("--- Logistic Regression Performance ---")
    print(f"Accuracy: {accuracy_score(y_test, y_pred_lr):.2f}")
    print(classification_report(y_test, y_pred_lr))
    
    # 2. Decision Tree
    dt_model = DecisionTreeClassifier(max_depth=5, random_state=42)
    dt_model.fit(X_train, y_train)
    y_pred_dt = dt_model.predict(X_test)
    
    print("\n--- Decision Tree Performance ---")
    print(f"Accuracy: {accuracy_score(y_test, y_pred_dt):.2f}")
    print(classification_report(y_test, y_pred_dt))
    
    # Save models
    os.makedirs('e:/EWS/models', exist_ok=True)
    joblib.dump(lr_model, 'e:/EWS/models/logistic_regression.pkl')
    joblib.dump(dt_model, 'e:/EWS/models/decision_tree.pkl')
    
    # Save feature names for reference in web app
    joblib.dump(X.columns.tolist(), 'e:/EWS/models/features.pkl')
    
    print("\nModels saved to e:/EWS/models/")

if __name__ == "__main__":
    train_models()
