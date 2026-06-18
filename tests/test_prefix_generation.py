import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1] / "src"))

import pandas as pd
import pytest
from prefix_extractor import compute_remaining_time, filter_short_prefixes
from config import TARGET_COLUMN


def test_compute_remaining_time():
    df = pd.DataFrame({
        "case_id": [1, 1],
        "timestamp": pd.to_datetime([
            "2026-01-01 10:00:00",
            "2026-01-01 10:10:00"
        ])
    })

    result = compute_remaining_time(df, "case_id", "timestamp")

    assert TARGET_COLUMN in result.columns
    assert result.loc[0, TARGET_COLUMN] == pytest.approx(1 / 6)
    assert result.loc[1, TARGET_COLUMN] == 0


def test_filter_short_prefixes():
    df = pd.DataFrame({
        "case_id": [1, 1, 2],
        "activity": ["A", "B", "A"]
    })

    result = filter_short_prefixes(df, "case_id", min_length=2)

    assert set(result["case_id"]) == {1}
