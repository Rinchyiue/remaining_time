def validate_required_columns(columns):
    required_columns = {"case_id", "activity", "timestamp"}

    return required_columns.issubset(set(columns))


def test_required_columns_present():
    columns = ["case_id", "activity", "timestamp", "priority"]

    assert validate_required_columns(columns) is True
