"""
A module for feature engineering, including encoding from prefixes to feature vectors.
"""

import pandas as pd

from sklearn.preprocessing import StandardScaler

def extract_static_case_attr(log, case_id_col, static_columns):
    """
    Extracts static case attributes.
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
    Extracts aggregated dynamic features.
    :param log: pandas.DataFrame with the log
    :param case_id_col: String with the name of the case ID column
    :param timestamp_col: String with the name of the timestamp column
    :param activity_col: String with the name of the activity column
    :return: pandas.DataFrame with the log containing new columns for aggregated dynamic features
    """
    print(f"Extracting aggregated dynamic features...")
    log["event_count"] = log.groupby(case_id_col).cumcount() + 1
    case_start_timestamp = log.groupby(case_id_col)[timestamp_col].transform("first")
    log["elapsed_time"] = (log[timestamp_col] - case_start_timestamp).dt.total_seconds() / 3600.0
    log["activity_count"] = log.groupby([case_id_col, activity_col]).cumcount() + 1
    return log

def extract_temporal_features(log, timestamp_col):
    """
    Extracts temporal features.
    :param log: pandas.DataFrame with the log
    :param timestamp_col: String with the name of the timestamp column
    :return: pandas.DataFrame with the log containing new columns for temporal features (one-hot encoding)
    """
    print("Extracting temporal features...")
    log["day_of_week"] = log[timestamp_col].dt.dayofweek.astype(str)
    log["hour"] = log[timestamp_col].dt.hour.astype(str)
    log = pd.get_dummies(log, columns=["day_of_week", "hour"], dtype=int)
    return log

def encode_categorical_features(log, categorical_cols):
    """
    Encodes categorical features using one-hot encoding.
    :param log: pandas.DataFrame with the log
    :param categorical_cols: List of strings with the column names of the categorical features
    :return: pandas.DataFrame with the log containing new columns for categorical features
    """
    print(f"Applying one-hot encoding to {categorical_cols}...")
    log = pd.get_dummies(log, columns=categorical_cols, dtype=int)
    return log

def scale_numeric_features(train_log, val_log, test_log, num_cols):
    """
    Scales numeric features using the StandardScaler.
    :param train_log: pandas.DataFrame with the training log
    :param val_log: pandas.DataFrame with the validation log
    :param test_log: pandas.DataFrame with the testing log
    :param num_cols: List of strings with the column names of the numeric features
    :return: pandas.Dataframes with scaled numeric features.
    """
    print("Scaling numerical features using StandardScaler...")
    sscaler = StandardScaler()
    train_log[num_cols] = sscaler.fit_transform(train_log[num_cols])
    val_log[num_cols] = sscaler.transform(val_log[num_cols])
    test_log[num_cols] = sscaler.transform(test_log[num_cols])
    return train_log, val_log, test_log

