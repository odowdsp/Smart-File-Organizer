# src/classifier.py

"""
V0.1 - Classification logic (rule-based)
"""

def classify(file_path):
    suffix = file_path.split(".")[-1].lower()

    if suffix in ["jpg", "jpeg", "png", "gif"]:
        return "Images"

    if suffix in ["pdf", "docx", "txt"]:
        return "Documents"

    if suffix in ["py", "js", "html", "css"]:
        return "Code"

    if suffix in ["zip", "rar", "tar", "gz"]:
        return "Archives"

    return "Other"
