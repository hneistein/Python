# Pomodoro Timer for macOS/Linux
# Default work duration is 25 minutes
# Default break duration is 5 minutes
# Default cycles is 4
import time
# Uncomment below for Windows
# import winsound
# Comment below for Windows
import sys

def pomodoro_timer_unix(work_duration=25, break_duration=5, cycles=4):
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

if __name__ == "__main__":
    work_duration = int(input("Enter work duration in minutes (default is 25): ") or 25)
    break_duration = int(input("Enter break duration in minutes (default is 5): ") or 5)
    cycles = int(input("Enter number of cycles (default is 4): ") or 4)

    pomodoro_timer_unix(work_duration, break_duration, cycles)