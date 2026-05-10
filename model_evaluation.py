from sklearn.metrics import (mean_absolute_error, root_mean_squared_error, median_absolute_error, r2_score)

# @para a_true: list of true values
# @para a_pred: list of predicted values
# @ output: a list which consists of MAE, RMSE, MedAE and R2-Score
def myScore(a_true, a_pred):
    return [mean_absolute_error(a_true,a_pred), root_mean_squared_error(a_true,a_pred),
            median_absolute_error(a_true,a_pred), r2_score(a_true,a_pred)]

# this is a function for Super relation between two models, without respect to frequency
# @para score1, score2: single score list obtained by myScore function
# @output : the partial Super value from the second model against the first model
def p_superScore(score1,score2):
    return sum(0.25 * (x-y)/x for x,y in zip(score1,score2))

#def super(freqList, scoreList1, scoreLst2) -> call p_superScore

#def compare(super) => super value from super function; return (enum,Bool,enum) => class,whether to keep,strict evaluation for that