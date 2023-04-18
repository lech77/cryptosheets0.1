import valueSheet, portfolioSheet, evalSheet, moduleInstaller, requests, time

def main():
    moduleInstaller.install("pycoingecko")
    moduleInstaller.install("pygsheets")
    while True:
        if requests.get("https://api.coingecko.com/api/v3/ping").status_code == 200:
            print("CoinGeckoAPI is working")
            valueSheet.fillValueSheet("Values")
            time.sleep(60)
            portfolioSheet.fillPortfolioValues("Portfolio")
            time.sleep(60)
            evalSheet.fillTokenEvalSheet("Evaluations")
            time.sleep(60)
        else:
            time.sleep(60)
        continue
    return

main()

