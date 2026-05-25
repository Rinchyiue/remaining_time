"""
A module for basic loading, validation and sorting of raw data.
"""

import pm4py
from config import XES_FILE_PATH

def load_data():
    """
    Loads raw data from XES file.
    :return: pandas.DataFrame with the raw data
    """
    print("Loading log...")
    log = pm4py.read_xes(XES_FILE_PATH)
    print("Log loaded successfully.")
    return log

def validate_columns(log, required_columns):
    """
    Validates if required columns are present in the log.
    :param log: pandas.DataFrame with the log
    :param required_columns: list of required columns
    """
    print("Validating columns...")
    for column in required_columns:
        if column not in log.columns:
            raise ValueError(f"Column '{column}' is missing from log.")
    print("Columns validated successfully.")

def sort_cases_by_timestamp(log, case_id_col, timestamp_col):
    """
    Sorts cases by timestamp.
    :param log: pandas.DataFrame with the log
    :param case_id_col: String with the name of the case ID column
    :param timestamp_col: String with the name of the timestamp column
    :return: pandas.DataFrame with the sorted log
    """
    print("Sorting cases by timestamp...")
    # Sorting values by case_id first and by timestamp for rows with the same case_id
    log.sort_values([case_id_col, timestamp_col], ascending=True, inplace=True)
    print("Cases sorted successfully.")
    return log

def filter_completed_cases(log, valid_end_activities=["Completed"]):
    """
    Filters the event log to keep only cases that successfully finished.
    :param log: pandas.DataFrame with the log
    :param valid_end_activities: list of valid end activities
    :return: pandas.DataFrame with the filtered log
    """
    print(f"Filtering for completed cases ending with {valid_end_activities}...")
    return pm4py.filter_end_activities(log, valid_end_activities)