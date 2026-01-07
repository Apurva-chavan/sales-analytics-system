# Integrates external product API and enrichment logic

import os
import requests


# -----------------------------
# Fetch products from API
# -----------------------------
def fetch_all_products():
    url = "https://dummyjson.com/products?limit=100"
    response = requests.get(url)
    data = response.json()

    products = []
    for p in data.get("products", []):
        products.append({
            "name": p["title"].lower(),   # normalize
            "category": p.get("category", "N/A"),
            "rating": p.get("rating", "N/A")
        })

    return products


# -----------------------------
# Create mapping
# -----------------------------
def create_product_mapping(products):
    mapping = {}
    for p in products:
        mapping[p["name"]] = p
    return mapping


# -----------------------------
# Enrich sales data
# -----------------------------
def enrich_sales_data(transactions, product_map):
    enriched = []

    for tx in transactions:
        tx_name = tx["product_name"].lower()
        matched = False

        for api_name, api_product in product_map.items():
            # BIDIRECTIONAL partial match
            if tx_name in api_name or api_name in tx_name:
                tx["API_Category"] = api_product["category"]
                tx["API_Rating"] = api_product["rating"]
                tx["API_Match"] = True
                matched = True
                break

        if not matched:
            tx["API_Category"] = "Unknown"
            tx["API_Rating"] = "N/A"
            tx["API_Match"] = False

        enriched.append(tx)

    return enriched


# -----------------------------
# Save enriched data
# -----------------------------
def save_enriched_data(enriched, filename="data/enriched_sales_data.txt"):
    os.makedirs("data", exist_ok=True)

    with open(filename, "w", encoding="utf-8") as f:
        f.write(
            "TransactionID|ProductName|API_Category|API_Rating|API_Match\n"
        )
        for t in enriched:
            f.write(
                f"{t['transaction_id']}|{t['product_name']}|"
                f"{t['API_Category']}|{t['API_Rating']}|{t['API_Match']}\n"
            )
