import urllib.request
import os
import sys
import subprocess
import time

GITHUB_VERSION = "https://raw.githubusercontent.com/jackninety9/exe-updater/main/version.txt"
GITHUB_NEW_MAIN = "https://github.com/jackninety9/exe-updater/raw/main/dist/main.exe"
LOCAL_VERSION_FILE = "local_version.txt"
UPDATER_EXE = "updater.exe"
LOCAL_MAIN = "main.exe"

def get_text_from_url(url):
    url += f"?_={int(time.time())}"  # cache-busting query
    with urllib.request.urlopen(url) as response:
        return response.read().decode().strip()

def check_for_update_and_run_updater():
    if not os.path.exists(LOCAL_VERSION_FILE):
        return

    with open(LOCAL_VERSION_FILE, 'r') as file:
        local_version = file.read().strip()

    try:
        latest_version = get_text_from_url(GITHUB_VERSION)
    except:
        return

    if local_version != latest_version:
        print("New version found. Launching updater...")
        # Launch the updater and pass arguments
        subprocess.Popen([
            UPDATER_EXE,
            GITHUB_NEW_MAIN,
            LOCAL_MAIN,
            latest_version
        ])
        sys.exit()  # Exit so updater can replace main.exe
