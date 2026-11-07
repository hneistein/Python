# Pomodoro Timer UI (Using Tkinter)

## Version 2: pomodoro_timer_tk.py

I modified the pomodoro_timer.py script (/scripts/PomodoroTimer/pomodoro_timer.py) and created a UI for it using Tkinter.  

✨ Features
In addition to the features in the pomodoro_timer.py script:
- The script is now wrapped in a UI, so no need to use command line, other than to launch it
- Error messages are denoted in red text in the console
- The submit button is disabled when the program starts to prevent accidental clicks while the program runs, which could cause your system to freeze
- The submit button is automatically enabled once processing completes, so you can start another round of cycles

## Tkinter module
The tkinter module is a part of Python, but may or may not be available in the Python packaged with your Linux distribution. Please follow the installation procedures for your distro if needed.

<img width="500" height="439" alt="Pomodoro_Timer_tk" src="https://github.com/user-attachments/assets/bf380ac6-5d94-4ac1-8d37-b28785202009" />

#### To run, navigate to the folder where you saved the script and type: python pomodoro_timer_tk.py

I plan to make these updates to version 2 in the near future:
 - Add validations to prevent entry of numeric values less than 1 and text that can't be converted to a number
 - Use a sound file instead of terminal beeps when a phase ends
 - Add a SMS feature to receive a text msg when break time ends
 - Package into an executable (and add instructions to the README.md on how to do it)
