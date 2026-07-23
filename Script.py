import pandas as pd


def process_medical_data(input_filepath, output_filepath):
    print("Starting data processing pipeline...")

    # Step 1: Load the raw data
    try:
        df = pd.read_csv(input_filepath)
        print(f"Successfully loaded {len(df)} records.")
    except FileNotFoundError:
        print("Error: The raw data file was not found.")
        return

    # Step 2: Clean the data (Drop empty critical rows)
    # We cannot calculate risk if Age or Failure Count is missing
    df = df.dropna(subset=['Age', 'Failure_Event_Count'])
    print("Data cleaned: Removed rows with missing critical values.")

    # Step 3: Feature Engineering (Calculate Risk Score)
    # Formula: (Age * 1.5) + (Failure_Event_Count * 3)
    # This gives heavier weight to machines that break down often
    df['Risk_Score'] = (df['Age'] * 1.5) + (df['Failure_Event_Count'] * 3)

    # Step 4: Categorize the Risk for the Power BI Dashboard
    def assign_risk_category(score):
        if score > 20:
            return 'High Risk - Urgent Review'
        elif score > 10:
            return 'Moderate Risk'
        else:
            return 'Low Risk'

    df['Risk_Category'] = df['Risk_Score'].apply(assign_risk_category)
    print("Risk scores and categories successfully calculated.")

    # Step 5: Export the clean, processed data
    df.to_csv(output_filepath, index=False)
    print(f"Pipeline complete! Clean data saved to: {output_filepath}")


# --- Execution Block ---
# This is where we tell the script exactly which files to use
RAW_DATA_FILE = 'Medical_Device_Failure_dataset.csv'
CLEAN_DATA_FILE = 'Processed_Medical_Device_Data.csv'

process_medical_data(RAW_DATA_FILE, CLEAN_DATA_FILE)