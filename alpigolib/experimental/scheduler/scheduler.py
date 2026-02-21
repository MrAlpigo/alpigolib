import threading
import time
from functools import wraps

def every(seconds: int):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            def loop():
                while True:
                    func(*args, **kwargs)
                    time.sleep(seconds)

            t = threading.Thread(target=loop, daemon=True)
            t.start()
            return t
        return wrapper
    return decorator
