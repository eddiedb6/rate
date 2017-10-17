from RateConfig import *

def FetchRate(browser):
    page = browser.FindSubUI("PageRateResult")

    rateTable = None
    count = RetryCount
    while count > 0:
        rateTable = page.TryToFindSubUI("TableResult")
        if rateTable is not None:
            break
        count -= 1
        
    if rateTable is None:
        print("Could not find rate table")
        return

    # The first result (row 2) and price of selling foreign cash (column 5)
    return rateTable.GetCellText(2, 5)

