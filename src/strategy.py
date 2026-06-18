from ta.momentum import RSIIndicator
from ta.trend import SMAIndicator
from ta.volatility import AverageTrueRange

def generate_signals(df):
    df["RSI"] = RSIIndicator(df["Price"], window=14).rsi()
    df["SMA_fast"] = SMAIndicator(df["Price"], window=20).sma_indicator()
    df["SMA_slow"] = SMAIndicator(df["Price"], window=50).sma_indicator()
    df["ATR"] = AverageTrueRange(df["Price"], df["Price"], df["Price"], window=14).average_true_range()

    df["buy_signal"] = (df["SMA_fast"] > df["SMA_slow"]) & (df["RSI"] < 65)
    df["sell_signal"] = (df["SMA_fast"] < df["SMA_slow"]) | (df["RSI"] > 70)

    return df