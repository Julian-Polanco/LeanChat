import os

import openai
from django.conf import settings
from openai.types.chat import ChatCompletionSystemMessageParam, ChatCompletionUserMessageParam

from .knowledge_base import SYSTEM_PROMPT, get_knowledge_base_text

client = openai.OpenAI(
  base_url="https://openrouter.ai/api/v1",
  api_key=settings.OPENROUTER_API_KEY,
)

class OpenRouterEngine:
    """
    A connector for the OpenRouter API.
    """
    def get_response(self, user_message: str) -> str:
        """
        Sends a message to the OpenRouter API and gets a response.

        Args:
            user_message: The message from the user.

        Returns:
            The response text from the API.
        """
        knowledge_base_text = get_knowledge_base_text()
        full_system_prompt = f"{SYSTEM_PROMPT}\n\n{knowledge_base_text}"

        try:
            messages = [
                ChatCompletionSystemMessageParam(role="system", content=full_system_prompt),
                ChatCompletionUserMessageParam(role="user", content=user_message)
            ]

            response = client.chat.completions.create(
                model=os.getenv("OPEN_ROUTER_MODEL"),
                messages=messages,
                max_tokens=os.getenv("OPEN_ROUTER_MAX_TOKENS"),
                temperature=os.getenv("OPEN_ROUTER_TEMPERATURE"),
                extra_headers={
                    "HTTP-Referer": os.getenv("OPEN_ROUTER_REFERER"),
                    "X-Title": "LeanChat AI",
                }
            )
            return response.choices[0].message.content.strip()
        except Exception as e:
            # Handle potential API errors
            print(f"An error occurred with OpenRouter API: {e}")
            return "Sorry, I'm having trouble connecting to my brain right now. Please try again later."
