"""Filter Met Museum artwork records by department keyword.

Reads a JSON database of artwork entries, removes any records whose
``department`` field contains a specified keyword (case-insensitive), and
writes the cleaned dataset to a new file.

Input:  ``data/raw/highlight_paintings_db.json``
Output: ``data/raw/highlight_non_asian_paintings_db.json``
"""
import json




# 1. Load your existing JSON
JSON_FILEPATH_SOURCE = "data/raw/highlight_paintings_db.json"
JSON_FILEPATH_OUTPUT = "data/raw/highlight_non_asian_paintings_db.json"
with open(JSON_FILEPATH_SOURCE, 'r', encoding='utf-8') as f:
    data = json.load(f)

# 2. Filter out any entry where WORD is in the department name
WORD="asian"
filtered_data = [
    item for item in data 
    if WORD not in item.get('department', '').lower()
]

# 3. Save the cleaned version
with open(JSON_FILEPATH_OUTPUT, 'w', encoding='utf-8') as f:
    json.dump(filtered_data, f, indent=4, ensure_ascii=False)

print(f"Original entries: {len(data)}")
print(f"Cleaned entries: {len(filtered_data)}")
print(f"Removed: {len(data) - len(filtered_data)}")