# Task 2
import csv
import datetime
import traceback
import custom_module

def read_employees():
    data_dict = {}
    rows = []
    try:
        # Read CSV file using try block and with statement
        with open('../csv/employees.csv', 'r') as csvfile:
            csv_reader = csv.reader(csvfile)
            
            # Get the first row (headers) and store in dict
            first_row = next(csv_reader)
            data_dict["fields"] = first_row
            
            # Loop through remaining rows and add to rows list
            for row in csv_reader:
                rows.append(row)
            
            # Add the rows list to the dict
            data_dict["rows"] = rows
            
        return data_dict
        
    except Exception as e:
        print("An exception occurred.")
        print(f"Exception type: {type(e).__name__}")
        print(f"Exception message: {str(e)}")
        print("Traceback information:")
        traceback.print_exc()
        exit()

employees = read_employees()


print(employees)

#TASK 3
def column_index(column_name):
    """Find the index of a column header in the employees fields array"""
    return employees["fields"].index(column_name)

# Call the function and store result in global variable
employees = read_employees()

# Print the result to verify the function works
print(employees)

# Initialize employee_id_column variable
employee_id_column = None

try:
    # Test the column_index function with "employee_id"
    employee_id_column = column_index("employee_id")
    print(f"Employee ID column index: {employee_id_column}")
except Exception as e:
    print(f"Error finding employee_id column: {e}")
    employee_id_column = None


#TASK 4
def first_name(row_number):
    name_index = column_index("first_name")
    return employees["rows"][row_number][name_index]

employees_id_column = column_index("employee_id")
print(employees)

# TASK 5
def employee_find(employee_id):
    def employee_match(row):
        return int(row[employee_id_column]) == employee_id

    matches = list(filter(employee_match, employees["rows"]))
    return matches

#TASK 6
def employee_find_2(employee_id):
    """Find employee rows that match the given employee_id using lambda"""
    matches = list(filter(lambda row: int(row[employee_id_column]) == employee_id, employees["rows"]))
    return matches

#TASK 7
def sort_by_last_name():
    """Sort the employees rows by last name"""
    employees["rows"].sort(key=lambda row: row[column_index("last_name")])
    return employees["rows"]

sort_by_last_name()
print("\n\n", employees)

#TASK 8
def employee_dict(row):
    """Convert a row to a dictionary with field names as keys"""
    return {employees["fields"][i]: row[i] for i in range(len(employees["fields"])) if employees["fields"][i] != "employee_id"}

print(employee_dict(employees["rows"][0]))

#TASK 9
def all_employees_dict():
    """Convert all employee rows to a dictionary with employee_id as keys"""
    return {row[employee_id_column]: employee_dict(row) for row in employees["rows"]}

#TASK 10
def get_this_value():
    """Return a specific value from the custom module"""
    return custom_module.secret

print(get_this_value())

#TASK 11
def set_that_secret(new_secret):
    """Set the secret value in the custom module"""
    custom_module.set_secret(new_secret)

print(set_that_secret("ABC"))
print(custom_module.secret)

#TASK 12
def read_minutes():
    with open("../csv/minutes1.csv") as file1:
        reader1 = csv.reader(file1)
        minutes1 = {}
        minutes1["fields"] = next(reader1)
        minutes1["rows"] = tuple([tuple(x) for x in reader1])

    with open("../csv/minutes2.csv") as file2:
        reader2 = csv.reader(file2)
        minutes2 = {}
        minutes2["fields"] = next(reader2)
        minutes2["rows"] = tuple([tuple(x) for x in reader2])

    return minutes1, minutes2


minutes1, minutes2 = read_minutes()
print(minutes1, minutes2)

#TASK 13
def create_minutes_set():
    """Create a set of unique values from the minutes rows"""
    set1 = set(minutes1["rows"])
    set2 = set(minutes2["rows"])
    set1.update(set2)
    return set1

minutes_set = create_minutes_set()
print(minutes_set)


#TASK 14
from datetime import datetime

def create_minutes_list(minutes_set):
    """Create a list of tuples from the minutes rows with datetime objects"""
    minutes_list = list(minutes_set)
    
    # Convert date strings to datetime objects
    minutes = [
        (x[0], datetime.strptime(x[1], "%B %d, %Y"))
        for x in minutes_list
    ]
    
    return minutes

print(create_minutes_list(minutes_set))

#TASK 15
def write_sorted_list():
    """Sort minutes_list, write to text file, and return sorted list"""
    # Get the minutes_list
    minutes_list = create_minutes_list(minutes_set)
    
    # Sort by datetime (second element of each tuple)
    sorted_list = sorted(minutes_list, key=lambda x: x[1])
    
    # Write to text file
    with open("sorted_minutes.txt", "w") as file:
        for item in sorted_list:
            file.write(f"{item[0]}: {item[1].strftime('%B %d, %Y')}\n")
    
    return sorted_list

# Call the function
sorted_minutes = write_sorted_list()
print(sorted_minutes)
