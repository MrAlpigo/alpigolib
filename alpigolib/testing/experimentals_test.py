# ===============================
# alpigolib – Experimental Demo
# ===============================

# ⏱️ Scheduler
from alpigolib.experimental.scheduler import every

# 🌱 Env Manager
from alpigolib.experimental.env import Env

# 💬 MsgBox
from alpigolib.experimental.msgbox import MsgBox, button, action

# 🔐 Crypto
from alpigolib.crypto import Crypto

# 📝 Logger
from alpigolib.logger import Logger


# -------------------------------
# Logger
# -------------------------------
log = Logger("demo")
log.info("alpigolib demo started")


# -------------------------------
# Env Manager
# -------------------------------
APP_NAME = Env.get("APP_NAME", default="AlpigoApp")
DEBUG = Env.bool("DEBUG", default=True)

log.info(f"App Name: {APP_NAME}")
log.info(f"Debug Mode: {DEBUG}")


# -------------------------------
# Scheduler
# -------------------------------
@every(seconds=3)
def background_job():
    log.info("Background job is running...")


# -------------------------------
# Crypto
# -------------------------------
password = "alpigolib123!"
hashed = Crypto.hash(password)

log.info(f"Password hash: {hashed}")
log.info(
    f"Password strength: {Crypto.password_strength(password)}"
)


# -------------------------------
# MsgBox
# -------------------------------
def custom_action():
    log.info("Custom action executed!")


msg = MsgBox(
    title="alpigolib Demo",
    message="Welcome to alpigolib experimental features 🚀",
    buttons=[
        button.OK,
        button.VISIT("https://github.com/alpigo/alpigolib"),
        button.Custom(
            "Custom Action",
            action.custom(custom_action)
        )
    ]
)

msg.show()


# -------------------------------
# Keep app alive for scheduler
# -------------------------------
import time
while True:
    time.sleep(1)
