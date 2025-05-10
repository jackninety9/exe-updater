import urllib.request
import time
import os
import subprocess
import sys

# Remote URLs
GITHUB_RAW_VERSION = "https://raw.githubusercontent.com/jackninety9/exe-updater/main/version.txt"
GITHUB_MAIN_EXE_URL = "https://github.com/jackninety9/exe-updater/raw/main/dist/main.exe"
GITHUB_UPDATER_EXE_URL = "https://github.com/jackninety9/exe-updater/raw/main/dist/update_helper.exe"

# Local files
LOCAL_VERSION_FILE = "local_version.txt"
LOCAL_MAIN_EXE = "main.exe"
LOCAL_UPDATER_EXE = "update_helper.exe"

def get_text_from_url(url):
    url_with_bust = f"{url}?_={int(time.time())}"
    with urllib.request.urlopen(url_with_bust) as response:
        return response.read().decode().strip()

def download_file(url, path):
    urllib.request.urlretrieve(url, path)

def check_for_update():
    if not os.path.exists(LOCAL_VERSION_FILE):
        print("No local_version.txt found.")
        return False

    with open(LOCAL_VERSION_FILE, 'r') as file:
        local_version = file.read().strip()

    try:
        latest_version = get_text_from_url(GITHUB_RAW_VERSION)
    except:
        print("Failed to fetch latest version.")
        return False

    if local_version != latest_version:
        print("New version found. Updating...")
        try:
            # Download and replace main.exe
            download_file(GITHUB_MAIN_EXE_URL, LOCAL_MAIN_EXE)

            # Download and replace update_helper.exe
            download_file(GITHUB_UPDATER_EXE_URL, LOCAL_UPDATER_EXE)

            # Update the version file
            with open(LOCAL_VERSION_FILE, 'w') as file:
                file.write(latest_version)

            print("Update complete.")
            return True
        except Exception as e:
            print(f"Failed to update files: {e}")
            return False
    else:
        print("You have the latest version.")
        return True

if __name__ == "__main__":
    updated = check_for_update()
    if updated:
        subprocess.Popen([LOCAL_MAIN_EXE, "--updated"])  # Relaunch with flag to skip updater loop

