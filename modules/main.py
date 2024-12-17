# main.py

import pandas as pd
import sys
import os

# Ensure the current directory is in the Python path
current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, current_dir)

from preprocess import preprocess_dataset
from modules.dolphin_patterns import greedy_match, DOLPHIN_PATTERNS
from modules.feature_extraction import compute_phonics_features
from model_training import train_and_evaluate_model

def main():
    # Default paths (can be modified as needed)
    dataset_path = "data.csv"
    whitelist_path = "whitelist.txt"

    # Load whitelist domains
    try:
        with open(whitelist_path, "r") as file:
            whitelist = set(domain.strip() for domain in file.readlines())
    except FileNotFoundError:
        print(f"Whitelist file {whitelist_path} not found. Continuing with empty whitelist.")
        whitelist = set()

    # Preprocess the dataset
    try:
        data = preprocess_dataset(dataset_path, whitelist)
    except FileNotFoundError:
        print(f"Dataset file {dataset_path} not found. Please check the file path.")
        return
    except Exception as e:
        print(f"Error processing dataset: {e}")
        return

    # Extract features
    features = []
    for _, row in data.iterrows():
        # Apply DOLPHIN pattern matching
        matches = greedy_match(row["domain_name"], DOLPHIN_PATTERNS)
        
        # Compute phonics features
        phonics_features = compute_phonics_features(matches)
        
        # Add label to features
        phonics_features["label"] = row["label"]
        
        features.append(phonics_features)

    # Convert to DataFrame
    features_df = pd.DataFrame(features)

    # Train and evaluate the model
    train_and_evaluate_model(features_df)

if __name__ == "__main__":
    main()