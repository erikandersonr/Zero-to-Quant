import yfinance as yf

palantir = yf.Ticker("pltr")

print(palantir.history(period="1d"))
