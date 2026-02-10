import tkinter as tk
from tkinter import messagebox

def on_button_click():
    label.config(text="Button Clicked!")
    messagebox.showinfo("Information", "You clicked the button!")

# Create the main window
root = tk.Tk()
root.title("Simple Tkinter GUI")
root.geometry("300x200")

# Create a text label
label = tk.Label(root, text="Hello, Tkinter!", font=("Arial", 14))
label.pack(pady=20)

# Create a button
button = tk.Button(root, text="Click Me", command=on_button_click)
button.pack(pady=10)

# Start the GUI event loop
root.mainloop()
