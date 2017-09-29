def SearchRate(browser):
    page = browser.FindSubUI("PageRateSearch")

    startDate = page.TryToFindSubUI("InputStartDate")
    if startDate is None:
        print "Could not find start date input"
        return
    startDate.InputText("2016-09-01")
    
    endDate = page.TryToFindSubUI("InputEndDate")
    if endDate is None:
        print "Could not find end date input"
        return
    endDate.InputText("2016-09-10")

    searchBtn = page.TryToFindSubUI("BtnSearch")
    if searchBtn is None:
        print "Could not find search button"
        return
    searchBtn.Click()

    

