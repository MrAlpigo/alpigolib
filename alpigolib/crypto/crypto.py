import hashlib
import secrets
import string
import hmac
from cryptography.fernet import Fernet

class Crypto:

    # 🔑 HASH
    @staticmethod
    def hash(text: str, algo: str = "sha256") -> str:
        h = hashlib.new(algo)
        h.update(text.encode("utf-8"))
        return h.hexdigest()

    # 🔐 AES KEY
    @staticmethod
    def generate_key() -> str:
        return Fernet.generate_key().decode()

    # 🔒 ENCRYPT
    @staticmethod
    def encrypt(text: str, key: str) -> str:
        f = Fernet(key.encode())
        return f.encrypt(text.encode()).decode()

    # 🔓 DECRYPT
    @staticmethod
    def decrypt(token: str, key: str) -> str:
        f = Fernet(key.encode())
        return f.decrypt(token.encode()).decode()

    # 🔐 SECURE RANDOM STRING
    @staticmethod
    def random_string(length: int = 32) -> str:
        alphabet = string.ascii_letters + string.digits
        return "".join(secrets.choice(alphabet) for _ in range(length))

    # 🛡️ PASSWORD STRENGTH
    @staticmethod
    def password_strength(password: str) -> dict:
        score = 0

        if len(password) >= 8:
            score += 1
        if any(c.islower() for c in password):
            score += 1
        if any(c.isupper() for c in password):
            score += 1
        if any(c.isdigit() for c in password):
            score += 1
        if any(c in "!@#$%^&*()-_=+[]{};:,.<>?" for c in password):
            score += 1

        levels = {
            0: "very weak",
            1: "weak",
            2: "medium",
            3: "good",
            4: "strong",
            5: "very strong"
        }

        return {
            "score": score,
            "level": levels.get(score, "unknown")
        }

    # ⏱️ TIMING SAFE COMPARE
    @staticmethod
    def safe_compare(a: str, b: str) -> bool:
        return hmac.compare_digest(a, b)
