import numpy as np
import yfinance as yf


AAPL = yf.download('AAPL','2008-01-01','2008-02-01')['Close']
MELI = yf.download('MELI','2008-01-01','2008-02-01')['Close']
MSFT = yf.download('MSFT','2008-01-01','2008-02-01')['Close']
AMZN = yf.download('AMZN','2008-01-01','2008-02-01')['Close']
KO = yf.download('KO','2008-01-01','2008-02-01')['Close']
print(KO)

