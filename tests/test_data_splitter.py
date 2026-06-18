import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1] / "src"))

import pandas as pd
from data_splitter import time_based_split


# This test checks whether the time-based split separates cases
# into train, validation, and test sets without mixing the same case
# across different splits.
#
# The split function sorts cases by their first timestamp and then
# assigns earlier cases to train, middle cases to validation,
# and later cases to test.
def test_time_based_split_does_not_mix_cases():

    log = pd.DataFrame({
        "case_id": [1, 1, 2, 2, 3, 3, 4, 4],
        "timestamp": pd.to_datetime([
            "2026-01-01 10:00:00",
            "2026-01-01 10:05:00",
            "2026-01-02 10:00:00",
            "2026-01-02 10:05:00",
            "2026-01-03 10:00:00",
            "2026-01-03 10:05:00",
            "2026-01-04 10:00:00",
            "2026-01-04 10:05:00",
        ])
    })

    train, val, test = time_based_split(
        log,
        "case_id",
        "timestamp",
        train_frac=0.5,
        val_frac=0.25
    )

    train_cases = set(train["case_id"])
    val_cases = set(val["case_id"])
    test_cases = set(test["case_id"])

    assert train_cases.isdisjoint(val_cases)
    assert train_cases.isdisjoint(test_cases)
    assert val_cases.isdisjoint(test_cases)


# This test checks whether the split respects time ordering.
#
# Since the cases are ordered by their start timestamp,
# earlier cases should be placed in the training set,
# the next case in the validation set,
# and the latest case in the test set.
def test_time_based_split_respects_case_start_order():

    log = pd.DataFrame({
        "case_id": [1, 1, 2, 2, 3, 3, 4, 4],
        "timestamp": pd.to_datetime([
            "2026-01-01 10:00:00",
            "2026-01-01 10:05:00",
            "2026-01-02 10:00:00",
            "2026-01-02 10:05:00",
            "2026-01-03 10:00:00",
            "2026-01-03 10:05:00",
            "2026-01-04 10:00:00",
            "2026-01-04 10:05:00",
        ])
    })

    train, val, test = time_based_split(
        log,
        "case_id",
        "timestamp",
        train_frac=0.5,
        val_frac=0.25
    )

    assert set(train["case_id"]) == {1, 2}
    assert set(val["case_id"]) == {3}
    assert set(test["case_id"]) == {4}
