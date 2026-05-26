from sklearn.metrics import (mean_absolute_error, root_mean_squared_error, median_absolute_error, r2_score)
import numpy as np
import pandas as pd
import main
import score_management
from pipeline_helper import get_variants, get_log_with_length_index

metrics = ["MAE","RMSE","MedAE","R2"]

# @para a_true:
#       type: numpy.ndarray
#       content: list of true values
# @para a_pred:
#       type: numpy.ndarray
#       content: list of predicted values
# @output:
#       type: numpy.ndarray
#       content: a list which consists of MAE, RMSE, MedAE and R2-Score
# functionality: calculate the metrics of given true and prediction values
def myScore(a_true, a_pred):
    return np.array([mean_absolute_error(a_true,a_pred), root_mean_squared_error(a_true,a_pred),
            median_absolute_error(a_true,a_pred), r2_score(a_true,a_pred)])

# @para metrics_list:
#       type: numpy.ndarray
#       content: output of myScore()
# @output:
#       type: np.float64
#       content: arithmetic average of the four metrics
# functionality: make a naive index which ranges in (0,1] with the property "the higher, the better"
# notice: we don't consider one of MAE, RMSE , or MedAe can reach infinity
def validScore(metrics_list):
    return np.average([1 / (metrics_list[i] + 1) for i in range(3)] + [metrics_list[3]])            # 1 is added to the divisor to keep it not equal 0

# @para score1, score2:
#       type: numpy.ndarray
#       content: single score list obtained by myScore function
# @output :
#       type: numpy.float64
#       content: the partial Super value from the second model against the first model
# functionality: this is a function for Super relation between two models with identical prefix length, without respect to frequency
def singleScore(score1,score2):
    return (sum(.25 * (score1[i] - score2[i]) / score1[i] for i in range(3)) + 0.25 * (score2[3] - score1[3]) / score2[3])

# @para df:
#       type: pandas.DataFrame
#       content: the data frame where metrics are stored
# @para new_model, old_model:
#       type: str
#       content: model name to look after
# @output:
#       type: numpy.float64
#       content: the relative super value
# functionality: calculate the relative super value of the given new_model against old_model
def general_super(df, old_model, new_model):
    res = 0
    for i in range(main().getVariance()):
        p_len = main().getLength(i)
        res += main().getFrequency(i) * singleScore(df.query("prefix_length == @p_len and name == @old_model")[metrics],
                                                    df.query("prefix_length == @p_len and name == @new_model")[metrics])
    return res

# @para df:
#       type: pandas.DataFrame
#       content: the data frame where metrics are stored
# @para model:
#       type: str
#       content: model name to look after
# @output:
#       type: numpy.float64
#       content: the absolute super value
# functionality: calculate the absolute super value of the given model (against baseline)
def abs_super(df, model):
    return general_super(df, "baseline", model)

# @para df1:
#       type: pandas.DataFrame
#       content: the data frame where metrics are stored
# @para df2:
#       type: pandas.DataFrame
#       content: the data frame where model scores are stored
# @para model:
#       type: str
#       content: model name to look after
# @output:
#       type: list (list of tuples)
#       content: a list of tuples consist of compared model name and the relative super value
# functionality: calculate the relative super value of the given model against (a list of) current "best" models
#                and store them with the compared models
def rel_super(df1, df2, model):
    res = []
    for name in score_management.getBest(df2):
        res.append((name, general_super(df1, name, model)))
    return res

# @para model:
#       type: str
#       content: current model name
# @para rel_super_list:
#       type: list
#       content: output of rel_super()
# @output:
#       type: list (list of tuples)
#       content: a list of tuples consist of compared model name and their status change ('D' | 'R') or status setting ('Y' | 'N')
# functionality: make loose comparison according to super definition and output the names of all compared mode and
#               their status change or status setting
def loose_compare(model, rel_super_list):
    res = []
    is_best = False
    for (name, rel_super) in rel_super_list:
        if rel_super >= -0.05:
            is_best = True
            if rel_super > 0.05:
                res.append((name, 'D'))         # 'D' means degrade
            else:
                res.append((name, 'R'))         # 'R' means retain
        else:
            res.append((name, 'R'))
    if is_best:
        res.append((model, 'Y'))                # 'Y' means yes
    else:
        res.append((model, 'N'))                # 'N' means no
    return res

# @para df1:
#       type: pandas.DataFrame
#       content: the data frame where metrics are stored
# @para df2:
#       type: pandas.DataFrame
#       content: the data frame where model scores are stored
# @output:
#       type: list (list of tuples)
#       content: a list of tuples consist of compared model name and their status change ('D' | 'R')
# functionality: find out the only "best" model among the list of "best" models, with strict distinction of relative super value with >=
#               i.e. the relative super value of the tested model against compared model should be not negative in order to have chance
#               to be selected
def strict_compare(df1, df2):
    res = []
    best_list = score_management.getBest(df2)
    while len(best_list) > 1:
        new_list = [best_list[0]]
        for i in range(len(best_list) - 1):
            if general_super(df1, best_list[i+1], best_list[i]) < 0:
                new_list.append(best_list[i+1])
        best_list = new_list
    res.append((best_list[0], 'R'))
    for name in score_management.getBest(df2):
        if name != best_list[0]:
            res.append((name, 'D'))
    return res

# @para model:
#       content: the model to be evaluated
# @para model_name:
#       type: str
#       content: the name of the model given
# @para test_data:
#       type: pandas.DataFrame
#       content: the test_data given
# @para result_string:
#       type: str
#       content: extra details for the model to be stored
# functionality: evaluate the model and store the evaluation results into .csv files
def evaluate_model(model, model_name, test_data, result_string):
    print(" --- start evaluating model --- ")
    df = pd.read_csv("model_metrics.csv")
    new_rows = []
    variants = get_variants(test_data)
    
    for i in range(len(variants)):
        variant = variants[i]
        log_data = get_log_with_length_index(test_data, i)
        
        x_test = log_data.iloc[:, :-1]
        y_test = log_data.iloc[:, -1]
        y_pred = model.predict(x_test)
        score = myScore(y_test, y_pred)
        
        new_rows.append({
            "name": model_name,
            "prefix_length": variant,
            "MAE": score[0],
            "RMSE": score[1],
            "MedAE": score[2],
            "R2": score[3]
        })
    df = score_management.add_list_of_lines(df, new_rows)
    df.to_csv("model_metrics.csv", index=False)
    print(" --- model metrics successfully stored --- ")

    df1 = pd.read_csv("model_metrics.csv")
    df2 = pd.read_csv("model_scores.csv")
    abs_super = abs_super(df1, df2, model_name)                     # the absolute super value calculated against baseline
    rel_super = rel_super(df1, df2, model_name)                     # a list of tuples of compared current 'best' model and relative super value calculated
    update_info = loose_compare(model_name, rel_super)              # the update/setting info

    print(" --- loose compare done --- ")

    score_management.update_and_set(df2, update_info, abs_super, result_string)
    df2.to_csv("model_scores.csv", index=False)
    print(" --- model score successfully stored and updated --- ")