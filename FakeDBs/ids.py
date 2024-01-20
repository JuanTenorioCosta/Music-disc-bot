import json
import os

current_dir = os.path.dirname(__file__)
file_rel_path = "ids.txt"
file_path = os.path.join(current_dir, file_rel_path)

with open(file_path, 'r') as file:
    ids = json.load(file)

def write_ids(ids):
    with open(file_path, "w") as writing_file:
      json.dump(ids, writing_file, indent=4)