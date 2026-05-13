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

import main
import score_management
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
import model_evaluation
from joblib import dump

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

x_train = main().getTrainData()[:,:-1]                 # all columns except the last one
y_train = main().getTrainData()[:,-1]                  # only the last column
reg_ols = LinearRegression()
reg_ols.fit(x_train, y_train)

# part_2: results
coef = reg_ols.coef_
incp = reg_ols.intercept_

# part_3: select hyperparameters (omitted, because ols is a naive regression model without hyperparameter)

# part_4: evaluate the model
# use the test set
# iterate over prefix lengths and store metrics respectively in rows of scores
scores = np.empty((0,5))                                # empty matrix with exact 5 columns

df = pd.read_csv("model_metrics.csv")
for i in range(main().getVariance()):                   # main().getVariance() returns the number of variance of prefix lengths (and assume that they are enumerated)
    x_test = main().getTestData(i)[:,:-1]               # getTestData(i) is the only data getter which requires a prefix length to obtain data set
    y_test = main().getTestData(i)[:,-1]
    y_pred  = reg_ols.predict(x_test)
    ols_score = model_evaluation.myScore(y_test,y_pred)
    score_management.add_new_line(df, "ols", main().getLength(i), ols_score)    # getLength(i) returns the prefix length value of index i

    scores = np.vstack([scores, np.insert(ols_score, 0, main().getLength(i))])    # create and append a new row with ols_score and the current prefix length (prepended)
df.to_csv("model_metrics.csv", index=False)

# mySuper() should be implemented, scoreLists & freqLists should be loaded/called

ols_abs_super = model_evaluation.mySuper(freqList, scoreList1, scoreList2)
super_val = model_evaluation.mySuper(freqList, scoreList1, scoreList2)

# Store into model_scores.csv
to_change = False
best = "N"
if super_val > 0.05:
    best = "Y"
    to_change = True
elif super_val >= -0.05:
    best = "Y"

# if to_change, use disprefer()





# part_5: save model
dump(reg_ols, 'reg_ols.pkl')