import tkinter as tk
from tkinter import ttk
import pyautogui
import time
import threading
import keyboard

# Set PyAutoGUI failsafe and pause
pyautogui.FAILSAFE = True
pyautogui.PAUSE = 0.1

class AutoInputApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Auto Mouse and Keyboard Input")
        self.root.geometry("400x650")
        
        # Variables
        self.running = False
        self.automation_mode = tk.StringVar(value="mouse_and_keyboard")
        self.click_mode = tk.StringVar(value="fixed")
        self.click_type = tk.StringVar(value="left")
        self.fixed_x = tk.StringVar(value="500")
        self.fixed_y = tk.StringVar(value="500")
        self.keys = [tk.StringVar(value="") for _ in range(5)]
        self.interval = tk.StringVar(value="1")
        
        # GUI Elements
        tk.Label(root, text="Auto Mouse and Keyboard Input", font=("Arial", 14)).pack(pady=10)
        
        # Automation Mode Dropdown
        tk.Label(root, text="Automation Mode:").pack()
        mode_dropdown = ttk.Combobox(root, textvariable=self.automation_mode, values=["mouse_and_keyboard", "mouse", "keyboard"], state="readonly")
        mode_dropdown.pack()
        
        # Click Type Dropdown
        tk.Label(root, text="Click Type:").pack()
        click_type_dropdown = ttk.Combobox(root, textvariable=self.click_type, values=["left", "right", "both"], state="readonly")
        click_type_dropdown.pack()
        
        # Click Mode Selection
        tk.Label(root, text="Mouse Click Mode:").pack()
        tk.Radiobutton(root, text="Fixed Position", variable=self.click_mode, value="fixed").pack()
        tk.Radiobutton(root, text="Follow Cursor", variable=self.click_mode, value="cursor").pack()
        
        # Fixed Position Inputs
        tk.Label(root, text="Fixed X Coordinate:").pack()
        tk.Entry(root, textvariable=self.fixed_x).pack()
        tk.Label(root, text="Fixed Y Coordinate:").pack()
        tk.Entry(root, textvariable=self.fixed_y).pack()
        
        # Keyboard Inputs
        tk.Label(root, text="Keyboard Inputs (Alphabet Keys, e.g., a, b):").pack()
        for i in range(5):
            tk.Entry(root, textvariable=self.keys[i]).pack()
        
        # Interval Input
        tk.Label(root, text="Interval (seconds):").pack()
        tk.Entry(root, textvariable=self.interval).pack()
        
        # Buttons
        tk.Button(root, text="Start/Stop (F6)", command=self.toggle).pack(pady=10)
        tk.Button(root, text="Record Position (F5)", command=self.record_position).pack()
        
        # Bind hotkeys
        keyboard.add_hotkey('f6', self.toggle)
        keyboard.add_hotkey('f5', self.record_position)
        
    def validate_inputs(self):
        try:
            # Validate coordinates if mouse mode is active
            if self.automation_mode.get() in ["mouse_and_keyboard", "mouse"] and self.click_mode.get() == "fixed":
                x = int(self.fixed_x.get())
                y = int(self.fixed_y.get())
                if not (0 <= x <= pyautogui.size()[0] and 0 <= y <= pyautogui.size()[1]):
                    raise ValueError("Coordinates out of screen bounds")
            
            # Validate keys if keyboard mode is active
            if self.automation_mode.get() in ["mouse_and_keyboard", "keyboard"]:
                for key_var in self.keys:
                    key = key_var.get().strip().lower()
                    if key and (not key.isalpha() or len(key) != 1):
                        raise ValueError(f"Invalid key: {key}. Use single alphabet letters.")
            
            # Validate interval
            interval = float(self.interval.get())
            if interval <= 0:
                raise ValueError("Interval must be positive")
                
            return True
        except ValueError as e:
            tk.messagebox.showerror("Error", str(e))
            return False
    
    def automation_loop(self):
        while self.running:
            mode = self.automation_mode.get()
            click_type = self.click_type.get()
            
            # Perform mouse actions
            if mode in ["mouse_and_keyboard", "mouse"]:
                if self.click_mode.get() == "fixed":
                    x, y = int(self.fixed_x.get()), int(self.fixed_y.get())
                    if click_type == "left":
                        pyautogui.click(x, y, button="left")
                    elif click_type == "right":
                        pyautogui.click(x, y, button="right")
                    else:  # both
                        pyautogui.click(x, y, button="left")
                        time.sleep(0.1)  # Small delay to distinguish clicks
                        pyautogui.click(x, y, button="right")
                else:  # cursor
                    if click_type == "left":
                        pyautogui.click(button="left")
                    elif click_type == "right":
                        pyautogui.click(button="right")
                    else:  # both
                        pyautogui.click(button="left")
                        time.sleep(0.1)
                        pyautogui.click(button="right")
            
            # Perform keyboard actions
            if mode in ["mouse_and_keyboard", "keyboard"]:
                for key_var in self.keys:
                    key = key_var.get().strip().lower()
                    if key:
                        pyautogui.press(key)
                    
            time.sleep(float(self.interval.get()))
    
    def toggle(self):
        if not self.running:
            if self.validate_inputs():
                self.running = True
                threading.Thread(target=self.automation_loop, daemon=True).start()
        else:
            self.running = False
    
    def record_position(self):
        # Record current mouse position and update X, Y fields
        x, y = pyautogui.position()
        self.fixed_x.set(str(x))
        self.fixed_y.set(str(y))

if __name__ == "__main__":
    root = tk.Tk()
    app = AutoInputApp(root)
    root.mainloop()