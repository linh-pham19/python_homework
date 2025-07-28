import pandas as pd
from pathlib import Path

def read_employees() -> list[str]:
    """
    Reads employee data from a CSV file and returns a list of employee full names
    that contain at least one 'e'.

    The CSV file should be located at "csv/employees.csv" relative to this script,
    with columns: id, first, last, phone.

    :return: List of employee full names (first and last) containing at least one 'e'.
    """
    file_path = Path(__file__).resolve().parent / "../csv/employees.csv"
    df = pd.read_csv(
        file_path,
        header=0,
        names=["id", "first", "last", "phone"],
    )
    employees = [
        f"{row['first']} {row['last']}"
        for _, row in df.iterrows()
    ]
    employees_e = [emp for emp in employees if "e" in emp]
    print(employees_e)
    return employees_e

employees = read_employees()
print("Employees with 'e' in their names:", employees)