import time
class SafeExchange:
    def __init__(self, exchange):
        self.exchange = exchange
    def safe_call(self, method, *args, retries=3):
        for i in range(retries):
            try:
                return getattr(self.exchange, method)(*args)
            except Exception as e:
                time.sleep(2 ** i)
        raise Exception("Exchange call failed")
