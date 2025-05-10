import os
import update_helper

update_helper.check_for_update()  # Explicitly run update check

# Read version from file
with open('local_version.txt', 'r') as file:
    version = file.read().strip()

message = f"current version 12345: {version}"
os.system(f'cmd /k echo {message}')