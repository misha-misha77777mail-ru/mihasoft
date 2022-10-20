import tkinter as tk
import winsound as w
import os
def f():
    os.startfile('qrread.exe')
    with open('fuck', 'w'):
        pass
    while True:
        w.Beep(300, 300)
        if not os.path.exists('fuck'):
            break
wi = tk.Tk()
b = tk.Button(wi, text='f', command=f)
b.pack()
wi.mainloop()