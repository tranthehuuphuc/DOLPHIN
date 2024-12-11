# Handles data preprocessing

import pandas as pd

def preprocess_dataset(file_path):
    """
    Reads a dataset from a CSV file and preprocesses it.

    Args:
        file_path (str): Path to the CSV file.

    Returns:
        pd.DataFrame: Cleaned dataset.
    """
    data = pd.read_csv(file_path)

    # Validate columns
    if "domain_name" not in data.columns or "label" not in data.columns:
        raise ValueError("Dataset must contain 'domain_name' and 'label' columns.")

    # Drop invalid rows
    data.dropna(subset=["domain_name", "label"], inplace=True)
    data = data[data["domain_name"].str.contains("\\.")]

    return data