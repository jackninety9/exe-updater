import os
import subprocess
import sys

# Run the compiled updater and exit
subprocess.Popen(["update_helper.exe"])
sys.exit()

# Read version from file
with open('local_version.txt', 'r') as file:
    version = file.read().strip()

message = f"current version 12345: {version}"
os.system(f'cmd /k echo {message}')