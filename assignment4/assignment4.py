import pandas as pd

#task 1
# Task 1.1 create the dictionary
data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['New York', 'Los Angeles', 'Chicago']
}

# convert the dictionary to a DataFrame
task1_data_frame = pd.DataFrame(data)
print(task1_data_frame)

task1_data_frame.to_csv('task1_data_frame.csv', index=False)

# TASK 1.2 Add a new column 'Salary'
task1_with_salary = task1_data_frame.copy()
task1_with_salary['Salary'] = [70000, 80000, 90000]
print(task1_with_salary)

#Task 1.3 Modify the 'Age' column
task1_older = task1_with_salary.copy()
task1_older['Age'] += 1
print(task1_older)

# Task 1.4 Write to CSV
task1_older_to_csv = 'employees.csv'
task1_older.to_csv(task1_older_to_csv, index=False)



