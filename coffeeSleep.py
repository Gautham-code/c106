import csv
import numpy as np


def getDataSource(data_path):
    Coffee_in_ml = []
    Sleep_in_hour = []
    with open(data_path) as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            Coffee_in_ml.append(float(row["Coffee in ml"]))
            Sleep_in_hour.append(float(row["sleep in hours"]))

    return {"x" :  Coffee_in_ml, "y": Sleep_in_hour}

def Correlation(datasource):
    correlation = np.corrcoef(datasource["x"], datasource["y"])
    print("Correlation between coffee and sleep : ",correlation[0,1])

def setup():
    datasource = getDataSource(data_path)
    findCorrelation(datasource)

setup()
