import csv

# Đọc file CSV
with open('trades.csv', 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(f"Cặp: {row['pair']}, Ngày: {row['trade_date']}, Giá: {row['price']}")