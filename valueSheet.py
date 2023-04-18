from pycoingecko import CoinGeckoAPI
import pygsheets
import json
import time
cg = CoinGeckoAPI()

service_file = 'credentials.json'
gc = pygsheets.authorize(service_file=service_file)
sheetname = "Cryptocurrency Investment Tracking"
sh = gc.open(sheetname)

def fillValueSheet(wks):
    print("Starting fillValueSheet")
    wks = sh.worksheet_by_title(wks)
    rawWKSData = json.dumps(wks.get_values("A2", "A1000", returnas="matrix", include_tailing_empty="false"))
    cleanWKSData = str(json.loads(rawWKSData)).translate({ord(i): None for i in "['']"})
    cleanWKSData = cleanWKSData.replace(", ", ",")
    cleanWKSData = cleanWKSData.replace(" ", "-")
    cleanWKSData = cleanWKSData.lower()
    rawData = json.dumps(cg.get_price(ids=cleanWKSData, vs_currencies="usd", include_market_cap='true', include_24hr_vol="true",include_24hr_change="true"))
    cleanData = json.loads(rawData)
    listWKSData = cleanWKSData.split(",")
    y = 0
    for item in listWKSData:
        tokenValue = cleanData[(listWKSData[y])]["usd"]
        tokenMC = cleanData[(listWKSData[y])]["usd_market_cap"]
        token24Vol = cleanData[(listWKSData[y])]["usd_24h_vol"]
        token24Cha = cleanData[(listWKSData[y])]["usd_24h_change"]
        wks.update_value("B" + str(y + 2), tokenValue)
        wks.update_value("C" + str(y + 2), tokenMC)
        wks.update_value("D" + str(y + 2), token24Vol)
        wks.update_value("E" + str(y + 2), token24Cha)
        print("Filled values for " + listWKSData[y] + "[VALUES]")
        y = y + 1
        time.sleep(4)
        continue
    print("Finished fillValueSheet")
    return
