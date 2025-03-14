import yfinance as yf
import pandas as pd

def get_implied_volatility(symbol="^SPX"):
    spx = yf.Ticker(symbol)
    expirations = spx.options
    
    if not expirations:
        return None  # No options data available

    # Select the nearest expiration date
    nearest_expiry = expirations[0]
    options = spx.option_chain(nearest_expiry)

    # Get implied volatilities from calls and puts
    iv_calls = options.calls["impliedVolatility"].dropna()
    iv_puts = options.puts["impliedVolatility"].dropna()
    
    if iv_calls.empty and iv_puts.empty:
        return None

    avg_iv = pd.concat([iv_calls, iv_puts]).mean() * 100  # Convert to percentage
    return avg_iv

def get_rsi(symbol="^SPX", period=14):
    spx = yf.Ticker(symbol)
    df = spx.history(period="3mo")

    delta = df["Close"].diff()
    gain = (delta.where(delta > 0, 0)).rolling(window=period).mean()
    loss = (-delta.where(delta < 0, 0)).rolling(window=period).mean()

    rs = gain / loss
    rsi = 100 - (100 / (1 + rs))

    return rsi.iloc[-1]  # Latest RSI value

def get_volume_breakout(symbol="^SPX", window=20):
    spx = yf.Ticker(symbol)
    df = spx.history(period="3mo")

    avg_volume = df["Volume"].rolling(window=window).mean()
    latest_volume = df["Volume"].iloc[-1]

    return latest_volume > avg_volume.iloc[-1]  # True if breakout

def trading_signal():
    iv = get_implied_volatility()
    rsi_value = get_rsi()
    volume_breakout = get_volume_breakout()

    if iv is None:
        return "IV data not available"

    if iv < 20:
        return "Buy (Low IV)"
    elif iv > 30:
        return "Hedge (High IV)"

    if rsi_value > 70:
        return "Sell (RSI Overbought)"
    elif volume_breakout:
        return "Buy (Volume Breakout Confirmed)"
    
    return "Hold"

if __name__ == "__main__":
    print("Trading Decision:", trading_signal())
