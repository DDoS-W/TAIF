"""
TAIF Project

Module:
experiment_manager.py

Purpose:
Manage experiment outputs.

Version:
Sprint 3.3
"""

import json
from pathlib import Path
from datetime import datetime


class ExperimentManager:

    def __init__(self, project_root):

        self.project_root = Path(project_root)

        self.output_dir = self.project_root / "experiments" / "outputs"

        self.prompt_dir = self.project_root / "experiments" / "prompts"

        self.log_dir = self.project_root / "experiments" / "logs"

        self.output_dir.mkdir(parents=True, exist_ok=True)
        self.prompt_dir.mkdir(parents=True, exist_ok=True)
        self.log_dir.mkdir(parents=True, exist_ok=True)

        print("Experiment Manager initialized.")

    def timestamp(self):

        return datetime.now().strftime("%Y%m%d_%H%M%S")

    def save_prompt(self, prompt):

        filename = self.prompt_dir / f"{self.timestamp()}.txt"

        with open(filename, "w", encoding="utf-8") as f:
            f.write(prompt)

        return filename

    def save_json(self, result):

        filename = self.output_dir / f"{self.timestamp()}.json"

        with open(filename, "w", encoding="utf-8") as f:
            json.dump(result, f, indent=4, ensure_ascii=False)

        return filename