from pyperclip import copy
from tkinter import messagebox

from src.functions import *
from src.init import m, root
from src.homex import *


def NumberSystems():
    ns = NSGlobals()

    def tns_to_home():
        homes()
        tns_title.destroy()
        tns_label_1.destroy()
        tns_label_2.destroy()
        tns_label_3.destroy()
        ns_input.destroy()
        tns_output.destroy()
        tns_off.destroy()
        tns_re_button.destroy()
        tns_clean_button.destroy()
        tns_from_combobox.destroy()
        tns_to_combobox.destroy()
        m.window.configure(width=788, height=m.abs_height)
        center_window(root, 678, m.abs_height)

    def tns_copy():
        if tns_output.get(1.0, END):
            copy(tns_output.get(1.0, END))

    def change(old_osn, osn, n):
        nums = '0123456789'
        p = 0
        ns_l = 0
        if n[0] == '-':
            n = n[1:]
            p += 1
        for ns_m in range(len(n)):
            if n[ns_m] in nums and int(n[ns_m]) + 1 > old_osn:
                ns_l += 1
            elif ns_l == 0:
                if ord(n[ns_m]) - 54 > old_osn:
                    ns_l += 1
        if ns_l == 0:
            if old_osn != 10:
                ns.ch2 = 0
                if old_osn < 10:
                    for j in range(len(n)):
                        ns.ch2 += int(n[j]) * old_osn ** (len(n) - j - 1)
                if old_osn > 10:
                    for k in range(len(n)):
                        if ord(n[k]) > 57:
                            ns.ch2 += (ord(n[k]) - 55) * old_osn ** (len(n) - k - 1)
                        else:
                            ns.ch2 += int(n[k]) * old_osn ** (len(n) - k - 1)
            if osn == 10:
                if p == 0:
                    tns_output.insert(1.0, str(ns.ch2))
                else:
                    tns_output.insert(1.0, str((ns.ch2 * -1)))
            else:
                res = ' '
                while ns.ch2 > 0:
                    c = ns.ch2 % osn
                    ns.ch2 //= osn
                    if c < 10:
                        res += str(c)
                    else:
                        res += chr(55 + c)
                if p == 0:
                    tns_output.insert(1.0, str((res[::-1])))
                else:
                    tns_output.insert(1.0, str((int(res[::-1]) * -1)))

    def tns_Begin():
        if tns_to_combobox.get() != '1':
            try:
                tns_output.configure(state=NORMAL)
                tns_Clean()
                if tns_from_combobox.get() != '10':
                    change(int(tns_from_combobox.get()), int(tns_to_combobox.get()), ns_input.get())
                else:
                    change(2, int(tns_to_combobox.get()), str(bin(int(ns_input.get()))).replace('0b', ''))
                tns_output.configure(state=DISABLED)
            except ValueError:
                messagebox.showwarning('INFO', 'Введены некорректные значения!')

    def tns_Clean():
        tns_output.delete(1.0, END)

    center_window(root, 620, 430)
    m.window.configure(width=620, height=430)
    root.title('NumberSystems')
    root.minsize(620, 430)

    tns_title = Label(m.window, text='NumberSystems', font=('Arial Bold', 15), fg='red')
    tns_title.place(x=40, y=20)

    tns_label_1 = Label(m.window, text='Введите значение:')
    tns_label_1.place(x=20, y=300)

    tns_label_2 = Label(m.window, text='ИЗ')
    tns_label_2.place(x=20, y=80)

    tns_label_3 = Label(m.window, text='В')
    tns_label_3.place(x=20, y=190)

    ns_input = Entry(m.window, width=24, font=('Arial Bold', 15))
    ns_input.place(x=20, y=320)

    tns_re_button = Button(m.window, text='Перевести', bg='white', fg='black', width=15, command=tns_Begin)
    tns_re_button.place(x=340, y=100)

    tns_clean_button = Button(m.window, text='Копировать', bg='red', fg='white', width=15, command=tns_copy)
    tns_clean_button.place(x=470, y=100)

    tns_from_combobox = Entry(m.window, font=('Arial Bold', 16), width=21)
    tns_from_combobox.place(x=20, y=100)

    tns_to_combobox = Entry(m.window, font=('Arial Bold', 16), width=21)
    tns_to_combobox.place(x=20, y=210)

    tns_output = Text(m.window, width=30, height=13, state=DISABLED)
    tns_output.place(x=340, y=130)

    tns_off = Button(m.window, text='⌂', font=('Arial Bold', 15), width=2, height=1, bg='black', fg='white',
                     command=tns_to_home)
    tns_off.place(x=0, y=0)
    ToolTip(tns_off, 'На главную...')
