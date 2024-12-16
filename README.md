# DOLPHIN Pattern Detection and Feature Extraction

This repository implements a system for detecting DOLPHIN patterns in domain names, extracting features based on these patterns, and training a classification model to identify malicious domains. The project is based on the paper ["DOLPHIN: Phonetics-Aware Detection of Malicious Domain Names"](https://aquatoney.github.io/files/dolphin-fgcs23-zhao.pdf) by Zhao et al., published in *Future Generation Computer Systems (2023)*. It includes modules for preprocessing datasets, applying pattern matching algorithms, extracting features, and training machine learning models.

## Features

- **DOLPHIN Pattern Matching**: Identifies predefined vowel and consonant patterns in domain names using a greedy matching algorithm.
- **Feature Extraction**: Computes phonics-based features such as vowel and consonant ratios, pattern diversity, and maximum pattern length.
- **Machine Learning Model**: Trains and evaluates a Random Forest classifier to classify domain names.
- **Preprocessing**: Handles data cleaning, filtering, and integration of a whitelist to exclude benign domains.

## Project Structure

```
.
├── main.py               # Main script to run the pipeline
├── preprocess.py         # Preprocessing module for dataset cleaning and filtering
├── dolphin_patterns.py   # Implements DOLPHIN pattern matching algorithm
├── feature_extraction.py # Feature extraction from pattern matches
├── model_training.py     # Training and evaluation of the machine learning model
├── tests/                # Unit tests
│   └── test_patterns.py  # Tests for DOLPHIN pattern matching
├── data.csv              # Example dataset (replace with your own dataset)
├── whitelist.txt         # Whitelist of benign domains
└── README.md             # Documentation (this file)
```

## Installation

1. Clone this repository:

   ```bash
   git clone <repository-url>
   cd <repository-folder>
   ```

2. Install required Python packages:

   ```bash
   pip install -r requirements.txt
   ```

## Usage

### 1. Prepare Your Dataset

- Place your dataset file in the root directory and name it `data.csv` (or modify the path in `main.py`).
- Ensure the dataset has the following columns:
  - `domain_name`: The domain names to analyze.
  - `label`: Labels for classification (e.g., `0` for benign, `1` for malicious).
- If you have a whitelist of domains, place them in `whitelist.txt` (one domain per line).

### 2. Run the Main Pipeline

Run the full pipeline using the following command:

```bash
python main.py
```

This will:

1. Preprocess the dataset and exclude whitelisted domains.
2. Perform DOLPHIN pattern matching on the domain names.
3. Extract phonics-based features.
4. Train and evaluate a Random Forest model.

### 3. Testing

Run the unit tests for the DOLPHIN pattern matching module:

```bash
pytest tests/test_patterns.py
```

## Modules

### `preprocess.py`

Cleans and preprocesses the input dataset. Filters out domains that match the whitelist and ensures all necessary fields are present.

### `dolphin_patterns.py`

Implements a greedy algorithm for matching predefined vowel and consonant patterns in domain names. Includes the `DolphinMatcher` class for pattern detection.

### `feature_extraction.py`

Computes features from the matched DOLPHIN patterns, such as vowel/consonant ratios, pattern diversity, and the maximum pattern length.

### `model_training.py`

Handles training and evaluation of a Random Forest classifier. Includes functionality for cross-validation, performance reporting, and feature importance analysis.

## Outputs

- **Console Logs**: The pipeline logs key metrics including cross-validation scores, classification reports, confusion matrices, and feature importances.
- **Model**: The trained Random Forest model is used for evaluation but not saved by default.

## Example Dataset

An example dataset (`data.csv`) is expected to have the following format:

| domain_name       | label |
|-------------------|-------|
| example.com       | 0     |
| malicious-site.io | 1     |
| benign.net        | 0     |

## Contributing

Contributions are welcome! Feel free to open issues or submit pull requests.
