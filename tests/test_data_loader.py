import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1] / "remaining_time"))

import pandas as pd
import pytest
from data_loader import validate_columns


def test_validate_columns_success():
    df = pd.DataFrame(columns=["case_id", "activity", "timestamp"])

    validate_columns(df, ["case_id", "activity", "timestamp"])


def test_validate_columns_missing():
    df = pd.DataFrame(columns=["case_id", "activity"])

    with pytest.raises(ValueError):
        validate_columns(df, ["case_id", "activity", "timestamp"])
