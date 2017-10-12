def FetchRate(browser):
    page = browser.FindSubUI("PageRateResult")

    rateTable = page.TryToFindSubUI("TableResult")
    if rateTable is None:
        print("Could not find rate table")
        return

    # The first result (row 2) and price of selling foreign cash (column 5)
    return rateTable.GetCellText(2, 5)

