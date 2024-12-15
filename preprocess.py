# preprocess.py

import pandas as pd
from typing import Set

def preprocess_dataset(dataset_path: str, whitelist: Set[str]) -> pd.DataFrame:
    """
    Preprocess the dataset by filtering and cleaning domain data.
    
    Args:
        dataset_path (str): Path to the input dataset
        whitelist (Set[str]): Set of whitelisted domains
    
    Returns:
        pd.DataFrame: Preprocessed dataset with filtered domains
    """
    try:
        # Read the dataset with header handling to ensure correct column names
        data = pd.read_csv(dataset_path, header=0)  # header=0 tells pandas to use the first row as header
    except Exception as e:
        print(f"Error reading dataset: {e}")
        raise
    
    # Ensure the dataset contains the expected columns
    if "domain_name" not in data.columns or "label" not in data.columns:
        print("Dataset missing expected columns. Assigning default headers.")
        data.columns = ["domain_name", "label"]  # In case columns are not correctly set
    
    # Check if 'label' column exists and assign default labels if missing
    if data['label'].isnull().all():
        print("No labels found in dataset. Assigning default labels (0).")
        data['label'] = 0  # Default label assignment

    # Preprocess domain names (strip whitespace and convert to lowercase)
    data['domain_name'] = data['domain_name'].str.lower().str.strip()

    # Filter out domains in the whitelist
    data = data[~data['domain_name'].isin(whitelist)]

    # Remove any rows with missing values in either 'domain_name' or 'label'
    data = data.dropna(subset=['domain_name', 'label'])

    return data
