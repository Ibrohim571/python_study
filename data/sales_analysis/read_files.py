import pandas as pd
import os

# result = pd.read_json('output/sales_data.json')
# print(result)

# result_excel = pd.read_excel('./output/sales_data.xlsx')
# print(result_excel)

os.makedirs('./output', exist_ok=True)

text = pd.DataFrame(["Hello programmer"])

text.to_csv("./output/example.txt", index=False)

# with open('./output/sales_data.xlsx', 'r') as f:
#     data = excel.load(f)
#     print(data)