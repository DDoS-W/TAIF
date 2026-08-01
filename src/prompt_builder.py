"""
TAIF Project

Module:
prompt_builder.py

Purpose:
Build standardized prompts for LLM investment analysis.

Version:
Sprint 3.1
"""

from typing import Dict, List


class PromptBuilder:

    def __init__(self):
        print("PromptBuilder initialized.")

    def build_prompt(
        self,
        stock_info: Dict,
        evidence_list: List[Dict]
    ) -> str:

        prompt = []

        # Role
        prompt.append(
            "You are a professional equity research analyst specializing in the Taiwan stock market.\n"
        )

        # Stock Information
        prompt.append("=== Stock Information ===")

        for key, value in stock_info.items():
            prompt.append(f"{key}: {value}")

        prompt.append("")

        # Evidence
        prompt.append("=== Market Evidence ===")

        if evidence_list:

            for i, item in enumerate(evidence_list, start=1):
                prompt.append(f"{i}. {item.get('title', '')}")

        else:

            prompt.append("No evidence available.")

        prompt.append("")

        # Task
        prompt.append("=== Analysis Task ===")

        prompt.append(
            """
Please analyze the stock based on the information above.

Return the following:

1. Investment Thesis

2. Sentiment
(Bullish / Neutral / Bearish)

3. Confidence
(0~100)

4. Key Risks

5. Recommendation

Return the answer in valid JSON.
"""
        )

        return "\n".join(prompt)