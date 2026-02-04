import pandas as pd
import os

def create_demo_excel():
    data = {
        'Student_ID': ['STU001', 'STU002', 'STU003', 'STU004', 'STU005'],
        'Student_Name': ['John Doe', 'Jane Smith', 'Alex Johnson', 'Sarah Williams', 'Michael Brown'],
        'Attendance': [85, 45, 92, 60, 78],
        'Midterm_Score': [78, 30, 88, 55, 65],
        'Assignment_Score': [82, 40, 95, 50, 70],
        'Previous_CGPA': [3.5, 2.1, 3.8, 2.6, 2.9],
        'Participation_Score': [8, 2, 9, 4, 6]
    }
    
    df = pd.DataFrame(data)
    os.makedirs('e:/EWS/data/static', exist_ok=True)
    filepath = 'e:/EWS/data/static/demo_students.xlsx'
    df.to_excel(filepath, index=False)
    print(f"Demo Excel file created at {filepath}")

if __name__ == "__main__":
    create_demo_excel()
