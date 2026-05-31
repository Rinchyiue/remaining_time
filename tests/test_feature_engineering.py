import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1] / "remaining_time"))

import pandas as pd
import pytest

from feature_engineering import (
    extract_static_case_attr,
    extract_aggr_dynamic_features,
    extract_temporal_features,
    encode_categorical_features,
)


# This test checks whether static case attributes are correctly copied
# from the first event of each case to all events of the same case.
def test_extract_static_case_attr():

    log = pd.DataFrame({
        "case_id": [1, 1, 2, 2],
        "priority": ["high", "low", "medium", "medium"]
    })

    result = extract_static_case_attr(log, "case_id", ["priority"])

    assert "static_priority" in result.columns
    assert list(result["static_priority"]) == ["high", "high", "medium", "medium"]


# This test checks whether aggregated dynamic features are created correctly.
#
# event_count should increase within each case.
# elapsed_time should measure the time since the first event of the case in hours.
# activity_count should count how often the same activity appeared within the case.
def test_extract_aggr_dynamic_features():

    log = pd.DataFrame({
        "case_id": [1, 1, 1],
        "activity": ["A", "B", "A"],
        "timestamp": pd.to_datetime([
            "2026-01-01 10:00:00",
            "2026-01-01 11:00:00",
            "2026-01-01 12:00:00"
        ])
    })

    result = extract_aggr_dynamic_features(
        log,
        "case_id",
        "timestamp",
        "activity"
    )

    assert list(result["event_count"]) == [1, 2, 3]
    assert list(result["elapsed_time"]) == [0.0, 1.0, 2.0]
    assert list(result["activity_count"]) == [1, 1, 2]


# This test checks whether temporal features are extracted from timestamps.
#
# The function should create one-hot encoded columns for day_of_week and hour.
def test_extract_temporal_features():

    log = pd.DataFrame({
        "timestamp": pd.to_datetime([
            "2026-01-05 10:00:00"
        ])
    })

    result = extract_temporal_features(log, "timestamp")

    assert "day_of_week_0" in result.columns
    assert "hour_10" in result.columns


# This test checks whether categorical columns are one-hot encoded correctly.
def test_encode_categorical_features():

    log = pd.DataFrame({
        "activity": ["A", "B", "A"]
    })

    result = encode_categorical_features(log, ["activity"])

    assert "activity_A" in result.columns
    assert "activity_B" in result.columns
    assert list(result["activity_A"]) == [1, 0, 1]
