import json
import sys


REQUIRED_FIELDS = [
    "environment",
    "appName",
    "version",
    "replicas",
    "logLevel",
    "database",
    "resources",
    "features"
]


def validate_environment(file_path, expected_environment):
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

    if not isinstance(data["appName"], str):
        print("ERROR: appName must be a string")
        return False

    if not isinstance(data["version"], str):
        print("ERROR: version must be a string")
        return False

    if not isinstance(data["replicas"], int):
        print("ERROR: replicas must be an integer")
        return False

    if not isinstance(data["logLevel"], str):
        print("ERROR: logLevel must be a string")
        return False

    if not isinstance(data["database"], dict):
        print("ERROR: database must be an object")
        return False

    if not isinstance(data["resources"], dict):
        print("ERROR: resources must be an object")
        return False

    if not isinstance(data["features"], dict):
        print("ERROR: features must be an object")
        return False

    print(f"Environment validation successful: {file_path}")
    return True


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print(
            "Usage: python validate_environment.py "
            "<json-file> <environment>"
        )
        sys.exit(1)

    file_path = sys.argv[1]
    expected_environment = sys.argv[2]

    if not validate_environment(file_path, expected_environment):
        sys.exit(1)
