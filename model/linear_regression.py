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
from sklearn.linear_model import LinearRegression
import model_evaluation
from joblib import dump

# model_1: ordinary least squares
# assume that the main function can bring a dataframe which carries all precessed data
# best case: there's kinda distinguish among the three sets (key assumption: remaining time is stored in the last column)`

# Notice: No validation dataset is used, because ols is a naive regression model without hyperparameter
# Warning: the perspective of prefix length (set of set) should be considered -> iterative

train_data = main().getTrainData()
test_data = main().getTestData()

# part_1: training
# use the training set
# @para x_train:
#       type:       numpy.ndarray (two-dimensional)
#       content:    a matrix whose rows represent respectively a case (activity trace)
# @para y_train:
#       type:       numpy.ndarray
#       content:    should be the target value (remaining time) to each case

x_train = train_data[:,:-1]                 # all columns except the last one
y_train = train_data[:,-1]                  # only the last column
reg_ols = LinearRegression()
reg_ols.fit(x_train, y_train)

# part_2: results
coef = reg_ols.coef_
incp = reg_ols.intercept_

# part_3: select hyperparameters (omitted, because ols is a naive regression model without hyperparameter)

# part_4: evaluate the model
# use the test set
x_test = test_data[:,:-1]
y_test = test_data[:,-1]
y_pred  = reg_ols.predict(x_test)
ols_score = model_evaluation.myScore(y_test,y_pred)

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

df = pd.read_csv("model_scores.csv")
score_management.add_new_line(df, "ols", length, ols_score, best, ols_abs_super, "coef: "+coef+" incp: "+incp)
df.to_csv("model_scores.csv", index=False)

# part_5: save model
dump(reg_ols, 'reg_ols.pkl')