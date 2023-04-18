from pycoingecko import CoinGeckoAPI
import pygsheets
import json
cg = CoinGeckoAPI()

service_file = 'credentials.json'
gc = pygsheets.authorize(service_file=service_file)
sheetname = "Cryptocurrency Investment Tracking"
sh = gc.open(sheetname)
wks = sh.worksheet_by_title("Top Performers")

