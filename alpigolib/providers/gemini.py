from alpigolib.base import BaseAI

class GeminiProvider(BaseAI):
    def chat(self, prompt: str):
        return f"[Gemini AI] {prompt}"
