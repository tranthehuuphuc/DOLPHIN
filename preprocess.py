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
        # Try reading as CSV first
        data = pd.read_csv(dataset_path, names=["domain_name", "label"])
    except Exception as e:
        print(f"Error reading as CSV: {e}. Attempting to read as text file...")
        try:
            # If not CSV, try reading as text file with regex for whitespace separator
            data = pd.read_csv(dataset_path, header=None, names=["domain_name", "label"], sep=r'\s+', engine="python")
        except Exception as e:
            print(f"Error reading dataset as text file: {e}")
            raise

    # Ensure label column exists
    if "label" not in data.columns or data["label"].isnull().all():
        print("No labels found in dataset. Assigning default labels (0).")
        data["label"] = 0  # Default label assignment

    # Preprocess domain names
    data['domain_name'] = data['domain_name'].str.lower().str.strip()

    # Filter out domains in whitelist
    data = data[~data['domain_name'].isin(whitelist)]

    # Remove any rows with missing data
    data = data.dropna()

    return data
