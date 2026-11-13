import tkinter as tk
import threading
from pathlib import Path
from dotenv import set_key
import time
import webbrowser

email_to_text = __import__("email-to-text")

class PomodoroApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Pomodoro Timer")
        self.root.geometry("300x200")
        self.root.option_add('*tearOff', tk.FALSE)

        # Timer state variables
        self.timer_id = None
        self.remaining_seconds = 0
        self.current_cycle = 0
        self.total_cycles = 0
        self.is_work_phase = True

        # Create Application Menu
        self.create_menu()

        # UI Elements
        # Add label and entry fields here for work duration, break duration, and num of cycles
        # Put them in a frame, in a Label: Entry field row
        self.status_label = tk.Label(root, text="Ready", font=("Helvetica", 14))
        self.status_label.pack(pady=(20, 5))

        self.time_label = tk.Label(root, text="00:00", font=("Helvetica", 36, "bold"))
        self.time_label.pack(pady=10)

        btn_frame = tk.Frame(root)
        btn_frame.pack(pady=10)

        self.start_btn = tk.Button(btn_frame, text="Start", width=10, command=self.start_pomodoro)
        self.start_btn.pack(side=tk.LEFT, padx=5)

        self.cancel_btn = tk.Button(btn_frame, text="Cancel", width=10, command=self.cancel_pomodoro, state=tk.DISABLED)
        self.cancel_btn.pack(side=tk.LEFT, padx=5)

        self.system_label = tk.Label(root, text="", font=("Helvetica", 12))
        self.system_label.pack()

    def create_menu(self):
        menubar = tk.Menu(self.root)
        self.root.config(menu=menubar)

        app_menu = tk.Menu(menubar)
        menubar.add_cascade(label="Application Menu", menu=app_menu)
        app_menu.add_command(label="Enter App Data", command=self.set_app_data)
        app_menu.add_command(label="SMS Setup", command=self.update_SMS_file)
        app_menu.add_command(label="About", command=self.create_about_page)

    def update_SMS_file(self):
        env_entry = tk.Toplevel(self.root)
        env_entry.title("Pomodoro Timer - Create or Update ENV file")
        env_entry.geometry("300x300")

        # Main content area (Simulating your app layout)
        main_frame = tk.LabelFrame(env_entry, text="Environment Variables Entry")
        main_frame.pack(fill="both", padx=10, pady=10)

        # main_frame labels and entry fields
        tk.Label(main_frame, text="SMTP Server:").pack()
        self.smtp_server = tk.Entry(main_frame)
        self.smtp_server.pack()
        tk.Label(main_frame, text="SMPT Port:").pack()
        self.smtp_port = tk.Entry(main_frame)
        self.smtp_port.pack()
        tk.Label(main_frame, text="Sender Email:").pack()
        self.sender_email = tk.Entry(main_frame)
        self.sender_email.pack() 
        tk.Label(main_frame, text="Sender Password:").pack()
        self.sender_pass = tk.Entry(main_frame)
        self.sender_pass.pack()
        tk.Label(main_frame, text="Recipient's SMS Gateway:").pack()
        self.recipient_sms_gateway = tk.Entry(main_frame)
        self.recipient_sms_gateway.pack() 
        self.submit_button = tk.Button(main_frame, text="Submit", width=12, command=self.update_env_file)
        self.submit_button.pack(side="left", padx=75)  

    def update_env_file(self):
        env_path = Path(".env")
        # Create the empty file if it doesn't exist yet
        env_path.touch(exist_ok=True)       

        set_key(str(env_path), "SMTP_SERVER", self.smtp_server.get())
        set_key(str(env_path), "SMTP_PORT", self.smtp_port.get())  
        set_key(str(env_path), "SENDER_EMAIL", self.sender_email.get())
        set_key(str(env_path), "SENDER_PASSWORD", self.sender_pass.get())
        set_key(str(env_path), "RECIPIENT_SMS_GATEWAY", self.recipient_sms_gateway.get())    

        status = "Creation / update of .env file successful."
        self.root.after(0, lambda: self.system_label.config(text=f"{status}"))
        self.submit_button.winfo_toplevel().destroy()

    def open_url(self, url):
        webbrowser.open_new(url)

    def create_about_page(self):
        about_pg = tk.Toplevel(self.root)
        about_pg.title("Pomodoro Timer - About")
        about_pg.geometry("300x200")

        self.link = tk.Label(
            about_pg, 
            text="Visit my website", 
            fg="blue",
            cursor="hand2",
            font=("Arial", 12, "underline")
        )
        self.link.pack(pady=50)

        #Bind the left mouse button click to open the URL
        self.link.bind("<Button-1>", lambda event: self.open_url("https://aechneisdevelopment.us"))

    def start_pomodoro(self):
        # Prevent starting multiple overlapping timers
        if self.timer_id is not None:
            return

        self.current_cycle = 1
        self.is_work_phase = True
        self.remaining_seconds = self.work_duration * 60

        self.start_btn.config(state=tk.DISABLED)
        self.cancel_btn.config(state=tk.NORMAL)
        self.update_status()
        self.countdown()

    def countdown(self):
        # Format seconds into MM:SS
        mins, secs = divmod(self.remaining_seconds, 60)
        self.time_label.config(text=f"{mins:02d}:{secs:02d}")

        if self.remaining_seconds > 0:
            self.remaining_seconds -= 1
            # Schedule this exact method to run again in 1000ms (1 second)
            self.timer_id = self.root.after(1000, self.countdown)
        else:
            self.handle_phase_transition()

    def handle_phase_transition(self):
        self.root.bell()
        if self.is_work_phase:
            # Switch from Work to Break
            self.is_work_phase = False
            self.remaining_seconds = self.break_duration * 60
            self.update_status()
            self.countdown()
        else:
            # Break finished -> Notify phone in the background
            threading.Thread(target=self.send_phone_alert, daemon=True).start()
            
            # check if more cycles remain
            if self.current_cycle < self.total_cycles:
                self.current_cycle += 1
                self.is_work_phase = True
                self.remaining_seconds = self.work_duration * 60
                self.update_status()
                self.countdown()
            else:
                self.finish_pomodoro()

    def set_app_data(self):
        app_entry = tk.Toplevel(self.root)
        app_entry.title("Pomodoro Timer - Application Entry")
        app_entry.geometry("300x250")

        # Main content area (Simulating your app layout)
        main_frame = tk.LabelFrame(app_entry, text="Application Entry")
        main_frame.pack(fill="both", padx=10, pady=10)
        
        # main_frame labels and entry fields
        tk.Label(main_frame, text="Work Duration:").pack()
        self.entry_work_duration = tk.Entry(main_frame)
        self.entry_work_duration.pack()
        tk.Label(main_frame, text="Break Duration:").pack()
        self.entry_break_duration = tk.Entry(main_frame)
        self.entry_break_duration.pack()
        tk.Label(main_frame, text="Cycles:").pack()
        self.entry_cycles = tk.Entry(main_frame)
        self.entry_cycles.pack()  
        self.submit_button = tk.Button(main_frame, text="Submit", width=12, command=self.get_app_data)
        self.submit_button.pack(side="left", padx=75)  

    def get_app_data(self):
        # Read the entry values, using defaults for empty fields.
        self.work_duration = int(self.entry_work_duration.get() or 25)   # minutes
        self.break_duration = int(self.entry_break_duration.get() or 5)   # minutes
        self.total_cycles = int(self.entry_cycles.get() or 4)

        self.submit_button.winfo_toplevel().destroy()
 
    def send_phone_alert(self):
        status = email_to_text.send_break_over_sms()
       
        self.root.after(0, lambda: self.system_label.config(text=f"{status}"))

    def update_status(self):
        phase = "Work" if self.is_work_phase else "Break"
        self.status_label.config(text=f"Cycle {self.current_cycle}/{self.total_cycles} - {phase}")
        self.system_label.config(text="")

    def cancel_pomodoro(self):
        if self.timer_id is not None:
            # Immediately stop the scheduled .after() callback
            self.root.after_cancel(self.timer_id)
            self.timer_id = None

        self.status_label.config(text="Canceled")
        self.time_label.config(text="00:00")
        self.start_btn.config(state=tk.NORMAL)
        self.cancel_btn.config(state=tk.DISABLED)
        self.system_label.config(text="")

    def finish_pomodoro(self):
        self.timer_id = None
        self.status_label.config(text="All Cycles Complete!")
        self.time_label.config(text="00:00")
        self.start_btn.config(state=tk.NORMAL)
        self.cancel_btn.config(state=tk.DISABLED)
        self.work_duration = None
        self.break_duration = None
        self.total_cycles = None

if __name__ == "__main__":
    root = tk.Tk()
    app = PomodoroApp(root)
    root.mainloop()
