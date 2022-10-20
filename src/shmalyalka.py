from random import randint
from tkinter import messagebox

from src.functions import *
from src.init import m, root
from src.homex import *


def Shmalyalka():
    """
    Авторский шутер
    """
    # Создание объекта с глобальными переменными
    sh = ShmalyalkaGlobals()

    def sh_to_home():
        """
        Возвращение на главную страницу MihaSoft
        """
        try:
            sh.parametrs_window.destroy()
        except AttributeError:
            pass

        sh_title.destroy()
        sh_label_1.destroy()
        sh_label_2.destroy()
        pushka.destroy()
        snaryad.destroy()
        cel.destroy()
        sh_up_button.destroy()
        sh_down_button.destroy()
        sh_shoot_button.destroy()
        sh_parametrs_button.destroy()
        sh_stop_button.destroy()
        sh_number_of_shots_label.destroy()
        sh_number_of_hits_label.destroy()
        sh_percents_label.destroy()
        sh_off.destroy()
        homes()
        m.window.configure(width=788, height=m.abs_height)
        center_window(root, 678, m.abs_height)

    def sh_to_shoot(sup=None):
        """
        Функция произведения выстрела из пушки
        """
        # Озвучка выстрела в случае наличия соответствующей настройки
        if os.path.exists('C:/MihaSoft Files/SoundFlagFile.miha'):
            Beep(300, 70)

        sh.x_snaryad = 100

        def odin():
            """
            Шаг итерации перемещения снаряда
            """
            snaryad.place(x=sh.x_snaryad)
            sh.x_snaryad += 5

        # Добавление нового выстрела к статистике
        sh.number_of_shots += 1
        sh_number_of_shots_label.configure(text=sh.number_of_shots)
        sh_percents_label.configure(text=str(int((sh.number_of_hits / sh.number_of_shots) * 100)) + '%')

        # Движение снаряда до уровня цели
        for i in range(100, 185):
            m.window.after(sh.speed_snar, odin())
            m.window.update()

        # Возвращение снаряда на исходное место
        sh.flag = True
        snaryad.place(x=100)

        # Перемещение цели на новую случайную позицию
        cel.place(x=530, y=randint(130, 530))

        # Проверка попадания снаряда в цель
        if 10 >= (snaryad.winfo_y() - cel.winfo_y()) >= -10:
            # Добавление нового попадания к статистике
            sh.number_of_hits += 1
            sh_number_of_hits_label.configure(text=sh.number_of_hits)
            sh_percents_label.configure(text=str(int((sh.number_of_hits / sh.number_of_shots) * 100)) + '%')
            # Озвучка попадания в случае наличия соответствующей настройки
            if os.path.exists('C:/MihaSoft Files/SoundFlagFile.miha'):
                Beep(500, 500)
        return sup

    def sh_up(par=None):
        """
        Функция движения пушки вверх
        """
        sh.flag = True

        def sh_up_one():
            """
            Шаг итерации движения пушки
            """
            # Проверка невыхода пушки за границы игрового поля
            if pushka.winfo_y() > 130:
                pushka.place(x=30, y=sh.y_pushka)
                snaryad.place(x=100, y=sh.y_pushka)
                sh.y_pushka -= 1

        # Движение пушки до границы игрового поля
        while pushka.winfo_y() != 130 and sh.flag:
            m.window.after(sh.speed_push, sh_up_one())
            m.window.update()

        # Движение пушки вниз после
        # достижения границы игрового поля
        while sh.flag:
            sh_down()
        return par

    def sh_down(par=None):
        """
        Функция движения пушки вниз
        """
        sh.flag = True

        def sh_down_one():
            """
            Шаг итерации движения пушки
            """
            if pushka.winfo_y() < 530:
                pushka.place(x=30, y=sh.y_pushka)
                snaryad.place(x=100, y=sh.y_pushka)
                sh.y_pushka += 1

        # Движение пушки до границы игрового поля
        while pushka.winfo_y() != 530 and sh.flag:
            m.window.after(sh.speed_push, sh_down_one())
            m.window.update()

        # Движение пушки вверх
        # после достижения границы игрового поля
        while sh.flag:
            sh_up()
        return par

    def sh_stop():
        sh.flag = False
        sh.y_pushka = 130
        pushka.place(x=30, y=130)
        snaryad.place(x=100, y=130)
        cel.place(x=530, y=randint(130, 530))
        cel.configure(bg='black')
        sh.number_of_hits = 0
        sh_number_of_hits_label.configure(text='0')
        sh.number_of_shots = 0
        sh_number_of_shots_label.configure(text='0')

    def sh_parametrs():
        """
        Функция изменения скорости
        движения пушки и снаряда
        """

        def sh_create_par_window():
            def sh_save_changes():
                """
                Функция сохранения изменений параметров
                """
                # Проверка корректности введённых параметров
                if not sh_parametrs_input_1.get().isdigit() and not sh_parametrs_input_2.get().isdigit():
                    messagebox.showinfo(title='INFO', message='Введите корректные значения!',
                                        parent=sh.parametrs_window)
                else:
                    if not sh_parametrs_input_1.get().isdigit():
                        if int(sh_parametrs_input_2.get()) < 0:
                            messagebox.showwarning(title='INFO', message='Скорость не должна быть меньше 0!',
                                                   parent=sh.parametrs_window)
                        elif int(sh_parametrs_input_2.get()) > 500:
                            messagebox.showwarning(title='INFO', message='Скорость не должна превышать 500 единиц!',
                                                   parent=sh.parametrs_window)
                        else:
                            sh.speed_snar = abs(500 - int(sh_parametrs_input_2.get()))
                            sh.parametrs_window.destroy()
                    elif not sh_parametrs_input_2.get().isdigit():
                        if int(sh_parametrs_input_1.get()) < 0:
                            messagebox.showwarning(title='INFO', message='Скорость не должна быть меньше 0!',
                                                   parent=sh.parametrs_window)
                        elif int(sh_parametrs_input_1.get()) > 500:
                            messagebox.showwarning(title='INFO', message='Скорость не должна превышать 500 единиц!',
                                                   parent=sh.parametrs_window)
                        else:
                            sh.speed_push = abs(500 - int(sh_parametrs_input_1.get()))
                            sh.parametrs_window.destroy()
                    else:
                        if int(sh_parametrs_input_1.get()) < 0 or int(sh_parametrs_input_2.get()) < 0:
                            messagebox.showwarning(title='INFO', message='Скорость не должна быть меньше 0!',
                                                   parent=sh.parametrs_window)
                        elif int(sh_parametrs_input_1.get()) > 500 or int(sh_parametrs_input_2.get()) > 500:
                            messagebox.showwarning(title='INFO', message='Скорость не должна превышать 500 единиц!',
                                                   parent=sh.parametrs_window)
                        else:
                            sh.speed_push = abs(500 - int(sh_parametrs_input_1.get()))
                            sh.speed_snar = abs(500 - int(sh_parametrs_input_2.get()))
                            sh.parametrs_window.destroy()

            def sh_exit_parametrs():
                """
                Отмена изменения параметров
                """
                sh.parametrs_window.destroy()

            sh.parametrs_window = Toplevel()
            center_window(sh.parametrs_window, 250, 200)
            sh.parametrs_window.resizable(False, False)
            sh.parametrs_window.title('Параметры')

            sh_parametrs_label_1 = Label(sh.parametrs_window, text='Скорость пушки:')
            sh_parametrs_label_1.place(x=5, y=5)

            # Поле ввода скорости движения пушки
            sh_parametrs_input_1 = Entry(sh.parametrs_window, width=20)
            sh_parametrs_input_1.place(x=10, y=50)

            sh_parametrs_label_2 = Label(sh.parametrs_window, text='Скорость снаряда:')
            sh_parametrs_label_2.place(x=5, y=90)

            # Поле ввода скорости движения снаряда
            sh_parametrs_input_2 = Entry(sh.parametrs_window, width=20)
            sh_parametrs_input_2.place(x=10, y=135)

            sh_parametrs_ok_button = Button(sh.parametrs_window, text='ОК', bg='#c0ebd6', width=8,
                                            command=sh_save_changes)
            sh_parametrs_ok_button.place(x=160, y=10)

            sh_parametrs_abort_button = Button(sh.parametrs_window, text='Отмена', bg='#ebc0d0', width=8,
                                               command=sh_exit_parametrs)
            sh_parametrs_abort_button.place(x=160, y=50)

        try:
            sh.parametrs_window.resizable(False, False)

        except AttributeError:
            sh_create_par_window()

        except TclError:
            sh_create_par_window()

    center_window(root, 600, 640)
    m.window.configure(width=600, height=640)
    root.title('Shmalyalka 1.2')
    root.minsize(600, 640)

    sh_title = Label(m.window, text='Shmalyalka 1.2', font=('Arial Bold', 16), fg='red')
    sh_title.place(x=40, y=20)

    sh_up_button = Button(m.window, text='⇧', font=('Arial Black', 20), bg='#90d69f', command=sh_up)
    sh_up_button.place(x=240, y=20)

    sh_down_button = Button(m.window, text='⇩', font=('Arial Black', 20), bg='#90d69f', command=sh_down)
    sh_down_button.place(x=310, y=20)

    pushka = Label(m.window, width=10, bg='#ff0000')
    pushka.place(x=30, y=130)

    snaryad = Label(m.window, width=2, bg='#11ff00')
    snaryad.place(x=100, y=130)

    cel = Label(m.window, width=2, bg='black')
    cel.place(x=530, y=randint(130, 530))

    sh_shoot_button = Button(m.window, text='ЗАЛП', bg='yellow', width=10, font=('Times New Roman', 16),
                             command=sh_to_shoot)
    sh_shoot_button.place(x=400, y=20)

    sh_label_1 = Label(m.window, text='Попаданий:')
    sh_label_1.place(x=30, y=70)

    sh_number_of_hits_label = Label(m.window, text='0')
    sh_number_of_hits_label.place(x=100, y=70)

    sh_label_2 = Label(m.window, text='Выстрелов:')
    sh_label_2.place(x=30, y=90)

    sh_number_of_shots_label = Label(m.window, text='0')
    sh_number_of_shots_label.place(x=100, y=90)

    sh_percents_label = Label(m.window)
    sh_percents_label.place(x=130, y=80)

    sh_stop_button = Button(m.window, text='ЗАНОВО', bg='#d47f7f', width=10, font=('Times New Roman', 16),
                            command=sh_stop)
    sh_stop_button.place(x=400, y=70)

    sh_parametrs_button = Button(m.window, text='Параметры', bg='#9be0df', width=10, font=('Times New Roman', 12),
                                 command=sh_parametrs)
    sh_parametrs_button.place(x=450, y=570)

    root.bind('<Return>', sh_to_shoot)
    root.bind('<space>', sh_to_shoot)
    root.bind('<Down>', sh_down)
    root.bind('<Up>', sh_up)

    sh_off = Button(m.window, text='⌂', font=('Arial Bold', 15), width=2, height=1, bg='black', fg='white',
                    command=sh_to_home)
    sh_off.place(x=0, y=5)
    ToolTip(sh_off, 'На главную...')
