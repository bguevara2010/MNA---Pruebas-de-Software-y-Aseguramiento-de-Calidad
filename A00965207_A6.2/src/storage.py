"""Storage module."""

import json
import os


class Storage:
    """Handles file persistence in JSON format."""

    @staticmethod
    def load(file_path: str) -> list:
        """Load JSON data from a file."""
        if not os.path.exists(file_path):
            return []

        try:
            with open(file_path, "r", encoding="utf-8") as file:
                return json.load(file)
        except (json.JSONDecodeError, IOError) as error:
            print(f"Error loading file {file_path}: {error}")
            return []

    @staticmethod
    def save(file_path: str, data: list) -> None:
        """Save data to a JSON file."""
        try:
            with open(file_path, "w", encoding="utf-8") as file:
                json.dump(data, file, indent=4)
        except IOError as error:
            print(f"Error saving file {file_path}: {error}")
