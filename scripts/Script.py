import sys
import os
import time

# __file__ will be AFW.py in auto/afw
sys.path.append(os.path.join(os.path.split(os.path.realpath(__file__))[0], "../../scripts"))
sys.path.append(os.path.join(os.path.split(os.path.realpath(__file__))[0], "../../util"))
sys.path.append(os.path.join(os.path.split(os.path.realpath(__file__))[0], "../.."))

from RateConfig import *
from ScriptRateSearch import *
from ScriptRateFetch import *
from DBUtil import *
from DumpUtil import *

# {
#     "date": "2016-09-01",
#     "currency": 2,
#     "rate": 660
# }
rates = []
if ImportPath == "":
    rates = FetchExchangeRateForUpdateFromDB()
else:
    rates = FetchExchangeRateForUpdateFromFile()

# Open browser
browser = afw.OpenWebBrowser("Browser")

# Fetch each rate from network
for rate in rates:
     # Open page
    if not browser.OpenURL("URLRate"):
        break

    time.sleep(SleepSeconds)
    if not SearchRate(browser, rate["date"], rate["currency"]):
        break

    time.sleep(SleepSeconds)
    rateString = FetchRate(browser)

    if rateString is not None:
        rate["rate"] = float(rateString)

browser.Quit()

if ExportPath == "":
    UpdateExchangeRateToDB(rates)
else:
    UpdateExchangeRateToFile(rates)

# Report
failedRates = []
print("")
for rate in rates:
    if "rate" in rate:
        print("Get rate: " + str(rate["rate"]) + ", " + rate["date"] + ", " + str(rate["currency"]))
    else:
        failedRates.append(rate)
print("")
for rate in failedRates:
    print("Failed to get rate: " + rate["date"] + ", " + str(rate["currency"]))
            

    
