# DOLPHIN Pattern Detection and Feature Extraction

This repository implements a system for detecting DOLPHIN patterns in domain names, extracting features based on these patterns, and training a classification model to identify malicious domains. The project is based on the paper ["DOLPHIN: Phonetics-Aware Detection of Malicious Domain Names"](https://aquatoney.github.io/files/dolphin-fgcs23-zhao.pdf) by Zhao et al., published in *Future Generation Computer Systems (2023)*. It includes modules for preprocessing datasets, applying pattern matching algorithms, extracting features, and training machine learning models.

## Features

- **DOLPHIN Pattern Matching**: Identifies predefined vowel and consonant patterns in domain names using a greedy matching algorithm.
- **Feature Extraction**: Computes phonics-based features such as vowel and consonant ratios, pattern diversity, and maximum pattern length.
- **Machine Learning Model**: Trains and evaluates a Random Forest classifier to classify domain names.
- **Preprocessing**: Handles data cleaning, filtering, and integration of a whitelist to exclude benign domains.

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

- Place your dataset file in the datasets/ directory and modify the path in `DOLPHIN.ipynb`.
- Ensure the dataset has the following columns: isDGA,domain,host,subclass. Or edit the file `DOLPHIN.ipynb` to match your datasets.
- If you have a whitelist of domains, place them in `whitelist.txt` (one domain per line).

### 2. Run the Main Pipeline

Run the full pipeline in `DOLPHIN.ipynb`.

This will:

1. Preprocess the dataset and exclude whitelisted domains.
2. Perform DOLPHIN pattern matching on the domain names.
3. Extract phonics-based features.
4. Train and evaluate a Random Forest model.

## Outputs

- **Console Logs**: The pipeline logs key metrics including cross-validation scores, classification reports, confusion matrices, and feature importances.
- **Model**: The trained Random Forest model is used for evaluation but not saved by default.

## Contributing

Contributions are welcome! Feel free to open issues or submit pull requests.
