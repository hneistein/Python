# Pomodoro Timer
https://github.com/wasmerio/Python-Scripts/blob/main/Pomodoro%20Timer/Pomodoro%20Timer%20MacOS%20Linux.py

I copied this script because I find the Pomodoro method (generally, 25 minutes focused, 5 minutes break, 4 cycles) very helpful. It keeps me from over-extending myself.

I may build a front-end for this...on my web site, or as a computer app. I also had the thought I could get a battery, case, and speaker for my second Raspberry Pi Zero 2w so I could make it portable. Because one flaw in having it as a computer app is: if I get up and walk away from my laptop during a 5-minute break, I'm probably not coming back. At least, not for several hours. Because AuDHD.

✨ Features
- Customizable Work and Break Durations: Set your preferred time for work and break sessions.
- Support for Multiple Cycles: Run multiple Pomodoro sessions in a row.
- Platform-Specific Alerts:
    - Windows: Uses sound alerts (winsound) to notify users when a session is complete.
        - currently commented, uncomment to use on Windows.
    - macOS/Linux: Uses terminal beep commands for notifications.
        - currently active, comment to use on Windows.

To run, navigate to the folder where you saved the script and type: python pomodoro_timer.py

Run pomodoro_timer_tk.py for a UI built in Tkinter. Build still in progress as of 11/5/26, output displays in terminal while input is entered in the UI.
