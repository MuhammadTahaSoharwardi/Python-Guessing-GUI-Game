from tkinter import *
from tkinter import messagebox
import random


def submit():
    text = int(entry.get())
    if text == comp:
        messagebox.showinfo(title="Win", message="You Win!")
        choice = messagebox.askyesno(title="Play again?", message="Play Again?")
        if choice:
            restart()
        else:
            window.destroy()
    elif text > comp:
        messagebox.showinfo(title="Guess Lesser", message="Guess Lesser")
    else:
        messagebox.showinfo(title="Guess Greater", message="Guess Greater")


def restart():
    window.destroy()
    create_window()


def create_window():
    global window, entry, comp, start, end
    window = Tk()
    window.geometry("400x500")
    window.config(bg="#6cc5d5")

    comp = random.randint(start, end)

    Label(
        window, text=f"Guess any number between {start} and {end}", width=50, height=2
    ).pack(pady=10)

    entry = Entry(window, width=40)
    entry.pack(padx=3, pady=10)

    Button(window, text="Submit", command=submit).pack()

    window.mainloop()


window = Tk()

window.geometry("400x500")
window.config(bg="#6cc5d5")

start = 5
end = 10

comp = random.randint(start, end)
# print (comp)

Label(
    window, text=f"Guess any number between {start} and {end}", width=50, height=2
).pack(pady=10)

entry = Entry(window, width=40)
entry.pack(padx=3, pady=10)

Button(window, text="Submit", command=submit).pack()


window.mainloop()
