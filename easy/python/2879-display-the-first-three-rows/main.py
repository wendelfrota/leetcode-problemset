import pandas as pd


def selectFirstRows(employees: pd.DataFrame) -> pd.DataFrame:
    return employees.head(3)


# df = pd.DataFrame({
#     'Nome': ['Ana', 'Bruno', 'Carlos', 'Diana'],
#     'Idade': [23, 34, 45, 29],
#     'Cidade': ['São Paulo', 'Rio de Janeiro', 'Belo Horizonte', 'Curitiba']
# })
#
# print(selectFirstRows(df))
