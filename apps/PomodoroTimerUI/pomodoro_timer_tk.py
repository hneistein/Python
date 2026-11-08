import tkinter as tk
from tkinter import ttk
import time
import sys

email_to_text = __import__("email-to-text")

class MessageConsole(tk.Text):
    def __init__(self, master, min_height=1, max_height=50, **kwargs):
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

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Pomodoro Timer")
        self.geometry("500x400")
        
        # Main content area (Simulating your app layout)
        main_frame = ttk.LabelFrame(self, text="Application Entry", padding=20)
        main_frame.pack(fill="both", expand=True, padx=10, pady=10)
        
        # main_frame labels and entry fields
        ttk.Label(main_frame, text="Work Duration:").pack()
        self.entry_work_duration = ttk.Entry(main_frame)
        self.entry_work_duration.pack()
        ttk.Label(main_frame, text="Break Duration:").pack()
        self.entry_break_duration = ttk.Entry(main_frame)
        self.entry_break_duration.pack()
        ttk.Label(main_frame, text="Cycles:").pack()
        self.entry_cycles = ttk.Entry(main_frame)
        self.entry_cycles.pack()
        frame = ttk.Frame(main_frame, relief='raised', borderwidth=5).pack()
        self.submit_button = ttk.Button(frame, text="Submit", command=self.submit_duration)
        self.submit_button.pack()
        
        # Console Frame at the bottom
        console_frame = ttk.LabelFrame(self, text="Message Console", padding=10)
        console_frame.pack(fill="x", side="bottom", padx=10, pady=10)
        
        # Instantiate our auto-resizing console
        # Caps growth at 8 rows so it doesn't take over the whole UI
        self.console = MessageConsole(console_frame, min_height=1, max_height=8, bg="#f5f5f5", relief="flat")
        self.console.pack(fill="x", expand=True)

    def submit_duration(self):
        # disable the submit button so it can't execute again while it is in process
        self.submit_button.config(state="disable")
        self.console.clear()
        self.console.log("Starting process...")
        self.update()

        try:

            work_duration = int(self.entry_work_duration.get() or 25)
            break_duration = int(self.entry_break_duration.get() or 5)
            cycles = int(self.entry_cycles.get() or 4)

            for cycle in range(cycles):
                self.console.log(f"Cycle {cycle + 1}/{cycles}: Start working for {work_duration} minutes.")
                # tells Tkinter to refresh the UI and update the message console
                self.update()
                time.sleep(work_duration * 60)
                self.bell()
                self.console.log(f"Break time! Relax for {break_duration} minutes.")
                # tells Tkinter to refresh the UI and update the message console
                self.update()
                time.sleep(break_duration * 60)
                self.bell()
                self.console.log("Break is over! Back to work.")
                self.console.log(email_to_text.send_break_over_sms())
                # tells Tkinter to refresh the UI and update the message console
                self.update()
                

            self.console.log("All cycles completed! Great job!")

        except Exception as e:
            self.console.log(f"An error occurred: {e}", is_error=True)

        finally:
            self.submit_button.config(state="normal")

if __name__ == "__main__":
    app = App()
    app.mainloop()
