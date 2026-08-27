# version 0.0.1

import secrets
from tkinter import ttk
from ttkthemes import ThemedTk

ALPHABET = 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz0123456789`~!@#$%^&*()-_=+[]{}\\|;:\'",.<>/?'
DEFAULT_SIZE = "400x200"

def create_password():
    """This function creates a random password.

    Returns:
        str: a random password.

    """
    password = ''

    for _ in range(12):
        password += secrets.choice(ALPHABET)

    return password

def copy_password(root, label):
    """This function copies a password.
    """
    root.clipboard_clear()
    root.clipboard_append(label['text'])

def show_password(label):
    """This function changes text to password.
    """
    password = create_password()
    label.config(text=password)

def create_ui(root):
    """This function creates a frame with buttons and a text label. 
    """

    frame = ttk.Frame(root)
    frame.pack(expand=True)

    password_label = ttk.Label(frame, text='')
    password_label.pack(pady=20)
    
    create_button = ttk.Button(frame, width=50, text="Create password", command=lambda: show_password(password_label))
    create_button.pack(pady=0)

    copy_button = ttk.Button(frame, width=50, text="Copy password", command=lambda: copy_password(root, password_label))
    copy_button.pack(pady=0)

def main():
    """This function creates a program window."""
    window = ThemedTk(theme="breeze")
    window.title("Password")
    window.geometry(DEFAULT_SIZE)

    create_ui(window)

    window.mainloop()

main()
