import socket
import uuid
import requests

class Network:

    @staticmethod
    def isOnline(host="8.8.8.8", port=53, timeout=3):
        try:
            socket.setdefaulttimeout(timeout)
            socket.socket(socket.AF_INET, socket.SOCK_STREAM).connect((host, port))
            return True
        except Exception:
            return False

    @staticmethod
    def localIP():
        try:
            return socket.gethostbyname(socket.gethostname())
        except Exception:
            return None

    @staticmethod
    def publicIP():
        try:
            return requests.get("https://api.ipify.org").text
        except Exception:
            return None

    @staticmethod
    def mac():
        mac = uuid.getnode()
        return ":".join(f"{(mac >> i) & 0xff:02x}" for i in range(40, -1, -8))
