import os

# Read version from file
with open('local_version.txt', 'r') as file:
    version = file.read().strip()

# Create the message
message = f"current version: {version}"

# Windows-specific way to open a terminal and show the message
os.system(f'cmd /k echo {message}')
