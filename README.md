# DOLPHIN Project

This project implements the DOLPHIN framework for detecting DGA-based botnets using phonics-based features.

## Structure

- `dolphin_patterns.py`: Defines patterns and matching logic.
- `feature_extraction.py`: Computes features based on DOLPHIN patterns.
- `preprocess.py`: Preprocesses the dataset.
- `model_training.py`: Handles training and evaluation.
- `main.py`: Runs the pipeline.
- `tests/`: Contains test cases.

## Usage

1. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

2. Run the pipeline:

   ```bash
   python main.py
   ```

3. Run tests:

   ```bash
   pytest tests/
   
