"""
Script to set up the environment and download+extract the raw data
"""

import os
import urllib.request
import zipfile
from config import RAW_DIR, PROCESSED_DIR

# module-specific configuration
DATA_URL = "https://data.4tu.nl/ndownloader/items/0fc5c579-e544-4fab-9143-fab1f5192432/versions/1"
ZIP_FILE_PATH = os.path.join(RAW_DIR, "BPI_Challenge_2013.zip")


def setup_environment():
    print("Creating directories...")
    os.makedirs(RAW_DIR, exist_ok=True)
    os.makedirs(PROCESSED_DIR, exist_ok=True)
    print(f"Directory '{RAW_DIR}' and '{PROCESSED_DIR}' have been created successfully.")


def download_data():
    if os.path.exists(ZIP_FILE_PATH):
        print(f"{ZIP_FILE_PATH} already exists. Skipping download.")
        return True

    print(f"Downloading data from: {DATA_URL}")
    print("Downloading data...")

    try:
        urllib.request.urlretrieve(DATA_URL, ZIP_FILE_PATH)
        print("Download has finished successfully.")
        return True
    except Exception as e:
        print(f"Error while downloading: {e}")
        return False


def extract_data():
    print(f"Extracting {ZIP_FILE_PATH}...")
    try:
        with zipfile.ZipFile(ZIP_FILE_PATH, 'r') as zip_ref:
            zip_ref.extractall(RAW_DIR)
        print(f"Data has been extracted into '{RAW_DIR}' successfully.")
        os.remove(ZIP_FILE_PATH)

    except Exception as e:
        print(f"Error while extracting: {e}")


if __name__ == "__main__":
    print("--- Starting data setup for remaining_time ---")
    setup_environment()

    if download_data():
        extract_data()

    print("--- Setup done ---")