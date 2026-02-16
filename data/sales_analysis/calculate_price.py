import pandas as pd
from helper import calculate_total, format_currency

df = pd.read_csv('./data/sales.csv')

print(df)

example = pd.DataFrame({
    "name": ["Ali", "Vali"],
    "age": [20, 25],
    "status": ["student", "teacher"]
})

for index, row in example.iterrows():
    print(row)

for index, row in df.iterrows():
    print(row)
    print('\n')

totals = []
for index, row in df.iterrows():
    total = calculate_total(row['quantity'], row['price'])
    totals.append(total)

df['total'] = totals

print("Sales Data:")
for index, row in df.iterrows():
    formatted_total = format_currency(row['total'])
    print(f"{row['product']}: {formatted_total}")

grand_total = df['total'].sum()
formatted_grand_total = format_currency(grand_total)
print(f"\nGrand Total: {formatted_grand_total}")