import tkinter as tk
import os

watchWindow = tk.Tk()
watchWindow.geometry("300x400")


p1scorevar = tk.IntVar(value=501)
p2scorevar = tk.IntVar(value=501)
logvar = tk.StringVar(value="Michael van Gerwen throws for 180, 321 remains.")
p1namevar = tk.StringVar(value="Micheal van Gerwen")
p2namevar = tk.StringVar(value="Dave Chisnall")
p1legsvar = tk.IntVar(value=0)
p2legsvar = tk.IntVar(value=0)
p1setsvar = tk.IntVar(value=0)
p2setsvar = tk.IntVar(value=0)

p1scoreWatch = tk.Label(textvariable=p1scorevar, background="black", foreground="white", borderwidth=2, relief="raised", font=("Arial", 50))
p2scoreWatch = tk.Label(textvariable=p2scorevar, background="black", foreground="white", borderwidth=2, relief="raised", font=("Arial", 50))
logfileWatch = tk.Label(textvariable=logvar, borderwidth=2, relief="ridge", width=50)
p1nameWatch = tk.Label(textvariable=p1namevar, borderwidth=2, relief="ridge", font=("Arial", 20), width=30)
p2nameWatch = tk.Label(textvariable=p2namevar, borderwidth=2, relief="ridge", font=("Arial", 20), width=30)
p1legWatch = tk.Label(text="Legs", borderwidth=2, relief="ridge", font=("Arial", 20))
p2legWatch = tk.Label(text="Legs", borderwidth=2, relief="ridge", font=("Arial", 20))
p1setWatch = tk.Label(text="Sets", borderwidth=2, relief="ridge", font=("Arial", 20))
p2setWatch = tk.Label(text="Sets", borderwidth=2, relief="ridge", font=("Arial", 20))
p1legsScoreWatch = tk.Label(textvariable=p1legsvar, background="black", foreground="white", borderwidth=2, relief="raised", font=("Arial", 20), width=2)
p2legsScoreWatch = tk.Label(textvariable=p2legsvar, background="black", foreground="white", borderwidth=2, relief="raised", font=("Arial", 20), width=2)
p1setsScoreWatch = tk.Label(textvariable=p1setsvar, background="black", foreground="white", borderwidth=2, relief="raised", font=("Arial", 20), width=2)
p2setsScoreWatch = tk.Label(textvariable=p2setsvar, background="black", foreground="white", borderwidth=2, relief="raised", font=("Arial", 20), width=2)

watchWindow.columnconfigure(0, weight=1)
watchWindow.columnconfigure(5, weight=1)
watchWindow.rowconfigure(0, weight=1)

p1scoreWatch.grid(row=1, column=0, columnspan=2, rowspan=2, sticky="news")
p2scoreWatch.grid(row=1, column=4, columnspan=2, rowspan=2, sticky="news")
logfileWatch.grid(row=1, column=2, columnspan=2, sticky="news")
p1nameWatch.grid(row=3, column=0, columnspan=2, sticky="news")
p2nameWatch.grid(row=3, column=4, columnspan=2, sticky="news")
p1legWatch.grid(row=4, column=0, sticky="news")
p1setWatch.grid(row=5, column=0, sticky="news")
p2legWatch.grid(row=4, column=5, sticky="news")
p2setWatch.grid(row=5, column=5, sticky="news")
p1legsScoreWatch.grid(row=4, column=1, sticky="news")
p1setsScoreWatch.grid(row=5, column=1, sticky="news")
p2legsScoreWatch.grid(row=4, column=4, sticky="news")
p2setsScoreWatch.grid(row=5, column=4, sticky="news")


watchWindow.mainloop()
