import json
import sys


PARAMETER_TYPES = {
    "nodeName": "string",
    "nodeType": "string",
    "region": "string",
    "availabilityZone": "string",
    "instanceType": "string",
    "os": "string",
    "kubernetes.role": "string",
    "kubernetes.version": "string",
    "resources.cpu": "string",
    "resources.memory": "string",
    "resources.disk": "string",
    "labels.team": "string",
}


def convert_value(value, value_type):
    if value_type == "string":
        return value

    raise ValueError(f"Unsupported value type: {value_type}")


def set_nested_value(data, parameter, value):
    parts = parameter.split(".")
    current = data

    for part in parts[:-1]:
        if part not in current or not isinstance(current[part], dict):
            raise KeyError(f"Invalid parameter path: {parameter}")
        current = current[part]

    current[parts[-1]] = value


def modify_node(file_path, parameter, value):
    if parameter not in PARAMETER_TYPES:
        raise ValueError(f"Unsupported parameter: {parameter}")

    with open(file_path, "r") as file:
        data = json.load(file)

    converted_value = convert_value(
        value,
        PARAMETER_TYPES[parameter]
    )

    set_nested_value(data, parameter, converted_value)

    with open(file_path, "w") as file:
        json.dump(data, file, indent=2)
        file.write("\n")

    print(f"Updated {parameter} in {file_path}")


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print(
            "Usage: python modify_node.py "
            "<json-file> <parameter> <value>"
        )
        sys.exit(1)

    json_file = sys.argv[1]
    parameter = sys.argv[2]
    value = sys.argv[3]

    try:
        modify_node(json_file, parameter, value)
    except (ValueError, KeyError, json.JSONDecodeError) as exc:
        print(f"ERROR: {exc}")
        sys.exit(1)
