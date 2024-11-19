import tkinter as tk

root = tk.Tk()
root.geometry("400x300")

label = tk.Label(root, text="Testing GUI")
label.grid(row=0, column=0, sticky="nsew")

root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)

root.mainloop()
