"""
TAIF Project

Module:
llm_engine.py

Purpose:
Unified interface for Large Language Models.

Version:
Sprint 3.2
"""


class LLMEngine:

    def __init__(self):

        print("LLM Engine initialized.")

    def generate(self, prompt: str) -> str:

        """
        Temporary mock response.

        Future:
            OpenAI
            Gemini
            Claude
        """

        response = f"""
MOCK RESPONSE

Prompt Length : {len(prompt)}

This is a temporary response.

Future versions will connect to:

- OpenAI
- Gemini
- Claude
"""

        return response