import pandas as pd
import json
import logging
import os


# -----------------------------------
# Load Configuration
# -----------------------------------

def load_config():

    with open("config.json", "r") as file:
        config = json.load(file)

    return config


# -----------------------------------
# Setup Logging
# -----------------------------------

def setup_logging(log_file):

    os.makedirs(os.path.dirname(log_file), exist_ok=True)

    logging.basicConfig(
        filename=log_file,
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s"
    )


# -----------------------------------
# Extract Data
# -----------------------------------

def extract_data(file_path):

    print("Extracting data...")

    df = pd.read_csv(file_path)

    logging.info(f"Extract stage: {len(df)} records")

    return df


# -----------------------------------
# Validate Columns
# -----------------------------------

def validate_columns(df, required_columns):

    for column in required_columns:

        if column not in df.columns:

            raise ValueError(
                f"Missing required column: {column}"
            )

    logging.info("Column validation successful")


# -----------------------------------
# Transform Data
# -----------------------------------

def transform_data(df, transformations):

    print("Transforming data...")

    # Convert names to uppercase
    if transformations["uppercase_name"]:

        df["name"] = df["name"].str.upper()


    # Calculate total amount
    if transformations["calculate_total"]:

        df["total"] = df["quantity"] * df["price"]


    logging.info(
        f"Transform stage: {len(df)} records"
    )

    return df


# -----------------------------------
# Final Validation
# -----------------------------------

def validate_data(df, validation):

    print("Validating data...")

    required_columns = validation["required_columns"]

    validate_columns(df, required_columns)

    # Check null values
    if validation["allow_nulls"] is False:

        if df.isnull().any().any():

            raise ValueError(
                "Validation failed: Null values found"
            )

    logging.info("Data validation successful")


# -----------------------------------
# Final Transformation
# -----------------------------------

def create_final_data(df, minimum_total):

    print("Creating final dataset...")

    final_df = df[df["total"] >= minimum_total].copy()

    logging.info(
        f"Final stage: {len(final_df)} records"
    )

    return final_df


# -----------------------------------
# Save Data
# -----------------------------------

def save_data(df, file_path):

    directory = os.path.dirname(file_path)

    if directory:

        os.makedirs(directory, exist_ok=True)

    df.to_csv(file_path, index=False)

    print(f"Saved: {file_path}")

    logging.info(
        f"File saved: {file_path}"
    )


# -----------------------------------
# Main ETL Pipeline
# -----------------------------------

def main():

    print("=" * 50)
    print("CONFIGURATION-DRIVEN ETL PIPELINE")
    print("=" * 50)

    # Load configuration
    config = load_config()

    # Setup logging
    setup_logging(
        config["logging"]["file"]
    )

    logging.info("ETL Pipeline started")

    try:

        # -----------------------------------
        # EXTRACT
        # -----------------------------------

        raw_df = extract_data(
            config["input"]["file"]
        )

        # Save raw data
        save_data(
            raw_df,
            config["output"]["raw"]
        )


        # -----------------------------------
        # VALIDATE
        # -----------------------------------

        validate_columns(
            raw_df,
            config["validation"]["required_columns"]
        )


        # -----------------------------------
        # TRANSFORM
        # -----------------------------------

        transformed_df = transform_data(
            raw_df,
            config["transformations"]
        )

        # Save transformed data
        save_data(
            transformed_df,
            config["output"]["transformed"]
        )


        # -----------------------------------
        # FINAL VALIDATION
        # -----------------------------------

        validate_data(
            transformed_df,
            config["validation"]
        )


        # -----------------------------------
        # FINAL DATA
        # -----------------------------------

        final_df = create_final_data(
            transformed_df,
            config["transformations"]["minimum_total"]
        )

        # Save final dataset
        save_data(
            final_df,
            config["output"]["final"]
        )


        print("\nETL Pipeline completed successfully!")

        print(
            f"\nRaw records: {len(raw_df)}"
        )

        print(
            f"Transformed records: {len(transformed_df)}"
        )

        print(
            f"Final records: {len(final_df)}"
        )

        logging.info("ETL Pipeline completed successfully")


    except Exception as error:

        print("\nETL Pipeline failed!")

        print("Error:", error)

        logging.error(
            f"ETL Pipeline failed: {error}"
        )


# -----------------------------------
# Run Program
# -----------------------------------

if __name__ == "__main__":

    main()