import pandas as pd
import os

def add_labels_from_csv(input_file, output_file, num_lines=10000, label=1):
    """
    Add labels to domain names from a CSV file and append them to the output CSV.
    :param input_file: Path to the input CSV file
    :param output_file: Path to the output CSV file
    :param num_lines: Number of rows to process from the input file (default 10000)
    :param label: Label to assign to domains (default is 1 for malicious)
    """
    domain_data = []

    # Read the input CSV file
    df = pd.read_csv(input_file)

    # Check if the CSV file has at least one column
    if df.empty:
        print("The input file is empty.")
        return

    # Iterate through the first 'num_lines' rows and extract the domain name (first column)
    for i in range(min(num_lines, len(df))):
        domain_name = df.iloc[i, 0]  # Extract the first column (domain)
        domain_data.append([domain_name, label])  # Add domain and label (1)

    # Create a DataFrame from the collected domain names and labels
    new_df = pd.DataFrame(domain_data, columns=['domain_name', 'label'])

    # Check if the output file exists and append if it does, otherwise create the file
    if os.path.exists(output_file):
        new_df.to_csv(output_file, mode='a', header=False, index=False)
    else:
        new_df.to_csv(output_file, mode='w', header=True, index=False)

def add_labels_from_txt(input_file, output_file, num_lines=1000, label=0):
    """
    Add labels to domain names from a text file and append them to the output CSV.
    :param input_file: Path to the input text file
    :param output_file: Path to the output CSV file
    :param num_lines: Number of lines to process from the input file (default 10000)
    :param label: Label to assign to domains (default is 0 for benign)
    """
    domain_data = []

    # Open the input file to read domain names
    with open(input_file, 'r') as file:
        # Read the first 'num_lines' lines
        for i, line in enumerate(file):
            if i >= num_lines:
                break
            domain_name = line.strip()  # Remove any extra whitespace/newlines
            domain_data.append([domain_name, label])  # Add domain and label (0)

    # Create a DataFrame from the collected domain names and labels
    df = pd.DataFrame(domain_data, columns=['domain_name', 'label'])

    # Check if the output file exists and append if it does, otherwise create the file
    if os.path.exists(output_file):
        df.to_csv(output_file, mode='a', header=False, index=False)
    else:
        df.to_csv(output_file, mode='w', header=True, index=False)

# Input and output file paths
input_file_csv = 'mal.csv'  # Replace with your input CSV file (malicious domains)
input_file_txt = 'alexa-domains.txt'  # Replace with your input text file (benign domains)
output_file = 'data.csv'  # Output file where domain names with labels will be stored

# Add labels to the first 10,000 domains from the CSV file (label 1 for malicious)
add_labels_from_csv(input_file_csv, output_file, num_lines=10000, label=1)

# Add labels to the first 10,000 domains from the text file (label 0 for benign)
add_labels_from_txt(input_file_txt, output_file, num_lines=1000, label=0)
