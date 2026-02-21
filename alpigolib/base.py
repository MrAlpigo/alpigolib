class BaseAI:
    def __init__(self, api_key: str):
        if not api_key:
            raise ValueError("API key boş olamaz")
        self.api_key = api_key

    def chat(self, prompt: str):
        raise NotImplementedError("chat() bu AI için tanımlı değil")