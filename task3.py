import csv
import json


def merge_data(csv_file, json_file, output_file):
    # Чтение данных из CSV-файла
    products = {}
    with open(csv_file, mode="r", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            products[row["product_id"]] = row["product_name"]

    # Чтение данных из JSON-файла
    with open(json_file, mode="r", encoding="utf-8") as file:
        sales = json.load(file)

    # Объединение данных
    merged_data = []
    for sale in sales:
        product_id = sale["product_id"]
        if product_id in products:
            sale["product_name"] = products[product_id]
            merged_data.append(sale)

    # Запись объединенных данных в новый JSON-файл
    with open(output_file, "w", encoding="utf-8") as file:
        json.dump(merged_data, file, indent=4)

    print(f"Data successfully merged and saved to {output_file}")


csv_file = "products.csv"
json_file = "sales.json"
output_file = "merged_data.json"
merge_data(csv_file, json_file, output_file)
