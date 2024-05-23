import pandas as pd


def createBonusColumn(employees: pd.DataFrame) -> pd.DataFrame:
    employees['bonus'] = employees.salary * 2
    return employees


# df = pd.DataFrame({
#     'name': ['Piper', 'Grace', 'Georgia', 'Willow', 'Finn', 'Thomas'],
#     'salary': [4548, 20150, 1103, 6593, 74576, 24433]
# })

# print(createBonusColumn(df))
