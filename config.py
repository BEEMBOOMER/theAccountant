from pathlib import Path

#Gets the current path of the directory
PROJECT_ROOT=Path(__file__).resolve().parent

DATA_DIR=PROJECT_ROOT/"data"
PATH_BANK_STATEMENT=DATA_DIR/"test.csv"
PATH_OUTPUT_FILE=DATA_DIR/"Book2.xlsx"