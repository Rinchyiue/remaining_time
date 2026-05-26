# Add the project module path so pytest can import files
# from the remaining_time package correctly
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1] / "remaining_time"))

# Import required libraries and functions to test
import numpy as np
from model_evaluation import myScore, validScore, loose_compare


# Test whether myScore() returns perfect metric values
# when predictions are exactly equal to true values
def test_myScore_perfect_prediction():

    # Example ground truth and prediction arrays
    y_true = np.array([1, 2, 3])
    y_pred = np.array([1, 2, 3])

    # Run the scoring function
    result = myScore(y_true, y_pred)

    # Expected:
    # MAE = 0
    # RMSE = 0
    # MedAE = 0
    # R2 = 1
    assert result[0] == 0
    assert result[1] == 0
    assert result[2] == 0
    assert result[3] == 1


# Test whether myScore() returns all four evaluation metrics
def test_myScore_returns_four_metrics():

    y_true = np.array([1, 2, 3])
    y_pred = np.array([1, 2, 4])

    result = myScore(y_true, y_pred)

    # The result should contain:
    # [MAE, RMSE, MedAE, R2]
    assert len(result) == 4


# Test whether validScore() returns a numeric score value
def test_validScore_returns_numeric_value():

    # Example metric values
    metrics = np.array([1.0, 2.0, 1.0, 0.8])

    # Run the validation score calculation
    result = validScore(metrics)

    # Check that the result is a numeric type
    assert isinstance(result, (float, np.floating))


# Test whether loose_compare() marks a model as best
# when its relative super value is not significantly worse
def test_loose_compare_marks_model_as_best_when_not_worse():

    # Example comparison against baseline
    rel_super_list = [("baseline", 0.01)]

    # Run loose comparison
    result = loose_compare("ridge", rel_super_list)

    # Expected behavior:
    # baseline should remain retained ("R")
    # ridge should become a best model ("Y")
    assert ("baseline", "R") in result
    assert ("ridge", "Y") in result
