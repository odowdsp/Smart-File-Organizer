# src/sorter.py

import os
import shutil

def move_file(file_path, category):
    """
    V0.1 DESIGN ONLY (not running yet)
    """

    folder = os.path.join(os.path.dirname(file_path), category)

    if not os.path.exists(folder):
        os.makedirs(folder)

    filename = os.path.basename(file_path)
    destination = os.path.join(folder, filename)

    shutil.move(file_path, destination)
