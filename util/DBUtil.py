import pymysql
from RateConfig import *

def FetchExchangeRateForUpdateFromDB():
    conn = pymysql.connect(host=DBHost, port=DBPort, user=DBUser, passwd=DBPassword, db=DBName)
    cur = conn.cursor()

    cur.execute("select * from exchangerate where Rate is null")

    rates = []
    for row in cur:
        if len(row) != 3:
            continue
        rate = {}
        rate["date"] = str(row[0]).split(" ")[0]
        rate["currency"] = row[1]
        rates.append(rate)

    cur.close()
    conn.close()
    
    return rates
    
