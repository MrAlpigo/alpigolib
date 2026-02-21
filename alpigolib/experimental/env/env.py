import os

class Env:
    @staticmethod
    def get(key: str, default=None, required: bool = False):
        value = os.getenv(key, default)

        if required and value is None:
            raise RuntimeError(f"Missing required env variable: {key}")

        return value

    @staticmethod
    def bool(key: str, default=False):
        return str(os.getenv(key, default)).lower() in ("1", "true", "yes")

    @staticmethod
    def int(key: str, default=0):
        return int(os.getenv(key, default))
