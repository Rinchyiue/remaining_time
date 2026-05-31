import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1] / "remaining_time"))

import pandas as pd
from model_evaluation import myScore, validScore, loose_compare


# This test verifies that myScore() returns the ideal metric values
# when predictions perfectly match the ground truth.
#
# Expected behaviour:
# MAE   = 0
# RMSE  = 0
# MedAE = 0
# R²    = 1
#
# This is an important sanity check because a perfect prediction
# should always produce perfect evaluation metrics.
def test_myScore_perfect_prediction():

    y_true = pd.DataFrame([1, 2, 3])
    y_pred = pd.DataFrame([1, 2, 3])

    result = myScore(y_true, y_pred)

    assert result[0] == 0
    assert result[1] == 0
    assert result[2] == 0
    assert result[3] == 1


# This test verifies that myScore() returns all expected metrics.
#
# According to the project design, myScore() should return:
# [MAE, RMSE, MedAE, R²]
#
# The test does not validate the exact values here,
# only that all four metrics are present.
def test_myScore_returns_four_metrics():

    y_true = pd.DataFrame([1, 2, 3])
    y_pred = pd.DataFrame([1, 2, 4])

    result = myScore(y_true, y_pred)

    assert len(result) == 4


# This test checks that validScore() produces a single
# numerical score from the four evaluation metrics.
#
# The resulting score is later used to compare different models,
# so it should always be a numeric value.
def test_validScore_returns_numeric_value():

    metrics = [1.0, 2.0, 1.0, 0.8]

    result = validScore(metrics)

    assert isinstance(result, float)


# This test verifies the decision logic of loose_compare().
#
# In this example the new model ("ridge") performs similarly
# to the current best model ("baseline"), therefore:
#
# - baseline should be retained ("R")
# - ridge should be accepted as a best model ("Y")
#
# This ensures that the comparison logic correctly handles
# models that are not significantly worse than the current best.
def test_loose_compare_marks_model_as_best_when_not_worse():

    rel_super_list = [("baseline", 0.01)]

    result = loose_compare("ridge", rel_super_list)

    assert ("baseline", "R") in result
    assert ("ridge", "Y") in result
