import tkinter as tk
from get_data import get_data_from


def grab_url():
    return site.get()


def count():
    results.delete('1.0', tk.END)
    results.insert('1.0', get_data_from(grab_url()))


master = tk.Tk()  # initiating tkinter

title = tk.Label(master, text="GUI to Count words in websites")  # title label
title.pack()

site = tk.Entry(master)
site.pack()

submit = tk.Button(master, text="submit", command=count)
submit.pack()

results = tk.Text(master)
results.pack()
tk.mainloop()




# print(get_data_from("www.google.com"))
