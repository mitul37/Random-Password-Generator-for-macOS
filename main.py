import tkinter as tk
from tkinter import messagebox
import random
import string

def generate_password():
    length = length_var.get()
    use_upper = upper_var.get()
    use_lower = lower_var.get()
    use_digits = digits_var.get()
    use_symbols = symbols_var.get()

    if not any([use_upper, use_lower, use_digits, use_symbols]):
        messagebox.showwarning("Warning", "Select at least one character type!")
        return

    chars = ""
    if use_upper:
        chars += string.ascii_uppercase
    if use_lower:
        chars += string.ascii_lowercase
    if use_digits:
        chars += string.digits
    if use_symbols:
        chars += string.punctuation

    password = ''.join(random.choice(chars) for _ in range(length))
    result_var.set(password)

# GUI Setup
root = tk.Tk()
root.title("Password Generator")
root.geometry("400x300")
root.resizable(False, False)

length_var = tk.IntVar(value=12)
upper_var = tk.BooleanVar(value=True)
lower_var = tk.BooleanVar(value=True)
digits_var = tk.BooleanVar(value=True)
symbols_var = tk.BooleanVar(value=False)
result_var = tk.StringVar()

tk.Label(root, text="Password Length:").pack()
tk.Entry(root, textvariable=length_var, width=5).pack()

tk.Checkbutton(root, text="Include Uppercase (A-Z)", variable=upper_var).pack()
tk.Checkbutton(root, text="Include Lowercase (a-z)", variable=lower_var).pack()
tk.Checkbutton(root, text="Include Digits (0-9)", variable=digits_var).pack()
tk.Checkbutton(root, text="Include Symbols (!@#$)", variable=symbols_var).pack()

tk.Button(root, text="Generate Password", command=generate_password).pack(pady=10)
tk.Entry(root, textvariable=result_var, width=40).pack()

root.mainloop()
