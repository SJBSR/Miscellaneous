# Importing stock prices from Yahoo Finance
import yfinance as yf
data = yf.download(["AAPL", "AMZN"],
                   start= "2025-01-01",
                   end= "2025-11-26",
                   group_by='ticker')
print(data)