import pandas as pd
import numpy as np
import random
from datetime import datetime, timedelta

# Base path
base_path = r'C:\Users\arshpreet\OneDrive\Desktop\employee-attendance-tracker'

# Settings
num_employees = 50
start_date = datetime(2024, 1, 1)
end_date = datetime(2024, 12, 31)

# Employee list
departments = ['HR', 'IT', 'Finance', 'Marketing', 'Operations']
statuses = ['Present', 'Absent', 'Late', 'Leave']

rows = []
for emp_id in range(1, num_employees + 1):
    current_date = start_date
    while current_date <= end_date:
        if current_date.weekday() < 5:  # Monday to Friday only
            rows.append({
                'Employee_ID': f'EMP{emp_id:03d}',
                'Name': f'Employee_{emp_id}',
                'Department': random.choice(departments),
                'Date': current_date.strftime('%Y-%m-%d'),
                'Status': random.choices(statuses, weights=[70, 10, 15, 5])[0]
            })
        current_date += timedelta(days=1)

df = pd.DataFrame(rows)
df.to_csv(fr'{base_path}\data\attendance_data.csv', index=False)
print("Dataset generated!", df.shape)
print(df.head())
