# preprocessed dataset (prefix set) should be imported
# mathematical notation: y(w,x) = w0 + w1x1 + ... + wnxn
# suggested features (which determines n):
#   baseline:
#           - time (derived duration)
#               - total duration before the inspected activity since start
#               - time since the inspected activity started
#               - duration of the inspected activity
#               - total duration after the inspected activity till completion
#           - trace (only prefix for now)
#               - prefix traces (merely variances)
#           - case ID
#           - case level attributes (e.g. cost, resource ...)
#   optional:
#           - event level attributes, esp. those of the inspected activity
#           - combine classification methods -> group and label the prefix traces (not merely absolute variances) => Pipeline
#           - more process respectives (e.g. resource sequence/combination ...)
# goal: find out "good" coefficients w = (w1,...,wn) and intercept w0

import numpy as np
from sklearn.linear_model import LinearRegression
from joblib import dump
from data_helpers import preprocess_data
from data_splitter import time_based_split
from model_evaluation import evaluate_model

# model_1: ordinary least squares
# assume that the main function can bring a dataframe which carries all precessed data
# best case: there's kinda distinguish among the three sets (key assumption: remaining time is stored in the last column)`

# Notice: No validation dataset is used, because ols is a naive regression model without hyperparameter

# part_1: training
# use the training set
# @para x_train:
#       type:       numpy.ndarray (two-dimensional)
#       content:    a matrix whose rows represent respectively a case (activity trace)
# @para y_train:
#       type:       numpy.ndarray
#       content:    a list of target values (remaining time) of each case
# Notice: x_train, y_train contains all training traces with all prefix lengths

log = preprocess_data()
train_data, val_data, test_data = time_based_split(log, 0, 2)

x_train = train_data[:,:-1]                 # all columns except the last one
y_train = train_data[:,-1]                  # only the last column
reg_ols = LinearRegression()
reg_ols.fit(x_train, y_train)

# part_2: results
coef = reg_ols.coef_
coef_string = np.array2string(coef, precision=4, separator=', ')
incp = reg_ols.intercept_
result_string = f"coefficient: {coef_string}, intercept: {incp:.4f}"

# part_3: select hyperparameters (omitted, because ols is a naive regression model without hyperparameter)

# part_4: evaluate the model
# use the test set
# iterate over prefix lengths and store metrics respectively in rows of scores
evaluate_model(reg_ols, "ols", test_data, result_string)

# part_5: save model
dump(reg_ols, 'reg_ols.pkl')