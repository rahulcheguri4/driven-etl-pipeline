#  🚀 Configuration-Driven ETL Pipeline
A simple Configuration-Driven ETL Pipeline built using Python and Pandas. The project extracts data from a CSV file, transforms and validates the data, and generates final datasets based on settings defined in a JSON configuration file.

#  📌 Project Overview
The main goal of this project is to separate ETL configuration from Python code.

Instead of changing the Python program whenever the input file, output location, validation rules, or transformation settings change, these values can be updated in config.json.

# 🎯 Objectives
-- Build a practical ETL pipeline
-- Extract data from CSV
-- Transform data using Pandas
-- Validate incoming data
-- Store raw, transformed, and final datasets
-- Use JSON for configuration
-- Implement pipeline logging
-- Practice data-engineering concepts

# 🛠️ Technologies Used
-- Python
-- Pandas
-- JSON
-- CSV
-- Python Logging


# 📂 Project Structure
etl_pipeline/
│
├── data.csv
├── config.json
├── etl_pipeline.py
│
├── output/
│   ├── raw.csv
│   ├── transformed.csv
│   └── final.csv
│
└── logs/
    └── etl.log


# 🔄 ETL Workflow
             data.csv
                 │
                 ▼
            ┌─────────┐
            │ Extract │
            └────┬────┘
                 │
                 ▼
             raw.csv
                 │
                 ▼
           ┌───────────┐
           │ Transform │
           └─────┬─────┘
                 │
                 ▼
          transformed.csv
                 │
                 ▼
           ┌──────────┐
           │ Validate │
           └────┬─────┘
                │
                ▼
          ┌────────────┐
          │ Final Data │
          └──────┬─────┘
                 │
                 ▼
             final.csv



# Expected output:
==================================================
CONFIGURATION-DRIVEN ETL PIPELINE
==================================================

Extracting data...
Saved: output/raw.csv

Transforming data...
Saved: output/transformed.csv

Validating data...
Creating final dataset...
Saved: output/final.csv

ETL Pipeline completed successfully!

Raw records: 10
Transformed records: 10
Final records: 8
