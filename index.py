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
@app.route('recommendation') 
def recommendation():
    return "Some html page(s)"

'''
Purpose: Obtain the current value (up to second) of a specific stock

Input: stockSymbol -> string 
Expected output: -> float if valid symbol, otherwise -1.
'''
def getCurrentStockValue(stockSymbol):
    return "An float number"

'''
Purpose: Obtain the 5 days history of the overall portfolio value
        !!!MAY NEED TO FURTHER SPLIT INTO SUB-FUNCTIONS!!!
Input: stockSymbol -> string
        days -> integer denoting the backtracking range
Expected output: -> array of length 5
'''
def getTrend(stockSymbol, days):
    return "An array of length 5"


'''
Purpose: Calculate the current overall portfolio value
Input: portfolio -> list of stocks/ETFs in portfolio 
        days -> integer denoting the backtracking range
Expected output: ->float number 
'''
def getCurrentPortfolioValue(portfolio):
    return 0


'''
Purpose: Assemble an array of length 5, each element denoting a previous day's overall portfolio value
Input: portfolio -> list of stocks/ETFs in portfolio 
        days -> integer denoting the backtracking range
Expected output: -> array of length 5
'''
def getPortfolioTrend(portfolio, days):
    return "A lsit of an array of length 5"

'''
Purpose: Read the config file containing hard-coded stock choices
Input: Path to configuration file
Expected output: -> a dictionary with key being stratey name and values being lists of selected stocks/ETFs
'''
def readConfigFile():
    return "A dictionary of harded coded stocks/ETFs: [strategy name] -> [a list of hard-coded stocks]"


if __name__ == '__main__':
    app.run(debug=True)

