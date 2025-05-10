import os
import subprocess
import sys

# Optional: replace old update_helper if new version exists
if os.path.exists("update_helper_new.exe"):
    try:
        os.remove("update_helper.exe")
        os.rename("update_helper_new.exe", "update_helper.exe")
        print("update_helper.exe updated successfully.")
    except Exception as e:
        print(f"Failed to replace update_helper.exe: {e}")

def run_main_logic():
    # Read version from file
    with open('local_version.txt', 'r') as file:
        version = file.read().strip()
    message = f"Current Version = {version}"
    os.system(f'cmd /k echo {message}')

# If --updated flag is present, skip updater
if "--updated" in sys.argv:
    run_main_logic()
else:
    # Launch updater and exit
    subprocess.Popen(["update_helper.exe"])
    sys.exit()
