import tkinter as tk

main_window = tk.Tk()
main_window.geometry("300x400")

label = tk.Label(main_window, text="Python", bg="grey")
label.place(x=200, y=30)
label.mainloop()
