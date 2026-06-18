"""
This is a collection for checker that are frequently used in this project
"""

import pandas as pd
import numpy as np

def df_type_check(df):
    if not isinstance(df , pd.DataFrame):
        raise TypeError("The given parameter is not a data frame")
    
def column_inclusion_check(df, column):
    if column not in df.columns:
        raise KeyError("No such column in the given data frame. ")