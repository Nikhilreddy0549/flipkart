import json
import sys


REQUIRED_FIELDS = [
    "environment",
    "nodeName",
    "nodeType",
    "region",
    "availabilityZone",
    "instanceType",
    "os",
    "kubernetes",
    "resources",
    "labels"
]


def validate_node(file_path, expected_environment):
    try:
        with open(file_path, "r") as file:
            data = json.load(file)
    except json.JSONDecodeError as exc:
        print(f"ERROR: Invalid JSON: {exc}")
        return False
    except FileNotFoundError:
        print(f"ERROR: File not found: {file_path}")
        return False

    for field in REQUIRED_FIELDS:
        if field not in data:
            print(f"ERROR: Missing required field: {field}")
            return False

    if data["environment"] != expected_environment:
        print(
            f"ERROR: Environment mismatch. "
            f"Expected '{expected_environment}', "
            f"found '{data['environment']}'"
        )
        return False

    string_fields = [
        "nodeName",
        "nodeType",
        "region",
        "availabilityZone",
        "instanceType",
        "os"
    ]

    for field in string_fields:
        if not isinstance(data[field], str):
            print(f"ERROR: {field} must be a string")
            return False

    if not isinstance(data["kubernetes"], dict):
        print("ERROR: kubernetes must be an object")
        return False

    if not isinstance(data["resources"], dict):
        print("ERROR: resources must be an object")
        return False

    if not isinstance(data["labels"], dict):
        print("ERROR: labels must be an object")
        return False

    print(f"Node validation successful: {file_path}")
    return True


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print(
            "Usage: python validate_node.py "
            "<json-file> <environment>"
        )
        sys.exit(1)

    file_path = sys.argv[1]
    expected_environment = sys.argv[2]

    if not validate_node(file_path, expected_environment):
        sys.exit(1)
