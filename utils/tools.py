import re


def sanitize_file_name(file: str) -> str:
    """
    Remove all characters that are not the following: 'a-zA-Z0-9_-'.
    If sanitized value is null-ish, trigger ValueError.
    """

    pattern = r"[^a-zA-Z0-9_-]+"  # Only allow these characters.
    sanitized = re.sub(pattern, "", file)

    if not sanitized:
        ValueError("String value had too many special characters.")

    return sanitized


def sanitize_ipv4(ip: str) -> str:
    """
    Only allow 'int' and '.' values.
    Does not validate if real IP.
    """

    pattern = r"[^0-9\.]+"
    sanitized = re.sub(pattern, "", ip)

    if not sanitized:
        ValueError("Int value had too many special and/or char characters.")

    return sanitized


def read_file(file: str) -> str:
    with open(file, 'r') as f:
        data = f.read()
    return data


def write_file(file: str, data: str) -> str:
    with open(file, 'w') as f:
        f.write(data)
    return "Write successful."
