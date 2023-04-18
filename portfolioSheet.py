from pycoingecko import CoinGeckoAPI
import pygsheets
import json
import time
cg = CoinGeckoAPI()

service_file = 'credentials.json'
gc = pygsheets.authorize(service_file=service_file)
sheetname = "Cryptocurrency Investment Tracking"
sh = gc.open(sheetname)

def fillPortfolioValues(wks):
    print("Starting fillPortfolioValues")
    wks = sh.worksheet_by_title(wks)
    rawWKSData = json.dumps(wks.get_values("A2", "A1000", returnas="matrix", include_tailing_empty="false"))
    cleanWKSData = str(json.loads(rawWKSData)).translate({ord(i): None for i in "['']"})
    cleanWKSData = cleanWKSData.replace(", ", ",")
    cleanWKSData = cleanWKSData.replace(" ", "-")
    cleanWKSData = cleanWKSData.lower()
    rawData = json.dumps(cg.get_price(ids=cleanWKSData, vs_currencies="usd"))
    cleanData = json.loads(rawData)
    listWKSData = cleanWKSData.split(",")
    y = 0
    for item in listWKSData:
        tokenValue = cleanData[(listWKSData[y])]["usd"]
        wks.update_value("B" + str(y + 2), tokenValue)
        print("Filled values for " + listWKSData[y] + "[PORTFOLIO]")
        y = y + 1
        time.sleep(1)
        continue
    print("Finished fillPortfolioValues")
    return
