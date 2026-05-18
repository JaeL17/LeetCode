import pandas as pd

def department_highest_salary(employee: pd.DataFrame, department: pd.DataFrame) -> pd.DataFrame:
    employee["max_salary"] = employee.groupby("departmentId")["salary"].transform("max")
    merged = employee.merge(department, left_on = "departmentId", right_on = "id")
    print(merged.head())

    return merged.loc[merged["salary"]==merged["max_salary"],["name_y", "name_x", "salary"]].rename(columns={"name_y":"Department",
    "name_x": "Employee", "salary":"Salary"})