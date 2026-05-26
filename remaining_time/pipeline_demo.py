# WARNING: this is not a pipeline yet, only for testing purpose
import pandas as pd
from pipeline_helper import numeric_split, preprocess_data
from baselines import mean_predictor, save_baseline

train_log, val_log, test_log = preprocess_data()

# only to test the baseline model functionality
x_train, y_train = numeric_split(train_log, "remaining_time")
x_test, y_test = numeric_split(test_log, "remaining_time")

mean_remaining_time = mean_predictor(y_train)
save_baseline(test_log, mean_remaining_time)