"""
TAIF Project

Module:
parser.py

Purpose:
Create standardized research records.

Version:
Sprint 3.4
"""

import json
from datetime import datetime


class TAIFParser:

    def __init__(self):

        print("TAIF Parser initialized.")

    def create_record(
        self,
        metadata,
        investment_thesis,
        sentiment,
        confidence,
        recommendation,
        key_risks
    ):

        return {

            "metadata": metadata,

            "analysis": {

                "investment_thesis": investment_thesis,

                "sentiment": sentiment,

                "confidence": confidence,

                "recommendation": recommendation

            },

            "risk": {

                "key_risks": key_risks

            }

        }

    def save_json(self, record, filepath):

        with open(filepath, "w", encoding="utf-8") as f:

            json.dump(
                record,
                f,
                indent=4,
                ensure_ascii=False
            )

        return filepath