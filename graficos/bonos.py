import yfinance as yf

def obtener_bono():
    bono = yf.Ticker("^TNX")
    return bono.fast_info["last_price"]