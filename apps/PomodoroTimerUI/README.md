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

## Version 3: pomodoro_timer_tkv2.py

Yeah...I'm re-writing the whole thing. Ran into an issue with version 2 when I started looking into adding a cancel button. The original script (pomodoro_timer.py) uses the time.sleep() method in a for loop. The program stops executing until the time.sleep() is complete. Which means there's no way to cancel it except pressing CTRL+C in the terminal. Which is not a good solution for a UI application.

✨ Features
In addition to the features in the pomodoro_timer_tk.py script:
- The main window is now a clean interface with a countdown timer
    - Label above the timer displays the timer's status (DONE)
    - Two buttons: Start and Cancel. Start is disabled once clicked (DONE)
    - Bottom Label displays system messages and errors (NOT STARTED)
- Replaced the loop and time.sleep() with Tkinter labels and timer functionality (DONE)
- Application Menu (SKELETON DONE) to display windows to:
    - Enter work and break duration, number of cycles (otherwise, default is 25, 5, 4) (NOT STARTED)
    - Create / update the .env file used for SMS message when break ends (NOT STARTED)
    - Display how-to and website URL (NOT STARTED)

This is the version I will be creating the application package out of.

<img width="301" height="270" alt="Screenshot From 2026-11-10 11-40-03" src="https://github.com/user-attachments/assets/5765a2ac-8325-4d99-9eb7-be2d34adeda9" />
