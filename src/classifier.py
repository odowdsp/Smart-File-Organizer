#src/classifier.py

def classify(file_path):
  suffix = file_path.split(".")[-1].lower()

  if suffix in ["jpg", "png", "jpeg"]:
      return "Images"
   
  if suffix in ["pdf", "docx", "txt"]:
      return "Documents"

  if suffix in ["py", "js", "html"]:
      return "Code"

  if suffix in ["zip", "rar"]:
      return "Archives"

  return "Other"
