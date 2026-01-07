# Generates text-based sales reports

import os

def generate_report(valid_transactions, invalid_count, analysis_result):
    os.makedirs("output", exist_ok=True)

    report_path = "output/sales_report.txt"

    total_revenue = analysis_result.get("total_revenue", 0)
    region_sales = analysis_result.get("region_sales", {})

    with open(report_path, "w", encoding="utf-8") as f:
        f.write("Sales Analytics Report\n")
        f.write("======================\n\n")

        f.write("Validation Summary\n")
        f.write("------------------\n")
        f.write(f"Valid Transactions: {len(valid_transactions)}\n")
        f.write(f"Invalid Transactions: {invalid_count}\n\n")

        f.write("Revenue Summary\n")
        f.write("---------------\n")
        f.write(f"Total Revenue: ₹{total_revenue}\n\n")

        f.write("Region-wise Sales\n")
        f.write("-----------------\n")
        for region, amount in region_sales.items():
            f.write(f"{region}: ₹{amount}\n")

        f.write("\nEnd of Report\n")

    return report_path
