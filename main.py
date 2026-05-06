import tkinter as tk
from tkinter import ttk
import subprocess
import os
import sys

class FastCrystalApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Fast Crystal")
        self.root.geometry("400x300")
        self.root.resizable(False, False)
        
        # Variables
        self.status = tk.BooleanVar(value=False)
        self.process1 = None
        self.process2 = None
        
        self.setup_ui()
        
    def setup_ui(self):
        # Title
        title = tk.Label(self.root, text="FAST CRYSTAL", font=("Arial", 18, "bold"))
        title.pack(pady=20)
        
        # Toggle
        toggle_frame = tk.Frame(self.root)
        toggle_frame.pack(pady=30)
        
        self.toggle = ttk.Checkbutton(
            toggle_frame,
            text="Toggle Fast Crystal Status",
            variable=self.status,
            style="Switch.TCheckbutton",
            command=self.toggle_changed
        )
        self.toggle.pack()
        
        # Status label
        self.status_label = tk.Label(self.root, text="Status: OFF", font=("Arial", 14), fg="red")
        self.status_label.pack(pady=20)
        
        # Apply custom style for better toggle look
        style = ttk.Style()
        style.configure("Switch.TCheckbutton", font=("Arial", 12))
        
    def toggle_changed(self):
        if self.status.get():  # Turned ON
            self.status_label.config(text="Status: ON", fg="green")
            self.start_scripts()
        else:  # Turned OFF
            self.status_label.config(text="Status: OFF", fg="red")
            self.stop_scripts()
    
    def start_scripts(self):
        try:
            script1 = "fast_crystal.py"
            script2 = "fast_crystal_test.py"
            
            if not os.path.exists(script1) or not os.path.exists(script2):
                self.status_label.config(text="Error: Python files not found!", fg="red")
                self.status.set(False)
                return
            
            # Run both scripts
            self.process1 = subprocess.Popen([sys.executable, script1], 
                                           cwd=os.getcwd(), 
                                           creationflags=subprocess.CREATE_NEW_CONSOLE)
            
            self.process2 = subprocess.Popen([sys.executable, script2], 
                                           cwd=os.getcwd(), 
                                           creationflags=subprocess.CREATE_NEW_CONSOLE)
            
        except Exception as e:
            self.status_label.config(text=f"Error: {str(e)}", fg="red")
            self.status.set(False)
    
    def stop_scripts(self):
        try:
            if self.process1:
                self.process1.terminate()
            if self.process2:
                self.process2.terminate()
        except:
            pass  # ignore errors when killing

    def run(self):
        self.root.protocol("WM_DELETE_WINDOW", self.on_close)
        self.root.mainloop()
    
    def on_close(self):
        self.stop_scripts()
        self.root.destroy()

if __name__ == "__main__":
    app = FastCrystalApp()
    app.run()