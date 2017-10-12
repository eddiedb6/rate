def SearchRate(browser, date, currency):
    currencyMap = {
        "GBP": "1314", # Britain Pound
        "HKD": "1315", # Hong Kong Dollar
        "USD": "1316", # US Dollar
        "SGD": "1375", # Singapore Dollar
        "JPY": "1323", # Japan Yen
        "CAD": "1324", # Canada Dollar
        "AUD": "1325", # Australia Dollar
        "EUR": "1326", # Euro
        "MOP": "1327", # Macau Pataca
        "PHP": "1328", # Philippines Peso
        "THB": "1329", # Thailand Baht
        "NZD": "1330", # New Zealand Dollar
        "KRW": "1331", # Korea Won
        "RUR": "1843", # Russia Ruble
        "MYR": "2890", # Malaysia Ringgit
        "TWD": "2895", # Taiwan Dollar
        "IDR": "3030"  # Indonesia Rupiah
    }
    
    page = browser.FindSubUI("PageRateSearch")

    startDate = page.TryToFindSubUI("InputStartDate")
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

    

