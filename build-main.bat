@echo off
pyinstaller --noconfirm --onefile main.py
del main.spec
rmdir /s /q build
echo Build complete. Only "dist" folder kept.
