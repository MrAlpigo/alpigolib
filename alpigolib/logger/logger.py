import datetime
import os

class Logger:
    LEVELS = {
        "INFO": "\033[94m",    # Blue
        "WARN": "\033[93m",    # Yellow
        "ERROR": "\033[91m",   # Red
        "DEBUG": "\033[90m"    # Gray
    }

    RESET = "\033[0m"

    def __init__(self, name="alpigolib", logfile=None, debug=False):
        self.name = name
        self.logfile = logfile
        self.debug_enabled = debug

        if logfile:
            os.makedirs(os.path.dirname(logfile), exist_ok=True)

    def _log(self, level, message):
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        color = self.LEVELS.get(level, "")
        formatted = f"[{timestamp}] [{self.name}] [{level}] {message}"

        print(f"{color}{formatted}{self.RESET}")

        if self.logfile:
            with open(self.logfile, "a", encoding="utf-8") as f:
                f.write(formatted + "\n")

    def info(self, message):
        self._log("INFO", message)

    def warn(self, message):
        self._log("WARN", message)

    def error(self, message):
        self._log("ERROR", message)

    def debug(self, message):
        if self.debug_enabled:
            self._log("DEBUG", message)
