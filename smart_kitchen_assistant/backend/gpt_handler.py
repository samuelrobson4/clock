import openai
from typing import Dict, Any

# Simple GPT prompt handler. In a real system you'd use more complex prompting
# and maintain conversation state. Here we just forward the message and optional
# function definitions to the OpenAI API and return the response text or
# function call data.

class GPTHandler:
    def __init__(self, api_key: str):
        openai.api_key = api_key
        self.model = "gpt-3.5-turbo"

    def chat(self, user_message: str, functions: Dict[str, Any] | None = None) -> Dict[str, Any]:
        messages = [{"role": "user", "content": user_message}]
        kwargs: Dict[str, Any] = {"model": self.model, "messages": messages}
        if functions:
            kwargs["functions"] = functions
        response = openai.ChatCompletion.create(**kwargs)
        choice = response.choices[0].message
        result = {"content": choice.get("content")}
        if "function_call" in choice:
            result["function_call"] = choice.function_call
        return result
