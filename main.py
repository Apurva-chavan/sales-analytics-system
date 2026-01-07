# Entry point for Sales Analytics System

from utils.file_handler import (
    read_sales_data,
    parse_transactions,
    show_filter_options,
    validate_transactions
)

from utils.data_processor import (
    calculate_total_revenue,
    region_wise_sales
)

from utils.api_handler import (
    fetch_all_products,
    create_product_mapping,
    enrich_sales_data,
    save_enriched_data
)
from utils.report_generator import generate_report


def main():
    try:
        print("=" * 40)
        print("       SALES ANALYTICS SYSTEM")
        print("=" * 40)

        # [1/10] Reading sales data
        print("\n[1/10] Reading sales data...")
        raw_data = read_sales_data("data/sales_data.txt")
        print(f"✓ Successfully read {len(raw_data) - 1} transactions")

        # [2/10] Parsing and cleaning
        print("\n[2/10] Parsing and cleaning data...")
        parsed_transactions = parse_transactions(raw_data)
        print(f"✓ Parsed {len(parsed_transactions)} records")

        # [3/10] Filter options (MANDATORY DISPLAY)
        apply_filter = show_filter_options(parsed_transactions)

        if apply_filter:
            print("Filtering not applied – continuing with full dataset")

        # [4/10] Validation
        print("\n[4/10] Validating transactions...")
        valid_transactions, invalid_transactions = validate_transactions(parsed_transactions)
        print(f"✓ Valid: {len(valid_transactions)} | Invalid: {len(invalid_transactions)}")

        total_revenue = calculate_total_revenue(valid_transactions)
        region_sales = region_wise_sales(valid_transactions)

        analysis_result = {
        "total_revenue": total_revenue,
        "region_sales": region_sales
        }

        print("✓ Analysis complete")


        # [6/10] API fetch
        print("\n[6/10] Fetching product data from API...")
        products = fetch_all_products()
        print(f"✓ Fetched {len(products)} products")

        # [7/10] Enrichment
        print("\n[7/10] Enriching sales data...")
        product_map = create_product_mapping(products)
        enriched_data = enrich_sales_data(valid_transactions, product_map)

        percentage = round((len(enriched_data) / len(valid_transactions)) * 100, 1)
        print(f"✓ Enriched {len(enriched_data)}/{len(valid_transactions)} transactions ({percentage}%)")

        # [8/10] Save enriched data
        print("\n[8/10] Saving enriched data...")
        save_enriched_data(enriched_data)
        print("✓ Saved to: data/enriched_sales_data.txt")

        print("\n[9/10] Generating report...")
        report_path = generate_report(
        valid_transactions,
        len(invalid_transactions),
        analysis_result
        )
        print(f"✓ Report saved to: {report_path}")


        # [10/10] Done
        print("\n[10/10] Process Complete!")
        print("=" * 40)

    except Exception as e:
        print("\n❌ An error occurred during execution")
        print("Error:", e)


if __name__ == "__main__":
    main()
