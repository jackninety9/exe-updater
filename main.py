import os
import subprocess
import sys

def run_main_logic():
    # Show current version
    with open('local_version.txt', 'r') as file:
        version = file.read().strip()
    message = f"Current Version: {version}"
    os.system(f'cmd /k echo {message}')

if "--updated" in sys.argv:
    run_main_logic()
else:
    # Launch updater and exit
    subprocess.Popen(["update_helper.exe"])
    sys.exit()
