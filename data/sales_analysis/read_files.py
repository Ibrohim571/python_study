import pandas as pd

result = pd.read_json('output/sales_data.json')
print(result)

result_excel = pd.read_excel('./output/sales_data.xlsx')
print(result_excel)