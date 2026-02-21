class action:
    @staticmethod
    def close():
        return {"type": "close"}

    @staticmethod
    def close_with_answer(answer):
        return {"type": "close", "answer": answer}

    @staticmethod
    def url(url: str, close_after=True):
        return {
            "type": "url",
            "url": url,
            "close": close_after
        }

    @staticmethod
    def exit():
        return {"type": "exit"}

    @staticmethod
    def exitWithWarn(message: str):
        return {"type": "exit_warn", "message": message}

    @staticmethod
    def custom(func):
        return {"type": "custom", "func": func}
