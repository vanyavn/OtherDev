import random
from tkinter import *
from tkinter import ttk
import tkinter.messagebox as messagebox
root = Tk()
random_text = StringVar()
def letov(): random_text.set(rndmzr())
def copystih():
    message = random_text.get()
    if message:
        root.clipboard_clear()
        root.clipboard_append(message)
        messagebox.showinfo("Здорово и вечно!", "Сообщение успешно скопировано в буфер обмена!")
    else: messagebox.showwarning("Увы!", "Сообщение не удалось скопировать в буфер обмена!")
root.title("ГрОбомайзер-Летовайзер v. 1.0")
root.geometry("430x190")
root.configure(bg="#AF9FC9")
btn = ttk.Button(text="Случайная строчка!", command=letov)
btn.configure()
btn.pack(anchor=CENTER, padx=9, pady=9)
btn2 = ttk.Button(text="Скопировать!", command=copystih)
btn2.configure()
btn2.pack(anchor=CENTER, padx=9, pady=9)
entry = ttk.Entry(root, textvariable=random_text, width=100)
entry.pack(anchor=CENTER, padx=9, pady=9)
def rndmzr():
    with open("letov_stihi.txt", "r") as file:
        non_empty_lines = [line.strip() for line in file if line.strip() and not any(char.isdigit() or char == "*" for char in line)]
        if non_empty_lines:random_line = random.choice(non_empty_lines)
        else: random_line = None
    return random_line
root.mainloop()