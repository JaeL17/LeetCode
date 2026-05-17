import pandas as pd

def calculate_special_bonus(employees: pd.DataFrame) -> pd.DataFrame:
    # id_and_bonus = []
    # for emp_id, name, salary in zip(employees["employee_id"], employees["name"], employees["salary"]):
    #     if emp_id % 2 ==1 and name[0] != "M":
    #         id_and_bonus.append([emp_id, salary])
    #     else:
    #         id_and_bonus.append([emp_id, 0])
    employees["bonus"] = 0 
    employees.loc[(employees["employee_id"] % 2 == 1) & ~employees["name"].str.startswith("M"), ["bonus"]] = employees["salary"]


    # return pd.DataFrame(id_and_bonus, columns = ["employee_id", "bonus"]).sort_values("employee_id")
    return employees[["employee_id", "bonus"]].sort_values("employee_id")