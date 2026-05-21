from config import REQUIRED_COLUMNS
from data_loader import load_data, validate_columns, sort_cases_by_timestamp
from prefix_extractor import compute_remaining_time, filter_short_prefixes


# An intermediate file for easy calls, copied from @Linas
def getLog():
    log = load_data()
    validate_columns(log, REQUIRED_COLUMNS)
    log = sort_cases_by_timestamp(log, REQUIRED_COLUMNS[0], REQUIRED_COLUMNS[2])
    log = compute_remaining_time(log, REQUIRED_COLUMNS[0], REQUIRED_COLUMNS[2])
    log = filter_short_prefixes(log, REQUIRED_COLUMNS[0], min_length=2)
    display_columns = [REQUIRED_COLUMNS[0], REQUIRED_COLUMNS[1], REQUIRED_COLUMNS[2], "remaining_time"]
    return display_columns