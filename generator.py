import tkinter as tk
from tkinter import messagebox
import random
import string

def generate_password():
    length = int(length_entry.get())

    chars = ""
    password = []

    if var_upper.get():
        chars += string.ascii_uppercase
        password.append(random.choice(string.ascii_uppercase))

    if var_lower.get():
        chars += string.ascii_lowercase
        password.append(random.choice(string.ascii_lowercase))

    if var_digit.get():
        chars += string.digits
        password.append(random.choice(string.digits))

    if var_symbol.get():
        chars += string.punctuation
        password.append(random.choice(string.punctuation))

    if chars == "":
        messagebox.showerror("Error", "Select at least one option")
        return

    if length < len(password):
        messagebox.showerror("Error", "Length too short for selected options")
        return

    for _ in range(length - len(password)):
        password.append(random.choice(chars))

    random.shuffle(password)
    final_password = "".join(password)

    result_var.set(final_password)


def copy_to_clipboard():
    root.clipboard_clear()
    root.clipboard_append(result_var.get())
    root.update()
    messagebox.showinfo("Copied", "Password copied to clipboard")


# GUI
root = tk.Tk()
root.title("Password Generator")
root.geometry("350x350")

tk.Label(root, text="Password Generator", font=("Arial", 14)).pack(pady=10)

# Length
tk.Label(root, text="Length:").pack()
length_entry = tk.Entry(root)
length_entry.insert(0, "8")
length_entry.pack()

# Options
var_upper = tk.BooleanVar()
var_lower = tk.BooleanVar()
var_digit = tk.BooleanVar()
var_symbol = tk.BooleanVar()

tk.Checkbutton(root, text="Uppercase", variable=var_upper).pack()
tk.Checkbutton(root, text="Lowercase", variable=var_lower).pack()
tk.Checkbutton(root, text="Numbers", variable=var_digit).pack()
tk.Checkbutton(root, text="Symbols", variable=var_symbol).pack()

# Result
result_var = tk.StringVar()
tk.Entry(root, textvariable=result_var, width=30).pack(pady=10)

# Buttons
tk.Button(root, text="Generate", command=generate_password).pack(pady=5)
tk.Button(root, text="Copy", command=copy_to_clipboard).pack(pady=5)

root.mainloop()