# Contains sales analytics and aggregation functions

from collections import defaultdict

def calculate_total_revenue(transactions):
    return round(sum(t["quantity"] * t["unit_price"] for t in transactions), 2)


def region_wise_sales(transactions):
    regions = defaultdict(float)
    for t in transactions:
        regions[t["region"]] += t["quantity"] * t["unit_price"]
    return dict(regions)


def top_selling_products(transactions, n=5):
    products = defaultdict(int)
    for t in transactions:
        products[t["product_name"]] += t["quantity"]
    return sorted(products.items(), key=lambda x: x[1], reverse=True)[:n]
