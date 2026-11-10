import tkinter as tk
from tkinter import messagebox

def do_nothing():
    messagebox.showinfo("Action", "Menu item clicked!")

def show_context_menu(event):
    # Displays the popup menu at the mouse cursor's screen coordinates
    context_menu.tk_popup(event.x_root, event.y_root)

root = tk.Tk()
root.title("Tkinter Menu Example")
root.geometry("400x300")

# Prevent dashed "tear-off" lines at the top of menus across the entire app
root.option_add('*tearOff', tk.FALSE)

# 1. Create the main top-level menu bar
menubar = tk.Menu(root)
root.config(menu=menubar)

# 2. Create the "File" submenu
file_menu = tk.Menu(menubar)
menubar.add_cascade(label="File", menu=file_menu)

file_menu.add_command(label="New", accelerator="Ctrl+N", command=do_nothing)
file_menu.add_command(label="Open...", accelerator="Ctrl+O", command=do_nothing)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)

# 3. Create the "Edit" submenu with a toggleable checkbutton
edit_menu = tk.Menu(menubar)
menubar.add_cascade(label="Edit", menu=edit_menu)

word_wrap = tk.BooleanVar(value=True)
edit_menu.add_checkbutton(label="Word Wrap", variable=word_wrap, command=do_nothing)

# 4. Create a nested submenu inside "Edit"
theme_submenu = tk.Menu(edit_menu)
edit_menu.add_cascade(label="Theme", menu=theme_submenu)

selected_theme = tk.StringVar(value="Light")
theme_submenu.add_radiobutton(label="Light", variable=selected_theme, value="Light")
theme_submenu.add_radiobutton(label="Dark", variable=selected_theme, value="Dark")

# 5. Create a right-click Context Menu
context_menu = tk.Menu(root)
context_menu.add_command(label="Cut", command=do_nothing)
context_menu.add_command(label="Copy", command=do_nothing)
context_menu.add_command(label="Paste", command=do_nothing)

# Bind right-click (<Button-3> on Windows/Linux, <Button-2> on macOS)
root.bind("<Button-3>", show_context_menu)
root.bind("<Button-2>", show_context_menu)

root.mainloop()
