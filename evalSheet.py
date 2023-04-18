from pycoingecko import CoinGeckoAPI
import pygsheets
import json
import time
cg = CoinGeckoAPI()

service_file = 'credentials.json'
gc = pygsheets.authorize(service_file=service_file)
sheetname = "Cryptocurrency Investment Tracking"
sh = gc.open(sheetname)

def fillTokenEvalSheet(wks):
    print("Starting fillTokenEvalSheet")
    wks = sh.worksheet_by_title(wks)
    wks.clear("B2", "F98")
    rawWKSData = json.dumps(wks.get_values("A2", "A1000", returnas="matrix", include_tailing_empty="false"))
    cleanWKSData = str(json.loads(rawWKSData)).translate({ord(i): None for i in "['']"})
    cleanWKSData = cleanWKSData.replace(", ", ",")
    cleanWKSData = cleanWKSData.replace(" ", "-")
    cleanWKSData = cleanWKSData.lower()
    rawData = json.dumps(cg.get_coins_markets(vs_currency="usd", ids=cleanWKSData))
    cleanData = json.loads(rawData)
    listWKSData = cleanWKSData.split(",")
    y = 0
    for item in listWKSData:
        tokenValue = cleanData[y]["current_price"]
        tokenMC = cleanData[y]["market_cap"]
        tokenCirculatingSupply = cleanData[y]["circulating_supply"]
        tokenMaxSupply = cleanData[y]["total_supply"]
        tokenFDV = cleanData[y]["fully_diluted_valuation"]
        wks.update_value("B" + str(y + 2), tokenValue)
        wks.update_value("C" + str(y + 2), tokenMC)
        wks.update_value("D" + str(y + 2), tokenCirculatingSupply)
        wks.update_value("E" + str(y + 2), tokenMaxSupply)
        wks.update_value("F" + str(y + 2), tokenFDV)
        print("Filled values for " + listWKSData[y] + "[EVALUATIONS]")
        y = y + 1
        time.sleep(5)
        continue
    print("Finished fillTokenEvalSheet")
    return

