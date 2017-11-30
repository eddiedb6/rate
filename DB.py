import sys
import os
import pickle

from util.DBUtil import *

def Usage():
    print("Usage:")
    print("    python DB.py export|import FILE_PATH")

if len(sys.argv) != 3:
    Usage()
    sys.exit(0)

opt = sys.argv[1]    
if opt != "export" and opt != "import":
    Usage()
    sys.exit(0)

path = sys.argv[2]    
    
if opt == "export":
    rates = FetchExchangeRateForUpdateFromDB()
    with open(path, "wb") as f:
        pickle.dump(rates, f)
elif opt == "import":
    with open(path, "rb") as f:
        rates = pickle.load(f)
        UpdateExchangeRateToDB(rates)

