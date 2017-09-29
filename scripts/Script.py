import sys
import os

# __file__ will be AFW.py in auto/afw
sys.path.append(os.path.join(os.path.split(os.path.realpath(__file__))[0], "../../scripts"))
sys.path.append(os.path.join(os.path.split(os.path.realpath(__file__))[0], "../.."))

from ScriptRateSearch import *

# Open browser
browser = afw.OpenWebBrowser("Browser")

# Open page
if browser.OpenURL("URLRate"):
    SearchRate(browser)
