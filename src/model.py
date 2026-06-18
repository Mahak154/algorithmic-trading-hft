from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

def train_model(df):
    df["Forward_Return"] = df["Price"].shift(-1) - df["Price"]
    df["Target"] = (df["Forward_Return"] > 0).astype(int)

    df = df.dropna()

    X = df[["RSI", "SMA_fast", "SMA_slow", "ATR"]]
    y = df["Target"]

    X_train, X_test, y_train, y_test = train_test_split(X, y, shuffle=False)

    model = RandomForestClassifier()
    model.fit(X_train, y_train)

    df["ML_Prob"] = model.predict_proba(X)[:, 1]

    return df