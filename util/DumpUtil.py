import pickle
import os

from RateConfig import *

def FetchExchangeRateForUpdateFromFile():
    rates = []
    path = ImportPath

    if not os.path.exists(path):
        print("Error: invalid import path: " + path)
        return rates
    
    with open(path, "rb") as f:
        rates = pickle.load(f)
    return rates
    
def UpdateExchangeRateToFile(rates):
    path = ExportPath
    with open(path, "wb") as f:
        pickle.dump(rates, f)
