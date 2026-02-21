from alpigolib.providers.openai import OpenAIProvider
from alpigolib.providers.gemini import GeminiProvider
from alpigolib.providers.anthropic import AnthropicProvider

class AI:
    @staticmethod
    def openai(api_key: str, **kwargs):
        return OpenAIProvider(api_key, **kwargs)

    @staticmethod
    def gemini(api_key: str):
        return GeminiProvider(api_key)

    @staticmethod
    def anthropic(api_key: str):
        return AnthropicProvider(api_key)
