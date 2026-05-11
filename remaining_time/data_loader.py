import pm4py
from config import XES_FILE_PATH

def load_data():
    print("Loading log...")
    log = pm4py.read_xes(XES_FILE_PATH)
    print("Log loaded successfully.")
    return log