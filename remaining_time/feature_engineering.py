"""
A module for feature engineering, including encoding from prefixes to feature vectors.
"""

def extract_static_case_attr(log, case_id_col, static_columns):
    """
    :param log: pandas.DataFrame with the log
    :param case_id_col: String with the name of the case ID column
    :param static_columns: List of strings with the column names of the static case attributes
    :return: pandas.DataFrame with the log containing new columns for static case attributes
    """
    print(f"Extracting static case attributes for {static_columns}...")
    for column in static_columns:
        new_column = f"static_{column}"
        log[new_column] = log.groupby(case_id_col)[column].transform("first")
    return log

def extract_aggr_dynamic_features(log, case_id_col, timestamp_col, activity_col):
    """
    :param log: pandas.DataFrame with the log
    :param case_id_col: String with the name of the case ID column
    :param timestamp_col: String with the name of the timestamp column
    :param activity_col: String with the name of the activity column
    :return: pandas.DataFrame with the log containing new columns for aggregated dynamic features
    """
    log["event_count"] = log.groupby(case_id_col).cumcount() + 1
    case_start_timestamp = log.groupby(case_id_col)[timestamp_col].transform("first")
    log["elapsed_time"] = (log[timestamp_col] - case_start_timestamp).dt.total_seconds() / 3600.0
    log["activity_count"] = log.groupby([case_id_col, activity_col]).cumcount() + 1

    return log
