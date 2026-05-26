"""
This is a pipeline for simple linear regression model
"""

from sklearn.pipeline import Pipeline
from sklearn.linear_model import LinearRegression, Ridge
from pipeline_helper import numeric_split, preprocess_data
from tempfile import mkdtemp
from shutil import rmtree

# stage 1: data preparation
train_log, val_log, test_log = preprocess_data()
x_train, y_train = numeric_split(train_log, "remaining_time")
x_test, y_test = numeric_split(test_log, "remaining_time")

# stage 2: build up pipeline
estimators = [('reg_ols', LinearRegression()), ()]
cachedir = mkdtemp()                            # cache the preprocessed data
pipe = Pipeline(estimators, memory=cachedir)









rmtree(cachedir)                                # erase the cache