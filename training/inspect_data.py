import pandas as pd

from huggingface_hub import hf_hub_download


train_path = hf_hub_download(
    repo_id="Cleanlab/amazon-reviews",
    filename="train.csv",
    repo_type="dataset",
)

test_path = hf_hub_download(
    repo_id="Cleanlab/amazon-reviews",
    filename="test.csv",
    repo_type="dataset",
)

train_df = pd.read_csv(train_path)
test_df = pd.read_csv(test_path)

print("Training shape:")
print(train_df.shape)

print("\nTest shape:")
print(test_df.shape)

print("\nColumns:")
print(train_df.columns.tolist())

print("\nFirst 5 rows:")
print(train_df.head())

print("\nMissing values:")
print(train_df.isnull().sum())

print("\nLabel distribution:")
print(train_df.iloc[:, -1].value_counts())