"""
Central configuration file containing declarations used in multiple modules.
"""

import os

PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RAW_DIR = os.path.join(PROJECT_ROOT, "data", "raw")
PROCESSED_DIR = os.path.join(PROJECT_ROOT, "data", "processed")
XES_FILE_PATH = os.path.join(RAW_DIR, "BPI_Challenge_2013_incidents.xes.gz")
REQUIRED_COLUMNS = ["case:concept:name", "concept:name", "time:timestamp"]
TARGET_COLUMN = "remaining_time"