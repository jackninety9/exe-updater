import os
import subprocess
import sys
import time

def replace_update_helper():
    if os.path.exists("update_helper_new.exe"):
        print("Attempting to replace update_helper.exe...")
        for attempt in range(5):  # Try up to 5 times
            try:
                os.remove("update_helper.exe")
                os.rename("update_helper_new.exe", "update_helper.exe")
                print("update_helper.exe updated successfully.")
                return
            except PermissionError:
                print(f"Attempt {attempt + 1}: Access denied. Retrying...")
                time.sleep(1)
            except Exception as e:
                print(f"Unexpected error during update_helper.exe replacement: {e}")
                break
        print("Failed to replace update_helper.exe after several attempts.")

def run_main_logic():
    with open('local_version.txt', 'r') as file:
        version = file.read().strip()
    message = f"current version: {version}"
    os.system(f'cmd /k echo {message}')

if "--updated" in sys.argv:
    run_main_logic()
else:
    replace_update_helper()
    subprocess.Popen(["update_helper.exe"])
    sys.exit()
