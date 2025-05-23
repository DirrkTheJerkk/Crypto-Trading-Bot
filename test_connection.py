import ccxt
from config import API_KEY, SECRET_KEY
try:
    exchange = ccxt.kraken({
        'apiKey': "V6EdLO1YdzG8JgcW3vqP8B7IDX5MPGzeIdVq6U0WZZRHssVhjv8Qyicx",
        'secret': "2d0b3wAVLlt669oK7q17MrgrMLWZT42c68SX1F3/4GSiYHtMxBD0DYvn4rANbZNwu/IGeP3QFcG4eiwT29J0YQ==",
        'enableRateLimit': True
    })
    balance = exchange.fetch_balance()
    print("✅ Connected successfully. Available balance:")
    print(balance)
except Exception as e:
    print("❌ Connection failed:", str(e))
