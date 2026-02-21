class MsgBox:
    def __init__(self, title: str, message: str, buttons: list):
        if len(buttons) > 3:
            raise ValueError("Maximum 3 buttons allowed")

        self.title = title
        self.message = message
        self.buttons = buttons

    def show(self):
        print(f"\n=== {self.title} ===")
        print(self.message)
        print()

        for i, btn in enumerate(self.buttons, 1):
            state = "" if btn.enabled else "(disabled)"
            print(f"{i}. {btn.label} {state}")

        choice = int(input("\nSelect: ")) - 1
        btn = self.buttons[choice]

        if btn.action:
            self._execute_action(btn.action)

    def _execute_action(self, action):
        t = action.get("type")

        if t == "close":
            print("MsgBox closed")
            return action.get("answer")

        if t == "url":
            print(f"Opening URL: {action['url']}")
            if action["close"]:
                print("MsgBox closed")

        if t == "exit":
            exit()

        if t == "exit_warn":
            print("WARNING:", action["message"])
            exit()

        if t == "custom":
            action["func"]()
