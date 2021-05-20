import yfinance as yf

msft = yf.Ticker("MSFT")

def getStocksInfo(ticker):
    try:
        tkr = yf.Ticker((ticker.upper()))
        info = tkr.info
        # print(info)
        return info
    except Exception as ex:
        print(str(ex))

def getHistoryData(ticker):
    try:
        history_data = yf.download(ticker, start="2017-01-01", end="2018-04-30")
        return history_data.to_dict()
    except Exception as ex:
        print("Error in History data: ",str(ex))

def getTickerDates(ticker):
    try:
        ticker_dates = yf.download(ticker, start="2017-01-01", end="2018-04-30", interval="1d")
        return list(ticker_dates["Close"].to_dict().keys())
    except Exception as ex:
        print("Error in getTickerDates data: ",str(ex))