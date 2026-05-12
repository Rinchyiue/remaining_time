import pm4py
from config import XES_FILE_PATH,  REQUIRED_COLUMNS

def load_data():
    print("Loading log...")
    log = pm4py.read_xes(XES_FILE_PATH)
    print("Log loaded successfully.")
    return log

def validate_columns(log, required_columns):
    print("Validating columns...")
    for column in required_columns:
        if column not in log.columns:
            raise ValueError(f"Column '{column}' is missing from log.")
    print("Columns validated successfully.")

def sort_cases_by_timestamp(log, case_id_col, timestamp_col):
    print("Sorting cases by timestamp...")
    log.sort_values([case_id_col, timestamp_col], ascending=True, inplace=True)
    print("Cases sorted successfully.")
    return log