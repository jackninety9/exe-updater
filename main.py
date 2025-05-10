import os
import update_helper

# Check for update (if needed, it will launch updater and exit)
update_helper.check_for_update_and_run_updater()

# Show version after update check
with open('local_version.txt', 'r') as file:
    version = file.read().strip()

message = f"current version: {version}"
os.system(f'cmd /k echo {message}')
