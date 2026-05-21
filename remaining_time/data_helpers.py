from config import REQUIRED_COLUMNS
from data_loader import load_data, validate_columns, sort_cases_by_timestamp
from prefix_extractor import compute_remaining_time, filter_short_prefixes

# lazy caller copied from @Linas
def preprocess_data():
    log = load_data()
    validate_columns(log, REQUIRED_COLUMNS)
    log = sort_cases_by_timestamp(log, REQUIRED_COLUMNS[0], REQUIRED_COLUMNS[2])
    log = compute_remaining_time(log, REQUIRED_COLUMNS[0], REQUIRED_COLUMNS[2])
    log = filter_short_prefixes(log, REQUIRED_COLUMNS[0], min_length=2)
    display_columns = [REQUIRED_COLUMNS[0], REQUIRED_COLUMNS[1], REQUIRED_COLUMNS[2], "remaining_time"]
    return log[display_columns]

# @para test_data:
#       type: pandas.DataFrame
#       content: the data frame for test data
# @output:
#       type: List of int
#       content: the variants of prefix lengths in the given test_data
# functionality: find out the list of  variants among prefix lengths
def get_variants(test_data):
    return sorted(test_data[REQUIRED_COLUMNS[0]].apply(len).unique())

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
    required_length = get_variants(test_data)[i]
    return test_data.groupby(REQUIRED_COLUMNS[0]).filter(lambda x: len(x) == required_length)