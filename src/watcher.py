# src/watcher.py

def on_new_file(file_path):
  """"""""""""""""
  V0.1 Design Only
  """"""""""""""""
  category = classify(file_path)
  move_file(file_path, category)
