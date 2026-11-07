import tkinter as tk
from tkinter import ttk
import random

class MessageConsole(tk.Text):
    def __init__(self, master, min_height=1, max_height=10, **kwargs):
        # Enforce settings required for auto-resizing
        kwargs.update({
            "wrap": "word",        # Wrap lines at word boundaries
            "height": min_height,   # Start at minimum height
            "state": "disabled"    # Start as read-only
        })
        super().__init__(master, **kwargs)
        
        self.min_height = min_height
        self.max_height = max_height
        
        # Style configuration for error messages
        self.tag_config("error", foreground="red")
        self.tag_config("info", foreground="black")

    def log(self, message, is_error=False):
        """Adds a message to the console and resizes it."""
        self.config(state="normal")
        
        # Append newline if there's already content
        if self.get("1.0", "end-1c"):
            self.insert("end", "\n")
            
        tag = "error" if is_error else "info"
        self.insert("end", message, tag)
        self.see("end")
        
        self.config(state="disabled")
        self.adjust_height()

    def clear(self):
        """Clears all messages and shrinks the console to minimum height."""
        self.config(state="normal")
        self.delete("1.0", "end")
        self.config(state="disabled")
        self.adjust_height()

    def adjust_height(self):
        """Computes and updates the widget height based on visual lines."""
        # Use 'count' to get the actual number of display lines (accounting for word wraps)
        try:
            display_lines = self.count("1.0", "end", "displaylines")[0]
        except (tk.TclError, TypeError):
            # Fallback if the text widget is empty or count returns None
            display_lines = len(self.get("1.0", "end-1c").split("\n"))

        # Clamp the height between min_height and max_height
        new_height = max(self.min_height, min(display_lines, self.max_height))
        self.config(height=new_height)


# --- Example Application Usage ---
class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Dynamic Console Demo")
        self.geometry("500x400")
        
        # Main content area (Simulating your app layout)
        main_frame = ttk.LabelFrame(self, text="Application Controls", padding=20)
        main_frame.pack(fill="both", expand=True, padx=10, pady=10)
        
        # Buttons to simulate events
        ttk.Button(main_frame, text="Log Short Info", command=self.add_short_info).pack(pady=5)
        ttk.Button(main_frame, text="Log Long Text (Triggers Wrapping)", command=self.add_long_info).pack(pady=5)
        ttk.Button(main_frame, text="Log Error", command=self.add_error).pack(pady=5)
        ttk.Button(main_frame, text="Clear Console", command=self.clear_console).pack(pady=5)
        
        # Console Frame at the bottom
        console_frame = ttk.LabelFrame(self, text="Message Console", padding=10)
        console_frame.pack(fill="x", side="bottom", padx=10, pady=10)
        
        # Instantiate our auto-resizing console
        # Caps growth at 8 rows so it doesn't take over the whole UI
        self.console = MessageConsole(console_frame, min_height=1, max_height=8, bg="#f5f5f5", relief="flat")
        self.console.pack(fill="x", expand=True)

    def add_short_info(self):
        self.console.log("Success: Action completed.")

    def add_long_info(self):
        phrases = [
            "This is a significantly longer log message designed to demonstrate how the console wrapper wraps words neatly.",
            "Processing internal application data pipelines and rendering the graphical user interface elements synchronously without crashing."
        ]
        self.console.log(random.choice(phrases))

    def add_error(self):
        self.console.log("CRITICAL ERROR: Failed to connect to server backend.", is_error=True)

    def clear_console(self):
        self.console.clear()

if __name__ == "__main__":
    app = App()
    app.mainloop()