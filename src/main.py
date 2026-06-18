import pandas as pd
from strategy import generate_signals
from model import train_model
from backtest import run_backtest

df = pd.read_csv("data.csv")

df = generate_signals(df)
df = train_model(df)

performance = run_backtest(df)

print(performance)