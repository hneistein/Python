# Pomodoro Timer
https://github.com/wasmerio/Python-Scripts/blob/main/Pomodoro%20Timer/Pomodoro%20Timer%20MacOS%20Linux.py

## Version 1: pomodoro_timer.py

I copied this script because I find the Pomodoro method (generally, 25 minutes focused, 5 minutes break, 4 cycles) very helpful. It keeps me from over-extending myself.

✨ Features
- Customizable Work and Break Durations: Set your preferred time for work and break sessions.
- Support for Multiple Cycles: Run multiple Pomodoro sessions in a row.
- Platform-Specific Alerts:
    - Windows: Uses sound alerts (winsound) to notify users when a session is complete.
        - currently commented, uncomment to use on Windows.
    - macOS/Linux: Uses terminal beep commands for notifications.
        - currently active, comment to use on Windows.
- Runs in the terminal

#### To run, navigate to the folder where you saved the script and type: python pomodoro_timer.py

## Version 2: pomodoro_timer_tk.py

I modified pomodoro_timer.py and created a UI for it using Tkinter.  Same features as above, it just runs in an app window instead of the terminal.

![Screenshot of Pomodoro Timer UI][def]

#### To run, navigate to the folder where you saved the script and type: python pomodoro_timer_tk.py

I plan to make these updates to version 2 in the near future:
 - Add validations to prevent entry of numeric values less than 1 and text that can't be converted to a number
 - Use a sound file instead of terminal beeps when a phase ends
 - Add a SMS feature to receive a text msg when break time ends
 - Package into an executable (and add instructions to the README.md on how to do it)


[def]: images/Pomodoro_Timer_tk.png