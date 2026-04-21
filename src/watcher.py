# src/watcher.py

"""
V0.1 - Design layer only

This file represents the idea of a system that reacts to new files.
No actual file watching is implemented yet.
"""

from classifier import classify
from sorter import move_file


def on_new_file(file_path):
    """
    Conceptual flow:
    1. Classify file
    2. Move file
    """
    category = classify(file_path)
    move_file(file_path, category)
