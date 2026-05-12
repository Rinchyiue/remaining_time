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
#       content: the data frame to be modified
# @para name:
#       type: str
#       content: name of the model to be added
# @para score:
#       type: numpy.ndarray
#       content: a list of floats which are returned from myScore function
# @para best:
#       type: str
#       content: can be either "Y" or "N", representing whether the current model is (one of) the best
# @para absSuper:
#       type: float
#       content: Super value calculated against baseline model
# @para details:
#       type: str
#       content: details to be added
# functionality: create a new line as DataFrame and append it to df
def add_new_line(df, name, length, score, best, absSuper, details):
    nl = pd.DataFrame([{"name":name, "prefix length":length, "MAE":score[0], "RMSE":score[1], "MedAE":score[2],
                    "R2":score[3], "best":best, "absSuper":absSuper, "details":details}])
    df = pd.concat([df, nl], ignore_index=True)

# a function to find out the "best" ones to implement