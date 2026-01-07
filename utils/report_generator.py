# Generates text-based sales reports

def generate_report(transactions):
    with open("output/sales_report.txt", "w", encoding="utf-8") as file:
        file.write("SALES ANALYTICS REPORT\n")
        file.write("=" * 40 + "\n")
        file.write(f"Total Records: {len(transactions)}\n")
