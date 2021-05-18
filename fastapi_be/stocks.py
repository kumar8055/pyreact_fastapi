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
