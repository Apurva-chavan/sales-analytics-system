# Handles file reading, parsing, and validation

import os

def read_sales_data(filename="data/sales_data.txt"):
    with open(filename, "r", encoding="utf-8") as file:
        lines = file.readlines()
    return lines


def parse_transactions(lines):
    headers = lines[0].strip().split("|")
    transactions = []

    for line in lines[1:]:
        values = line.strip().split("|")
        if len(values) != len(headers):
            continue

        tx = dict(zip(headers, values))

        try:
            tx = {
                "transaction_id": tx["TransactionID"],
                "date": tx["Date"],
                "product_name": tx["ProductName"],
                "quantity": int(tx["Quantity"]),
                "unit_price": float(tx["UnitPrice"]),
                "customer_id": tx["CustomerID"],
                "region": tx["Region"]
            }
            transactions.append(tx)
        except:
            continue

    return transactions


def validate_transactions(transactions):
    valid = []
    invalid = []

    for tx in transactions:
        if tx["quantity"] > 0 and tx["unit_price"] > 0 and tx["region"]:
            valid.append(tx)
        else:
            invalid.append(tx)

    return valid, invalid

def show_filter_options(transactions):
    regions = sorted(
        {tx.get("region") for tx in transactions if tx.get("region")}
    )

    amounts = [
        tx["quantity"] * tx["unit_price"]
        for tx in transactions
        if isinstance(tx.get("quantity"), (int, float))
        and isinstance(tx.get("unit_price"), (int, float))
    ]

    print("\n[3/10] Filter Options Available:")

    if regions:
        print("Regions:", ", ".join(regions))
    else:
        print("Regions: Not Available")

    if amounts:
        print(f"Amount Range: ₹{int(min(amounts))} - ₹{int(max(amounts))}")
    else:
        print("Amount Range: Not Available")

    choice = input("\nDo you want to filter data? (y/n): ").strip().lower()
    return choice == "y"
