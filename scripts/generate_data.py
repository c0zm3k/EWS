import pandas as pd
import numpy as np
import os

def generate_student_data(num_students=500):
    np.random.seed(42)
    
    data = {
        'Student_ID': [f'STU{i:03d}' for i in range(1, num_students + 1)],
        'Attendance': np.random.randint(40, 100, size=num_students),
        'Midterm_Score': np.random.randint(20, 100, size=num_students),
        'Assignment_Score': np.random.randint(30, 100, size=num_students),
        'Previous_CGPA': np.round(np.random.uniform(2.0, 4.0, size=num_students), 2),
        'Participation_Score': np.random.randint(0, 10, size=num_students)
    }
    
    df = pd.DataFrame(data)
    
    # Define "Pass/Fail" logic (Status)
    # A student is at risk (0) if they have low attendance AND low midterm scores, or very low CGPA
    def determine_status(row):
        score = (row['Attendance'] * 0.3 + 
                 row['Midterm_Score'] * 0.4 + 
                 row['Assignment_Score'] * 0.2 + 
                 row['Previous_CGPA'] * 2.5) # Normalized roughly
        
        # Add some noise
        noise = np.random.normal(0, 5)
        final_score = score + noise
        
        return 1 if final_score > 55 else 0

    df['Status'] = df.apply(determine_status, axis=1)
    
    os.makedirs('e:/EWS/data', exist_ok=True)
    df.to_csv('e:/EWS/data/students.csv', index=False)
    print(f"Generated {num_students} student records in e:/EWS/data/students.csv")
    print(f"Status distribution:\n{df['Status'].value_counts()}")

if __name__ == "__main__":
    generate_student_data()
