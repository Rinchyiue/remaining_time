"""
A module for the pipeline of the system.
"""
from config import REQUIRED_COLUMNS
from data_loader import load_data, validate_columns, sort_cases_by_timestamp
from prefix_extractor import compute_remaining_time, filter_short_prefixes


def main():
    print("--- Starting pipeline for remaining time ---")

    # 1. Loading the data
    log = load_data()

    # 2. Validating the existence of the essential columns within the data
    validate_columns(log, REQUIRED_COLUMNS)

    # 3. Sorting of the cases by timestamp
    log = sort_cases_by_timestamp(log, REQUIRED_COLUMNS[0], REQUIRED_COLUMNS[2])

    # 4. Computing remaining time of each prefix of a case within a new column
    log = compute_remaining_time(log, REQUIRED_COLUMNS[0], REQUIRED_COLUMNS[2])

    # 5. Filtering out cases with less than min_length events
    log = filter_short_prefixes(log, REQUIRED_COLUMNS[0], min_length=2)

    # display of essential columns for testing purposes
    display_columns = [REQUIRED_COLUMNS[0], REQUIRED_COLUMNS[1], REQUIRED_COLUMNS[2], "remaining_time"]
    print(log[display_columns].head())


if __name__ == "__main__":
    main()