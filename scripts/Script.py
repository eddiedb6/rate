import sys
import os
import time

# __file__ will be AFW.py in auto/afw
sys.path.append(os.path.join(os.path.split(os.path.realpath(__file__))[0], "../../scripts"))
sys.path.append(os.path.join(os.path.split(os.path.realpath(__file__))[0], "../../util"))
sys.path.append(os.path.join(os.path.split(os.path.realpath(__file__))[0], "../.."))

from ScriptRateSearch import *
from ScriptRateFetch import *

from DBUtil import *

# {
#     "date": "2016-09-01",
#     "currency": "USD",
#     "rate": 660
# }
rates = FetchExchangeRateForUpdateFromDB()
#[
#{
#    "date": "2016-09-01",
#    "currency": "USD"
#},
#{
#    "date": "2017-09-01",
#    "currency": "EUR"
#}]

print(rates)

# Open browser
browser = afw.OpenWebBrowser("Browser")

isFirstOpen = True
for rate in rates:
     # Open page
    if not browser.OpenURL("URLRate"):
        break

    if isFirstOpen:
        time.sleep(8)
        isFirstOpen = False
    else:
        time.sleep(3)

    if not SearchRate(browser, rate["date"], rate["currency"]):
        break

    time.sleep(3)
    rateString = FetchRate(browser)

    if rateString is not None:
        rate["rate"] = float(rateString)

print(rates)

