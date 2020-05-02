from flask import Flask
app = Flask(__name__)

'''
Step 1: user enters the 'amount of investment' and 'choice(s) of investment strategy / strategies'

Step 2: program assigns appropriate stocks or ETF(s) to each investment strategy. (at 3 stocks or EFT(s) for each strategy) 

Step 3: program shows a) how the money is split into each strategy
                        b) current value of the overall portfolio 
                          c) overall portfolio value from the last 5 days (each single day's value) ---> as "trend". 
'''

'''
Index page 

Needs: 1) input text box for investment amount 
        2) selection menu for investment strategy 
'''
@app.route('/')
def index():
    return 'Hello, World!'


'''
Information page showing the recommendation results 

Needs: 1) display of stocks/ETFs corresponding to each strategy
        2) MAYBE current and last 5 days' overall value of the whole portfolio
          3) CAN ADD: current value and last 5 days' value of each single stock/ETF
'''
@app.route('recommendation') 
def recommendation():
    return "Some html page(s)"


# obtain the current value (up to second) of a specific stock.
def getCurrentData(stockSymbol):
    return "An float number"


# obtain the 5 days history of the overall portfolio value
# MAY NEED TO FURTHER SPLIT INTO SUB-FUNCTIONS
def getWeeklyTrend(stockSymbol):
    return "A list/array of length 5"


def getCurrentPortfolioValue():
    return 0

def getPortfolioTrend():
    return "A lsit of an array of length 5"


# Read the config file containing hard-coded stock choices
def readConfigFile():
    return "A dictionary of harded coded stocks/ETFs: [strategy name] -> [a list of hard-coded stocks]"


if __name__ == '__main__':
    app.run(debug=True)

