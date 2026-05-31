# mathematical notation: y(w,x) = w0 + w1x1 + ... + wnxn
# goal: find out "good" coefficients w = (w1,...,wn) and intercept w0

import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import FunctionTransformer
from joblib import dump
from pipeline_helper import preprocess_data, numeric_split
from model_evaluation import evaluate_model

# --- part_1: get data ---
print(" --- start getting data --- ")
train_data, val_data, test_data = preprocess_data()
_, y_train = numeric_split(train_data, "remaining_time")

def split_numeric_X_train(df):
    if "remaining_time" in df.columns:
        return numeric_split(df, "remaining_time")[0]
    return df
preprocessor = FunctionTransformer(split_numeric_X_train)

# --- part_2: build and train pipeline ---
print(" --- start training linear regression pipeline --- ")
pipe = Pipeline(steps=[
    ('preprocessor', preprocessor),
    ('regressor', LinearRegression())
])
pipe.fit(train_data, y_train)

# --- part_3: results extraction ---
model_step = pipe.named_steps['regressor']
coef = model_step.coef_
incp = model_step.intercept_

coef_string = np.array2string(coef, precision=4, separator=', ')
result_string = f"coefficient: {coef_string}, intercept: {incp}"
print(" --- training completed --- ")

# --- part_4: evaluate the model ---
evaluate_model(pipe, "ols_pipeline", test_data, result_string)
print(" --- model evaluation done --- ")

# --- part_5: save model ---
print(" --- start saving pipeline --- ")
dump(pipe, 'reg_ols_pipeline.pkl')
print(" --- pipeline saved successfully --- ")