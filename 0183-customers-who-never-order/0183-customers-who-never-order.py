import pandas as pd

def find_customers(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    result = customers.loc[ ~customers["id"].isin(orders["customerId"]), ["name"]]

    return result.rename(columns={"name":"Customers"})