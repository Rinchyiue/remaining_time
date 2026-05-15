from config import TARGET_COLUMN

def compute_remaining_time(log, case_id_col, timestamp_col):
    print("Computing remaining time for each prefix...")
    log["case_end_timestamp"] = log.groupby(case_id_col)[timestamp_col].transform("max")
    log[TARGET_COLUMN] = (log["case_end_timestamp"] - log[timestamp_col]).dt.total_seconds()
    log.drop(columns=["case_end_timestamp"], inplace=True)
    print("Remaining time for each prefix has been computed successfully.")
    return log

def filter_short_prefixes(log, case_id_col, min_length):
    print(f"Filtering cases with less than {min_length} events...")
    log = log.groupby(case_id_col).filter(lambda x: len(x) >= min_length)
    print("Cases have been filtered successfully.")
    return log