"""
A module containing baseline models to benchmark more advanced models.
"""

import numpy as np
import pandas as pd
from pathlib import Path
from model_evaluation import myScore
from pipeline_helper import get_log_with_length_index, get_variants
from checker import df_type_check, column_inclusion_check

def mean_predictor(train_log, target_col="remaining_time"):
    """
    Predicts mean remaining time of all training prefixes.
    :param train_log: pandas.DataFrame with the training logs
    :param target_col: String with the name of the remaining time column
    """
    df_type_check(train_log)
    column_inclusion_check(train_log, target_col)
    print("--- Running Mean Baseline Predictor ---")
    mean_remaining_time = train_log[target_col].mean()
    print(f"The mean remaining time of all training prefixes is {mean_remaining_time:.4f} hours.")
    return mean_remaining_time

# @para: test_log:
#       type: pandas.DataFrame
#       content: the whole test data (feature with target)
# functionality: initialize model_metrics.csv and model_scores.csv with baseline model data
def save_baseline(test_log, mean_remaining_time):
    df_type_check(test_log)
    artifacts_dir = Path(__file__).resolve().parents[1] / "artifacts"
    data_model_scores = {
        'name':['baseline'],
        'best':['Y'],
        'abs_super':[0],                    # according to the definition of abs_super, identical inputs always result in 0
        'details':['This model predicts every input simply as the mean value of time of the training data. ']
    }
    df1 = pd.DataFrame(data_model_scores)
    df1.to_csv(artifacts_dir / "model_scores.csv", index=False)
    print(f" --- {artifacts_dir.name}/model_scores.csv successfully created --- ")

    df2 = pd.DataFrame(columns=['name', 'prefix_length', 'MAE', 'RMSE', 'MedAE', 'R2'])
    res_list = []
    for i in range(len(get_variants(test_log))):
        y_test = get_log_with_length_index(test_log, i).iloc[:,-1]
        y_pred = np.full(y_test.shape, mean_remaining_time)
        score = myScore(pd.DataFrame(y_test), pd.DataFrame(y_pred))
        row = {
            'name':'baseline',
            'prefix_length': get_variants(test_log)[i],
            'MAE':score[0],
            'RMSE':score[1],
            'MedAE':score[2],
            'R2':score[3]
        }
        res_list.append(row)
    df2 = pd.DataFrame(res_list)
    df2.to_csv(artifacts_dir / "model_metrics.csv", index=False)
    print(f" --- {artifacts_dir.name}/model_metrics.csv successfully created --- ")