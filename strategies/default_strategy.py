def generate_signal(df):
    if df['macd'].iloc[-1] > df['macdsignal'].iloc[-1] and df['rsi'].iloc[-1] < 30:
        return 'buy'
    elif df['rsi'].iloc[-1] > 70:
        return 'sell'
    return 'hold'
