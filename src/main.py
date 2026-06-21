# --- START OF FILE main.py ---
"""
A module for the full preprocessing and model training pipeline.
"""
import pm4py
import pandas as pd

from config import REQUIRED_COLUMNS, COLS_ENCODE, NUM_COLS_SCALE
from data_loader import load_data, validate_columns, sort_cases_by_timestamp, filter_completed_cases
from prefix_extractor import compute_remaining_time, filter_short_prefixes
from data_splitter import time_based_split
from feature_engineering import (extract_static_case_attr, extract_aggr_dynamic_features, extract_temporal_features, encode_categorical_features, scale_numeric_features)
from baselines import mean_predictor, save_baseline
from run_pipeline import run_ols_pipeline, run_ridge_pipeline
from visualization import run_all_visualizations

def run_preprocessing():
    print("--- Starting Preprocessing ---")
    log = load_data()
    validate_columns(log, REQUIRED_COLUMNS)
    log = sort_cases_by_timestamp(log, REQUIRED_COLUMNS[0], REQUIRED_COLUMNS[2])
    log = filter_completed_cases(log)
    log = compute_remaining_time(log, REQUIRED_COLUMNS[0], REQUIRED_COLUMNS[2])
    log = filter_short_prefixes(log, REQUIRED_COLUMNS[0], min_length=2)

    log = extract_static_case_attr(log, REQUIRED_COLUMNS[0], ["impact", "product", "organization involved"])
    log = extract_aggr_dynamic_features(log, REQUIRED_COLUMNS[0], REQUIRED_COLUMNS[2], REQUIRED_COLUMNS[1])
    log = extract_temporal_features(log, REQUIRED_COLUMNS[2])
    log = encode_categorical_features(log, COLS_ENCODE)

    train_log, val_log, test_log = time_based_split(log, REQUIRED_COLUMNS[0], REQUIRED_COLUMNS[2])
    train_log, val_log, test_log = scale_numeric_features(train_log, val_log, test_log, NUM_COLS_SCALE)
    
    return train_log, val_log, test_log

def main():
    train_log, val_log, test_log = run_preprocessing()
    print("\n--- Phase 1: Baseline Model ---")
    mean_val = mean_predictor(train_log, target_col="remaining_time")
    save_baseline(test_log, mean_val)

    print("\n--- Phase 2: OLS Regression ---")
    run_ols_pipeline(train_log, test_log)

    print("\n--- Phase 3: Ridge Regression ---")
    run_ridge_pipeline(train_log, val_log, test_log)

    print("\n--- All pipelines completed successfully ---")

    run_all_visualizations()

    print("\n--- All pipelines and visualizations completed successfully ---")

if __name__ == "__main__":
    main()