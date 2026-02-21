from alpigolib.base import BaseAI

class OpenAIProvider(BaseAI):
    def __init__(self, api_key: str, model="gpt-4o-mini"):
        super().__init__(api_key)
        self.model = model
        # gerçek entegrasyonda:
        # import openai
        # openai.api_key = api_key

    def chat(self, prompt: str):
        # MOCK – gerçek API sonra
        return f"[OpenAI:{self.model}] {prompt}"
