import os 
import csv

path = os.path.join("..", "data", "messy_data.csv")

with open(path, "r" ) as file:
    reader = csv.DictReader(file)
    rows = list(reader)


try:
    with open(path, "r" ) as file:
        reader = csv.DictReader(file)
        rows = list(reader)

except FileNotFoundError:
    print("File Not Found!")

else:
    skipped_rows = [] #list to hold skipped rows
    clean_rows = []    #list to hold clean rows

    for row_number, row in enumerate(rows, start=1):
        if None in row:
            key_error_message = f"Row {row_number}: KeyError - extra column detected - skipped"
            skipped_rows.append(key_error_message)
            continue

        try:
            entry = {
                "name":row["name"],
                "category":row["category"],
                "amount":float(row["amount"])
            }
            clean_rows.append(entry)

        except ValueError:
            value_error_message = f"Row {row_number}: ValueError - could not convert '{row['amount']}' to float"
            skipped_rows.append(value_error_message)

    skipped_rows_total = len(skipped_rows)
    clean_rows_total = len(clean_rows)

    print("=== CSV Report ===")
    print(f"{'Rows attempted:':<18}{skipped_rows_total+clean_rows_total:>5}")
    print(f"{'Rows Parsed:':<18}{clean_rows_total:>5}")
    print(f"{'Rows Skipped:':<18}{skipped_rows_total:>5}")
    print()

    print("Skipped rows:")
    for row in skipped_rows:
        print(f" {row}")

    print()
    print("Clean data:")
    for row in clean_rows:
        name = row['name']
        category = row['category']
        amount = row['amount']

        print(f" {name} | {category} | ${amount:.2f}")