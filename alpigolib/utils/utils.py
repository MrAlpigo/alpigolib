import uuid
import time
import hashlib
import re
import random

class Utils:

    @staticmethod
    def uuid():
        return str(uuid.uuid4())

    @staticmethod
    def timestamp(ms=False):
        return int(time.time() * 1000) if ms else int(time.time())

    @staticmethod
    def hash(text, algo="sha256"):
        h = hashlib.new(algo)
        h.update(text.encode("utf-8"))
        return h.hexdigest()

    @staticmethod
    def slugify(text):
        text = text.lower()
        text = re.sub(r"[^\w\s-]", "", text)
        text = re.sub(r"[\s_-]+", "-", text)
        return text.strip("-")

    @staticmethod
    def random_int(min=0, max=100):
        return random.randint(min, max)
