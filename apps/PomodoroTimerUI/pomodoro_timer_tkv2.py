import tkinter as tk
import threading

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

    def create_menu(self):
        menubar = tk.Menu(self.root)
        self.root.config(menu=menubar)

        app_menu = tk.Menu(menubar)
        menubar.add_cascade(label="Application Menu", menu=app_menu)
        app_menu.add_command(label="Enter App Data", command=self.set_app_data)
        app_menu.add_command(label="SMS Setup", command=self.update_SMS_file)
        app_menu.add_command(label="About", command=self.create_about_page)

    def set_app_data(self):
        print("Window to set work and break duration, and number of cycles")

    def update_SMS_file(self):
        print("Window to create or update env file for SMS vars")

    def create_about_page(self):
        print("Static resource to provide help and link to web site")

    def start_pomodoro(self):
        # Prevent starting multiple overlapping timers
        if self.timer_id is not None:
            return

        # Replace these hardcoded values with .get() from your Entry widgets
        self.work_duration = 1   # minutes
        self.break_duration = 1   # minutes
        self.total_cycles = 1

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

    def send_phone_alert(self):
        email_to_text.send_break_over_sms()

    def update_status(self):
        phase = "Work" if self.is_work_phase else "Break"
        self.status_label.config(text=f"Cycle {self.current_cycle}/{self.total_cycles} - {phase}")

    def cancel_pomodoro(self):
        if self.timer_id is not None:
            # Immediately stop the scheduled .after() callback
            self.root.after_cancel(self.timer_id)
            self.timer_id = None

        self.status_label.config(text="Canceled")
        self.time_label.config(text="00:00")
        self.start_btn.config(state=tk.NORMAL)
        self.cancel_btn.config(state=tk.DISABLED)

    def finish_pomodoro(self):
        self.timer_id = None
        self.status_label.config(text="All Cycles Complete!")
        self.time_label.config(text="00:00")
        self.start_btn.config(state=tk.NORMAL)
        self.cancel_btn.config(state=tk.DISABLED)

if __name__ == "__main__":
    root = tk.Tk()
    app = PomodoroApp(root)
    root.mainloop()
