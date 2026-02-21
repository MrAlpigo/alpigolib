class Button:
    def __init__(self, label, action=None, enabled=True):
        self.label = label
        self.action = action
        self.enabled = enabled


class button:
    OK = Button("OK")
    NO = Button("No")
    CANCEL = Button("Cancel")

    @staticmethod
    def OK_NO():
        return [button.OK, button.NO]

    @staticmethod
    def VISIT(url: str):
        from .actions import action
        return Button("Visit", action.url(url))

    @staticmethod
    def Custom(text: str, action=None, enabled=True):
        return Button(text, action, enabled)
