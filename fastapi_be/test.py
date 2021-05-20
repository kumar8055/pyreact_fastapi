import yfinance as yf
import pandas as pd

# data = yf.download("SPY", start="2017-01-01", end="2017-04-30")
# df = pd.DataFrame(data, columns=("Open","High","Low","Close","Adj","Close","Volume"))
# print(df.Open.to_json())
# print(df.to_dict())

## Moving Average 
# data = yf.download("SPY", interval="1d")["Close"][-10:].mean()
# print(data)

# data = yf.download("SPY", start="2017-01-01", end="2017-04-30",interval="1d")
# print(data.shape[0])
# print(data["Close"].to_json())
# date_keys = [key for key, value in (data["Close"].to_json()).items()]
# print(data["Close"].to_dict().keys())
    # ma = [value[i-200:i].mean() for i in range(0, data.shape[0]+1)]


# msft = yf.Ticker("MSFT")
# data = msft.history(period = "5d", interval = "1h")
# print(data["Date"][])


msft = yf.Ticker("MSFT")
df = msft.history(period = "5d", interval = "1h")
df.reset_index(inplace = True)
print(df["Date"][0])
print(df["Date"][1])
print(df["Date"][2])



# ma = [data["Close"][i-200:i].mean() for i in range(0, data.shape[0]+1)]
# print(ma)
# print(data["Date"].to_list())


# df = yahoo_fin.stock_info.get_data('a', interval='1d')
# moving_average = [df['close'][i-50:i].mean() for i in range(50, df.shape[0]+1)]

# import yahoo_fin
# from yahoo_fin import stock_info
# yahoo_fin.stock_info.get_data('a', interval='1d')['close'][-50:].mean()


# for x in data:
#     # print({"Date":x.Date})
#     print("row---",x)
# import yfinance as yf

# msft = yf.Ticker("MSFT")
# hist = msft.history(period="max")
# hist = msft.history(start="2017-01-01", end="2017-04-30")
# print(hist)
# print(msft.actions)
# print(msft.dividends)
# show financials
# print(msft.financials)
# print(msft.quarterly_financials)

# # show major holders
# print(msft.major_holders)

# show institutional holders
# print(msft.institutional_holders)

# # show balance sheet
# print(msft.balance_sheet)
# print(msft.quarterly_balance_sheet)

# show cashflow
# print(msft.cashflow)
# print(msft.quarterly_cashflow)

# show earnings
# print(msft.earnings)
# print(msft.quarterly_earnings)

# # show sustainability
# print(msft.sustainability)

# show analysts recommendations
# print(msft.recommendations)

# show next event (earnings, etc)
# print(msft.calendar)

# show ISIN code - *experimental*
# ISIN = International Securities Identification Number
# print(msft.isin)

# show options expirations
# print(msft.options)

# get option chain for specific expiration
# # opt = msft.option_chain('YYYY-MM-DD')
# opt = msft.option_chain('2021-06-25')
# # data available via: opt.calls, opt.puts
# print(opt.calls)