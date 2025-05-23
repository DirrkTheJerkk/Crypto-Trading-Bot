import ccxt
from config import API_KEY, SECRET_KEY
exchange = ccxt.kraken({
    'apiKey': API_KEY,
    'secret': SECRET_KEY,
    'enableRateLimit': True
})
