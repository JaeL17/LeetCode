import pandas as pd

def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:
    
    # pd series for employee salary
    salary = employee["salary"].drop_duplicates().sort_values(ascending=False)

    if len(salary) < 2:
        return pd.DataFrame({"SecondHighestSalary": [None]})
    else:
        return pd.DataFrame({"SecondHighestSalary": [salary.iloc[1]]})
    