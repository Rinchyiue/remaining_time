import pandas as pd
from checker import df_type_check

# @para df:
#       type: pandas.DataFrame
#       content: the data frame to be modified
# @para model:
#       type: str
#       content: name of the model to be modified
# functionality: set the key of "best" column of the given model as "N"
def disprefer(df, model):
    df_type_check(df)
    df.loc[df["name"] == model, "best"] = "N"

# @para df:
#       type: pandas.DataFrame
#       content: the data frame to be looked after (df of model_scores.csv especially)
# @output:
#       type: list
#       content: the list of name of the current "best" models
def getBest(df):
    df_type_check(df)
    return (df.query("best == 'Y'")["name"].tolist())

# @para df:
#       type: pandas.DataFrame
#       content: the data frame to be modified
# @para update_info:
#       type: list
#       content: a list of update information either get from model_evaluation.loose_compare()
#               or from model_evaluation.strict_compare
# functionality: if a model is marked with 'D', degrade it in the given data frame with disprefer()
def update(df, update_info):
    df_type_check(df)
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
def update_and_set(df, update_info, abs_super, details):
    df_type_check(df)
    update(df, update_info)
    nl= pd.DataFrame([{"name": update_info[-1][0], "best": update_info[-1][1], "abs_super": abs_super, "details": details}])        # update_info[-1] is a tuple where information of model to be set is stored
    df = pd.concat([df, nl], ignore_index=True)

# @para df:
#       type: pandas.DataFrame
#       content: the data frame to be modified
# @para list_of_rows:
#       type: List
#       content: the list of rows to be added
# functionality: add the list of rows to the df, while newly added rows should be sorted by prefix length with all existing rows
def add_list_of_lines(df, list_of_rows):
    df_type_check(df)
    row_df = pd.DataFrame(list_of_rows)
    df = pd.concat(df, row_df)
    df = df.sort_values(by='prefix_length', kind='stable', ignore_index=True)