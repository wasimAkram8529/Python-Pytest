import csv
from pathlib import Path

dataFile = "data.csv"
cfgDirectory = "config"

Base_dir = Path(__file__).resolve().parent.parent
filePath = Base_dir.joinpath(cfgDirectory).joinpath(dataFile)

def get_data():
  with open(filePath, 'r') as f:
    reader = csv.reader(f)
    next(reader)
    data = [tuple(row) for row in reader]

  return data


# print(get_data())