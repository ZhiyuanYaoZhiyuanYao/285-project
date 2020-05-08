import requests
import json
import os
import sys
from flask import Flask
app = Flask(__name__)

'''
Required execution steps: 
Step 1: user enters the 'amount of investment' and 'choice(s) of investment strategy / strategies'

Step 2: program assigns appropriate stocks or ETF(s) to each investment strategy. (at 3 stocks or EFT(s) for each strategy) 

Step 3: program shows a) how the money is split into each strategy
                        b) current value of the overall portfolio 
                          c) overall portfolio value from the last 5 days (each single day's value) ---> as "trend". 
'''

'''
Additional functions: 
1. user signup/login?
2. storage of user portfolio?
'''

'''
Purpose: Index page 

Needs: 1) input text box for investment amount 
        2) selection menu for investment strategy 
Input: None
Expected output: A HTML page
'''
@app.route('/')
def index():
    return "Index page HTML"


'''
Purpose: Information page showing the recommendation results 

Needs: 1) display of stocks/ETFs corresponding to each strategy ----> What style? What graphs/charts? 
        2) current and last 5 days' overall value of the whole portfolio ---> Where:On this page or another new page? 
          3) CAN ADD: current value and last 5 days' value of each single stock/ETF

Input:None
Expected output: A HTML page
'''
@app.route('/recommendation') 
def recommendation():
    return "Some html page(s)"

'''
Purpose: Obtain the current value (up to second) of a specific stock

Input: stockSymbol -> string 
Expected output: -> float if valid symbol, otherwise -1.

Claimant: Wei He
'''
# @app.route('/getCurrentStockValue') 
# def getCurrentStockValue(stockSymbol='ADBE'):
def getCurrentStockValue(stockSymbol):
    url = "https://apidojo-yahoo-finance-v1.p.rapidapi.com/stock/v2/get-summary"

    querystring = {"region":"US"}
    querystring["symbol"] = stockSymbol.upper()

    headers = {
        'x-rapidapi-host': "apidojo-yahoo-finance-v1.p.rapidapi.com",
        'x-rapidapi-key': "10a797419dmsh47591f5e347fa1bp11e285jsn16824a531007"
        }   

    response = requests.request("GET", url, headers=headers, params=querystring)

    if response.text != '':
        price_info = response.json()['price']
        CurrentStockValue = 0.0 if price_info['regularMarketPrice'] == {} else float(price_info['regularMarketPrice']['fmt'])
        
        return CurrentStockValue
    else:
        return -1


'''
Purpose: Obtain specified days history of the overall portfolio value
        !!!MAY NEED TO FURTHER BE SPLIT INTO SUB-FUNCTIONS!!!

Input: stockSymbol -> string
        days -> integer denoting the backtracking range (trading day only, excluding weekneds/holidays)
Expected output: -> list of previous days' value
'''
def getStockTrend(stockSymbol, days):
    return "A list of each of the previous day's value"


'''
Purpose: Calculate the current overall portfolio value

Input: portfolio -> list of stocks/ETFs in portfolio 
Expected output: ->float number 

Claimant: Wei He
'''
# @app.route('/getCurrentPortfolioValue') 
# def getCurrentPortfolioValue(portfolio = ['VTI', 'IXUS', 'ILTB', 'APPL', 'ADBE', 'NSRGY']):
def getCurrentPortfolioValue(portfolio):
    currentPortfolioValue = 0.0
    for stk_sym in portfolio:
        currentPortfolioValue += getCurrentStockValue(stk_sym)

    # return str(currentPortfolioValue)
    return currentPortfolioValue


'''
Purpose: Assemble an array of length 5, each element denoting a previous day's overall portfolio value

Input: portfolio -> list of stocks/ETFs in portfolio 
        days -> integer denoting the backtracking range
Expected output: -> list of previous days' value
'''
def getPortfolioTrend(portfolio, days):
    return "A list of each of the previous day's value"

'''
Purpose: Read the config file containing hard-coded stock choices

Input: filePath -> string denoting path to configuration file
Expected output: -> a dictionary with key being stratey name and values being lists of selected stocks/ETFs

Claimant: Wei He
'''
# @app.route('/readConfigFile') 
def readConfigFile():
    dict_stratege_stock = {}
    with open(os.path.join(sys.path[0], "stock_engine.txt"), "r") as f:
        for i in range(5): 
            key_strategy = f.readline()[:-1]
            value_stocks = []
            for j in range(5):
                value_stocks.append(f.readline()[:-1])
            dict_stratege_stock[key_strategy]= value_stocks
    return dict_stratege_stock


if __name__ == '__main__':
    app.run(debug=True)

