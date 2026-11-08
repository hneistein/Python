# Pomodoro Timer UI (Using Tkinter)

## Version 2: pomodoro_timer_tk.py

I modified the pomodoro_timer.py script (/scripts/PomodoroTimer/pomodoro_timer.py) and created a UI for it using Tkinter.  

✨ Features
In addition to the features in the pomodoro_timer.py script:
- The script is now wrapped in a UI, so no need to use command line, other than to launch it
- Error messages are denoted in red text in the console
- The submit button is disabled when the program starts to prevent accidental clicks while the program runs, which could cause your system to freeze
- The submit button is automatically enabled once processing completes, so you can start another round of cycles
- An SMS message is sent at the end of a break period, in case you're away from your desk
- A bell chimes at the end of each work and break period

## Tkinter module
The tkinter module is a part of Python, but may or may not be available in the Python packaged with your Linux distribution. Please follow the installation procedures for your distro if needed.

## EMAIL TO TEXT FUNCTIONALITY
The email to text functionality is a separate script (email-to-text.py) and requires the creation of an .env file in the same location of both the email-to-text script and the pomodoro timer app. 

The .env file contains the following environment variables:
- SMTP_SERVER
- SMTP_PORT
- SENDER_EMAIL
- SENDER_PASSWORD
- RECIPIENT_SMS_GATEWAY

Check the comments in the email-to-text.py for more details on these variables.

<img width="500" height="439" alt="Pomodoro_Timer_tk" src="https://github.com/user-attachments/assets/bf380ac6-5d94-4ac1-8d37-b28785202009" />

#### To run, navigate to the folder where you saved the script and type: python pomodoro_timer_tk.py

I plan to make these updates to version 2 in the near future:

 - Package into an executable (and add instructions to the README.md on how to do it)
