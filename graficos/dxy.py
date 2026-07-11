import yfinance as yf

def obtener_dxy():
    dxy = yf.Ticker("DX-Y.NYB")
    return dxy.fast_info["last_price"]