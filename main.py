import yfinance as yf
import pandas as pd

cdpr = yf.Ticker("CDR.WA")

data = cdpr.history(period="max")