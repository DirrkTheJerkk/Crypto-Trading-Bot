import pandas as pd, time
def replay_trades(file_path, speed=1.0):
    df = pd.read_csv(file_path)
    for _, row in df.iterrows():
        print(f"{row['timestamp']}: {row['symbol']} {row['signal'].upper()} @ {row['price']}")
        time.sleep(speed)
