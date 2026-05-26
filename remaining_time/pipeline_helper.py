import pandas as pd
from config import REQUIRED_COLUMNS, COLS_ENCODE, NUM_COLS_SCALE
from data_loader import load_data, validate_columns, sort_cases_by_timestamp, filter_completed_cases
from prefix_extractor import compute_remaining_time, filter_short_prefixes
from data_splitter import time_based_split
from feature_engineering import extract_static_case_attr, extract_aggr_dynamic_features, extract_temporal_features, encode_categorical_features, scale_numeric_features

# @para log:
#       type: pandas.DataFrame
#       content: the log to be split into a feature log and a numeric target log
# @para column_name:
#       type: str
#       content: the name of column within the log, which is the target column name
# @output:
#       type: 2 arity tuple of DataFrame
#       content: the first parameter is the feature log, the second is the target log
# functionality: split the log into a feature log and a numeric target log
def numeric_split(log, column_name):
    if not isinstance(log, pd.DataFrame):
        raise TypeError("The given log is not a data frame. ")
    if column_name not in log.columns:
        raise KeyError("No such column in the given log. ")
    target = log[[column_name]]
    feature = log.drop(columns=[column_name]).select_dtypes(include=["number"])
    return feature, target

# lazy caller copied from @Linas, this part is only designed for development usage, it'll be later merged into main.py
def preprocess_data():
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

    return train_log, val_log, test_log

# @para test_data:
#       type: pandas.DataFrame
#       content: the data frame for test data
# @output:
#       type: List of int
#       content: the variants of prefix lengths in the given test_data
# functionality: find out the list of  variants among prefix lengths
def get_variants(test_data):
    if not isinstance(test_data, pd.DataFrame):
        raise TypeError("The given log is not a data frame. ")
    try:
        case_lengths = test_data.groupby(REQUIRED_COLUMNS[0]).size()
        return sorted(case_lengths.unique())
    except KeyError:
        raise KeyError(f"The column {REQUIRED_COLUMNS[0]} does not exist. ")

# @para test_data:
#       type: pandas.DataFrame
#       content: the data frame for test data
# @para i:
#       type: int
#       content: the index within the prefix length variants list
# @output:
#       type: pandas.DataFrame
#       content: the test_data with certain prefix length
# functionality: split the test data according to the given index of prefix length
def get_log_with_length_index(test_data, i):
    if not isinstance(test_data, pd.DataFrame):
        raise TypeError("The given log is not a data frame. ")
    try:
        required_length = get_variants(test_data)[i]
        return test_data.groupby(REQUIRED_COLUMNS[0]).filter(lambda x: len(x) == required_length)
    except IndexError:
        raise IndexError(f"Index i is out of bound. ")
    except KeyError:
        raise KeyError("The column 0 does not exist. ")