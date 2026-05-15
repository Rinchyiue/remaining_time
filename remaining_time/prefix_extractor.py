"""
A module for computing remaining time for each prefix per case.
Also used for filtering cases with less than min_length events.
"""

from config import TARGET_COLUMN

def compute_remaining_time(log, case_id_col, timestamp_col):
    """
    Computes the remaining time for each prefix per case.
    :param log: pandas.DataFrame with the log
    :param case_id_col: String with the name of the case ID column
    :param timestamp_col: String with the name of the timestamp column
    :return: pandas.DataFrame with the log containing a new column for the remaining time
    """
    print("Computing remaining time for each prefix...")
    # adds case_end_timestamp to each group of a case as a new column
    log["case_end_timestamp"] = log.groupby(case_id_col)[timestamp_col].transform("max")
    # computes remaining_time column as case_end_timestamp - timestamp of last event in seconds
    log[TARGET_COLUMN] = (log["case_end_timestamp"] - log[timestamp_col]).dt.total_seconds()
    # removes case_end_timestamp column
    log.drop(columns=["case_end_timestamp"], inplace=True)
    print("Remaining time for each prefix has been computed successfully.")
    return log

def filter_short_prefixes(log, case_id_col, min_length):
    """
    Filters cases with less than min_length events.
    :param log: pandas.DataFrame with the log
    :param case_id_col: String with the name of the case ID column
    :param min_length: Integer with the minimum number of events
    :return: pandas.DataFrame with the log without cases with less than min_length events
    """
    print(f"Filtering cases with less than {min_length} events...")
    log = log.groupby(case_id_col).filter(lambda x: len(x) >= min_length)
    print("Cases have been filtered successfully.")
    return log