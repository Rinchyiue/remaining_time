"""
A module containing baseline models to benchmark more advanced models.
"""

from model_evaluation import myScore

def mean_predictor(train_log, test_log, target_col="remaining_time"):
    """
    Predicts mean remaining time of all training prefixes.
    :param train_log: pandas.DataFrame with the training log
    :param test_log: pandas.DataFrame with the test log (or validation log if wanted)
    :param target_col: String with the name of the remaining time column
    :return: Tuple of (pandas.DataFrame with predictions, Array of Scores)
    """
    print("--- Running Mean Baseline Predictor ---")

    mean_remaining_time = train_log[target_col].mean()
    print(f"The mean remaining time of all training prefixes is {mean_remaining_time:.4f} hours.")

    test_log_prediction = test_log.copy()
    test_log_prediction["prediction"] = mean_remaining_time

    metrics_array = myScore(test_log_prediction[target_col], test_log_prediction["prediction"])
    mae, rmse, medae, r2 = metrics_array

    print(f"Baseline Results:")
    print(f"  MAE:   {mae:.4f} hours")
    print(f"  RMSE:  {rmse:.4f} hours")
    print(f"  MedAE: {medae:.4f} hours")
    print(f"  R2:    {r2:.4f}")

    return test_log_prediction, metrics_array
