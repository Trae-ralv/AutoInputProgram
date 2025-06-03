# Auto Mouse and Keyboard Input

## Description
Auto Mouse and Keyboard Input is a Windows tool for automating mouse clicks and keyboard inputs through an intuitive Tkinter GUI. It offers three automation modes (mouse and keyboard, mouse only, keyboard only), selectable click types (left, right, or both), and fixed or cursor-based mouse clicks. Users can input up to five alphabet keys, set custom intervals, record mouse positions with F5, and toggle automation with F6. Packaged as a standalone .exe, it’s ideal for repetitive tasks like form filling or gaming macros.

## Prerequisites
- **Operating System**: Windows 7 or later.
- **Python**: Version 3.13.3 (Microsoft Store or python.org).
- **Dependencies**: `pyautogui`, `keyboard`, `pyinstaller` (via pip).
- **Storage**: ~20 MB for .exe and source.

## Installation
Steps to create the .exe from source.

1. **Install Python 3.13.3**:
   - Download from python.org (recommended) or use Microsoft Store version.
   - Check “Add Python to PATH” during installation.
   - Verify:
     ```
     python --version
     ```
     Expected: `Python 3.13.3`.

2. **Install Dependencies**:
   - In PowerShell or Command Prompt:
     ```
     python -m pip install pyautogui keyboard pyinstaller
     ```
   - Verify PyInstaller:
     ```
     python -m PyInstaller --version
     ```
     Expected: `6.13.0` or higher.

3. **Set Up Project Folder**:
   - Create `C:\AutoInputProgram`.
   - Save `auto_input_program.py` (provided separately) in this folder.

4. **Create the .exe**:
   - Navigate:
     ```
     cd C:\AutoInputProgram
     ```
   - Run:
     ```
     python -m PyInstaller --onefile --windowed auto_input_program.py
     ```
     - If PyInstaller fails, use:
       ```
       C:\Users\<YourUser>\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\Scripts\pyinstaller.exe --onefile --windowed auto_input_program.py
       ```
       Replace `<YourUser>` with your username.
     - Output: `C:\AutoInputProgram\dist\auto_input_program.exe`.

5. **Set Up .exe Folder**:
   - Create `C:\AutoInputApp`.
   - Copy `auto_input_program.exe` from `C:\AutoInputProgram\dist` to `C:\AutoInputApp`.
   - Optionally delete `C:\AutoInputProgram\build`, `C:\AutoInputProgram\dist`, `auto_input_program.spec`.

## Usage
1. **Run**:
   - Double-click `auto_input_program.exe` in `C:\AutoInputApp`.
   - GUI opens at 400x500 pixels (adjustable in source).

2. **Configure**:
   - **Automation Mode**: Choose “mouse_and_keyboard,” “mouse,” or “keyboard” from dropdown.
   - **Click Type**: Select “left,” “right,” or “both” for mouse-enabled modes.
   - **Mouse Click Mode**: Pick “Fixed Position” (uses X, Y) or “Follow Cursor.”
   - **Fixed X, Y**: Enter manually or use F5 to record mouse position.
   - **Keyboard Inputs**: Add 0–5 alphabet letters (e.g., a, b) for keyboard-enabled modes.
   - **Interval**: Set delay in seconds (e.g., 1).

3. **Run Automation**:
   - Press F6 or click “Start/Stop (F6)” to start/stop.
   - Failsafe: Move mouse to screen corner to stop.

4. **Record Position**:
   - Move mouse, press F5 or click “Record Position (F5)” to set X, Y.

## Customization
- **Window Size**: Edit `self.root.geometry("400x500")` in `auto_input_program.py` (e.g., `400x550`), then recompile.
- **Features**: Modify script and recompile.

## Troubleshooting
- **PyInstaller Not Recognized**:
  - Use `python -m PyInstaller` or add to PATH:
    - Environment Variables > `Path` > Add: `C:\Users\<YourUser>\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\Scripts`.
  - Reinstall:
    ```
    python -m pip install --upgrade pyinstaller
    ```
- **.exe Fails**:
  - Install Microsoft Visual C++ Redistributable (microsoft.com).
  - Exclude `auto_input_program.exe` from antivirus.
- **GUI Issues**:
  - Increase height (e.g., `400x550`) if elements are cut off.
- **Hotkeys**:
  - Check F5/F6 conflicts.
- **Microsoft Store Python**:
  - Switch to python.org’s Python 3.13.3 if needed:
    - Uninstall Store version, install from python.org, reinstall dependencies.

## License
Unlicensed, provided as-is for personal use.

## Support
For issues, check script comments or seek Python/Tkinter/PyInstaller community support.