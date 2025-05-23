def generate_order_book_signal(order_book):
    return 'buy' if order_book['bids'][0][1] > order_book['asks'][0][1] else 'sell'
