import os
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression, Ridge
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import FunctionTransformer
from sklearn.model_selection import GridSearchCV, PredefinedSplit
from sklearn.metrics import make_scorer
from joblib import dump
from config import ARTIFACTS_DIR

from pipeline_helper import numeric_split
from model_evaluation import myScore, validScore, evaluate_model

def split_numeric_X(df):
    if isinstance(df, pd.DataFrame):
        if "remaining_time" in df.columns:
            return df.drop(columns=["remaining_time"]).select_dtypes(include=["number"])
        return df.select_dtypes(include=["number"])
    return df

def run_ols_pipeline(train_data, test_data):
    print(" --- start training linear regression pipeline (OLS) --- ")
    _, y_train = numeric_split(train_data, "remaining_time")

    preprocessor = FunctionTransformer(split_numeric_X)

    pipe = Pipeline(steps=[
        ('preprocessor', preprocessor),
        ('regressor', LinearRegression())
    ])
    
    pipe.fit(train_data, y_train)

    model_step = pipe.named_steps['regressor']
    result_string = f"coefficient: {np.array2string(model_step.coef_, precision=4)}, intercept: {model_step.intercept_}"
    
    evaluate_model(pipe, "ols_pipeline", test_data, result_string)
    save_path = os.path.join(ARTIFACTS_DIR, 'reg_ols_pipeline.pkl')
    dump(pipe, save_path)
    print(" --- OLS pipeline completed and saved --- ")

def run_ridge_pipeline(train_data, val_data, test_data):
    print(" --- start training ridge regression pipeline --- ")
    
    def score_func(y_valid, pred):
        return validScore(myScore(pd.DataFrame(y_valid), pd.DataFrame(pred)))
    
    custom_scorer = make_scorer(score_func, greater_is_better=True)

    x_train, y_train = numeric_split(train_data, "remaining_time")
    x_valid, y_valid = numeric_split(val_data, "remaining_time")

    x_combined = pd.concat([x_train, x_valid])
    y_combined = pd.concat([y_train, y_valid])
    
    test_fold = np.concatenate([
        np.full(x_train.shape[0], -1), 
        np.full(x_valid.shape[0], 0)
    ])
    split = PredefinedSplit(test_fold)

    pipe = Pipeline([('model', Ridge())])
    param_grid = [{'model__alpha': [0.0001, 0.001, 0.01, 0.1, 1, 10, 100, 1000]}]
    
    grid_search = GridSearchCV(estimator=pipe, param_grid=param_grid, cv=split, scoring=custom_scorer)
    grid_search.fit(x_combined, y_combined)
    
    best_alpha = grid_search.best_params_['model__alpha']
    pipe.set_params(model__alpha=best_alpha)
    pipe.fit(x_combined, y_combined)

    model_step = pipe.named_steps['model']
    result_string = f"alpha: {best_alpha}, coefficient: {np.array2string(model_step.coef_, precision=4)}, intercept: {model_step.intercept_}"
    
    evaluate_model(pipe, "pipe_ridge", test_data, result_string)
    save_path = os.path.join(ARTIFACTS_DIR, 'pipe_ridge.pkl')
    dump(pipe, save_path)
    print(" --- Ridge pipeline completed and saved --- ")