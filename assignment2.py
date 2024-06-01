import tkinter as tk
from tkinter import messagebox

def add():
    try:
        result = float(entry1.get()) + float(entry2.get())
        result_label.config(text="Result: " + str(result))
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numbers")

def subtract():
    try:
        result = float(entry1.get()) - float(entry2.get())
        result_label.config(text="Result: " + str(result))
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numbers")

def multiply():
    try:
        result = float(entry1.get()) * float(entry2.get())
        result_label.config(text="Result: " + str(result))
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numbers")

def divide():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        if num2 != 0:
            result = num1 / num2
            result_label.config(text="Result: " + str(result))
        else:
            messagebox.showerror("Math Error", "Cannot divide by zero")
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numbers")

# Create the main window
root = tk.Tk()
root.title("Simple Calculator")

# Create and place the widgets
entry1 = tk.Entry(root, width=10)
entry1.grid(row=0, column=1, padx=5, pady=5)

entry2 = tk.Entry(root, width=10)
entry2.grid(row=1, column=1, padx=5, pady=5)

label1 = tk.Label(root, text="First number:")
label1.grid(row=0, column=0, padx=5, pady=5)

label2 = tk.Label(root, text="Second number:")
label2.grid(row=1, column=0, padx=5, pady=5)

result_label = tk.Label(root, text="Result: ")
result_label.grid(row=2, column=0, columnspan=2, padx=5, pady=5)

add_button = tk.Button(root, text="Add", command=add)
add_button.grid(row=3, column=0, padx=5, pady=5)

subtract_button = tk.Button(root, text="Subtract", command=subtract)
subtract_button.grid(row=3, column=1, padx=5, pady=5)

multiply_button = tk.Button(root, text="Multiply", command=multiply)
multiply_button.grid(row=4, column=0, padx=5, pady=5)

divide_button = tk.Button(root, text="Divide", command=divide)
divide_button.grid(row=4, column=1, padx=5, pady=5)

# Run the application
root.mainloop()
