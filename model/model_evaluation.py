from sklearn.metrics import (mean_absolute_error, root_mean_squared_error, median_absolute_error, r2_score)
import numpy as np
import pandas as pd
import main
import score_management

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