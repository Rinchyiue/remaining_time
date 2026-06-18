import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1] / "src"))

import pandas as pd
from data_loader import validate_columns, sort_cases_by_timestamp
from prefix_extractor import compute_remaining_time, filter_short_prefixes
from config import TARGET_COLUMN


# Test the basic preprocessing pipeline on a small synthetic event log
def test_basic_pipeline_smoke():

    log = pd.DataFrame({
        "case_id": [1, 1, 2, 2],
        "activity": ["A", "B", "A", "B"],
        "timestamp": pd.to_datetime([
            "2026-01-01 10:10:00",
            "2026-01-01 10:00:00",
            "2026-01-01 11:00:00",
            "2026-01-01 11:20:00"
        ])
    })

    required_columns = ["case_id", "activity", "timestamp"]

    validate_columns(log, required_columns)

    sorted_log = sort_cases_by_timestamp(log, "case_id", "timestamp")
    result = compute_remaining_time(sorted_log, "case_id", "timestamp")
    result = filter_short_prefixes(result, "case_id", min_length=2)

    assert TARGET_COLUMN in result.columns
    assert len(result) == 4
    assert result.groupby("case_id").size().tolist() == [2, 2]
    assert result["remaining_time"].min() == 0
