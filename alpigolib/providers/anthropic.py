from alpigolib.base import BaseAI

class AnthropicProvider(BaseAI):
    def chat(self, prompt: str):
        return f"[Claude AI] {prompt}"
