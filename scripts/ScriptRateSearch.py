from RateConfig import *

def SearchRate(browser, date, currency):
    currencyMap = {
        7: "1314", # Britain Pound
        12: "1315", # Hong Kong Dollar
        2: "1316", # US Dollar
        17: "1375", # Singapore Dollar
        4: "1323", # Japan Yen
        8: "1324", # Canada Dollar
        9: "1325", # Australia Dollar
        3: "1326", # Euro
        18: "1327", # Macau Pataca
        16: "1328", # Philippines Peso
        6: "1329", # Thailand Baht
        10: "1330", # New Zealand Dollar
        5: "1331", # Korea Won
        11: "1843", # Russia Ruble
        15: "2890", # Malaysia Ringgit
        13: "2895", # Taiwan Dollar
        14: "3030"  # Indonesia Rupiah
    }
    
    page = browser.FindSubUI("PageRateSearch")

    startDate = None
    count = RetryCount
    while count > 0:
        startDate = page.TryToFindSubUI("InputStartDate")
        if startDate is not None:
            break
        count -= 1
        
    if startDate is None:
        print("Could not find start date input")
        return False
    startDate.InputText(date)
    
    endDate = page.TryToFindSubUI("InputEndDate")
    if endDate is None:
        print("Could not find end date input")
        return False
    endDate.InputText(date)

    currencyCombo = page.TryToFindSubUI("ComboboxCurrency")
    if currencyCombo is None:
        print("Could not find currency combobox")
        return False
    currencyCombo.Select(currencyMap[currency])

    searchBtn = page.TryToFindSubUI("BtnSearch")
    if searchBtn is None:
        print("Could not find search button")
        return False
    return searchBtn.Click()

    

