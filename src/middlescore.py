from src.functions import *
from src.init import m, root

from tkinter import messagebox
from homex import *


def MiddleScore():
    """
    Приложение для подсчёта среднего балла набора оценок.
    Подробнее - https://mihasoft.glitch.me/mso.html
    """

    def mso_to_home():
        """
        Возвращение на главную страницу MihaSoft
        """
        mso_title.destroy()
        mso_label_1.destroy()
        mso_label_2.destroy()
        mso_label_3.destroy()
        mso_label_4.destroy()
        mso_label_5.destroy()
        mso_label_6.destroy()
        mso_label_7.destroy()
        mso_label_8.destroy()
        mso_off.destroy()
        mso_input_1.destroy()
        mso_input_2.destroy()
        mso_result_button.destroy()
        homes()
        m.window.configure(width=788, height=720)
        center_window(root, 678, 730)

    def mso_Done():
        """
        Функция расчёта среднего балла
        """

        # Проверка корректности введённых оценок
        if not mso_input_1.get().isdigit() or (not mso_input_2.get().isdigit() and mso_input_2.get() != ''):
            messagebox.showwarning('INFO', 'Введены некорректные значения!')
        else:
            mso_flag = 1
            mso_j = 0
            mso_score_list_1 = list(map(int, str(mso_input_1.get())))
            # Удаление чисел, не являющихся оценками
            for i in range(len(mso_score_list_1)):
                if (mso_score_list_1[i] != 2) and (mso_score_list_1[i] != 3) and (mso_score_list_1[i] != 4) and (
                        mso_score_list_1[i] != 5):
                    mso_score_list_1[i] = 0
            while 0 in mso_score_list_1:
                mso_score_list_1.remove(0)
            mso_score_list_2 = list(map(int, str(mso_input_2.get())))
            if mso_score_list_2 == [0]:
                mso_flag = 0
            for i in range(len(mso_score_list_2)):
                if (mso_score_list_2[i] != 2) and (mso_score_list_2[i] != 3) and (mso_score_list_2[i] != 4) and (
                        mso_score_list_2[i] != 5) and (mso_score_list_2[i] != 0):
                    mso_score_list_2[i] = 0
            while 0 in mso_score_list_2:
                mso_score_list_2.remove(0)
            if mso_flag == 0:
                mso_q = sum(mso_score_list_1) / len(mso_score_list_1)
                mso_label_4.configure(text=mso_q)
                if (mso_q >= 3.6) and (mso_q <= 4.6):
                    mso_label_5.configure(text='Можете расслабиться!!!')
                    # Расчёт необходимого числа дополнительных пятёрок
                    while sum(mso_score_list_1) / len(mso_score_list_1) < 4.6:
                        mso_score_list_1.append(5)
                        mso_j += 1
                    if mso_j == 1:
                        mso_label_6.configure(text='У вас выходит четвёрка. Вам нужно получить ещё')
                        mso_label_7.configure(text=mso_j)
                        mso_label_8.configure(text='отличную оценку до пятёрки в триместре.')
                    if (mso_j == 2) or (mso_j == 3) or (mso_j == 4):
                        mso_label_6.configure(text='У вас выходит четвёрка. Вам нужно получить ещё')
                        mso_label_7.configure(text=mso_j)
                        mso_label_8.configure(text='отличные оценки до пятёрки в триместре.')
                    if mso_j >= 5:
                        mso_label_6.configure(text='У вас выходит четвёрка. Вам нужно получить ещё')
                        mso_label_7.configure(text=mso_j)
                        mso_label_8.configure(text='отличных оценок до пятёрки в триместре.')
                if (mso_q >= 2.6) and (mso_q < 3.6):
                    mso_label_5.configure(text='Внимание!!!')
                    while sum(mso_score_list_1) / len(mso_score_list_1) < 3.6:
                        mso_score_list_1.append(5)
                        mso_j += 1
                    if mso_j == 1:
                        mso_label_6.configure(text='У вас выходит тройка. Вам нужно получить ещё')
                        mso_label_7.configure(text=mso_j)
                        mso_label_8.configure(text='отличную оценку до четвёрки в триместре.')
                    if (mso_j == 2) or (mso_j == 3) or (mso_j == 4):
                        mso_label_6.configure(text='У вас выходит тройка. Вам нужно получить ещё')
                        mso_label_7.configure(text=mso_j)
                        mso_label_8.configure(text='отличные оценки до четвёрки в триместре.')
                    if mso_j >= 5:
                        mso_label_6.configure(text='У вас выходит тройка. Вам нужно получить ещё')
                        mso_label_7.configure(text=mso_j)
                        mso_label_8.configure(text='отличных оценок до четвёрки в триместре.')
                if (mso_q >= 2) and (mso_q < 2.6):
                    mso_label_5.configure(text='Вам трындец!!!!')
                    while sum(mso_score_list_1) / len(mso_score_list_1) < 2.6:
                        mso_score_list_1.append(5)
                        mso_j += 1
                    if mso_j == 1:
                        mso_label_6.configure(text='У вас выходит ДВОЙКА. Вам нужно получить ещё')
                        mso_label_7.configure(text=mso_j)
                        mso_label_8.configure(text='отличную оценку до тройки в триместре.')
                    if (mso_j == 2) or (mso_j == 3) or (mso_j == 4):
                        mso_label_6.configure(text='У вас выходит ДВОЙКА. Вам нужно получить ещё')
                        mso_label_7.configure(text=mso_j)
                        mso_label_8.configure(text='отличные оценки до тройки в триместре.')
                    if mso_j >= 5:
                        mso_label_6.configure(text='У вас выходит ДВОЙКА. Вам нужно получить ещё')
                        mso_label_7.configure(text=mso_j)
                        mso_label_8.configure(text='отличных оценок до тройки в триместре.')
                if (mso_q >= 4.6) and (mso_q <= 5):
                    mso_label_6.configure(text='')
                    mso_label_7.configure(text='')
                    mso_label_8.configure(text='')
                    mso_label_5.configure(text='У вас выходит пятёрка! Не получайте плохих оценок.')
            if mso_flag != 0:
                mso_z = (sum(mso_score_list_2) * 2 + sum(mso_score_list_1)) / (
                        len(mso_score_list_1) + len(mso_score_list_2) * 2)
                mso_label_4.configure(text=mso_z)
                if (mso_z >= 3.6) and (mso_z <= 4.6):
                    mso_label_5.configure(text='Можете расслабиться!!!')
                    while (sum(mso_score_list_2) * 2 + sum(mso_score_list_1)) / (
                            len(mso_score_list_1) + len(mso_score_list_2) * 2) < 4.6:
                        mso_score_list_1.append(5)
                        mso_j += 1
                    if mso_j == 1:
                        mso_label_6.configure(text='У вас выходит четвёрка. Вам нужно получить ещё')
                        mso_label_7.configure(text=mso_j)
                        mso_label_8.configure(text='отличную оценку до пятёрки в триместре.')
                    if (mso_j == 2) or (mso_j == 3) or (mso_j == 4):
                        mso_label_6.configure(text='У вас выходит четвёрка. Вам нужно получить ещё')
                        mso_label_7.configure(text=mso_j)
                        mso_label_8.configure(text='отличные оценки до пятёрки в триместре.')
                    if mso_j >= 5:
                        mso_label_6.configure(text='У вас выходит четвёрка. Вам нужно получить ещё')
                        mso_label_7.configure(text=mso_j)
                        mso_label_8.configure(text='отличных оценок до пятёрки в триместре.')
                if (mso_z >= 2.6) and (mso_z < 3.6):
                    mso_label_5.configure(text='Внимание!!!')
                    while (sum(mso_score_list_2) * 2 + sum(mso_score_list_1)) / (
                            len(mso_score_list_1) + len(mso_score_list_2) * 2) < 3.6:
                        mso_score_list_1.append(5)
                        mso_j += 1
                    if mso_j == 1:
                        mso_label_6.configure(text='У вас выходит тройка. Вам нужно получить ещё')
                        mso_label_7.configure(text=mso_j)
                        mso_label_8.configure(text='отличную оценку до четвёрки в триместре.')
                    if (mso_j == 2) or (mso_j == 3) or (mso_j == 4):
                        mso_label_6.configure(text='У вас выходит тройка. Вам нужно получить ещё')
                        mso_label_7.configure(text=mso_j)
                        mso_label_8.configure(text='отличные оценки до четвёрки в триместре.')
                    if mso_j >= 5:
                        mso_label_6.configure(text='У вас выходит тройка. Вам нужно получить ещё')
                        mso_label_7.configure(text=mso_j)
                        mso_label_8.configure(text='отличных оценок до четвёрки в триместре.')
                if (mso_z >= 2) and (mso_z < 2.6):
                    mso_label_5.configure(text='Вам трындец!!!!')
                    while (sum(mso_score_list_2) * 2 + sum(mso_score_list_1)) / (
                            len(mso_score_list_1) + len(mso_score_list_2) * 2) < 2.6:
                        mso_score_list_1.append(5)
                        mso_j += 1
                    if mso_j == 1:
                        mso_label_6.configure(text='У вас выходит ДВОЙКА. Вам нужно получить ещё')
                        mso_label_7.configure(text=mso_j)
                        mso_label_8.configure(text='отличную оценку до тройки в триместре.')
                    if (mso_j == 2) or (mso_j == 3) or (mso_j == 4):
                        mso_label_6.configure(text='У вас выходит ДВОЙКА. Вам нужно получить ещё')
                        mso_label_7.configure(text=mso_j)
                        mso_label_8.configure(text='отличные оценки до тройки в триместре.')
                    if mso_j >= 5:
                        mso_label_6.configure(text='У вас выходит ДВОЙКА. Вам нужно получить ещё')
                        mso_label_7.configure(text=mso_j)
                        mso_label_8.configure(text='отличных оценок до тройки в триместре.')
                if (mso_z >= 4.6) and (mso_z <= 5):
                    mso_label_6.configure(text='')
                    mso_label_7.configure(text='')
                    mso_label_8.configure(text='')
                    mso_label_5.configure(text='У вас выходит пятёрка!\n Не получайте плохих оценок!')

    center_window(root, 790, 320)
    m.window.configure(width=790, height=320)
    root.title('MiddleScore 5.1')
    root.minsize(790, 320)

    mso_title = Label(m.window, text='MiddleScore 5.1', font=('Arial Bold', 16), fg='red')
    mso_title.place(x=40, y=20)

    mso_label_1 = Label(m.window, text='Введите оценки без индекса:', font=('Times New Roman', 12))
    mso_label_1.place(x=40, y=60)

    # Поле ввода оценок без индекса
    mso_input_1 = Entry(m.window, width=40)
    mso_input_1.place(x=40, y=100)

    mso_label_2 = Label(m.window, text='Введите оценки с индексом «2»:', font=('Times New Roman', 12))
    mso_label_2.place(x=40, y=140)

    # Поле ввода оценок с индексом
    mso_input_2 = Entry(m.window, width=40)
    mso_input_2.place(x=40, y=180)
    ToolTip(mso_input_2, '5₂')

    mso_result_button = Button(m.window, text='РАССЧИТАТЬ', width=19, height=2, bg='black', fg='white',
                               command=mso_Done)
    mso_result_button.place(x=40, y=220)

    mso_label_3 = Label(m.window, text='Ваш средний балл: ', font=('Times New Roman', 16))
    mso_label_3.place(x=290, y=20)

    # Области вывода данных
    mso_label_4 = Label(m.window, font=('Times New Roman', 16))
    mso_label_4.place(x=310, y=60)

    mso_label_5 = Label(m.window, font=('Times New Roman', 16))
    mso_label_5.place(x=310, y=100)

    mso_label_6 = Label(m.window, font=('Times New Roman', 14))
    mso_label_6.place(x=310, y=140)

    mso_label_7 = Label(m.window, font=('Times New Roman', 14))
    mso_label_7.place(x=310, y=170)

    mso_label_8 = Label(m.window, font=('Times New Roman', 14))
    mso_label_8.place(x=333, y=170)

    mso_off = Button(m.window, text='⌂', font=('Arial Bold', 15), width=2, height=1, bg='black', fg='white',
                     command=mso_to_home)
    mso_off.place(x=0, y=5)
    ToolTip(mso_off, 'На главную...')
