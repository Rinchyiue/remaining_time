import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1] / "remaining_time"))

import pandas as pd
from score_management import getBest, disprefer, update


# Test whether getBest() returns only models marked as best
def test_getBest_returns_best_models():

    df = pd.DataFrame({
        "name": ["baseline", "ridge", "linear"],
        "best": ["Y", "N", "Y"]
    })

    result = getBest(df)

    assert result == ["baseline", "linear"]


# Test whether disprefer() changes a model's best status to "N"
def test_disprefer_sets_model_to_not_best():

    df = pd.DataFrame({
        "name": ["baseline", "ridge"],
        "best": ["Y", "Y"]
    })

    disprefer(df, "ridge")

    assert df.loc[df["name"] == "ridge", "best"].iloc[0] == "N"


# Test whether update() applies degrade information correctly
def test_update_degrades_marked_models():

    df = pd.DataFrame({
        "name": ["baseline", "ridge"],
        "best": ["Y", "Y"]
    })

    update_info = [("ridge", "D")]

    update(df, update_info)

    assert df.loc[df["name"] == "ridge", "best"].iloc[0] == "N"
