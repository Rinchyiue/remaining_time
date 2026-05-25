"""
A module for the pipeline of the system.
"""
import pm4py
import pandas as pd

from config import REQUIRED_COLUMNS, COLS_ENCODE, NUM_COLS_SCALE
from data_loader import load_data, validate_columns, sort_cases_by_timestamp, filter_completed_cases
from prefix_extractor import compute_remaining_time, filter_short_prefixes
from data_splitter import time_based_split
from feature_engineering import extract_static_case_attr, extract_aggr_dynamic_features, extract_temporal_features, encode_categorical_features, scale_numeric_features

def main():
    print("--- Starting pipeline for remaining time ---")

    # 1. Loading the data
    log = load_data()

    # 2. Validating the existence of the essential columns within the data
    validate_columns(log, REQUIRED_COLUMNS)

    # 3. Sorting of the cases by timestamp
    log = sort_cases_by_timestamp(log, REQUIRED_COLUMNS[0], REQUIRED_COLUMNS[2])

    # 4. Filtering cases that are not finished
    log = filter_completed_cases(log)

    # 5. Computing remaining time of each prefix of a case within a new column
    log = compute_remaining_time(log, REQUIRED_COLUMNS[0], REQUIRED_COLUMNS[2])

    # 6. Filtering out cases with less than min_length events
    log = filter_short_prefixes(log, REQUIRED_COLUMNS[0], min_length=2)

    # 7. Feature Engineering
    # 7.1. Extracting static case attributes
    log = extract_static_case_attr(log, REQUIRED_COLUMNS[0], ["impact", "product", "organization involved"])
    # 7.2. Extracting aggregated dynamic features
    log = extract_aggr_dynamic_features(log, REQUIRED_COLUMNS[0], REQUIRED_COLUMNS[2], REQUIRED_COLUMNS[1])
    # 7.3. Extracting temporal features
    log = extract_temporal_features(log, REQUIRED_COLUMNS[2])
    # 7.4. Encoding categorical features
    log = encode_categorical_features(log, COLS_ENCODE)

    # 8. Performing time-based data split (70% training, 15% validation and testing)
    train_log, val_log, test_log = time_based_split(log, REQUIRED_COLUMNS[0], REQUIRED_COLUMNS[2])

    # 9. Scaling numerical features
    train_log, val_log, test_log = scale_numeric_features(train_log, val_log, test_log, NUM_COLS_SCALE)

if __name__ == "__main__":
    main()