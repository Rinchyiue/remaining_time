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
#           - combine classification methods -> group and label the prefix traces (not merely absolute variances)
#           - more process respectives (e.g. resource sequence/combination ...)
# goal: find out "good" coefficients w = (w1,...,wn) and intercept w0

import numpy as np
from sklearn.linear_model import LinearRegression
import model_evaluation

# model_1: ordinary least squares

# part_1: training
# use the training set
# @para x_train should be a matrix whose row represents a case (activity trace)
# @para y_train should be the target value (remaining time) to each case
x_train = np.array(train_matrix)
y_train = np.array(train_target)
reg_ols = LinearRegression()
reg_ols.fit(x_train, y_train)

# part_2: results
coef = reg_ols.coef_
incp = reg_ols.intercept_

# part_3: evaluation
# use the validation set
# since this is the first model, no Super value will be calculated
x_valid = np.array(valid_matrix)
y_valid = np.array(valid_target)
y_pred  = reg_ols.predict(x_valid)
ols_score = model_evaluation.myScore(y_valid,y_pred)