import pandas as pd 
import openpyxl

# xl_file = pd.ExcelFile('/Users/sarantuaa/Documents/эксель компании/1 АО Алтайвагон.xlsx', engine='openpyxl')

# dfs = {sheet_name: xl_file.parse(sheet_name) 
#           for sheet_name in xl_file.sheet_names}

# print(dfs)

df = pd.read_excel('/Users/sarantuaa/Documents/эксель компании/1 АО Алтайвагон.xlsx', engine='openpyxl', sheet_name=None)
# headers = [i for i in df['Название комании']]

# print(headers)

print(df)
# df.to_csv(path_or_buf='out.csv', index=False)

# print(df.head())
