## preprocess.py
# Handles data preprocessing

import pandas as pd

def preprocess_dataset(file_path, whitelist):
    """
    Reads a dataset from a CSV file and preprocesses it.

    Args:
        file_path (str): Path to the CSV file.
        whitelist (set): Set of whitelisted domain names to exclude.

    Returns:
        pd.DataFrame: Cleaned dataset.
    """
    # data = pd.read_csv(file_path)

    # # Validate columns
    # if "domain_name" not in data.columns or "label" not in data.columns:
    #     raise ValueError("Dataset must contain 'domain_name' and 'label' columns.")

    # # Drop invalid rows
    # data.dropna(subset=["domain_name", "label"], inplace=True)
    # data = data[data["domain_name"].str.contains("\\.")]

    # # Exclude whitelisted domains
    # data = data[~data["domain_name"].isin(whitelist)]

    # return data

    if file_path.endswith('.csv'):
        # data = pd.read_csv(file_path)

        # # Validate columns
        # if "domain_name" not in data.columns or "label" not in data.columns:
        #     raise ValueError("Dataset must contain 'domain_name' and 'label' columns.")

        # # Drop invalid rows
        # data.dropna(subset=["domain_name", "label"], inplace=True)
        # data = data[data["domain_name"].str.contains("\\.")]
        data = pd.read_csv(file_path)

        # Validate columns
        required_columns = {"domain", "class"}
        if not required_columns.issubset(data.columns):
            raise ValueError(f"Dataset must contain the following columns: {required_columns}")

        # Drop invalid rows
        data.dropna(subset=["domain", "class"], inplace=True)
        data = data[data["domain"].str.contains("\\.")]

    elif file_path.endswith('.txt'):
        with open(file_path, 'r') as file:
            domain_names = [line.strip() for line in file if line.strip()]
        data = pd.DataFrame({"domain_name": domain_names, "label": -1})  # Assign -1 as default label for TXT files

    else:
        raise ValueError("Unsupported file format. Please use .csv or .txt files.")

    # Exclude whitelisted domains
    data = data[~data["domain_name"].isin(whitelist)]

    return data