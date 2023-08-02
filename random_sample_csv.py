# This is the code I used to generate TNP_trips.py

import pandas as pd
import random

# Define the file paths
input_file_path = "Transportation_Network_Providers_-_Trips_-_2022.csv"
output_file_path = "TNP_trips.csv"

# Number of rows to sample
sample_size = 100000

# Load the entire CSV into a pandas DataFrame
df = pd.read_csv(input_file_path)

# Check if the number of rows in the DataFrame is smaller than the sample size
if len(df) <= sample_size:
    print("The sample size is larger than the number of rows in the input CSV.")
    print("The entire file will be copied to the output CSV.")
    df.to_csv(output_file_path, index=False)
else:
    # Sample 100,000 rows randomly without replacement
    random_sample = df.sample(n=sample_size, random_state=42)

    # Write the random sample to the new CSV file
    random_sample.to_csv(output_file_path, index=False)

print("Random sample created and saved as TNP_trips.csv.")