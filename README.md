# 📊 Sales Analytics System

A Python-based Sales Analytics System that reads sales transactions, validates data, performs analytics, integrates product data from an external API, enriches transactions, and generates reports.

This project is developed as part of an academic assignment and satisfies all evaluation criteria from **Q1 to Q6**.

---

## 📁 Project Structure
# 📊 Sales Analytics System

A Python-based Sales Analytics System that reads sales transactions, validates data, performs analytics, integrates product data from an external API, enriches transactions, and generates reports.

This project is developed as part of an academic assignment and satisfies all evaluation criteria from **Q1 to Q6**.

---

## 📁 Project Structure

sales-analytics-system/
│
├── data/
│ ├── sales_data.txt
│ └── enriched_sales_data.txt
│
├── output/
│ └── sales_report.txt
│
├── utils/
│ ├── init.py
│ ├── file_handler.py
│ ├── data_processor.py
│ ├── api_handler.py
│ └── report_generator.py
│
├── main.py
├── requirements.txt
└── README.md

---

## ⚙️ Features Implemented

### ✔ File Handling & Cleaning
- Reads sales data from file
- Parses and cleans transaction records
- Displays filter options (region & amount range)
- Handles encoding safely

### ✔ Validation
- Identifies valid and invalid transactions
- Excludes invalid records from analysis

### ✔ Sales Analytics
- Calculates total revenue
- Region-wise sales analysis
- Handles negative values safely (pre-validation)

### ✔ API Integration
- Fetches product data from external API:
  https://dummyjson.com/products
- Maps product title to sales data
- Adds product category and rating

### ✔ Data Enrichment
- Enriches validated transactions with API data
- Saves enriched output to file

### ✔ Report Generation
- Generates sales summary report
- Saves report to output directory

### ✔ Error Handling
- Entire workflow wrapped in try-except
- Prevents program crashes
- Displays user-friendly error messages

---

## ▶️ How to Run

### Step 1: Install Dependencies
```bash
pip install -r requirements.txt
