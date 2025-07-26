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
    def get_response(self, conversation_history: list) -> str:
        """
        Sends a conversation history to the OpenRouter API and gets a response.

        Args:
            conversation_history: A list of message objects from the conversation.

        Returns:
            The response text from the API.
        """
        knowledge_base_text = get_knowledge_base_text()
        full_system_prompt = f"{SYSTEM_PROMPT}\n\n{knowledge_base_text}"

        messages = [
            ChatCompletionSystemMessageParam(role="system", content=full_system_prompt)
        ]
        for message in conversation_history:
            messages.append(ChatCompletionUserMessageParam(role=message["role"], content=message["content"]))

        try:
            response = client.chat.completions.create(
                model="openai/gpt-3.5-turbo-16k",
                messages=messages,
                max_tokens=500,
                temperature=0.5,
                extra_headers={
                    "HTTP-Referer": os.getenv("OPEN_ROUTER_REFERER"),
                    "X-Title": "LeanChat AI",
                }
            )
            return response.choices[0].message.content.strip()
        except Exception as e:
            print(f"An error occurred with OpenRouter API: {e}")
            return "Sorry, I'm having trouble connecting to my brain right now. Please try again later."
