import sys
import time
import os
import urllib.request
import subprocess

def download_file(url, path):
    urllib.request.urlretrieve(url, path)

def main():
    if len(sys.argv) < 4:
        print("Usage: updater.exe <download_url> <target_exe> <new_version>")
        return

    download_url = sys.argv[1]
    target_exe = sys.argv[2]
    new_version = sys.argv[3]

    # Wait until target_exe can be written to (not running)
    print("Waiting for main.exe to close...")
    while True:
        try:
            os.rename(target_exe, target_exe)  # Touch file to test if unlocked
            break
        except PermissionError:
            time.sleep(1)

    # Download new main.exe
    try:
        print("Downloading new version...")
        download_file(download_url, target_exe)
    except Exception as e:
        print(f"Download failed: {e}")
        return

    # Update version number
    with open("local_version.txt", "w") as f:
        f.write(new_version)

    # Restart main.exe
    subprocess.Popen([target_exe])
    print("Update complete.")

if __name__ == "__main__":
    main()
