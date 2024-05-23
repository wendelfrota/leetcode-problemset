import pandas as pd


def modifySalaryColumn(employees: pd.DataFrame) -> pd.DataFrame:
    employees.salary *= 2
    return employees


# df = pandas.DataFrame({
#     'name': ['Jack', 'Piper', 'Mia', 'Ulysses'],
#     'salary': [19666, 74754, 62509, 54866]
# })

# print(modifySalaryColumn(df))
