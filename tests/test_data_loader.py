from remaining_time.data_loader import validate_columns
import pandas as pd
import pytest


def test_validate_columns_success():
    df = pd.DataFrame(columns=["case_id", "activity", "timestamp"])

    validate_columns(df, ["case_id", "activity", "timestamp"])


def test_validate_columns_missing():
    df = pd.DataFrame(columns=["case_id", "activity"])

    with pytest.raises(ValueError):
        validate_columns(df, ["case_id", "activity", "timestamp"])
