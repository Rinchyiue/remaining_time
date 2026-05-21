# idea: minimize a penalized sum of squares: min ||y - Xw||^2_2 + alpha * ||w||^2_2
# ridge regression also follows y(w,x) = w0 + w1x1 + ... + wnxn of linear regression
# hyperparameter to tune: alpha

import pandas as pd
import numpy as np
from sklearn import linear_model
from joblib import dump
from data_helpers import preprocess_data
from data_splitter import time_based_split
from model_evaluation import myScore, validScore, evaluate_model
from config import REQUIRED_COLUMNS

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
train_data, val_data, test_data = time_based_split(log, REQUIRED_COLUMNS[0], REQUIRED_COLUMNS[2])

x_train = train_data[:,:-1]                 # all columns except the last one
y_train = train_data[:,-1]                  # only the last column

alphas = [0.0001, 0.001, 0.01, 0.1, 1, 10, 100, 1000]           # a set of alphas to try
models = [linear_model.Ridge(alpha=a) for a in alphas]          # a set of corresponding models
for model in models:
    model.fit(x_train, y_train)                        # train the models

# part_2: select hyperparameters
# use the validation set
x_valid = val_data[:,:-1]
y_valid = val_data[:,-1]

best_model = None
best_score = 0      # any model can have a score greater than 0 as the output of validScore() is defined in (0,1]
index = -1
for i in range(len(models)):
    pred = models[i].predict(x_valid)
    score_list = myScore(y_valid, pred)
    valid_score = validScore(score_list)
    if valid_score > best_score:
        best_score = valid_score
        best_model = models[i]
        index = i

tuned_alpha = alphas[index]     # index of alphas and models coincide

# part_3: retrain model
# base on both training set and validation set
x_retrain = pd.concat([x_train, x_valid])
y_retrain = pd.concat([y_train, y_valid])
cur_model = linear_model.Ridge(alpha=tuned_alpha)
cur_model.fit(x_retrain, y_retrain)

# part_4: results
coef = cur_model.coef_
coef_string = np.array2string(coef, precision=4, separator=', ')
incp = cur_model.intercept_
result_string = f"alpha: {tuned_alpha}, coefficient: {coef_string}, intercept: {incp:.4f}"

# part_5 evaluate the model
# use the test set
# iterate over prefix lengths and store metrics respectively in rows of scores
evaluate_model(cur_model, "ridge", test_data, result_string)

# part_6: save model
dump(cur_model, 'ridge.pkl')