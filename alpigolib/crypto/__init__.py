from .crypto import Crypto

def sha256(text: str) -> str:
    return Crypto.hash(text, "sha256")

__all__ = ["Crypto", "sha256"]
