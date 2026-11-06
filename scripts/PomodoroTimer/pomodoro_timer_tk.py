import tkinter as tk
import time
import sys

def submit_duration():
    work_duration = int(entry_work_duration.get() or 25)
    print(f"work_duration: {work_duration}")
    break_duration = int(entry_break_duration.get() or 5)
    print(f"break_duration: {break_duration}")   
    cycles = int(entry_cycles.get() or 4)
    print(f"cycles: {cycles}")       

    for cycle in range(cycles):
         print(f"Cycle {cycle + 1}/{cycles}: Start working for {work_duration} minutes.")
         time.sleep(work_duration * 60)
         # Comment below for Windows
         sys.stdout.write('\a') # Make a beep sound on macOS/Linux
         sys.stdout.flush()
         # Uncomment below for Windows
         # winsound.Beep(1000, 1000)  # Sound an alert to indicate work period end
         print("Time's up! Take a break.")

         print(f"Break time! Relax for {break_duration} minutes.")
         time.sleep(break_duration * 60)
         # Comment below for Windows
         sys.stdout.write('\a') # Make a beep sound on macOS/Linux
         sys.stdout.flush()
         # Uncomment below for Windows 
         # winsound.Beep(1000, 1000)  # Sound an alert to indicate break period end      
         print("Break is over! Back to work.")

    print("All cycles completed! Great job!")

window = tk.Tk()
window.title("Pomodoro Timer")
label_work_duration = tk.Label(master=window, text="Enter work duration in minutes (default is 25):")
entry_work_duration = tk.Entry(window)
label_work_duration.pack()
entry_work_duration.pack()
label_break_duration = tk.Label(master=window, text="Enter break duration in minutes (default is 5):")
entry_break_duration = tk.Entry(window)
label_break_duration.pack()
entry_break_duration.pack()
label_cycles = tk.Label(master=window, text="Enter number of cycles (default is 4):")
entry_cycles = tk.Entry(window)
label_cycles.pack()
entry_cycles.pack()
frame = tk.Frame(master=window, relief='raised', borderwidth=5)
frame.pack()
btn_submit = tk.Button(master=frame, text="Submit", command=submit_duration)
btn_submit.pack()
window.mainloop()