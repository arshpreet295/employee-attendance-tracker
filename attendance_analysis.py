import pandas as pd
import matplotlib.pyplot as plt
import os

# Base path
base_path = r'C:\Users\arshpreet\OneDrive\Desktop\employee-attendance-tracker'

# Load Data
df = pd.read_csv(os.path.join(base_path, 'data', 'attendance_data.csv'))

print("Shape:", df.shape)
print(df.head())
print(df.isnull().sum())

# ---- ANALYSIS ----

# 1. Attendance Summary
attendance_summary = df['Status'].value_counts().reset_index()
attendance_summary.columns = ['Status', 'Count']
print(attendance_summary)

# 2. Department wise Attendance
dept_attendance = df.groupby(['Department', 'Status']).size().reset_index(name='Count')
print(dept_attendance)

# 3. Monthly Attendance Trend
df['Date'] = pd.to_datetime(df['Date'])
df['Month'] = df['Date'].dt.to_period('M')
monthly_trend = df.groupby(['Month', 'Status']).size().reset_index(name='Count')
print(monthly_trend)

# 4. Top 10 Absent Employees
absent_emp = df[df['Status'] == 'Absent'].groupby('Employee_ID').size().nlargest(10).reset_index()
absent_emp.columns = ['Employee_ID', 'Absent Days']
print(absent_emp)

# ---- CHARTS ----

os.makedirs(os.path.join(base_path, 'charts'), exist_ok=True)

# Chart 1 - Attendance Status Distribution
plt.figure(figsize=(8,5))
plt.bar(attendance_summary['Status'], attendance_summary['Count'], color=['green','red','orange','blue'])
plt.title('Overall Attendance Status Distribution')
plt.xlabel('Status')
plt.ylabel('Count')
plt.tight_layout()
plt.savefig(os.path.join(base_path, 'charts', 'attendance_summary.png'))
plt.close()

# Chart 2 - Top 10 Absent Employees
plt.figure(figsize=(10,5))
plt.bar(absent_emp['Employee_ID'], absent_emp['Absent Days'], color='red')
plt.title('Top 10 Most Absent Employees')
plt.xlabel('Employee ID')
plt.ylabel('Absent Days')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig(os.path.join(base_path, 'charts', 'top_absent.png'))
plt.close()

# ---- EXPORT TO EXCEL ----

with pd.ExcelWriter(os.path.join(base_path, 'attendance_cleaned.xlsx'), engine='openpyxl') as writer:
    df.to_excel(writer, sheet_name='Raw Data', index=False)
    attendance_summary.to_excel(writer, sheet_name='Attendance Summary', index=False)
    dept_attendance.to_excel(writer, sheet_name='Department Wise', index=False)
    absent_emp.to_excel(writer, sheet_name='Top Absentees', index=False)

print("✅ Excel exported!")
print("✅ Charts saved!")
