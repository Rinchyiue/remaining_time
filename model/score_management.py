import pandas as pd

# @para df:
#       type: pandas.DataFrame
#       content: the data frame to be modified
# @para model:
#       type: str
#       content: name of the model to be modified
# functionality: set the key of "best" column of the given model as "N"
def disprefer(df, model):
    df.loc[df["name"] == model, "best"] = "N"

# @para df:
#       type: pandas.DataFrame
#       content: the data frame to be looked after (df of model_scores.csv especially)
# @output:
#       type: list
#       content: the list of name of the current "best" models
def getBest(df):
    return (df.query("best == 'Y'")["name"].tolist())

# @para df:
#       type: pandas.DataFrame
#       content: the data frame to be looked after
# @para column:
#       type: str
#       content: target column name
# @para value:
#       type: object
#       content: the target value in the column
# @output:
#       type: pandas.core.indexes.numeric.Int64Index
#       content: a sequence of indexes which fulfils df[column] == value
# functionality: find out the corresponding indexes of target columns regarding the given value
def find_index(df, column, value):
    return (df.index[df[column] == value])

# @para df:
#       type: pandas.DataFrame
#       content: the data frame to be modified
# @para update_info:
#       type: list
#       content: a list of update information either get from model_evaluation.loose_compare()
#               or from model_evaluation.strict_compare
# functionality: if a model is marked with 'D', degrade it in the given data frame with disprefer()
def update(df, update_info):
    for (name, info) in update_info:
        if info == 'D':
            disprefer(df, name)

# @para df:
#       type: pandas.DataFrame
#       content: the data frame to be modified
# @para update_info:
#       type: list
#       content: a list of update information either get from model_evaluation.loose_compare()
#               or from model_evaluation.strict_compare
# @para abs_super:
#       type: numpy.float64
#       content: the absolute super value of the model to be added
# functionality: update the status of best in the data frame and add a new row with information of the new model
def update_and_set(df, update_info, abs_super):
    update(df, update_info)
    nl= pd.DataFrame([{"name": update_info[-1][0], "best": update_info[-1][1], "abs_super": abs_super}])        # update_info[-1] is a tuple where information of model to be set is stored
    df = pd.concat([df, nl], ignore_index=True)

# @para df:
#       type: pandas.DataFrame
#       content: the data frame to be modified
# @para name:
#       type: str
#       content: name of the model to be added
# @para score:
#       type: numpy.ndarray
#       content: a list of floats which are returned from myScore function
# functionality: create a new line as DataFrame and append it after the last column df in which has the same prefix length
def add_new_line(df, name, length, score):
    nl = pd.DataFrame([{"name":name, "prefix_length":length, "MAE":score[0], "RMSE":score[1], "MedAE":score[2], "R2":score[3]}])
    idx = find_index(df, "prefix_length", length).max()                         # the last row matched
    df = pd.concat([df.iloc[:idx+1], nl, df.iloc[idx+1:]], ignore_index=True)