# Entry point for the pipeline

import pandas as pd
from preprocess import preprocess_dataset
from dolphin_patterns import greedy_match, DOLPHIN_PATTERNS
from feature_extraction import compute_phonics_features
from model_training import train_and_evaluate_model

def main():
    dataset_path = "path/to/dataset.csv"
    data = preprocess_dataset(dataset_path)

    features = []
    for _, row in data.iterrows():
        matches = greedy_match(row["domain_name"], DOLPHIN_PATTERNS)
        phonics_features = compute_phonics_features(matches)
        phonics_features["label"] = row["label"]
        features.append(phonics_features)

    features_df = pd.DataFrame(features)
    train_and_evaluate_model(features_df)

if __name__ == "__main__":
    main()