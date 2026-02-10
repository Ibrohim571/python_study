import pandas as pd
import os

# Check if we're in the right place
print("Current directory:", os.getcwd())

# Check if our data file exists
data_path = "data/sales.csv"
if os.path.exists(data_path):
    print(f"✅ Found {data_path}")
else:
    print(f"❌ Cannot find {data_path}")
    print("Make sure you're running from the sales-analysis folder!")

df = pd.read_csv(data_path)
print("CSV Data:")

# print(df)
# print(df.shape)
# print(f"\nShape: {df.shape[0]} rows, {df.shape[1]} columns")

df['total'] = df['quantity'] * df['price']
print("\nWith totals:")
print(df)

os.makedirs('output', exist_ok=True)

df.to_json('output/sales_data.json', orient='records', indent=2)

df.to_excel('output/sales_data.xlsx', index=False)

df.to_csv('output/sales_with_totals.csv', index=True)

print("\nFiles saved:")
print("- output/sales_data.json")
print("- output/sales_data.xlsx")
print("- output/sales_with_totals.csv")