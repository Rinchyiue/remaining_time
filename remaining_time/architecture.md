__init__.py: dummy file to make this directory a python package.

baseline.py: the baseline predictor function and baseline model saving function which also initialize model_metrics.csv and model_scores.csv.

checker.py: checker functions for format, like pandas.DataFrame.

config.py: central configuration file containing declarations used in multiple modules.

data_loader.py: a module for basic loading, validation and sorting of raw data.

data_splitter.py: a module for performing the time-based data split.

feature_engineering.py: a module for feature engineering, including encoding from prefixes to feature vectors.

linear_regression.py: functions and the pipeline to train the linear regression model.

main.py: a module for the pipeline of the system.

model_evaluation.py: functions to evaluate the models, as well as compare and update the results. 

pipeline_demo.py: the pipeline for the baseline model.

pipeline_helper.py: helper functions for pipeline, also contains some getter functions.

prefix_extracter.py: a module for computing remaining time for each prefix per case; also used for filtering cases with less than min_length events.

ridge_regression.py: functions and the pipeline to train the ridge regression model, and uses grid search cross validation to select hyperparameter alpha, which is finally 100.

score_management.py: functions to manage model scores.

visualization.py: functiosn to provide visualizations whose resulting plots can be found in outputs/plots.
