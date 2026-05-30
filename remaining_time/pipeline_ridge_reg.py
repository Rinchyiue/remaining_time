# idea: minimize a penalized sum of squares: min ||y - Xw||^2_2 + alpha * ||w||^2_2
# ridge regression also follows y(w,x) = w0 + w1x1 + ... + wnxn of linear regression
# hyperparameter to tune: alpha

import pandas as pd
import numpy as np
from sklearn.linear_model import Ridge
from sklearn.model_selection import GridSearchCV, PredefinedSplit
from sklearn.metrics import make_scorer
from joblib import dump
from pipeline_helper import preprocess_data, numeric_split, get_checked_prefix
from model_evaluation import myScore, validScore, evaluate_model
from sklearn.pipeline import Pipeline

# part_0: make the score
print(" --- start making score --- ")
def score_func(y_valid, pred):
    score_list = myScore(pd.DataFrame(y_valid), pd.DataFrame(pred))
    valid_score = validScore(score_list)
    return valid_score
score = make_scorer(score_func, greater_is_better=True)
print(" --- score established --- ")

# part_1: preprocess data
print( " --- start preprocessing data --- ")
train_data, val_data, test_data = preprocess_data()
x_train, y_train = numeric_split(train_data, "remaining_time")
x_valid, y_valid = numeric_split(val_data, "remaining_time")

# combine the validation set and training set for cross validation using predefined split
x_combined = pd.concat([x_train, x_valid])
y_combined = pd.concat([y_train, y_valid])
train_indices = np.full(x_train.shape[0], -1)
val_indices = np.full(x_valid.shape[0], 0)
test_fold = np.concatenate([train_indices, val_indices])
split = PredefinedSplit(test_fold)

print(" --- data prepared --- ")

# part_2: set up GridSearchCV
print(" --- start grid search cross validation --- ")
model = Ridge()
pipe = Pipeline([('model', model)])
param_grid = [{'model__alpha':[0.0001, 0.001, 0.01, 0.1, 1, 10, 100, 1000]}]
grid_search = GridSearchCV(
    estimator=pipe,
    param_grid=param_grid,
    cv=split,
    scoring=score
)

grid_search.fit(x_combined, y_combined)
best_alpha = grid_search.best_params_['model__alpha']
print(f"Best alpha found: {best_alpha}")
print(" --- grid search cross validation done --- ")

# part_3: retrain the model with the found best alpha
print(" --- start retraining --- ")
pipe.set_params(model__alpha = best_alpha)
pipe.fit(x_combined, y_combined)

coef = pipe.named_steps['model'].coef_
coef_string = np.array2string(coef, precision=4, separator=', ')
incp = pipe.named_steps['model'].intercept_
result_string = f"alpha: {best_alpha}, coefficient: {coef_string}, intercept: {incp}"
print(" --- retrain completed --- ")

# part_5: evaluate the model
evaluate_model(pipe, "pipe_ridge", test_data, result_string)
print(" --- evaluation done --- ")

# part_6: save model
print(" --- saving model --- ")
dump(pipe, 'pipe_ridge.pkl')
print(" --- model saved --- ")