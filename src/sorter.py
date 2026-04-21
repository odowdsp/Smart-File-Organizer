# src/sorter.py

"""
V0.1 - File movement logic (no automation yet)
"""

import os
import shutil


def move_file(file_path, category):
    """
    Moves file into category folder.
    """

    folder = os.path.join(os.path.dirname(file_path), category)

    if not os.path.exists(folder):
        os.makedirs(folder)

    filename = os.path.basename(file_path)
    destination = os.path.join(folder, filename)

    shutil.move(file_path, destination)
