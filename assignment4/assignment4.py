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

# Task 2
# Task 2.1 Read the CSV file
task2_employees = pd.read_csv(task1_older_to_csv)
print(task2_employees)

# Task 2.2 Read JSON
# How do you create a DataFrame from a JSON file?
import json

additional_employees = [
    {"Name": "Eve", "Age": 28, "City": "Miami", "Salary": 60000},
    {"Name": "Frank", "Age": 40, "City": "Seattle", "Salary": 95000}
]

with open('additional_employees.json', 'w') as json_file:
    json.dump(additional_employees, json_file)

#load json file into a DataFrame
json_employees = pd.read_json('additional_employees.json')

# verify the DataFrame
print(json_employees)

#task 2.3 Combine DataFrames
more_employees = pd.concat([task2_employees, json_employees], ignore_index=True)
print(more_employees)

# Task 3 
#3.1 Use the head() method
first_three = more_employees.head(3)
print(first_three)

#3.2 Use the tail() method
last_two = more_employees.tail(2)
print(last_two)

#3.3 Get the shape of the DataFrame
employee_shape = more_employees.shape
print(employee_shape)

#3.4 info method
more_employees_info = more_employees.info()
print(more_employees_info)

# Task 4.1
dirty_data = pd.read_csv('dirty_data.csv')


print("Dirty Data:")
print(dirty_data)


clean_data = dirty_data.copy()


print("\nClean Data (initial copy):")
print(clean_data)

#task 4.2
#remove duplicates
clean_data.drop_duplicates(inplace=True)
print("\nClean Data (after removing duplicates):")
print(clean_data)

#4.3
# Convert 'Age' to numeric, coercing errors
clean_data['Age'] = pd.to_numeric(clean_data['Age'], errors='coerce')
print("\nClean Data (after converting 'Age' to numeric):")
print(clean_data)

#4.4 convert 'Salary' to numeric, replacing 'unknown' and 'n/a' with NaN
clean_data['Salary'] = clean_data['Salary'].replace(['unknown', 'n/a'], pd.NA)
clean_data['Salary'] = pd.to_numeric(clean_data['Salary'], errors='coerce')
print("\nClean Data (after converting 'Salary' to numeric):")
print(clean_data)

#4.5 fill numeric values with fillna. Fill Age with mean and salary with median
clean_data['Age'].fillna(clean_data['Age'].mean(), inplace=True)
clean_data['Salary'].fillna(clean_data['Salary'].median(), inplace=True)
print("\nClean Data (after filling NaN values):")
print(clean_data)

#4.6 convert 'Hire Date' to datetime
clean_data['Hire Date'] = pd.to_datetime(clean_data['Hire Date'], errors='coerce')
clean_data['Hire Date'] = clean_data['Hire Date'].fillna(pd.Timestamp('today'))

print("\nClean Data (after converting 'Hire Date' to datetime):")
print(clean_data)

#4.7 strip whitespace from 'Name' and 'Department' and standardize them to uppercase
clean_data['Name'] = clean_data['Name'].str.strip()
clean_data['Department'] = clean_data['Department'].str.strip().str.upper()
print("\nClean Data (after stripping whitespace and standardizing 'Department'):")
print(clean_data)
