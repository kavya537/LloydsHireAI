def read_file(file_path):
    with open(file_path, 'r') as file:
        return file.read()

def write_file(file_path, content):
    with open(file_path, 'w') as file:
        file.write(content)

def log_message(message):
    print(f"[LOG] {message}")

def validate_email(email):
    import re
    return re.match(r'^[\w\.-]+@[\w\.-]+$', email) is not None

def ensure_directory_exists(directory):
    import os
    if not os.path.exists(directory):
        os.makedirs(directory)