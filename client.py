import requests, time
from functools import wraps

class RateLimiter:
    def __init__(self, max_calls=60, period=60):
        self.calls = []
        self.max = max_calls
        self.period = period

    def __call__(self, func):
        @wraps(func)
        def wrapper(*a, **kw):
            now = time.time()
            self.calls = [t for t in self.calls if now - t < self.period]
            if len(self.calls) >= self.max:
                time.sleep(self.period - (now - self.calls[0]))
            self.calls.append(time.time())
            return func(*a, **kw)
        return wrapper
