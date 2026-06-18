"""
A module for performing the time-based data split.
"""

def time_based_split(log, case_id_col, timestamp_col, train_frac=0.7, val_frac=0.15):
    """
    Performs the time-based data split.
    :param log: pandas.DataFrame with the log
    :param case_id_col: String with the name of the case ID column
    :param timestamp_col: String with the name of the timestamp column
    :param train_frac: Float with the fraction of the training data
    :param val_frac: Float with the fraction of the validation data
    :return: Iterable with the pandas.DataFrames of each split
    """
    print("Performing time-based training/validation/testing split...")
    # determine start time of each case
    case_start_times = log.groupby(case_id_col)[timestamp_col].min()
    # sort cases ascending by start time
    case_start_times = case_start_times.sort_values(ascending=True)
    sorted_case_ids = case_start_times.index.tolist()

    total_cases = len(sorted_case_ids)
    train_end = int(total_cases * train_frac)
    val_end = train_end + int(total_cases * val_frac)

    train_case_ids = sorted_case_ids[:train_end]
    val_case_ids = sorted_case_ids[train_end:val_end]
    test_case_ids = sorted_case_ids[val_end:]

    # filters log by comparison to a mask containing true/false dependent on whether case is included in x_case_ids
    train_log = log[log[case_id_col].isin(train_case_ids)]
    val_log = log[log[case_id_col].isin(val_case_ids)]
    test_log = log[log[case_id_col].isin(test_case_ids)]

    print(f"Data splitting has been completed successfully. The data has been split into: "
          f"{len(train_case_ids)} training, {len(val_case_ids)} validation and {len(test_case_ids)} test cases. Total: {total_cases} cases.")

    return train_log, val_log, test_log