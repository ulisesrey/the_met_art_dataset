"""Filter Met Museum artwork records by department keyword."""
import argparse
import json


def filter_by_department(source: str, output: str, exclude: str) -> None:
    """Filter artwork records by excluding a department keyword.

    Reads a JSON database of artwork entries, removes any records whose
    ``department`` field contains the given keyword (case-insensitive), and
    writes the cleaned dataset to a new file.

    Args:
        source: Path to the input JSON file.
        output: Path to write the filtered JSON file.
        exclude: Keyword to exclude from the ``department`` field.
    """
    with open(source, 'r', encoding='utf-8') as f:
        data = json.load(f)

    filtered_data = [
        item for item in data
        if exclude.lower() not in item.get('department', '').lower()
    ]

    with open(output, 'w', encoding='utf-8') as f:
        json.dump(filtered_data, f, indent=4, ensure_ascii=False)

    print(f"Original entries: {len(data)}")
    print(f"Cleaned entries:  {len(filtered_data)}")
    print(f"Removed:          {len(data) - len(filtered_data)}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Filter Met artwork records by department keyword.")
    parser.add_argument("--input", default="data/raw/highlight_paintings_db.json", help="Input JSON file path.")
    parser.add_argument("--output", default="data/raw/highlight_non_asian_paintings_db.json", help="Output JSON file path.")
    parser.add_argument("--exclude", default="european", help="Department keyword to exclude (case-insensitive). Defaults to 'european'.")
    args = parser.parse_args()

    filter_by_department(source=args.input, output=args.output, exclude=args.exclude)
