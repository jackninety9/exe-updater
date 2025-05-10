import urllib.request
import os

GITHUB_RAW_VERSION = "https://raw.githubusercontent.com/jackninety9/exe-updater/main/version.txt"
GITHUB_EXE_URL = "https://github.com/jackninety9/exe-updater/raw/main/main.exe"
LOCAL_VERSION_FILE = "local_version.txt"
LOCAL_EXE_FILE = "main.exe"


def get_text_from_url(url):
    with urllib.request.urlopen(url) as response:
        return response.read().decode().strip()

def download_file(url, path):
    urllib.request.urlretrieve(url, path)

def check_for_update():
    # Get local version
    if not os.path.exists(LOCAL_VERSION_FILE):
        print("No local_version.txt found.")
        return

    with open(LOCAL_VERSION_FILE, 'r') as file:
        local_version = file.read().strip()

    # Get latest version from GitHub
    try:
        latest_version = get_text_from_url(GITHUB_RAW_VERSION)
    except:
        print("Failed to fetch latest version.")
        return

    # Compare versions
    if local_version != latest_version:
        print("New version found. Updating...")
        try:
            download_file(GITHUB_EXE_URL, LOCAL_EXE_FILE)
            with open(LOCAL_VERSION_FILE, 'w') as file:
                file.write(latest_version)
            print("Update complete.")
        except:
            print("Failed to download or save the new version.")
    else:
        print("You have the latest version.")

if __name__ == "__main__":
    check_for_update()
