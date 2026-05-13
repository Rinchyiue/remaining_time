from sklearn.metrics import (mean_absolute_error, root_mean_squared_error, median_absolute_error, r2_score)
import numpy as np

# @para a_true:
#       type: numpy.ndarray
#       content: list of true values
# @para a_pred:
#       type: numpy.ndarray
#       content: list of predicted values
# @output:
#       type: numpy.ndarray
#       content: a list which consists of MAE, RMSE, MedAE and R2-Score
def myScore(a_true, a_pred):
    return np.array([mean_absolute_error(a_true,a_pred), root_mean_squared_error(a_true,a_pred),
            median_absolute_error(a_true,a_pred), r2_score(a_true,a_pred)])

# @para score1, score2:
#       type: numpy.ndarray
#       content: single score list obtained by myScore function
# @output :
#       type: numpy.float64
#       content: the partial Super value from the second model against the first model
# functionality: this is a function for Super relation between two models with identical prefix length, without respect to frequency
def singleScore(score1,score2):
    return sum(0.25 * (x-y)/x for x,y in zip(score1,score2))

#def mySuper(freqList, scoreList1, scoreList2) -> call p_superScore

#def compare(super) => super value from super function; return (enum,Bool,enum) => class,whether to keep,strict evaluation for that