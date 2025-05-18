import numerapi
import pandas as pd

# Initialize Numerai API
napi = numerapi.NumerAPI()

# Download latest training data
current_round = napi.get_current_round()
#print(f"Downloading Numerai round {current_round} data...")

# list the datasets and available versions
all_datasets = napi.list_datasets()
dataset_versions = list(set(d.split('/')[0] for d in all_datasets))
print("Available versions:\n", dataset_versions)

# Set data version to one of the latest datasets
DATA_VERSION = "v5.0"

# Print all files available for download for our version
current_version_files = [f for f in all_datasets if f.startswith(DATA_VERSION)]
print("Available", DATA_VERSION, "files:\n", current_version_files)
#napi.download_dataset(f"v5.0/train.parquet", "train_v5_0.parquet")

# Load into DataFrame
#nemam dosta mozak od racnolo :/ -> try dask or see if you can load subset of parquet
df = pd.read_parquet("train_v5_0.parquet", engine='pyarrow')

print(df.head())
print(f"Dataset shape: {df.shape}")

