# mathematical notation: y(w,x) = w0 + w1x1 + ... + wnxn
# goal: find out "good" coefficients w = (w1,...,wn) and intercept w0

import numpy as np
from sklearn.linear_model import LinearRegression
from joblib import dump
from pipeline_helper import preprocess_data, numeric_split
from model_evaluation import evaluate_model

# part_1: preprocess data
train_data, val_data, test_data = preprocess_data()
x_train, y_train = numeric_split(train_data, "remaining_time")
x_test, y_test = numeric_split(test_data, "remaining_time")

# part_2: train model
reg_ols = LinearRegression()
reg_ols.fit(x_train, y_train)

# part_2: results
coef = reg_ols.coef_
coef_string = np.array2string(coef, precision=4, separator=', ')
incp = reg_ols.intercept_
result_string = f"coefficient: {coef_string}, intercept: {incp}"

# part_3: evaluate the model
# use the test set
# iterate over prefix lengths and store metrics respectively in rows of scores
evaluate_model(reg_ols, "ols", test_data, result_string)

# part_4: save model
dump(reg_ols, 'reg_ols.pkl')