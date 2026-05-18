import pandas as pd

def nth_highest_salary(employee: pd.DataFrame, N: int) -> pd.DataFrame:
    employee = employee.drop_duplicates("salary").sort_values("salary", ascending=False)
    if N <= 0 or len(employee) < N:
        return pd.DataFrame({f"getNthHighestSalary({N})": [None]})
    else:
        row_idx = N-1
        return pd.DataFrame({f"getNthHighestSalary({N})": [employee.iloc[row_idx, 1]]})

