#import
import os
import csv
from datetime import datetime

#
if not os.path.exists("../data/expenses.csv"):
    print("expenses.csv not found.")

else: 
    #with open('../data/expenses.csv', 'r') as file:
       # reader = csv.DictReader(file)
        #for row in reader:
            #print(f"{row['date']}, {row['category']}, {row['description']}, {row['amount']}")

# Load all rows into memory
    with open('../data/expenses.csv', 'r') as file:
        records = list(csv.DictReader(file))

    # Convert string to a float
    for item in records:
        item['amount'] = float(item['amount'])
       

    # Filter to Food Category
    food_items = [item for item in records if item['category'] == 'Food']
   
    # Compute total inventory value
    total_amount_spent = sum(item['amount'] * 1  for item in food_items)

now = datetime.now()
#print(f"Food Expense Report — {now.strftime("%B, %d, %Y")}") 



with open('food_report.txt', 'w') as file:
    file.write(f"\nFood Expense Report — generated {now.strftime('%B %d, %Y')}")
    for item in food_items:
        file.write(f"\n{item['date']}: ${item['amount']:.2f}")

    file.write(f"\nTotal: ${total_amount_spent:.2f}")