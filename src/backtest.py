def run_backtest(df):
    total_profit = 0

    for i in range(len(df)-1):
        if df["buy_signal"][i] and df["ML_Prob"][i] > 0.55:
            profit = df["Price"][i+1] - df["Price"][i]
            total_profit += profit

    return {"Total Profit": total_profit}