from pathlib import Path
import pandas as pd

# Get project folder
BASE_DIR = Path(__file__).resolve().parent

# Load dataset
data = pd.read_csv(
    BASE_DIR / "dataset.csv",
    encoding="latin-1"
)

# Keep only useful columns
data = data[["v1", "v2"]]

# Rename columns
data.columns = ["label", "message"]

print("Dataset loaded successfully!")

print("\nFirst 5 rows:")
print(data.head())

print("\nSpam/Ham counts:")
print(data["label"].value_counts())

print("\nDataset shape:")
print(data.shape)