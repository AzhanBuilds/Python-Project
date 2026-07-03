# Simple GUI App

import tkinter as tk

# Main Window
root = tk.Tk()
root.title("Simple GUI App")
root.geometry("400x400")
root.configure(bg = "aqua")

# Title label
title_label = tk.Label(root, text = "Welcome to My GUI App", font = ("Arial", 18), bg = "#FF79C6")
title_label.pack(pady = 20)

# Name label
name_label = tk.Label(root, text = "Enter your name:", font = ("Arial", 12), bg = "#FF79C6")
name_label.pack(pady = 20)

# Name Entry
name_entry = tk.Entry(root, font = ("Arial", 12), width = 30)
name_entry.pack(pady = 10)

# Greeting function
def greet_user():
    name = name_entry.get()
    if name:
        greeting_label.config(text = f"Hello, {name}!", fg = "#FF79C6")
    else:
        greeting_label.config(text = "Please enter your name!", fg = "#FF79C6")

# Reset function
def reset():
    name_entry.delete(0, tk.END)
    greeting_label.config(text = "")

# Greet Button
greet_button = tk.Button(root, text = "Greet Me", command = greet_user, font = ("Arial", 12), bg = "red", fg = "#50FA7B")
greet_button.pack(pady = 10)

# Reset Button
reset_button = tk.Button(root, text = "Reset", command = reset, font = ("Arial", 12), bg = "red", fg = "#BD93F9")
reset_button.pack(pady = 5)

# Greeting label
greeting_label = tk.Label(root, text = "", font = ("Arial", 12), bg = "#606C38")
greeting_label.pack(pady = 20)

# Run the Application
root.mainloop()