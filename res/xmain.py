# ------------------------------------------------------------------------------------ #
#            M     M   M   M                  MMMMMMM          MMMM     M              #
#            M M M M       M         M        M         MMMM   M        M              #
#            M  M  M   M   MMMM   MMMM        MMMMMMM   M  M   MMMM   MMMMM            #
#            M     M   M   M  M   M  M              M   M  M   M        M              #
#            M     M   M   M  M   MMMMMM      MMMMMMM   MMMM   M        MMM            #
#                                                                                      #
#    Copyright (C) 2022 Vlasko M.M. <https://mihasoft.glitch.me> All rights reserved.  #
# ------------------------------------------------------------------------------------ #

# - 1 ------------- ИМПОРТЫ ---------------------


import datetime
import os
# import cv2
import requests
from json import loads
from tkinter.font import families
from random import randint, choice
from shutil import rmtree
from time import sleep, strftime
from tkinter import *
from tkinter import colorchooser
from tkinter import messagebox
from tkinter import ttk
from tkinter.filedialog import asksaveasfile
from tkinter.ttk import Radiobutton
from turtle import *
from autopy.bitmap import capture_screen
from numpy import save, load
from winsound import Beep
from PIL import Image, ImageDraw, ImageFont, UnidentifiedImageError, ImageTk
from tkinter.filedialog import asksaveasfilename, askopenfilename
from webbrowser import open_new
from pyperclip import copy, paste
from qrcode import make
from qrcode.exceptions import DataOverflowError
from subprocess import Popen
from math import ceil
import PyInstaller
import PyInstaller.__main__


# - 2 ------------- ОБЩИЕ ФУНКЦИИ ---------------


def center_window(roots, x_width, height):
    """
    Функция для размещения окон в центре экрана
    """

    x_window_height = height
    x_window_width = x_width

    # Получение ширины и высоты экрана монитора
    screen_width = roots.winfo_screenwidth()
    screen_height = roots.winfo_screenheight()

    # Расчёт координаты верхнего левого угла окна
    x_coordinate = int((screen_width / 2) - (x_window_width / 2))
    y_coordinate = int((screen_height / 2) - (x_window_height / 2))

    roots.geometry('{}x{}+{}+{}'.format(x_window_width, x_window_height, x_coordinate, y_coordinate))


class ToolTipBase:
    """
    Прототип всплывающих при наведении
    курсора на объект подсказок
    """

    def __init__(self, button, text):
        self.button = button
        self.text = text
        self.tipwindow = None
        self.id = None
        self.x = self.y = 0
        self._id1 = self.button.bind('<Enter>', self.enter)  # Событие при наведении курсора
        self._id2 = self.button.bind('<Leave>', self.leave)  # Событие при отводе курсора от объекта
        self._id3 = self.button.bind('<ButtonPress>', self.leave)  # Событие при нажатии на объект (кнопку)

    def enter(self, event=None):
        """
        Появление подсказки
        """

        self.schedule()
        return event

    def leave(self, event=None):
        """
        Исчезновение подсказки
        """

        self.unschedule()
        self.hidetip()
        return event

    def schedule(self):
        self.unschedule()
        self.id = self.button.after(15, self.showtip)

    def unschedule(self):
        ad = self.id
        self.id = None
        if ad:
            self.button.after_cancel(ad)

    def showtip(self):
        if self.tipwindow:
            return
        xx = self.button.winfo_rootx() + 20
        yy = self.button.winfo_rooty() + self.button.winfo_height() + 1
        self.tipwindow = tw = Toplevel(self.button)
        tw.wm_overrideredirect(True)
        tw.wm_geometry('+%d+%d' % (xx, yy))
        self.showcontents()

    def showcontents(self):
        label = Label(self.tipwindow, text=str(self.text), justify=LEFT,
                      background='white', relief=SOLID, borderwidth=1)
        label.pack()

    def hidetip(self):
        tw = self.tipwindow
        self.tipwindow = None
        if tw:
            tw.destroy()


class ToolTipok(ToolTipBase):
    """
    Объект подсказки
    """

    def __init__(self, button, text):
        ToolTipBase.__init__(self, button, text)

    def showcontents(self):
        ToolTipBase.showcontents(self)


def ToolTip(button, text):
    """
    Функция, благодаря которой всплывающие подсказки появляются только
    при включении соответствующих настроек
    """

    if os.path.exists('MihaSoft Files/TintFlagFile.miha'):
        ToolTipok(button, text)


class Gif(Label, object):
    def __init__(self, master, path, forever=True):
        self._master = master
        self._loc = 0
        self._forever = forever

        self._is_running = False

        im = Image.open(path)
        self._frames = []
        i = 0
        try:
            while True:
                photo_frame = ImageTk.PhotoImage(im.copy().convert('RGBA'))
                self._frames.append(photo_frame)

                i += 1
                im.seek(i)
        except EOFError:
            pass

        self._last_index = len(self._frames) - 1

        self._delay = im.info['duration']

        self._callback_id = None

        super(Gif, self).__init__(master, image=self._frames[0])

    def start_animation(self, frame=None):
        if self._is_running:
            return

        if frame is not None:
            self._loc = 0
            self.configure(image=self._frames[frame])

        self._master.after(self._delay, self._animate_GIF)
        self._is_running = True

    def stop_animation(self):
        if not self._is_running:
            return

        if self._callback_id is not None:
            self.after_cancel(self._callback_id)
            self._callback_id = None

        self._is_running = False

    def _animate_GIF(self):
        self._loc += 1
        self.configure(image=self._frames[self._loc])

        if self._loc == self._last_index:
            if self._forever:
                self._loc = 0
                self._callback_id = self._master.after(self._delay, self._animate_GIF)
            else:
                self._callback_id = None
                self._is_running = False
        else:
            self._callback_id = self._master.after(self._delay, self._animate_GIF)

    def pack(self, start_animation=True, **kwargs):
        if start_animation:
            self.start_animation()

        super(Gif, self).pack(**kwargs)

    def grid(self, start_animation=True, **kwargs):
        if start_animation:
            self.start_animation()

        super(Gif, self).grid(**kwargs)

    def place(self, start_animation=True, **kwargs):
        if start_animation:
            self.start_animation()

        super(Gif, self).place(**kwargs)


class Main:
    def __init__(self):
        self.abs_height = 0
        self.enu = None
        self.help_window = None
        self.info_window = None
        self.qr_window = None
        self.bac_window = None
        self.ct_window = None
        self.valute_window = None
        self.mess_window = None
        self.set_window = None
        self.dict_window = None
        self.mus_flag = True
        self.monk_window = []


class YourAgeOnlineGlobals:
    """
    Глобальные переменные для приложения
    YourAgeOnline
    """

    def __init__(self):
        self.open_window = None
        self.save_window = None
        self.delete_window = None


class NSGlobals:
    def __init__(self):
        self.ch2 = 0


class SMLGlobals:
    """
    Глобальные переменные для приложения
    The Simplest Mihail's language (SML) - IDE and Compiler
    """

    def __init__(self):
        self.run_result = None
        self.flag = None
        self.flag_1 = None
        self.help_window = None
        self.example_window = None
        self.save_window = None
        self.open_window = None
        self.delete_window = None
        self.run_window = None


class CrossZeroGlobals:
    """
    Глобальные переменные для приложения CrossZero
    """

    def __init__(self):
        self.flag_1 = 3
        self.flag_2 = 3
        self.flag_3 = 3
        self.flag_4 = 3
        self.flag_5 = 3
        self.flag_6 = 3
        self.flag_7 = 3
        self.flag_8 = 3
        self.flag_9 = 3
        self.number_of_moves = 0
        self.winner = ''
        self.player_1 = ''
        self.player_2 = ''
        self.naming_condition = 0
        self.condition = 3
        self.number_of_moves_str = None
        self.name_of_winner_str = None
        self.save_string = None
        self.game_condition = True
        self.game_res_condition = None
        self.rng_window = None
        self.parametrs_window = None
        self.report_window = None
        self.open_window = None
        self.delete_window = None


class MihNoteGlobals:
    """
    Глобальные переменные для приложения MihNote
    """

    def __init__(self):
        self.open_combobox = None
        self.open_ok_button = None
        self.edit_combobox = None
        self.edit_ok_button = None
        self.delete_combobox = None
        self.delete_ask_button = None
        self.new_note_window = None
        self.save_window = None
        self.delete_window = None
        self.edit_window = None
        self.open_flag = False
        self.edit_flag = False
        self.del_flag = False


class PaintGlobals:
    """
    Глобальные переменные для приложения Paint
    """

    def __init__(self):
        self.choose_flag = True
        self.save_flag = True
        self.chosen_color = 'white'
        self.now_color = None
        self.file_name = None
        self.save_window = None
        self.open_window = None
        self.delete_window = None


class SaperGlobals:
    """
    Глобальные переменные для приложения Saper
    """

    def __init__(self):
        self.to_flags_list = [False, False, False, False, False, False, False, False, False, False, False, False, False,
                              False, False, False, False, False, False, False, False, False, False, False, False]
        self.flag_a1 = None
        self.flag_a2 = None
        self.flag_a3 = None
        self.flag_a4 = None
        self.flag_a5 = None
        self.flag_b1 = None
        self.flag_b2 = None
        self.flag_b3 = None
        self.flag_b4 = None
        self.flag_b5 = None
        self.flag_c1 = None
        self.flag_c2 = None
        self.flag_c3 = None
        self.flag_c4 = None
        self.flag_c5 = None
        self.flag_d1 = None
        self.flag_d2 = None
        self.flag_d3 = None
        self.flag_d4 = None
        self.flag_d5 = None
        self.flag_e1 = None
        self.flag_e2 = None
        self.flag_e3 = None
        self.flag_e4 = None
        self.flag_e5 = None
        self.bomb_list = None
        self.box_list = None
        self.global_flag = None
        self.number_of_mines = 5
        self.start_flag = None
        self.flags_array = None
        self.glob_but = None
        self.stat_window = None
        self.params_window = None


class ShmalyalkaGlobals:
    """
    Глобальные переменные для приложения Shmalyalka
    """

    def __init__(self):
        self.number_of_hits = 0
        self.number_of_shots = 0
        self.flag = True
        self.speed_push = 2
        self.speed_snar = 1
        self.y_pushka = 130
        self.x_snaryad = None
        self.parametrs_window = None


class WindowManagerGlobals:
    """
    Глобальные переменные для приложения WindowManager
    """

    def __init__(self):
        self.width = None
        self.height = None
        self.x_cord = None
        self.y_cord = None
        self.cust_title = None
        self.text = None
        self.font = None
        self.fsize = None
        self.color = ''
        self.text_x = None
        self.text_y = None
        self.open_path = None
        self.flag = True
        self.custom_window = None
        self.open_window = None
        self.save_window = None
        self.edit_window = None
        self.delete_window = None
        self.font_window = None


class YourWarningsGlobals:
    """
    Глобальные переменные для приложения YourWarnings
    """

    def __init__(self):
        self.preview_window = None
        self.preview_ask_window = None
        self.delete_window = None


class AccountManagerGlobals:
    """
    Глобальные переменные для приложения AccountManager
    """

    def __init__(self):
        self.open_window = None
        self.delete_window = None
        self.quest_window = None


class TurtlePaintGlobal:
    """
    Глобальная переменная для приложения TurtlePaint
    """

    def __init__(self):
        self.colors = None
        self.help_window = None
        self.now_color = 'red'


class WaterMarksGlobals:
    """
    Глобальная переменная для приложения TurtlePaint
    """

    def __init__(self):
        self.file = None
        self.color = (0, 0, 0)
        self.image = None
        self.edit_window = None
        self.save_window = None
        self.delete_window = None
        self.view_window = None
        self.flag = True
        self.open_path = None


class HyperTextGlobals:
    """
    Глобальная переменная для приложения HyperText
    """

    def __init__(self):
        self.background = 'white'
        self.color = 'black'
        self.key = 0
        self.but_color = 'white'
        self.but_f_color = 'black'
        self.name_x = ''
        self.all_color = 'white'
        self.block = ''
        self.image = None
        self.i_i = None
        self.req_win = None
        self.resp_window = None


class BACGlobals:
    """
    Глобальная переменная для приложения BAC
    """

    def __init__(self):
        self.number = None
        self.k = 0
        self.flag = True
        self.s_window = None


class LoadingLineGlobals:
    """
    Глобальные переменные для функции
    анимации загрузки программы
    """

    def __init__(self):
        self.line_height = 1
        self.logo_size = 1


class PoupGlobals:
    """
    Глобальные переменные для функции
    выпадающего меню
    """

    def __init__(self):
        self.x = None
        self.y = None


# - 3 ------------ ОСНОВНЫЕ ПРИЛОЖЕНИЯ --------------


def YourAge():
    """
    Приложение для расчёта времени, прошедшего между двумя датами.
    Подробнее - https://mihasoft.glitch.me/yao.html
    """
    yao = YourAgeOnlineGlobals()

    def yao_to_home():
        """
         Функция возвращения на главную страницу MihaSoft
        (Уничтожение (destroy()) всех виджетов и запуск функции главной страницы)
        """
        try:
            yao.save_window.destroy()
        except AttributeError:
            pass

        try:
            yao.delete_window.destroy()
        except AttributeError:
            pass

        try:
            yao.open_window.destroy()
        except AttributeError:
            pass

        yao_title.destroy()
        yao_label_8.destroy()
        yao_label_7.destroy()
        yao_label_6.destroy()
        yao_label_5.destroy()
        yao_label_4.destroy()
        yao_label_3.destroy()
        yao_label_2.destroy()
        yao_label_1.destroy()
        yao_day_input.destroy()
        yao_month_input.destroy()
        yao_year_input.destroy()
        yao_now_day_input.destroy()
        yao_now_month_input.destroy()
        yao_now_year_input.destroy()
        yao_sysdate_button.destroy()
        yao_save_button.destroy()
        yao_birthday_button.destroy()
        yao_delete_button.destroy()
        yao_clean_button.destroy()
        yao_result_button.destroy()
        yao_choice_radbut_1.destroy()
        yao_choice_radbut_2.destroy()
        yao_off.destroy()
        home()
        window.configure(width=700, height=m.abs_height)
        center_window(root, 678, m.abs_height)

    def yao_begin():
        """
        Функция расчёта возраста при нажатии
        соответствующей кнопки
        """

        # Проверка корректности введённых пользователем данных.
        # Функция isdigit() проверяет, является ли введённое значение числом.

        if (not yao_day_input.get().isdigit()) or (not yao_month_input.get().isdigit()) or (
                not yao_year_input.get().isdigit()) or (not yao_now_day_input.get().isdigit()) or (
                not yao_now_month_input.get().isdigit()) or (not yao_now_year_input.get().isdigit()):
            messagebox.showwarning('INFO', 'Введены некорректные значения!')

        else:
            yao_days = 0
            yao_day_1 = int(yao_day_input.get())
            yao_month_1 = int(yao_month_input.get())
            yao_year_1 = int(yao_year_input.get())
            yao_day_2 = int(yao_now_day_input.get())
            yao_month_2 = int(yao_now_month_input.get())
            yao_year_2 = int(yao_now_year_input.get())

            # Проверка соответствия введённых чисел размерам месяца, года
            # и того факта, что текущая дата больше, чем исходная.

            if ((yao_day_1 >= 1) and (yao_day_1 <= 31)) and ((yao_month_1 >= 1) and (yao_month_1 <= 12)) and (
                    yao_year_1 > 0) and ((yao_day_2 >= 1) and (yao_day_2 <= 31)) and (
                    (yao_month_2 >= 1) and (yao_month_2 <= 12)) and (yao_year_2 > 0) and (yao_year_2 >= yao_year_1):
                z: int = yao_month_2 - 1
                yao_years = yao_year_2 - yao_year_1 - 1
                h: int = 12 - yao_month_1

                # Обработка потенциальной високосности года:

                if yao_month_1 != 2:
                    if yao_month_1 % 2 == 0:
                        k = 30 - yao_day_1
                        yao_days = k + yao_day_2
                        if yao_days >= 30:
                            h += 1
                            yao_days = yao_days - 30
                    else:
                        k = 31 - yao_day_1
                        yao_days = k + yao_day_2
                        if yao_days >= 31:
                            h += 1
                            yao_days = yao_days - 31
                else:
                    if yao_year_1 % 4 == 0:
                        k = 29 - yao_day_1
                        yao_days = k + yao_day_2
                        if yao_days >= 19:
                            h += 1
                            yao_days = yao_days - 29
                        else:
                            k = 28 - yao_day_1
                            yao_days = k + yao_day_2
                        if yao_days >= 28:
                            h += 1
                            yao_days = yao_days - 28
                yao_months = h + z
                if yao_months >= 12:
                    yao_years += 1
                    yao_months = yao_months - 12
                if z % 2 == 0:
                    yao_days += 1

                # Обработка выбранной пользователем формы вывода данных
                # и подбор нужных окончаний слов в зависимости от числа.

                yao_l = yao_choice_def.get()
                if yao_l == 1:
                    if yao_years == 0:
                        yao_label_8.configure(
                            text=(str(yao_years) + ' год ' + str(yao_months) + ' месяцев ' + str(
                                yao_days - 1) + ' дней.'))
                    elif yao_years == 1:
                        yao_label_8.configure(text=(str(yao_years) + ' год ' + str(yao_months) + ' месяцев ' + str(
                            yao_days - 1) + ' дней.'))
                    elif (yao_years == 2) or (yao_years == 3) or (yao_years == 4):
                        yao_label_8.configure(
                            text=(str(yao_years) + ' года ' + str(yao_months) + ' месяцев ' + str(
                                yao_days - 1) + ' дней.'))
                    else:
                        yao_label_8.configure(text=(str(yao_years) + ' лет ' + str(yao_months) + ' месяцев ' + str(
                            yao_days - 1) + ' дней.'))
                if yao_l == 2:
                    yao_label_8.configure(
                        text=(str(int(
                            (365.29 * yao_years) + (yao_months * 30.25) + (yao_days - 2) // 1 + 2)) + ' дней.'))
            else:
                messagebox.showwarning('INFO', 'Проверьте правильность ввода!')

    def yao_Now_Date():
        """
        Функция получения текущего системного времени
        и его подстановки в соответствующие поля ввода
        """
        yao_now_day_input.delete(0, END)
        yao_now_month_input.delete(0, END)
        yao_now_year_input.delete(0, END)
        yao_now = datetime.datetime.now()
        yao_now_day_input.insert(0, str(yao_now.day))
        yao_now_month_input.insert(0, str(yao_now.month))
        yao_now_year_input.insert(0, str(yao_now.year))

    def yao_Save():
        """
        Функция сохранения в файл данных об исходной
        дате, введённой пользователем
        """

        def yao_Save_Abort():
            """
            Закрытие окна без сохранения
            """
            yao.save_window.destroy()

        def yao_create_save_window():
            def yao_Save_OK():
                """
                Сохранение файла с введённым
                названием и закрытие окна сохранения
                """
                text_file = open('MihaSoft Files/YAO Files/' + str(yao_save_name_input.get()), 'w')
                text_file.write(str(yao_day_input.get()) + '/' + str(yao_month_input.get()) + '*' + str(
                    yao_year_input.get()) + '.')
                text_file.close()
                yao.save_window.destroy()

            yao.save_window = Toplevel()
            center_window(yao.save_window, 250, 100)
            yao.save_window.resizable(False, False)  # Неизменяемый размер окна
            yao.save_window.title('Сохранение')

            yao_save_label = Label(yao.save_window, text='Введите имя...')
            yao_save_label.place(x=5, y=5)

            # Поле ввода имени файла
            yao_save_name_input = Entry(yao.save_window, width=20)
            yao_save_name_input.place(x=5, y=30)

            yao_saving_button = Button(yao.save_window, text='Сохранить', width=10, height=1, bg="#8ceb8a",
                                       command=yao_Save_OK)
            yao_saving_button.place(x=140, y=29)

            yao_save_abort_button = Button(yao.save_window, text='Отмена', width=10, height=1, bg='#999999',
                                           command=yao_Save_Abort)
            yao_save_abort_button.place(x=140, y=64)

        try:
            yao.save_window.resizable(False, False)

        except AttributeError:
            yao_create_save_window()

        except TclError:
            yao_create_save_window()

    def yao_Open():
        """
        Функция подстановки ранее сохранённой исходной
        даты в соответствующие поля ввода
        """

        def yao_Open_Abort():
            """
            Закрытие окна без вывода данных
            """
            yao.open_window.destroy()

        def yao_create_op_window():
            def yao_Open_OK():
                """
                Открытие выбранного файла и вывод данных
                """
                if yao_files_list:
                    yao_open_file = open('MihaSoft Files/YAO Files/' + str(yao_open_combobox.get()), 'r')
                    yao_file = yao_open_file.read()
                    yao_open_file.close()

                    yao_data_from_file = list(str(yao_file))

                    yao_day = yao_month = yao_year = ''

                    # Структура сохраняемых файлов: 11/11*1111.
                    # Следующие циклы for считывают цифры между соответствующими
                    # знаками и записывают их в соответствующие переменные.

                    for i in range(0, yao_data_from_file.index('/')):
                        yao_day += str(yao_data_from_file[i])

                    for i in range(yao_data_from_file.index('/') + 1, yao_data_from_file.index('*')):
                        yao_month += str(yao_data_from_file[i])

                    for i in range(yao_data_from_file.index('*') + 1, yao_data_from_file.index('.')):
                        yao_year += str(yao_data_from_file[i])

                    yao_day_input.delete(0, END)
                    yao_month_input.delete(0, END)
                    yao_year_input.delete(0, END)

                    yao_day_input.insert(0, yao_day)
                    yao_month_input.insert(0, yao_month)
                    yao_year_input.insert(0, yao_year)
                    yao.open_window.destroy()

            yao.open_window = Toplevel()
            center_window(yao.open_window, 300, 150)
            yao.open_window.resizable(False, False)
            yao.open_window.title('Подставить...')

            yao_open_label = Label(yao.open_window, text='Выберите имя...')
            yao_open_label.place(x=5, y=5)

            # Выпадающий список имеющихся файлов
            yao_open_combobox = ttk.Combobox(yao.open_window, values=os.listdir('MihaSoft Files/YAO Files'),
                                             font=('Arial Bold', 16),
                                             state='readonly')
            yao_open_combobox.place(x=10, y=50)

            yao_open_button = Button(yao.open_window, text='Подставить', font=('Arial Bold', 10), bg='#7bd491',
                                     width=14,
                                     command=yao_Open_OK)
            yao_open_button.place(x=10, y=100)

            yao_open_abort_button = Button(yao.open_window, text='Отмена', font=('Arial Bold', 10), bg='#999999',
                                           width=14,
                                           command=yao_Open_Abort)
            yao_open_abort_button.place(x=150, y=100)

        try:
            yao.open_window.resizable(False, False)

        except AttributeError:
            yao_create_op_window()

        except TclError:
            yao_create_op_window()

    def yao_Delete():
        """
        Функция удаления ранее записанных файлов
        """

        def yao_Delete_Abort():
            """
            Закрытие окна без удаления
            """
            yao.delete_window.destroy()

        def yao_create_del_window():
            def yao_Delete_OK():
                """
                Удаление выбранного файла и закрытие окна
                """

                if yao_files_list:  # Проверяет, выбран ли хоть какой-то файл
                    os.remove('MihaSoft Files/YAO Files/' + str(yao_del_combobox.get()))
                    yao.delete_window.destroy()

            yao.delete_window = Toplevel()
            yao.delete_window.geometry('300x150+70+70')
            center_window(yao.delete_window, 300, 150)
            yao.delete_window.resizable(False, False)
            yao.delete_window.title('Удаление записи')

            yao_del_label = Label(yao.delete_window, text='Выберите запись для удаления...')
            yao_del_label.place(x=5, y=5)

            # Выпадающий список имеющихся файлов
            yao_del_combobox = ttk.Combobox(yao.delete_window, values=os.listdir('MihaSoft Files/YAO Files'),
                                            font=('Arial Bold', 16),
                                            state='readonly')
            yao_del_combobox.place(x=10, y=50)

            yao_del_ok_button = Button(yao.delete_window, text='Удалить', font=('Arial Bold', 10), bg='#eb8a8a',
                                       width=14, command=yao_Delete_OK)
            yao_del_ok_button.place(x=10, y=100)

            yao_del_abort_button = Button(yao.delete_window, text='Отмена', font=('Arial Bold', 10),
                                          bg='#999999', width=14, command=yao_Delete_Abort)
            yao_del_abort_button.place(x=150, y=100)

        try:
            yao.delete_window.resizable(False, False)

        except AttributeError:
            yao_create_del_window()

        except TclError:
            yao_create_del_window()

    def yao_Clean():
        """
        Функция очистки всех полей ввода
        """
        yao_day_input.delete(0, 'end')
        yao_now_day_input.delete(0, 'end')
        yao_month_input.delete(0, 'end')
        yao_now_month_input.delete(0, 'end')
        yao_year_input.delete(0, 'end')
        yao_now_year_input.delete(0, 'end')

    # Создание папки файлов приложения в случае отсутствия таковой:
    if not os.path.exists('MihaSoft Files/YAO Files'):
        os.mkdir('MihaSoft Files/YAO Files')

    yao_files_list = os.listdir('MihaSoft Files/YAO Files')
    center_window(root, 620, 250)
    root.title('YourAge 3.0')
    window.configure(width=620, height=250)
    root.minsize(620, 250)

    yao_title = Label(window, text='YourAge 3.0', font=('Arial Bold', 16), fg='red')
    yao_title.place(x=40, y=20)

    yao_label_1 = Label(window, text='Дата рождения:', font=('Times New Roman', 12))
    yao_label_1.place(x=40, y=60)

    # Поле ввода исходного дня
    yao_day_input = Entry(window, width=4)
    yao_day_input.place(x=40, y=100)
    ToolTip(yao_day_input, 'День')

    yao_label_2 = Label(window, text='.', font=('Times New Roman', 12))
    yao_label_2.place(x=73, y=103)

    # Поле ввода исходного месяца
    yao_month_input = Entry(window, width=4)
    yao_month_input.place(x=90, y=100)
    ToolTip(yao_month_input, 'Месяц')

    yao_label_3 = Label(window, text='.', font=('Times New Roman', 12))
    yao_label_3.place(x=124, y=100)

    # Поле ввода исходного года
    yao_year_input = Entry(window, width=9)
    yao_year_input.place(x=140, y=100)
    ToolTip(yao_year_input, 'Год')

    yao_sysdate_button = Button(window, text='Подставить т. д.', width=13, height=1, bg='#eef5b3',
                                command=yao_Now_Date)
    yao_sysdate_button.place(x=250, y=20)
    ToolTip(yao_sysdate_button, 'Подставить системную дату...')

    yao_save_button = Button(window, text='Сохранить зап.', width=13, height=1, bg='#8ceb8a',
                             command=yao_Save)
    yao_save_button.place(x=490, y=120)
    ToolTip(yao_save_button, 'Сохранить данные о дате рождения...')

    yao_birthday_button = Button(window, text='Подставить д. р.', width=13, height=1, bg='#b3f5ec',
                                 command=yao_Open)
    yao_birthday_button.place(x=370, y=20)
    ToolTip(yao_birthday_button, 'Подставить сохранённую дату рождения...')

    yao_delete_button = Button(window, text='Удалить зап.', width=13, height=1, bg='#eb8a8a', fg='black',
                               command=yao_Delete)
    yao_delete_button.place(x=490, y=70)
    ToolTip(yao_delete_button, 'Удалить запись о дате рождения...')

    yao_clean_button = Button(window, text='Очистить', width=13, height=1, bg='#ebd38a', command=yao_Clean)
    yao_clean_button.place(x=490, y=20)
    ToolTip(yao_clean_button, 'Очистить поля ввода...')

    yao_label_4 = Label(window, text='Текущая дата:', font=('Times New Roman', 12))
    yao_label_4.place(x=300, y=60)

    # Поле ввода текущего дня
    yao_now_day_input = Entry(window, width=4)
    yao_now_day_input.place(x=300, y=100)
    ToolTip(yao_now_day_input, 'День')

    yao_label_5 = Label(window, text='.', font=('Times New Roman', 12))
    yao_label_5.place(x=333, y=100)

    # Поле ввода текущего месяца
    yao_now_month_input = Entry(window, width=4)
    yao_now_month_input.place(x=350, y=100)
    ToolTip(yao_now_month_input, 'Месяц')

    yao_label_6 = Label(window, text='.', font=('Times New Roman', 12))
    yao_label_6.place(x=384, y=100)

    # Поле ввода текущего года
    yao_now_year_input = Entry(window, width=9)
    yao_now_year_input.place(x=400, y=100)
    ToolTip(yao_now_year_input, 'Год')

    # Получение выбранного способа вывода данных
    yao_choice_def = IntVar()

    # Кнопки выбора одного из двух способов вывода данных:
    yao_choice_radbut_1 = Radiobutton(window, text='Вывести возраст в годах, месяцах и днях', variable=yao_choice_def,
                                      value=1)
    yao_choice_radbut_1.place(x=40, y=150)

    yao_choice_radbut_2 = Radiobutton(window, text='Вывести возраст в днях', variable=yao_choice_def, value=2)
    yao_choice_radbut_2.place(x=300, y=150)

    yao_result_button = Button(window, text='РАССЧИТАТЬ', width=19, height=2, bg='black', fg='white', command=yao_begin)
    yao_result_button.place(x=40, y=190)

    yao_label_7 = Label(window, text='Ваш возраст: ', font=('Times New Roman', 16))
    yao_label_7.place(x=220, y=190)

    yao_label_8 = Label(window, font=('Times New Roman', 16))
    yao_label_8.place(x=350, y=190)

    yao_off = Button(window, text='⌂', font=('Arial Bold', 15), width=2, height=1, bg='black', fg='white',
                     command=yao_to_home)
    yao_off.place(x=0, y=5)
    ToolTip(yao_off, 'На главную...')


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
        home()
        window.configure(width=700, height=720)
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
    window.configure(width=790, height=320)
    root.title('MiddleScore 5.1')
    root.minsize(790, 320)

    mso_title = Label(window, text='MiddleScore 5.1', font=('Arial Bold', 16), fg='red')
    mso_title.place(x=40, y=20)

    mso_label_1 = Label(window, text='Введите оценки без индекса:', font=('Times New Roman', 12))
    mso_label_1.place(x=40, y=60)

    # Поле ввода оценок без индекса
    mso_input_1 = Entry(window, width=40)
    mso_input_1.place(x=40, y=100)

    mso_label_2 = Label(window, text='Введите оценки с индексом «2»:', font=('Times New Roman', 12))
    mso_label_2.place(x=40, y=140)

    # Поле ввода оценок с индексом
    mso_input_2 = Entry(window, width=40)
    mso_input_2.place(x=40, y=180)
    ToolTip(mso_input_2, '5₂')

    mso_result_button = Button(window, text='РАССЧИТАТЬ', width=19, height=2, bg='black', fg='white', command=mso_Done)
    mso_result_button.place(x=40, y=220)

    mso_label_3 = Label(window, text='Ваш средний балл: ', font=('Times New Roman', 16))
    mso_label_3.place(x=290, y=20)

    # Области вывода данных
    mso_label_4 = Label(window, font=('Times New Roman', 16))
    mso_label_4.place(x=310, y=60)

    mso_label_5 = Label(window, font=('Times New Roman', 16))
    mso_label_5.place(x=310, y=100)

    mso_label_6 = Label(window, font=('Times New Roman', 14))
    mso_label_6.place(x=310, y=140)

    mso_label_7 = Label(window, font=('Times New Roman', 14))
    mso_label_7.place(x=310, y=170)

    mso_label_8 = Label(window, font=('Times New Roman', 14))
    mso_label_8.place(x=333, y=170)

    mso_off = Button(window, text='⌂', font=('Arial Bold', 15), width=2, height=1, bg='black', fg='white',
                     command=mso_to_home)
    mso_off.place(x=0, y=5)
    ToolTip(mso_off, 'На главную...')


def SML():
    """
    Интерпретатор простейшего самодельного
    языка программирования
    Подробнее - https://mihasoft.glitch.me
    """
    sml = SMLGlobals()

    def sml_to_home():
        """
        Возвращение на главную страницу MihaSoft
        """
        try:
            sml.example_window.destroy()
        except AttributeError:
            pass

        try:
            sml.help_window.destroy()
        except AttributeError:
            pass

        try:
            sml.open_window.destroy()
        except AttributeError:
            pass

        try:
            sml.save_window.destroy()
        except AttributeError:
            pass

        try:
            sml.delete_window.destroy()
        except AttributeError:
            pass

        try:
            sml.run_window.destroy()
        except AttributeError:
            pass

        sml_error_1.destroy()
        sml_error_2.destroy()
        sml_error_3.destroy()
        sml_error_4.destroy()
        sml_error_5.destroy()
        sml_error_6.destroy()
        sml_title.destroy()
        sml_begin_button.destroy()
        sml_open_button.destroy()
        sml_save_button.destroy()
        sml_delete_button.destroy()
        sml_help_button.destroy()
        sml_off.destroy()
        sml_code_input.destroy()
        home()
        window.configure(width=700, height=m.abs_height)
        center_window(root, 678, m.abs_height)

    def sml_Help():
        """
        Функция вывода справочной информации
        """

        def sml_Help_Example():
            """
            Пример работы SML-программы
            """

            def sml_create_example_window():
                sml.example_window = Toplevel()
                sml.example_window.title('miha')
                center_window(sml.example_window, 200, 100)
                sml.example_window.resizable(False, False)
                sml_example_label = Label(sml.example_window, text='5 + 5 = 10')
                sml_example_label.place(x=10, y=30)

            try:
                sml.example_window.resizable(False, False)

            except AttributeError:
                sml_create_example_window()

            except TclError:
                sml_create_example_window()

        def sml_Help_Exit():
            """
            Закрытие окна справки
            """
            sml.help_window.destroy()

            try:
                sml.example_window.destroy()
            except AttributeError:
                pass

        def sml_create_help_window():
            sml.help_window = Toplevel()
            sml.help_window.title('Справка')
            center_window(sml.help_window, 1200, 540)
            sml.help_window.resizable(False, False)

            sml_help_field = Text(sml.help_window, width=145, height=28, font=('Times New Roman', 12))
            sml_help_field.place(x=5, y=5)

            sml_help_text = '''
            The Simplest Mihail’s Language
               _____________
            1 строка - название программы: program <name>;
               _____________
            2 строка - объявление типа: using input; (вводить числа с клавиатуры) или using const; (конкретные числа)  
               _____________
            3 строка - если using input;: method=x;, где x это с (сложение), в (вычитание), у (умножение), д (деление), 
            ц (целочисленное деление), д (деление с остатком)  
                       если using const;: const1=x;, где x - первое значение  
               _____________  
            4 строка - если using input;: окончание программы: end;  
                       если using const;: const2=y, где y - второе значение
               _____________  
            5 строка - если using const;: method=x;, где x это с (сложение), в (вычитание), у (умножение), д (деление), 
            ц (целочисленное деление), д (деление с остатком)  
               _____________  
            6 строка - если using const;: окончание программы: end;

            ПРИМЕР:  
              program miha;
              using const;
              const1=5;
              const2=5;
              method=с;
              end;  
            '''
            sml_help_field.insert(1.0, sml_help_text)
            sml_help_field.configure(state='disabled')

            sml_show_example_button = Button(sml.help_window, text='ВЫПОЛНИТЬ', bg='white', command=sml_Help_Example)
            sml_show_example_button.place(x=153, y=450)

            sml_exit_help_button = Button(sml.help_window, text='ЗАКРЫТЬ', bg='#e6bebe', command=sml_Help_Exit)
            sml_exit_help_button.place(x=1000, y=450)

        try:
            sml.help_window.resizable(False, False)

        except AttributeError:
            sml_create_help_window()

        except TclError:
            sml_create_help_window()

    def sml_Begin():
        """
        Функция выполнения SML-программы
        """
        try:
            sml.run_window.destroy()
        except AttributeError:
            pass

        # Очистка сообщений об ошибках
        sml_error_1.configure(text='')
        sml_error_2.configure(text='')
        sml_error_3.configure(text='')
        sml_error_4.configure(text='')
        sml_error_5.configure(text='')
        sml_error_6.configure(text='')

        def ex():
            """
            Функция выполнения программы при
            использовании метода input
            """
            # Получения введённых значений
            sml_args_1 = int(sml_run_input_1.get())
            sml_args_2 = int(sml_run_input_2.get())

            # Выполнение выбранной пользователем операции
            if sml.flag_1 == '+':
                sml.run_result = sml_args_1 + sml_args_2
            elif sml.flag_1 == '-':
                sml.run_result = sml_args_1 - sml_args_2
            elif sml.flag_1 == '*':
                sml.run_result = sml_args_1 * sml_args_2
            elif sml.flag_1 == '/':
                sml.run_result = sml_args_1 / sml_args_2
            elif sml.flag_1 == '//':
                sml.run_result = sml_args_1 // sml_args_2
            elif sml.flag_1 == '%':
                sml.run_result = sml_args_1 % sml_args_2

            sml_run_result_label.configure(text=sml.run_result)

        # Построчный разбор строчек введённого кода
        # и вывод потенциальных сообщений об ошибках
        if sml_code_input.get('1.0', '1.7') != 'program' or ';' not in sml_code_input.get('1.0', '1.50'):
            sml_error_1.configure(text='Ошибка: линия 1')
        else:
            # 1 вариант работы программы: арифметические операции
            # с конкретными числами
            if (sml_code_input.get('2.0', '2.12') != 'using const;') and (
                    sml_code_input.get('2.0', '2.12') != 'using input;'):
                sml_error_2.configure(text='Ошибка: линия 2')
            else:
                if sml_code_input.get('2.0', '2.12') == 'using const;':
                    if sml_code_input.get('3.0', '3.7') != 'const1=':
                        sml_error_3.configure(text='Ошибка: линия 3')
                    else:
                        if sml_code_input.get('4.0', '4.7') != 'const2=':
                            sml_error_4.configure(text='Ошибка: линия 4')
                        else:

                            sml_arg_1 = sml_code_input.get('3.7', '3.20')
                            sml_arg_2 = sml_code_input.get('4.7', '4.20')
                            sml_arg_1 = sml_arg_1.replace('const1=', '')
                            sml_arg_1 = int(sml_arg_1.replace(';', ''))
                            sml_arg_2 = sml_arg_2.replace('const2=', '')
                            sml_arg_2 = int(sml_arg_2.replace(';', ''))

                            if sml_code_input.get('5.0', '5.7') != 'method=':
                                sml_error_5.configure(text='Ошибка: линия 5')
                            else:
                                if sml_code_input.get('5.7') == 'с':
                                    sml.flag = '+'
                                elif sml_code_input.get('5.7') == 'в':
                                    sml.flag = '-'
                                elif sml_code_input.get('5.7') == 'у':
                                    sml.flag = '*'
                                elif sml_code_input.get('5.7') == "д":
                                    sml.flag = '/'
                                elif sml_code_input.get('5.7') == 'ц':
                                    sml.flag = '//'
                                elif sml_code_input.get('5.7') == 'о':
                                    sml.flag = '%'
                                if sml_code_input.get('6.0', '6.4') != 'end;':
                                    sml_error_6.configure(text='Ошибка: линия 6')
                                else:
                                    sml.run_window = Toplevel()
                                    sml.run_window.title(
                                        sml_code_input.get('1.0', '1.50').replace('program ', '').replace(';', ''))
                                    center_window(sml.run_window, 200, 100)
                                    sml.run_window.resizable(False, False)

                                    if sml.flag == '+':
                                        sml.run_result = sml_arg_1 + sml_arg_2
                                    elif sml.flag == '-':
                                        sml.run_result = sml_arg_1 - sml_arg_2
                                    elif sml.flag == '*':
                                        sml.run_result = sml_arg_1 * sml_arg_2
                                    elif sml.flag == '/':
                                        sml.run_result = sml_arg_1 / sml_arg_2
                                    elif sml.flag == '//':
                                        sml.run_result = sml_arg_1 // sml_arg_2
                                    elif sml.flag == '%':
                                        sml.run_result = sml_arg_1 % sml_arg_2

                                    sml_run_label = Label(sml.run_window,
                                                          text='{} {} {} = {}'.format(str(sml_arg_1), str(sml.flag),
                                                                                      str(sml_arg_2),
                                                                                      str(sml.run_result)))
                                    sml_run_label.place(x=10, y=30)

                # 2 вариант: арифметические операции с произвольными числами
                elif sml_code_input.get('2.0', '2.12') == 'using input;':
                    if sml_code_input.get('3.0', '3.7') != 'method=':
                        sml_error_3.configure(text='Ошибка: линия 3')
                    else:
                        if sml_code_input.get('4.0', '4.4') != 'end;':
                            sml_error_4.configure(text='Ошибка: линия 4')
                        else:
                            if sml_code_input.get('3.7') == 'с':
                                sml.flag_1 = '+'
                            elif sml_code_input.get('3.7') == 'в':
                                sml.flag_1 = '-'
                            elif sml_code_input.get('3.7') == 'у':
                                sml.flag_1 = '*'
                            elif sml_code_input.get('3.7') == 'д':
                                sml.flag_1 = '/'
                            elif sml_code_input.get('3.7') == 'ц':
                                sml.flag_1 = '//'
                            elif sml_code_input.get('3.7') == 'о':
                                sml.flag_1 = '%'
                            sml.run_window = Toplevel()
                            sml.run_window.title(
                                sml_code_input.get('1.0', '1.50').replace('program ', '').replace(';', ''))
                            center_window(sml.run_window, 200, 130)
                            sml.run_window.resizable(False, False)

                            sml_run_input_1 = Entry(sml.run_window, width=10)
                            sml_run_input_1.place(x=10, y=30)

                            sml_run_arg = Label(sml.run_window, text=sml.flag_1)
                            sml_run_arg.place(x=85, y=30)

                            sml_run_input_2 = Entry(sml.run_window, width=10)
                            sml_run_input_2.place(x=100, y=30)

                            sml_run_label = Label(sml.run_window, text='=')
                            sml_run_label.place(x=170, y=30)

                            sml_run_result_label = Label(sml.run_window)
                            sml_run_result_label.place(x=10, y=60)

                            sml_run_button = Button(sml.run_window, text='ВЫПОЛНИТЬ', command=ex)
                            sml_run_button.place(x=10, y=90)

    def sml_Save():
        """
        Функция сохранения исходного кода программ
        в файл
        """

        def sml_Save_Abort():
            """
            Отмена сохранения
            """
            sml.save_window.destroy()

        def sml_create_save_window():
            def sml_Save_OK():
                """
                Считывание введённого имени файла
                и его сохранение
                """
                sml_text_file = open('MihaSoft Files/SML Files/' + str(sml_save_input.get()) + '.miha', "w")
                sml_text_file.write(sml_code_input.get(1.0, END))
                sml_text_file.close()
                sml.save_window.destroy()

            sml.save_window = Toplevel()
            sml.save_window.title('Сохранение')
            center_window(sml.save_window, 350, 100)
            sml.save_window.resizable(False, False)

            sml_save_label = Label(sml.save_window, text='Введите название программы...')
            sml_save_label.place(x=5, y=5)

            # Поле ввода названия программы
            sml_save_input = Entry(sml.save_window, width=30)
            sml_save_input.place(x=10, y=40)

            sml_save_input.insert(0, sml_code_input.get('1.0', '1.50').replace('program ', '').replace(';', ''))

            sml_save_ok_button = Button(sml.save_window, text='Сохранить', bg='#c0ebd6', command=sml_Save_OK, width=10)
            sml_save_ok_button.place(x=225, y=10)

            sml_save_abort_button = Button(sml.save_window, text='Отмена', bg='#b8b8b8', command=sml_Save_Abort,
                                           width=10)
            sml_save_abort_button.place(x=225, y=50)

        try:
            sml.save_window.resizable(False, False)

        except AttributeError:
            sml_create_save_window()

        except TclError:
            sml_create_save_window()

    def sml_Open():
        """
        Функция подстановки сохранённого кода
        в поле ввода
        """

        def sml_Open_Abort():
            """
            Отмена подстановки
            """
            sml.open_window.destroy()

        def sml_create_open_window():
            def sml_Open_OK():
                """
                Открытие файла и подстановка кода
                """
                sml_text_file = open('MihaSoft Files/SML Files/' + str(sml_open_combobox.get()), "r")
                sml_code_input.delete(1.0, END)
                sml_code_input.insert(END, sml_text_file.read())
                sml_text_file.close()
                sml.open_window.destroy()

            sml.open_window = Toplevel()
            sml.open_window.title('Открыть')
            center_window(sml.open_window, 350, 120)
            sml.open_window.resizable(False, False)

            sml_open_label = Label(sml.open_window, text='Выберите файл...')
            sml_open_label.place(x=5, y=5)

            # Список существующих файлов
            sml_open_combobox = ttk.Combobox(sml.open_window, values=os.listdir('MihaSoft Files/SML Files'),
                                             font=('Arial Bold', 16), width=20, state='readonly')
            sml_open_combobox.place(x=10, y=40)

            sml_open_ok_button = Button(sml.open_window, text='Открыть', bg='#c0ebd6', command=sml_Open_OK, width=10)
            sml_open_ok_button.place(x=225, y=80)

            sml_open_abort_button = Button(sml.open_window, text='Отмена', bg='#b8b8b8', command=sml_Open_Abort,
                                           width=10)
            sml_open_abort_button.place(x=135, y=80)

        try:
            sml.open_window.resizable(False, False)

        except AttributeError:
            sml_create_open_window()

        except TclError:
            sml_create_open_window()

    def sml_Delete():
        """
        Функция удаления ранее сохранённого кода
        """

        def sml_Delete_Abort():
            """
            Отмена удаления
            """
            sml.delete_window.destroy()

        def sml_create_del_window():
            def sml_Delete_OK():
                """
                Удаление выбранного файла
                """
                os.remove('MihaSoft Files/SML Files/' + str(sml_delete_combobox.get()))
                sml.delete_window.destroy()

            sml.delete_window = Toplevel()
            sml.delete_window.title('Удалить')
            center_window(sml.delete_window, 350, 120)
            sml.delete_window.resizable(False, False)

            sml_delete_label = Label(sml.delete_window, text='Выберите файл...')
            sml_delete_label.place(x=5, y=5)

            # Список существующих файлов
            sml_delete_combobox = ttk.Combobox(sml.delete_window, values=os.listdir('MihaSoft Files/SML Files'),
                                               font=('Arial Bold', 16), width=20, state='readonly')
            sml_delete_combobox.place(x=10, y=40)

            sml_delete_ok_button = Button(sml.delete_window, text='Удалить', bg='#eb9898', command=sml_Delete_OK,
                                          width=10)
            sml_delete_ok_button.place(x=225, y=80)

            sml_delete_abort_button = Button(sml.delete_window, text='Отмена', bg='#b8b8b8', command=sml_Delete_Abort,
                                             width=10)
            sml_delete_abort_button.place(x=135, y=80)

        try:
            sml.delete_window.resizable(False, False)

        except AttributeError:
            sml_create_del_window()

        except TclError:
            sml_create_del_window()

    # Создание папки для файлов SML в случае отсутствия таковой
    if not os.path.exists('MihaSoft Files/SML Files'):
        os.mkdir('MihaSoft Files/SML Files')

    center_window(root, 830, 320)
    window.configure(width=830, height=320)
    root.title('The Simplest Mihail’s Language - IDE & Interpreter')
    root.minsize(830, 320)

    sml_title = Label(window, text='The Simplest Mihail’s Language - IDE & Interpreter', font=('Arial Bold', 24),
                      fg='red')
    sml_title.place(x=35, y=15)

    sml_help_button = Button(window, text='Справка', bg='red', fg="white", command=sml_Help)
    sml_help_button.place(x=15, y=70)

    # Поле ввода исходного кода
    sml_code_input = Text(window, width=75, height=12)
    sml_code_input.place(x=15, y=110)
    ToolTip(sml_code_input, 'Ваш код...')

    sml_begin_button = Button(window, text='ВЫПОЛНИТЬ', bg='green', fg='white', width=15, command=sml_Begin)
    sml_begin_button.place(x=90, y=70)
    ToolTip(sml_begin_button, 'Запустить программу...')

    sml_save_button = Button(window, text='СОХРАНИТЬ', bg='yellow', width=15, command=sml_Save)
    sml_save_button.place(x=220, y=70)
    ToolTip(sml_save_button, 'Сохранить введённый код...')

    sml_open_button = Button(window, text='ОТКРЫТЬ', bg='grey', width=15, command=sml_Open)
    sml_open_button.place(x=350, y=70)
    ToolTip(sml_open_button, 'Подставить сохранённый код...')

    sml_delete_button = Button(window, text='УДАЛИТЬ', bg='#eb9898', width=15, command=sml_Delete)
    sml_delete_button.place(x=480, y=70)
    ToolTip(sml_delete_button, 'Удалить сохранённый код...')

    # Область вывода сообщений об ошибках на соответствующих строках
    sml_error_1 = Label(window, fg='red')
    sml_error_1.place(x=640, y=110)

    sml_error_2 = Label(window, fg='red')
    sml_error_2.place(x=640, y=140)

    sml_error_3 = Label(window, fg='red')
    sml_error_3.place(x=640, y=170)

    sml_error_4 = Label(window, fg='red')
    sml_error_4.place(x=640, y=200)

    sml_error_5 = Label(window, fg='red')
    sml_error_5.place(x=640, y=230)

    sml_error_6 = Label(window, fg='red')
    sml_error_6.place(x=640, y=260)

    sml_off = Button(window, text='⌂', font=('Arial Bold', 15), width=2, height=1, bg='black', fg='white',
                     command=sml_to_home)
    sml_off.place(x=0, y=5)
    ToolTip(sml_off, 'На главную...')


def NumberSystems():
    ns = NSGlobals()

    def tns_to_home():
        home()
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
        window.configure(width=700, height=m.abs_height)
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
    window.configure(width=620, height=430)
    root.title('NumberSystems')
    root.minsize(620, 430)

    tns_title = Label(window, text='NumberSystems', font=('Arial Bold', 15), fg='red')
    tns_title.place(x=40, y=20)

    tns_label_1 = Label(window, text='Введите значение:')
    tns_label_1.place(x=20, y=300)

    tns_label_2 = Label(window, text='ИЗ')
    tns_label_2.place(x=20, y=80)

    tns_label_3 = Label(window, text='В')
    tns_label_3.place(x=20, y=190)

    ns_input = Entry(window, width=24, font=('Arial Bold', 15))
    ns_input.place(x=20, y=320)

    tns_re_button = Button(window, text='Перевести', bg='white', fg='black', width=15, command=tns_Begin)
    tns_re_button.place(x=340, y=100)

    tns_clean_button = Button(window, text='Копировать', bg='red', fg='white', width=15, command=tns_copy)
    tns_clean_button.place(x=470, y=100)

    tns_from_combobox = Entry(window, font=('Arial Bold', 16), width=21)
    tns_from_combobox.place(x=20, y=100)

    tns_to_combobox = Entry(window, font=('Arial Bold', 16), width=21)
    tns_to_combobox.place(x=20, y=210)

    tns_output = Text(window, width=30, height=13, state=DISABLED)
    tns_output.place(x=340, y=130)

    tns_off = Button(window, text='⌂', font=('Arial Bold', 15), width=2, height=1, bg='black', fg='white',
                     command=tns_to_home)
    tns_off.place(x=0, y=0)
    ToolTip(tns_off, 'На главную...')


def CrossZero():
    """
    Игра "Крестики-нолики"
    """
    # Создание объекта с глобальными переменными
    cz = CrossZeroGlobals()

    def cz_to_home():
        try:
            cz.parametrs_window.destroy()
        except AttributeError:
            pass

        try:
            cz.rng_window.destroy()
        except AttributeError:
            pass

        try:
            cz.report_window.destroy()
        except AttributeError:
            pass

        try:
            cz.open_window.destroy()
        except AttributeError:
            pass

        try:
            cz.delete_window.destroy()
        except AttributeError:
            pass

        cz_title.destroy()
        cz_name_of_winner_label.destroy()
        cz_numb_of_moves_label.destroy()
        cz_info_label.destroy()
        cz_game_condition_label.destroy()
        cz_save_button.destroy()
        cz_open_button.destroy()
        cz_delete_button.destroy()
        cz_new_game_button.destroy()
        cz_parametrs_button.destroy()
        cz_box_1.destroy()
        cz_box_2.destroy()
        cz_box_3.destroy()
        cz_box_4.destroy()
        cz_box_5.destroy()
        cz_box_6.destroy()
        cz_box_7.destroy()
        cz_box_8.destroy()
        cz_box_9.destroy()
        cz_off.destroy()
        home()
        window.configure(width=700, height=m.abs_height)
        center_window(root, 678, m.abs_height)

    def cz_parametrs():
        """
        Функция определения имён игроков
        """

        def cz_close_parametrs():
            """
            Закрытие окна без сохранения параметров
            """
            cz.parametrs_window.destroy()

        def cz_create_par_window():
            def cz_save_parametrs():
                """
                Функция сохранения выбранных параметров
                """
                cz.player_1 = str(cz_parametrs_input_1.get())
                cz.player_2 = str(cz_parametrs_input_2.get())
                cz.naming_condition = 1
                cz.parametrs_window.destroy()

            cz.parametrs_window = Toplevel()
            cz.parametrs_window.title('Параметры')
            center_window(cz.parametrs_window, 300, 110)
            cz.parametrs_window.resizable(False, False)

            cz_parametrs_label_1 = Label(cz.parametrs_window, text='Имя первого игрока:')
            cz_parametrs_label_1.place(x=5, y=5)

            # Поле ввода имени первого игрока (крестик)
            cz_parametrs_input_1 = Entry(cz.parametrs_window, width=17)
            cz_parametrs_input_1.place(x=130, y=5)

            cz_parametrs_label_2 = Label(cz.parametrs_window, text='Имя второго игрока:')
            cz_parametrs_label_2.place(x=5, y=40)

            # Поле ввода имени второго игрока (нолик)
            cz_parametrs_input_2 = Entry(cz.parametrs_window, width=17)
            cz_parametrs_input_2.place(x=130, y=40)

            cz_parametrs_save_button = Button(cz.parametrs_window, text='ОК', bg='#c0ebd6', width=10,
                                              command=cz_save_parametrs)
            cz_parametrs_save_button.place(x=180, y=70)

            cz_close_button = Button(cz.parametrs_window, text='Отмена', bg='#b8b8b8', width=10,
                                     command=cz_close_parametrs)
            cz_close_button.place(x=80, y=70)

        try:
            cz.parametrs_window.resizable(False, False)

        except AttributeError:
            cz_create_par_window()

        except TclError:
            cz_create_par_window()

    def cz_new_game():
        """
        Функция сброса параметров текущей игры
        и начало новой
        """
        try:
            cz.rng_window.destroy()
        except AttributeError:
            pass

        # Счётчик количества ходов
        cz.number_of_moves = 0

        # Переменная, отмечающая ход игры или её завершение
        cz.game_condition = True

        # Переменная, отмечающая наличие ничьи или победы одного из игроков
        cz.game_res_condition = False
        cz_numb_of_moves_label.configure(text='1')
        cz_info_label.configure(text='  ход')
        cz_box_1.configure(text='')
        cz_box_2.configure(text='')
        cz_box_3.configure(text='')
        cz_box_4.configure(text='')
        cz_box_5.configure(text='')
        cz_box_6.configure(text='')
        cz_box_7.configure(text='')
        cz_box_8.configure(text='')
        cz_box_9.configure(text='')
        cz_game_condition_label.configure(text='')
        cz_name_of_winner_label.configure(text='')

        # Переменные, регулирующие состояние каждой клетки игрового поля
        cz.flag_1 = 3
        cz.flag_2 = 3
        cz.flag_3 = 3
        cz.flag_4 = 3
        cz.flag_5 = 3
        cz.flag_6 = 3
        cz.flag_7 = 3
        cz.flag_8 = 3
        cz.flag_9 = 3

    def cz_check_gameover():
        """
        Функция, проверяющая при каждом нажатии на клетку поля
        наличие ситуации, знаменующей завершение игры
        """

        def cz_cg_to_zero():
            cz.flag_1 = cz.flag_2 = cz.flag_3 = cz.flag_4 = cz.flag_5 = cz.flag_6 = cz.flag_7 = cz.flag_8 = \
                cz.flag_9 = 0

        def cz_req_new_game():
            def cz_rng_yes():
                cz_new_game()
                cz.rng_window.destroy()

            def cz_rng_no():
                cz.rng_window.destroy()

            if os.path.exists('MihaSoft Files/CzReportFlag.miha'):
                cz_save_report()

            cz.rng_window = Toplevel()
            cz.rng_window.title('Новая игра')
            center_window(cz.rng_window, 200, 100)
            cz.rng_window.resizable(False, False)

            cz_rng_label = Label(cz.rng_window, text='Начать новую игру?')
            cz_rng_label.place(x=5, y=5)

            cz_rng_yes_button = Button(cz.rng_window, text='ДА', bg='#c0ebd6', width=10, command=cz_rng_yes)
            cz_rng_yes_button.place(x=10, y=45)

            cz_rng_no_button = Button(cz.rng_window, text='НЕТ', bg='#ebc0d0', width=10, command=cz_rng_no)
            cz_rng_no_button.place(x=110, y=45)

        cz_numb_of_moves_label.configure(text=cz.number_of_moves + 2)
        if os.path.exists('MihaSoft Files/SoundFlagFile.miha'):
            Beep(200, 50)
        # cz.flag = 1 : крестик; cz.flag = 0 : нолик
        if ((cz.flag_1 == 1 and cz.flag_2 == 1 and cz.flag_3 == 1) or (
                cz.flag_4 == 1 and cz.flag_5 == 1 and cz.flag_6 == 1) or (
                cz.flag_7 == 1 and cz.flag_8 == 1 and cz.flag_9 == 1) or (
                cz.flag_1 == 1 and cz.flag_4 == 1 and cz.flag_7 == 1) or (
                cz.flag_2 == 1 and cz.flag_5 == 1 and cz.flag_8 == 1) or (
                cz.flag_3 == 1 and cz.flag_6 == 1 and cz.flag_9 == 1) or (
                cz.flag_1 == 1 and cz.flag_5 == 1 and cz.flag_9 == 1) or (
                cz.flag_3 == 1 and cz.flag_5 == 1 and cz.flag_7 == 1)):
            cz_cg_to_zero()
            cz.game_condition = False
            cz.game_res_condition = False
            cz_game_condition_label.configure(text='Победил(а)')
            cz.condition = 1
            if cz.naming_condition == 0:
                cz_name_of_winner_label.configure(text='Игрок 1')
            else:
                cz_name_of_winner_label.configure(text=cz.player_1)
            cz_numb_of_moves_label.configure(text=cz.number_of_moves + 1)
            cz_info_label.configure(text='  ходов')
            cz_req_new_game()
            cz.winner = cz.player_1
            if os.path.exists('MihaSoft Files/SoundFlagFile.miha'):
                Beep(50, 200)
                Beep(100, 400)
                Beep(200, 800)
        elif ((cz.flag_1 == 0 and cz.flag_2 == 0 and cz.flag_3 == 0) or (
                cz.flag_4 == 0 and cz.flag_5 == 0 and cz.flag_6 == 0) or (
                      cz.flag_7 == 0 and cz.flag_8 == 0 and cz.flag_9 == 0) or (
                      cz.flag_1 == 0 and cz.flag_4 == 0 and cz.flag_7 == 0) or (
                      cz.flag_2 == 0 and cz.flag_5 == 0 and cz.flag_8 == 0) or (
                      cz.flag_3 == 0 and cz.flag_6 == 0 and cz.flag_9 == 0) or (
                      cz.flag_1 == 0 and cz.flag_5 == 0 and cz.flag_9 == 0) or (
                      cz.flag_3 == 0 and cz.flag_5 == 0 and cz.flag_7 == 0)):
            cz_cg_to_zero()
            cz.game_condition = False
            cz.game_res_condition = False
            cz_game_condition_label.configure(text='Победил(а)')
            cz.condition = 2
            if cz.naming_condition == 0:
                cz_name_of_winner_label.configure(text='Игрок 2')
            else:
                cz_name_of_winner_label.configure(text=cz.player_2)
            cz_numb_of_moves_label.configure(text=cz.number_of_moves + 1)
            cz_info_label.configure(text='  ходов')
            cz_req_new_game()
            cz.winner = cz.player_2
            if os.path.exists('MihaSoft Files/SoundFlagFile.miha'):
                Beep(200, 200)
                Beep(100, 400)
                Beep(90, 800)
        # cz.flag = 3 : клетка не была нажата
        elif (cz.flag_1 != 3) and (cz.flag_2 != 3) and (cz.flag_3 != 3) and (cz.flag_4 != 3) and (
                cz.flag_5 != 3) and (cz.flag_6 != 3) and (cz.flag_7 != 3) and (cz.flag_8 != 3) and (
                cz.flag_9 != 3):
            cz_cg_to_zero()
            cz.condition = 4
            cz.game_condition = False
            cz.game_res_condition = True
            cz_game_condition_label.configure(text='НИЧЬЯ!')
            cz_req_new_game()
            if os.path.exists('MihaSoft Files/SoundFlagFile.miha'):
                Beep(1000, 800)

    # Функции нажатия для каждой клетки
    def cz_on_click_1():
        if cz.flag_1 != 1 and cz.flag_1 != 0:
            if cz.number_of_moves % 2 == 0:
                cz_box_1.configure(text='╳')
                cz.flag_1 = 1
            else:
                cz_box_1.configure(text='◯')
                cz.flag_1 = 0
            cz_check_gameover()
            cz.number_of_moves += 1

    def cz_on_click_2():
        if cz.flag_2 != 1 and cz.flag_2 != 0:
            if cz.number_of_moves % 2 == 0:
                cz_box_2.configure(text='╳')
                cz.flag_2 = 1
            else:
                cz_box_2.configure(text='◯')
                cz.flag_2 = 0
            cz_check_gameover()
            cz.number_of_moves += 1

    def cz_on_click_3():
        if cz.flag_3 != 1 and cz.flag_3 != 0:
            if cz.number_of_moves % 2 == 0:
                cz_box_3.configure(text='╳')
                cz.flag_3 = 1
            else:
                cz_box_3.configure(text='◯')
                cz.flag_3 = 0
            cz_check_gameover()
            cz.number_of_moves += 1

    def cz_on_click_4():
        if cz.flag_4 != 1 and cz.flag_4 != 0:
            if cz.number_of_moves % 2 == 0:
                cz_box_4.configure(text='╳')
                cz.flag_4 = 1
            else:
                cz_box_4.configure(text='◯')
                cz.flag_4 = 0
            cz_check_gameover()
            cz.number_of_moves += 1

    def cz_on_click_5():
        if cz.flag_5 != 1 and cz.flag_5 != 0:
            if cz.number_of_moves % 2 == 0:
                cz_box_5.configure(text='╳')
                cz.flag_5 = 1
            else:
                cz_box_5.configure(text='◯')
                cz.flag_5 = 0
            cz_check_gameover()
            cz.number_of_moves += 1

    def cz_on_click_6():
        if cz.flag_6 != 1 and cz.flag_6 != 0:
            if cz.number_of_moves % 2 == 0:
                cz_box_6.configure(text='╳')
                cz.flag_6 = 1
            else:
                cz_box_6.configure(text='◯')
                cz.flag_6 = 0
            cz_check_gameover()
            cz.number_of_moves += 1

    def cz_on_click_7():
        if cz.flag_7 != 1 and cz.flag_7 != 0:
            if cz.number_of_moves % 2 == 0:
                cz_box_7.configure(text='╳')
                cz.flag_7 = 1
            else:
                cz_box_7.configure(text='◯')
                cz.flag_7 = 0
            cz_check_gameover()
            cz.number_of_moves += 1

    def cz_on_click_8():
        if cz.flag_8 != 1 and cz.flag_8 != 0:
            if cz.number_of_moves % 2 == 0:
                cz_box_8.configure(text='╳')
                cz.flag_8 = 1
            else:
                cz_box_8.configure(text='◯')
                cz.flag_8 = 0
            cz_check_gameover()
            cz.number_of_moves += 1

    def cz_on_click_9():
        if cz.flag_9 != 1 and cz.flag_9 != 0:
            if cz.number_of_moves % 2 == 0:
                cz_box_9.configure(text='╳')
                cz.flag_9 = 1
            else:
                cz_box_9.configure(text='◯')
                cz.flag_9 = 0
            cz_check_gameover()
            cz.number_of_moves += 1

    def cz_save_report_set():
        if os.path.exists('MihaSoft Files/CzReportFlag.miha'):
            os.remove('MihaSoft Files/CzReportFlag.miha')
            cz_save_button.configure(text='Сохранять\n отчёты')
            messagebox.showinfo('ОК', 'Функция сохранения отчётов отключена.')
        else:
            cz_flag_file = open('MihaSoft Files/CzReportFlag.miha', 'w')
            cz_flag_file.close()
            cz_save_button.configure(text='Не сохранять\n отчёты')
            messagebox.showinfo('ОК', 'Функция сохранения отчётов включена.')

    def cz_save_report():

        """
        Функция сохранения отчёта об игре
        Создание строки отчёта и запись её в файл
        """
        if cz.condition == 1 or cz.condition == 2 or cz.condition == 4:
            if cz.condition == 1 and cz.naming_condition == 0:
                cz.name_of_winner_str = 'Игрок 1'
            elif cz.condition == 2 and cz.naming_condition == 0:
                cz.name_of_winner_str = 'Игрок 2'
            else:
                cz.name_of_winner_str = str(cz.winner)
        else:
            messagebox.showinfo('INFO', 'Нет завершённых игр!')

        cz_number_of_moves_str = str(cz.number_of_moves)

        if cz.game_res_condition:
            cz_save_string = 'Ничья ' + ' за ' + cz_number_of_moves_str + ' ходов. '
        else:
            cz_save_string = 'Победил ' + cz.name_of_winner_str + ' за ' + cz_number_of_moves_str + ' ходов. '

        cz_now = datetime.datetime.now()
        cz_text_file = open(
            'MihaSoft Files/CZ Files/Log_' + str(cz_now.strftime('%d-%m-%Y %H.%M.%S')) + '.miha', 'w')
        cz_text_file.write(cz_save_string)
        cz_text_file.close()

    def cz_open_report():
        """
        Функция вывода ранее сохранённого отчёта
        """

        def cz_open_abort():
            """
            Закрытие окна выбора отчёта
            """
            cz.open_window.destroy()

        try:
            cz.report_window.destroy()
        except AttributeError:
            pass

        def cz_create_open_window():
            def cz_open_ok():
                """
                Открытие выбранного отчёта в отдельном окне
                """

                def cz_close_report():
                    """
                    Функция закрытия окна с отчётом
                    """
                    cz.report_window.destroy()

                if cz_open_combobox.get():
                    cz_report_name = str(cz_open_combobox.get())
                    cz.open_window.destroy()

                    cz.report_window = Toplevel()
                    cz.report_window.title("Отчёт")
                    center_window(cz.report_window, 200, 100)
                    cz.report_window.resizable(False, False)

                    # Область вывода строки отчёта
                    cz_report = Label(cz.report_window, text="")
                    cz_report.place(x=5, y=5)

                    cz_report_close_button = Button(cz.report_window, text='OK', command=cz_close_report)
                    cz_report_close_button.place(x=15, y=35)

                    # Открытие файла с отчётом и вывод строки на экран
                    cz_report_file = open("MihaSoft Files/CZ Files/" + cz_report_name, "r")
                    cz_report.configure(text=str(cz_report_file.readline()))
                    cz_report_file.close()

            cz.open_window = Toplevel()
            cz.open_window.title('Открыть отчёт')
            center_window(cz.open_window, 385, 140)
            cz.open_window.resizable(False, False)

            cz_open_label = Label(cz.open_window, text='Выберите запись...')
            cz_open_label.place(x=5, y=5)

            # Список существующих отчётов
            cz_open_combobox = ttk.Combobox(cz.open_window, values=os.listdir('MihaSoft Files/CZ Files'),
                                            font=("Arial Bold", 16), width=27, state="readonly")
            cz_open_combobox.place(x=10, y=40)

            cz_open_ok_button = Button(cz.open_window, text='Открыть', bg='#c0ebd6', width=10, command=cz_open_ok)
            cz_open_ok_button.place(x=280, y=90)

            cz_open_abort_button = Button(cz.open_window, text='Отмена', bg='#b8b8b8', width=10, command=cz_open_abort)
            cz_open_abort_button.place(x=170, y=90)

        try:
            cz.open_window.resizable(False, False)

        except AttributeError:
            cz_create_open_window()

        except TclError:
            cz_create_open_window()

    def cz_delete_report():
        """
        Функция удаления отчётов об играх
        """

        def cz_delete_abort():
            """
            Отмена удаления
            """
            cz.delete_window.destroy()

        def cz_create_del_window():
            def cz_delete_ok():
                """
                Удаление выбранного отчёта
                """
                os.remove('MihaSoft Files/CZ Files/' + str(cz_delete_combobox.get()))
                cz.delete_window.destroy()

            cz.delete_window = Toplevel()
            cz.delete_window.title('Удалить отчёт')
            center_window(cz.delete_window, 385, 140)
            cz.delete_window.resizable(False, False)

            cz_delete_label = Label(cz.delete_window, text='Выберите запись...')
            cz_delete_label.place(x=5, y=5)

            # Список существующих отчётов
            cz_delete_combobox = ttk.Combobox(cz.delete_window, values=os.listdir('MihaSoft Files/CZ Files'),
                                              font=('Arial Bold', 16), width=27, state='readonly')
            cz_delete_combobox.place(x=10, y=40)

            cz_delete_ok_button = Button(cz.delete_window, text='Удалить', bg='#eb9898', width=10, command=cz_delete_ok)
            cz_delete_ok_button.place(x=280, y=90)

            cz_delete_abort_button = Button(cz.delete_window, text='Отмена', bg='#b8b8b8', width=10,
                                            command=cz_delete_abort)
            cz_delete_abort_button.place(x=170, y=90)

        try:
            cz.delete_window.resizable(False, False)

        except AttributeError:
            cz_create_del_window()

        except TclError:
            cz_create_del_window()

    # Создание папки для отчётов в случае отсутствия таковой
    if not os.path.exists('MihaSoft Files/CZ Files'):
        os.mkdir('MihaSoft Files/CZ Files')

    center_window(root, 600, 440)
    window.configure(width=600, height=440)
    root.title('CrossZero 2.1')
    root.minsize(600, 440)

    cz_title = Label(window, text='CrossZero', font=('Times New Roman', 26), fg='red')
    cz_title.place(x=50, y=65)

    # Клетки
    cz_box_1 = Button(window, font=('Arial Black', 21), fg='red', bg='#b1d4e6', width=5, height=2,
                      command=cz_on_click_1)
    cz_box_1.place(x=250, y=80)

    cz_box_2 = Button(window, font=('Arial Black', 21), fg='red', bg='#b1d4e6', width=5, height=2,
                      command=cz_on_click_2)
    cz_box_2.place(x=360, y=80)

    cz_box_3 = Button(window, font=('Arial Black', 21), fg='red', bg='#b1d4e6', width=5, height=2,
                      command=cz_on_click_3)
    cz_box_3.place(x=470, y=80)

    cz_box_4 = Button(window, font=('Arial Black', 21), fg='red', bg='#b1d4e6', width=5, height=2,
                      command=cz_on_click_4)
    cz_box_4.place(x=250, y=195)

    cz_box_5 = Button(window, font=('Arial Black', 21), fg='red', bg='#b1d4e6', width=5, height=2,
                      command=cz_on_click_5)
    cz_box_5.place(x=360, y=195)

    cz_box_6 = Button(window, font=('Arial Black', 21), fg='red', bg='#b1d4e6', width=5, height=2,
                      command=cz_on_click_6)
    cz_box_6.place(x=470, y=195)

    cz_box_7 = Button(window, font=('Arial Black', 21), fg='red', bg='#b1d4e6', width=5, height=2,
                      command=cz_on_click_7)
    cz_box_7.place(x=250, y=310)

    cz_box_8 = Button(window, font=('Arial Black', 21), fg='red', bg='#b1d4e6', width=5, height=2,
                      command=cz_on_click_8)
    cz_box_8.place(x=360, y=310)

    cz_box_9 = Button(window, font=('Arial Black', 21), fg='red', bg='#b1d4e6', width=5, height=2,
                      command=cz_on_click_9)
    cz_box_9.place(x=470, y=310)

    cz_parametrs_button = Button(window, text='Параметры', font=('Times New Roman', 11), fg='blue', bg='#ddc0eb',
                                 command=cz_parametrs, width=10, height=2)
    cz_parametrs_button.place(x=50, y=10)
    ToolTip(cz_parametrs_button, 'Присвоить игрокам произвольные имена...')

    cz_new_game_button = Button(window, text='Новая игра', font=('Times New Roman', 11), fg='blue', bg='#c0ebcb',
                                command=cz_new_game, width=10, height=2)
    cz_new_game_button.place(x=160, y=10)
    ToolTip(cz_new_game_button, 'Обновить поле и начать новую игру...')

    if not os.path.exists('MihaSoft Files/CzReportFlag.miha'):
        cz_text = 'Сохранять\n отчёты'
    else:
        cz_text = 'Не сохранять\n отчёты'

    cz_save_button = Button(window, text=cz_text, font=('Times New Roman', 11), fg='blue', bg='#e0cf92',
                            command=cz_save_report_set, width=10)
    cz_save_button.place(x=270, y=10)
    ToolTip(cz_save_button, 'Сохранить отчёт о последней игре...')

    cz_open_button = Button(window, text='Открыть\n отчёт', font=('Times New Roman', 11), fg='blue', bg='#87e6ad',
                            command=cz_open_report, width=10)
    cz_open_button.place(x=380, y=10)
    ToolTip(cz_open_button, 'Открыть отчёт в новом окне...')

    cz_delete_button = Button(window, text='Удалить\n отчёт', font=('Times New Roman', 11), fg='blue', bg='#eb9898',
                              command=cz_delete_report, width=10)
    cz_delete_button.place(x=490, y=10)
    ToolTip(cz_delete_button, 'Удалить существующий отчёт...')

    # Строки вывода информации о результате игры
    cz_game_condition_label = Label(window, font=('Times New Roman', 20), fg='blue')
    cz_game_condition_label.place(x=50, y=180)

    cz_name_of_winner_label = Label(window, font=('Times New Roman', 20), fg='blue')
    cz_name_of_winner_label.place(x=50, y=240)

    cz_numb_of_moves_label = Label(window, text='1', font=('Times New Roman', 20), fg='blue')
    cz_numb_of_moves_label.place(x=50, y=120)

    cz_info_label = Label(window, text='ХОД', font=('Times New Roman', 20), fg='blue')
    cz_info_label.place(x=90, y=120)

    cz_off = Button(window, text='⌂', font=('Arial Bold', 15), width=2, height=1, bg='black', fg='white',
                    command=cz_to_home)
    cz_off.place(x=0, y=5)
    ToolTip(cz_off, 'На главную...')


def MihNote():
    """
    Блокнот
    """
    # Создание объекта с глобальными переменными
    mn = MihNoteGlobals()

    def mn_to_home():
        """
        Возвращение на главную страницу MihaSoft
        """
        mn_title.destroy()
        mn_line.destroy()
        mn_new_note_button.destroy()
        mn_delete_button.destroy()
        mn_open_button.destroy()
        mn_edit_button.destroy()
        mn_note_ground.destroy()
        mn_off.destroy()

        # Удаление виджетов, появляющихся в процессе работы приложения
        # если они не были удалены до этого
        try:
            mn.open_combobox.destroy()
            mn.open_ok_button.destroy()
        except AttributeError:
            pass

        try:
            mn.delete_combobox.destroy()
            mn.delete_ask_button.destroy()
        except AttributeError:
            pass

        try:
            mn.edit_combobox.destroy()
            mn.edit_ok_button.destroy()
        except AttributeError:
            pass

        try:
            mn.edit_window.destroy()
        except AttributeError:
            pass

        try:
            mn.save_window.destroy()
        except AttributeError:
            pass

        try:
            mn.delete_window.destroy()
        except AttributeError:
            pass

        try:
            mn.new_note_window.destroy()
        except AttributeError:
            pass

        home()
        window.configure(width=700, height=m.abs_height)
        center_window(root, 678, m.abs_height)

    def mn_new_note():
        """
        Функция создания новой заметки
        """

        def mn_close_nn_window():
            """
            Отмена создания новой заметки
            """
            mn.new_note_window.destroy()

        def mn_create_nn_window():
            def mn_save_note():
                """
                Функция сохранения созданной заметки
                """

                def mn_save_note_abort():
                    """
                    Отмена сохранения
                    """
                    mn.save_window.destroy()

                def mn_create_save_window():
                    def mn_save_note_ok():
                        """
                        Подтверждение сохранения
                        """
                        mn_text_file = open('MihaSoft Files/MihNote Files/' + str(mn_save_input.get()) + '.miha',
                                            'w')
                        mn_text_file.write(mn_new_note_ground.get(1.0, END))
                        mn_text_file.close()
                        mn.save_window.destroy()
                        mn.new_note_window.destroy()

                    mn.save_window = Toplevel()
                    center_window(mn.save_window, 300, 100)
                    mn.save_window.resizable(False, False)
                    mn.save_window.title('Сохранение')

                    mn_save_label = Label(mn.save_window, text='Введите название файла:')
                    mn_save_label.place(x=5, y=5)

                    # Поле ввода названия заметки
                    mn_save_input = Entry(mn.save_window, width=20)
                    mn_save_input.place(x=10, y=35)

                    mn_save_label_1 = Label(mn.save_window, text='.miha')
                    mn_save_label_1.place(x=125, y=35)

                    mn_save_ok_button = Button(mn.save_window, text='Сохранить', font=('Arial Bold', 10), bg='#b2e6ae',
                                               width=13,
                                               command=mn_save_note_ok)
                    mn_save_ok_button.place(x=170, y=60)

                    mn_save_abort_button = Button(mn.save_window, text='Отмена', font=('Arial Bold', 10), bg='#b8b8b8',
                                                  width=13,
                                                  command=mn_save_note_abort)
                    mn_save_abort_button.place(x=170, y=20)

                try:
                    mn.save_window.resizable(False, False)

                except AttributeError:
                    mn_create_save_window()

                except TclError:
                    mn_create_save_window()

            mn.new_note_window = Toplevel()
            center_window(mn.new_note_window, 450, 310)
            mn.new_note_window.resizable(False, False)
            mn.new_note_window.title('Создание новой заметки')

            mn_nn_save_button = Button(mn.new_note_window, text='Сохранить', font=('Arial Bold', 12), bg='#b2e6ae',
                                       width=13,
                                       command=mn_save_note)
            mn_nn_save_button.place(x=15, y=5)

            # Поле ввода текста новой заметки
            mn_new_note_ground = Text(mn.new_note_window, width=50, height=15)
            mn_new_note_ground.place(x=15, y=50)

            mn_nn_close_button = Button(mn.new_note_window, text='Отмена', font=('Arial Bold', 12), bg='#b8b8b8',
                                        width=13,
                                        command=mn_close_nn_window)
            mn_nn_close_button.place(x=290, y=5)

        try:
            mn.new_note_window.resizable(False, False)

        except AttributeError:
            mn_create_nn_window()

        except TclError:
            mn_create_nn_window()

    def mn_open_note():
        """
        Функция открытия сохранённой заметки
        """
        # Очистка поля вывода заметки
        mn_note_ground.delete(1.0, END)

        def open_note_ok():
            """
            Подтверждение открытия
            """
            # Проверка наличия существующих заметок
            if os.listdir('MihaSoft Files/MihNote Files') and mn.open_combobox.get():
                mn_file_name = str(mn.open_combobox.get())
                # Удаление виджетов открытия
                mn.open_combobox.destroy()
                mn.open_ok_button.destroy()
                mn.open_flag = False
                mn_open_text_file = open('MihaSoft Files/MihNote Files/' + mn_file_name, 'r')
                mn_note_ground.configure(state='normal')
                mn_note_ground.delete(1.0, END)
                mn_note_ground.insert(1.0, str(mn_open_text_file.read()))
                mn_note_ground.configure(state='disabled')
                mn_open_text_file.close()

        if not mn.open_flag:

            if mn.del_flag:
                mn.delete_combobox.destroy()
                mn.delete_ask_button.destroy()
                mn.del_flag = False

            if mn.edit_flag:
                mn.edit_combobox.destroy()
                mn.edit_ok_button.destroy()
                mn.edit_flag = False

            # Список существующих заметок
            mn.open_flag = True
            mn.open_combobox = ttk.Combobox(window, values=os.listdir('MihaSoft Files/MihNote Files'),
                                            font=('Arial Bold', 16), state='readonly')
            mn.open_combobox.place(x=20, y=60)

            mn.open_ok_button = Button(window, text='Открыть', font=('Arial Bold', 10), bg='#7bd491', width=14,
                                       command=open_note_ok)
            mn.open_ok_button.place(x=300, y=60)

    def mn_delete_note():
        """
        Функция удаления существующей заметки
        """
        # Очистка поля вывода заметки
        mn_note_ground.delete(1.0, END)

        def mn_delete_ask():
            """
            Вывод окна с запросом
            о подтверждении удаления
            """
            # Проверка наличия существующих заметок
            if os.listdir('MihaSoft Files/MihNote Files') and mn.delete_combobox.get():
                def mn_delete_ok():
                    mn_delete_file_name = str(mn.delete_combobox.get())
                    # Удаление виджетов удаления
                    mn.delete_combobox.destroy()
                    mn.delete_ask_button.destroy()
                    mn.del_flag = False
                    os.remove('MihaSoft Files/MihNote Files/' + mn_delete_file_name)
                    mn.delete_window.destroy()

                def CloseDel():
                    """
                    Отмена удаления
                    """
                    mn.delete_window.destroy()

                def mn_create_del_window():
                    mn.delete_window = Toplevel()
                    center_window(mn.delete_window, 300, 100)
                    mn.delete_window.resizable(False, False)
                    mn.delete_window.title("Удаление")

                    mn_delete_label = Label(mn.delete_window, text="Удалить файл?")
                    mn_delete_label.place(x=5, y=5)

                    mn_delete_ok_button = Button(mn.delete_window, text="ОК", font=("Arial Bold", 10), fg="black",
                                                 bg='#c97979', width=13, command=mn_delete_ok)
                    mn_delete_ok_button.place(x=170, y=60)

                    mn_close_button = Button(mn.delete_window, text='Отмена', font=('Arial Bold', 10), bg='#b8b8b8',
                                             width=13,
                                             command=CloseDel)
                    mn_close_button.place(x=170, y=15)

                try:
                    mn.delete_window.resizable(False, False)

                except AttributeError:
                    mn_create_del_window()

                except TclError:
                    mn_create_del_window()

        # Список существующих заметок
        if not mn.del_flag:

            if mn.open_flag:
                mn.open_combobox.destroy()
                mn.open_ok_button.destroy()
                mn.open_flag = False

            if mn.edit_flag:
                mn.edit_combobox.destroy()
                mn.edit_ok_button.destroy()
                mn.edit_flag = False

            mn.del_flag = True

            mn.delete_combobox = ttk.Combobox(window, values=os.listdir('MihaSoft Files/MihNote Files'),
                                              font=('Arial Bold', 16), state='readonly')
            mn.delete_combobox.place(x=20, y=60)

            mn.delete_ask_button = Button(window, text='Удалить', font=('Arial Bold', 10), fg="black", bg='#c97979',
                                          width=14,
                                          command=mn_delete_ask)
            mn.delete_ask_button.place(x=300, y=60)

    def mn_edit_note():
        """
        Функция редактирования существующей заметки
        """
        mn_note_ground.delete(1.0, END)

        def mn_edit_ok():
            """
            Функция сохранения внесённых изменений
            """
            # Проверка наличия существующих заметок
            if os.listdir('MihaSoft Files/MihNote Files') and mn.edit_combobox.get():

                def mn_edit_abort():
                    """
                    Отмена сохранения изменений
                    """
                    mn.edit_window.destroy()

                def mn_create_edit_window():
                    def save_changes():
                        """
                        Подтверждение сохранения изменений
                        """
                        mn_edit_file = open('MihaSoft Files/MihNote Files/' + mn_edit_file_name, 'w')
                        mn_edit_file.write(mn_edit_ground.get(1.0, END))
                        mn_edit_file.close()
                        mn.edit_window.destroy()

                    mn_edit_file_name = str(mn.edit_combobox.get())
                    mn.edit_combobox.destroy()
                    mn.edit_ok_button.destroy()
                    mn.edit_flag = False

                    mn.edit_window = Toplevel()
                    center_window(mn.edit_window, 450, 310)
                    mn.edit_window.resizable(False, False)
                    mn.edit_window.title('Редактирование')

                    mn_sch_button = Button(mn.edit_window, text='Сохранить', font=('Arial Bold', 12), bg='#b2e6ae',
                                           width=13,
                                           command=save_changes)
                    mn_sch_button.place(x=15, y=5)

                    # Поле вывода текста для редактирования
                    mn_edit_ground = Text(mn.edit_window, width=50, height=15)
                    mn_edit_ground.place(x=15, y=50)

                    # Открытие выбранного файла и вывод текста заметки в поле редактирования
                    mn_edit_open_file = open('MihaSoft Files/MihNote Files/' + mn_edit_file_name, 'r')
                    mn_edit_ground.insert(END, mn_edit_open_file.read())
                    mn_edit_open_file.close()

                    mn_close_button = Button(mn.edit_window, text='Отмена', font=('Arial Bold', 12), bg='#b8b8b8',
                                             width=13,
                                             command=mn_edit_abort)
                    mn_close_button.place(x=290, y=5)

                try:
                    mn.edit_window.resizable(False, False)

                except AttributeError:
                    mn_create_edit_window()

                except TclError:
                    mn_create_edit_window()

        if not mn.edit_flag:

            if mn.del_flag:
                mn.delete_combobox.destroy()
                mn.delete_ask_button.destroy()
                mn.del_flag = False

            if mn.open_flag:
                mn.open_combobox.destroy()
                mn.open_ok_button.destroy()
                mn.open_flag = False

            # Список существующих заметок
            mn.edit_flag = True
            mn.edit_combobox = ttk.Combobox(window, values=os.listdir('MihaSoft Files/MihNote Files'),
                                            font=('Arial Bold', 16), state='readonly')
            mn.edit_combobox.place(x=20, y=60)

            mn.edit_ok_button = Button(window, text='Редактировать', font=('Arial Bold', 10), bg='#79a7c9', width=14,
                                       command=mn_edit_ok)
            mn.edit_ok_button.place(x=300, y=60)

    # Создание папки для заметок в случае отсутствия таковой
    if not os.path.exists('MihaSoft Files/MihNote Files'):
        os.mkdir('MihaSoft Files/MihNote Files')

    center_window(root, 810, 390)
    window.configure(width=810, height=390)
    root.title('MihNote 1.1')
    root.minsize(810, 390)

    mn_title = Label(window, text='MihNote 1.1', font=('Arial Bold', 16), fg='red')
    mn_title.place(x=80, y=10)

    mn_open_button = Button(window, text='Открыть', font=('Arial Bold', 12), bg='#e6aeae', width=13,
                            command=mn_open_note)
    mn_open_button.place(x=210, y=10)
    ToolTip(mn_open_button, 'Открыть файл...')

    mn_edit_button = Button(window, text='Редактировать', font=('Arial Bold', 12), bg='#aeb4e6', width=13,
                            command=mn_edit_note)
    mn_edit_button.place(x=350, y=10)
    ToolTip(mn_edit_button, 'Редактировать существующий файл...')

    mn_new_note_button = Button(window, text='Создать', font=('Arial Bold', 12), bg='#aee6c9', width=13,
                                command=mn_new_note)
    mn_new_note_button.place(x=490, y=10)
    ToolTip(mn_new_note_button, 'Создать новый файл...')

    mn_delete_button = Button(window, text='Удалить', font=('Arial Bold', 12), bg='#e6e2ae', width=13,
                              command=mn_delete_note)
    mn_delete_button.place(x=630, y=10)
    ToolTip(mn_delete_button, 'Удалить файл...')

    # Линия, ограждающая кнопок от области вывода заметок
    mn_line = Label(window,
                    text='_' * 154)
    mn_line.place(x=10, y=90)

    # Область вывода заметок
    mn_note_ground = Text(window, font=('Times New Roman', 14), width=80, height=12, state='disabled')
    mn_note_ground.place(x=35, y=120)

    mn_off = Button(window, text='⌂', font=('Arial Bold', 15), width=2, height=1, bg='black', fg="white",
                    command=mn_to_home)

    mn_off.place(x=0, y=5)
    ToolTip(mn_off, 'На главную...')


def WindowManager():
    """
    Приложения для создания и сохранение окон
    с надписями
    """
    # Создание объекта с глобальными переменными
    wm = WindowManagerGlobals()

    def wm_to_home():
        """
        Возвращение на главную страницу MihaSoft
        """
        try:
            wm.custom_window.destroy()
        except AttributeError:
            pass

        try:
            wm.open_window.destroy()
        except AttributeError:
            pass

        try:
            wm.save_window.destroy()
        except AttributeError:
            pass

        try:
            wm.edit_window.destroy()
        except AttributeError:
            pass

        try:
            wm.delete_window.destroy()
        except AttributeError:
            pass

        try:
            wm.font_window.destroy()
        except AttributeError:
            pass

        wm_title.destroy()
        wm_label_1.destroy()
        wm_label_2.destroy()
        wm_label_3.destroy()
        wm_label_4.destroy()
        wm_label_5.destroy()
        wm_label_6.destroy()
        wm_label_8.destroy()
        wm_label_9.destroy()
        wm_label_10.destroy()
        wm_label_11.destroy()
        wm_label_12.destroy()
        wm_label_13.destroy()
        wm_label_14.destroy()
        wm_width_input.destroy()
        wm_height_input.destroy()
        wm_x_cord_input.destroy()
        wm_y_cord_input.destroy()
        wm_cust_title_input.destroy()
        wm_text_x_input.destroy()
        wm_text_y_input.destroy()
        wm_font_ground.destroy()
        wm_fsize_input.destroy()
        wm_text_ground.destroy()
        wm_font_button.destroy()
        wm_demo_ground.destroy()
        wm_choose_button.destroy()
        wm_create_button.destroy()
        wm_save_button.destroy()
        wm_open_button.destroy()
        wm_clean_button.destroy()
        wm_delete_button.destroy()
        wm_edit_button.destroy()
        wm_off.destroy()
        home()
        window.configure(width=700, height=m.abs_height)
        center_window(root, 678, m.abs_height)

    def wm_read_data():
        """
        Функция считывания введённых параметров
        окна и запись их в переменные
        """
        wm.width = str(wm_width_input.get())
        wm.height = str(wm_height_input.get())
        wm.x_cord = str(wm_x_cord_input.get())
        wm.y_cord = str(wm_y_cord_input.get())
        wm.cust_title = str(wm_cust_title_input.get())
        wm.text = str(wm_text_ground.get('1.0', END))
        wm.font = str(wm_font_ground.get())
        wm.fsize = str(wm_fsize_input.get())
        wm.text_x = str(wm_text_x_input.get())
        wm.text_y = str(wm_text_y_input.get())

    def wm_choose_color():
        """
        Функция выбора цвета надписи
        """
        wm_colorchooser = colorchooser.askcolor()
        wm.color = str(wm_colorchooser[1])
        wm_demo_ground.configure(bg=str(wm.color))

    def wm_open_custom_window():
        """
        Функция открытия окна
        с введёнными параметрами
        """
        wm_read_data()

        # Проверка правильности заполнения полей с параметрами
        if (not wm.width.isdigit()) or (not wm.height.isdigit()) or (not wm.x_cord.isdigit()) or (
                not wm.y_cord.isdigit()) or (wm.cust_title == '') or (
                wm.text == '') or (wm.font == '') or (not wm.fsize.isdigit()) or (wm.color == '') or (
                not wm.text_x.isdigit()) or (
                not wm.text_y.isdigit()):
            messagebox.showwarning('INFO', 'Проверьте корректность введённых данных!')
        else:
            # Вывод окна на экран
            wm.custom_window = Toplevel()
            wm.custom_window.geometry(wm.width + 'x' + wm.height + '+' + wm.x_cord + '+' + wm.y_cord)
            wm.custom_window.title(wm.cust_title)

            wm.custom_label = Label(wm.custom_window, text=wm.text, font=(wm.font, wm.fsize), fg=wm.color)
            wm.custom_label.place(x=wm.text_x, y=wm.text_y)

    def wm_save():
        """
        Функция сохранения параметров
        окна в файл
        """

        def wm_save_changes():
            """
            Функция сохранения изменений в
            открытом для редактирования файла
            """
            save(wm.open_path,
                 [wm.width, wm.height, wm.x_cord, wm.y_cord, wm.cust_title, wm.text, wm.font, wm.fsize, wm.color,
                  wm.text_x, wm.text_y])
            wm.flag = True
            wm.save_window.destroy()

        def wm_save_abort():
            """
            Отмена сохранения
            """
            wm.save_window.destroy()

        wm_read_data()

        # Проверка значения переменной, отвечающей за состояние
        # приложения (создание нового файла или редактирование существующего)
        # и вызов соответствующего окна.

        # Проверка правильности заполнения полей с параметрами
        def wm_create_save_window():
            def wm_save_file():
                """
                Функция сохранения нового файла
                """
                save('MihaSoft Files/WM Files/' + str(wm_save_input.get()),
                     [wm.width, wm.height, wm.x_cord, wm.y_cord, wm.cust_title, wm.text, wm.font, wm.fsize, wm.color,
                      wm.text_x, wm.text_y])
                wm.save_window.destroy()

            if (not wm.width.isdigit()) or (not wm.height.isdigit()) or (not wm.x_cord.isdigit()) or (
                    not wm.y_cord.isdigit()) or (wm.cust_title == '') or (
                    wm.text == '') or (wm.font == '') or (not wm.fsize.isdigit()) or (wm.color == '') or (
                    not wm.text_x.isdigit()) or (
                    not wm.text_y.isdigit()):
                messagebox.showwarning('INFO', 'Проверьте корректность введённых данных!')
            else:
                if not wm.flag:
                    wm.save_window = Toplevel()
                    center_window(wm.save_window, 300, 100)
                    wm.save_window.resizable(False, False)
                    wm.save_window.title('Сохранение')

                    wm_save_label = Label(wm.save_window, text='Сохранить изменения?')
                    wm_save_label.place(x=5, y=5)

                    wm_save_ok_button = Button(wm.save_window, text='ОК', width=10, bg='#93e6a8',
                                               command=wm_save_changes)
                    wm_save_ok_button.place(x=200, y=43)

                    wm_close_button = Button(wm.save_window, text='Отмена', bg='#b8b8b8', width=10,
                                             command=wm_save_abort)
                    wm_close_button.place(x=100, y=43)

                else:
                    wm.save_window = Toplevel()
                    center_window(wm.save_window, 300, 100)
                    wm.save_window.resizable(False, False)
                    wm.save_window.title('Сохранение')

                    wm_save_label = Label(wm.save_window, text='Введите название файла...')
                    wm_save_label.place(x=5, y=5)

                    # Поле ввода названия нового файла
                    wm_save_input = Entry(wm.save_window, width=25)
                    wm_save_input.place(x=10, y=45)

                    wm_save_ok_button = Button(wm.save_window, text='Сохранить', width=10, bg='#93e6a8',
                                               command=wm_save_file)
                    wm_save_ok_button.place(x=200, y=53)

                    wm_save_close_button = Button(wm.save_window, text='Отмена', bg='#b8b8b8', width=10,
                                                  command=wm_save_abort)
                    wm_save_close_button.place(x=200, y=13)

        try:
            wm.save_window.resizable(False, False)

        except AttributeError:
            wm_create_save_window()

        except TclError:
            wm_create_save_window()

    def wm_edit():
        """
        Функция редактирования существующего файла
        (подстановка параметров из существующего файла
        в соответствующие поля
        """

        def wm_edit_abort():
            """
            Отмена редактирования
            """
            wm.edit_window.destroy()

        def wm_create_edit_window():
            def wm_edit_ok():
                """
                Функция вывода параметров в соответствующие поля
                из выбранного файла
                """
                wm_clean()
                wm_edit_path = str(wm_edit_combobox.get())
                wm_data_list = load('MihaSoft Files/WM Files/' + wm_edit_path)
                wm.open_path = 'MihaSoft Files/WM Files/' + wm_edit_path
                wm_width_input.insert(0, wm_data_list[0])
                wm_height_input.insert(0, wm_data_list[1])
                wm_x_cord_input.insert(0, wm_data_list[2])
                wm_y_cord_input.insert(0, wm_data_list[3])
                wm_cust_title_input.insert(0, wm_data_list[4])
                wm_text_ground.insert(1.0, wm_data_list[5])
                wm_font_ground.configure(state='normal')
                wm_font_ground.insert(0, wm_data_list[6])
                wm_fsize_input.insert(0, wm_data_list[7])
                wm_font_ground.configure(state='readonly')
                wm_demo_ground.configure(bg=wm_data_list[8])
                wm_text_x_input.insert(0, wm_data_list[9])
                wm_text_y_input.insert(0, wm_data_list[10])
                wm.flag = False
                wm.edit_window.destroy()

            wm.edit_window = Toplevel()
            center_window(wm.edit_window, 300, 100)
            wm.edit_window.resizable(False, False)
            wm.edit_window.title('Открыть')

            wm_edit_label = Label(wm.edit_window, text='Выберите файл...')
            wm_edit_label.place(x=5, y=5)

            # Список существующих файлов
            wm_edit_combobox = ttk.Combobox(wm.edit_window, values=os.listdir('MihaSoft Files/WM Files'),
                                            state='readonly')
            wm_edit_combobox.place(x=10, y=45)

            wm_edit_ok_button = Button(wm.edit_window, text='Редактировать', width=13, bg='#93e6a8', command=wm_edit_ok)
            wm_edit_ok_button.place(x=180, y=53)

            wm_edit_close_button = Button(wm.edit_window, text='Отмена', bg='#b8b8b8', width=13, command=wm_edit_abort)
            wm_edit_close_button.place(x=180, y=13)

        try:
            wm.edit_window.resizable(False, False)

        except AttributeError:
            wm_create_edit_window()

        except TclError:
            wm_create_edit_window()

    def wm_open():
        """
        Функция открытия окна по сохранённым
        ранее параметрам
        """

        def wm_open_abort():
            """
            Отмена открытия
            """
            wm.open_window.destroy()

        def wm_create_open_window():
            def wm_open_ok():
                """
                Открытие выбранного файла
                """
                wm_op_path = str(wm_open_combobox.get())
                wm_open_data_list = load('MihaSoft Files/WM Files/' + wm_op_path)

                wm.width = wm_open_data_list[0]
                wm.height = wm_open_data_list[1]
                wm.x_cord = wm_open_data_list[2]
                wm.y_cord = wm_open_data_list[3]
                wm.cust_title = wm_open_data_list[4]
                wm.text = wm_open_data_list[5]
                wm.font = wm_open_data_list[6]
                wm.fsize = wm_open_data_list[7]
                wm.color = wm_open_data_list[8]
                wm.text_x = wm_open_data_list[9]
                wm.text_y = wm_open_data_list[10]

                # Проверка корректности сохранённых параметров
                if (not wm.width.isdigit()) or (not wm.height.isdigit()) or (not wm.x_cord.isdigit()) or (
                        not wm.y_cord.isdigit()) or (wm.cust_title == '') or (
                        wm.text == '') or (wm.font == '') or (not wm.fsize.isdigit()) or (wm.color == '') or (
                        not wm.text_x.isdigit()) or (
                        not wm.text_y.isdigit()):
                    messagebox.showwarning('INFO', 'Проверьте корректность введённых данных!')
                else:
                    wm_open_cust_window = Toplevel()
                    wm_open_cust_window.geometry(wm.width + 'x' + wm.height + '+' + wm.x_cord + '+' + wm.y_cord)
                    wm_open_cust_window.title(wm.cust_title)
                    wm_open_cust_label = Label(wm_open_cust_window, text=wm.text, font=(wm.font, wm.fsize), fg=wm.color)
                    wm_open_cust_label.place(x=wm.text_x, y=wm.text_y)
                wm.open_window.destroy()

            wm.open_window = Toplevel()
            center_window(wm.open_window, 300, 100)
            wm.open_window.resizable(False, False)
            wm.open_window.title('Открыть')

            wm_open_label = Label(wm.open_window, text='Выберите файл...')
            wm_open_label.place(x=5, y=5)

            # Список существующих файлов
            wm_open_combobox = ttk.Combobox(wm.open_window, values=os.listdir('MihaSoft Files/WM Files'),
                                            state='readonly')
            wm_open_combobox.place(x=10, y=45)

            wm_open_ok_button = Button(wm.open_window, text='Открыть', width=10, bg='#93e6a8', command=wm_open_ok)
            wm_open_ok_button.place(x=200, y=53)

            wm_open_close_button = Button(wm.open_window, text='Отмена', bg='#b8b8b8', width=10, command=wm_open_abort)
            wm_open_close_button.place(x=200, y=13)

        try:
            wm.open_window.resizable(False, False)

        except AttributeError:
            wm_create_open_window()

        except TclError:
            wm_create_open_window()

    def wm_clean():
        """
        Функция очистки полей
        ввода параметров
        """
        wm_font_ground.configure(state='normal')
        wm_font_ground.delete(0, END)
        wm_font_ground.configure(state='readonly')
        wm_fsize_input.delete(0, END)
        wm_width_input.delete(0, 'end')
        wm_height_input.delete(0, 'end')
        wm_x_cord_input.delete(0, 'end')
        wm_y_cord_input.delete(0, 'end')
        wm_cust_title_input.delete(0, 'end')
        wm_text_x_input.delete(0, 'end')
        wm_text_y_input.delete(0, 'end')
        wm_text_ground.delete(1.0, END)
        wm_demo_ground.configure(bg='white')
        wm.flag = True

    def wm_delete():
        """
        Функция удаления ранее сохранённых файлов
        """

        def wm_delete_abort():
            """
            Отмена удаления
            """
            wm.delete_window.destroy()

        def wm_create_del_window():
            def wm_delete_ok():
                """
                Удаление выбранного файла
                """
                wm_delete_path = str(wm_delete_combobox.get())
                os.remove('MihaSoft Files/WM Files/' + wm_delete_path)
                wm.delete_window.destroy()

            wm.delete_window = Toplevel()
            center_window(wm.delete_window, 300, 100)
            wm.delete_window.resizable(False, False)
            wm.delete_window.title('Удалить')

            wm_delete_label = Label(wm.delete_window, text='Выберите файл...')
            wm_delete_label.place(x=5, y=5)

            # Список существующих файлов
            wm_delete_combobox = ttk.Combobox(wm.delete_window, values=os.listdir('MihaSoft Files/WM Files'),
                                              state='readonly')
            wm_delete_combobox.place(x=10, y=45)

            wm_delete_ok_button = Button(wm.delete_window, text='Удалить', width=10, bg='#e69b93', command=wm_delete_ok)
            wm_delete_ok_button.place(x=200, y=53)

            wm_delete_close_button = Button(wm.delete_window, text='Отмена', bg='#b8b8b8', width=10,
                                            command=wm_delete_abort)
            wm_delete_close_button.place(x=200, y=13)

        try:
            wm.delete_window.resizable(False, False)

        except AttributeError:
            wm_create_del_window()

        except TclError:
            wm_create_del_window()

    def wm_font_chooser():
        def wm_font_abort():
            wm.font_window.destroy()

        def wm_create_font_window():
            def wm_font_ok():
                wm_font_ground.configure(state='normal')
                wm_font_ground.delete(0, END)
                wm_font_ground.insert(0, str(wm_font_combobox.get()))
                wm_font_ground.configure(state='readonly')
                wm.font_window.destroy()

            wm.font_window = Toplevel()
            center_window(wm.font_window, 180, 100)
            wm.font_window.resizable(False, False)
            wm.font_window.title('Выбор шрифта')

            wm_font_combobox = ttk.Combobox(wm.font_window, values=list(families()), state='readonly')
            wm_font_combobox.place(x=10, y=20)

            wm_font_ok_button = Button(wm.font_window, text='OK', width=6, command=wm_font_ok)
            wm_font_ok_button.place(x=10, y=50)

            wm_font_abort_button = Button(wm.font_window, text='Отмена', width=6, command=wm_font_abort)
            wm_font_abort_button.place(x=95, y=50)

        try:
            wm.font_window.resizable(False, False)

        except AttributeError:
            wm_create_font_window()

        except TclError:
            wm_create_font_window()

    # Создание папки с файлами в случае отсутствия таковой
    if not os.path.exists('MihaSoft Files/WM Files'):
        os.mkdir('MihaSoft Files/WM Files')

    center_window(root, 600, 500)
    window.configure(width=600, height=500)
    root.title('WindowManager 1.3')
    root.minsize(600, 500)

    wm_title = Label(window, text='WindowManager 1.3', font=('Times New Roman', 20), fg='red')
    wm_title.place(x=50, y=5)

    wm_label_1 = Label(window, text='Размеры окна:', font=('Times New Roman', 12))
    wm_label_1.place(x=20, y=60)

    # Поле ввода ширины окна
    wm_width_input = Entry(window, width=12)
    wm_width_input.place(x=30, y=100)
    ToolTip(wm_width_input, 'Ширина')

    wm_label_2 = Label(window, text='X')
    wm_label_2.place(x=110, y=100)

    # Поле ввода высоты окна
    wm_height_input = Entry(window, width=12)
    wm_height_input.place(x=125, y=100)
    ToolTip(wm_height_input, 'Высота')

    wm_label_3 = Label(window, text='Расстояние от границ экрана:', font=('Times New Roman', 12))
    wm_label_3.place(x=20, y=130)

    wm_label_4 = Label(window, text='X =')
    wm_label_4.place(x=20, y=170)

    # Поле ввода расстояния от верхнего левого угла окна до левой границы экрана
    wm_x_cord_input = Entry(window, width=10)
    wm_x_cord_input.place(x=50, y=170)
    ToolTip(wm_x_cord_input, 'От левой границы')

    wm_label_5 = Label(window, text='Y =')
    wm_label_5.place(x=20, y=200)

    # Поле ввода расстояния от левого верхнего угла окна до верхней границы экрана
    wm_y_cord_input = Entry(window, width=10)
    wm_y_cord_input.place(x=50, y=200)
    ToolTip(wm_y_cord_input, 'От верхней границы')

    wm_label_6 = Label(window, text='Заголовок:', font=('Times New Roman', 12))
    wm_label_6.place(x=20, y=230)

    # Поле ввода заголовка окна
    wm_cust_title_input = Entry(window, width=28)
    wm_cust_title_input.place(x=30, y=260)

    wm_label_8 = Label(window, text='Введите текст:', font=('Times New Roman', 12))
    wm_label_8.place(x=300, y=80)

    # Поле ввода текста надписи, выводимой в окне
    wm_text_ground = Text(window, width=30, height=3)
    wm_text_ground.place(x=300, y=110)

    wm_label_9 = Label(window, text='Шрифт текста:', font=('Times New Roman', 12))
    wm_label_9.place(x=300, y=170)

    wm_font_ground = Entry(window, width=22, bg='white', state='readonly')
    wm_font_ground.place(x=300, y=200)

    wm_label_10 = Label(window, text='Размер шрифта:', font=('Times New Roman', 12))
    wm_label_10.place(x=300, y=230)

    # Поле ввода размера шрифта надписи
    wm_fsize_input = Entry(window, width=22)
    wm_fsize_input.place(x=300, y=260)

    wm_font_button = Button(window, text='Выбрать', bg='#93bbe6', command=wm_font_chooser)
    wm_font_button.place(x=460, y=200)

    wm_label_11 = Label(window, text='Цвет текста:', font=('Times New Roman', 12))
    wm_label_11.place(x=300, y=290)

    wm_choose_button = Button(window, text='Выбрать', bg='yellow', width=15, command=wm_choose_color)
    wm_choose_button.place(x=300, y=320)

    # Поле демонстрации выбранного цвета надписи
    wm_demo_ground = Label(window, text='', width=30, height=10)
    wm_demo_ground.place(x=30, y=320)

    wm_label_12 = Label(window, text='Расположение текста в окне:', font=('Times New Roman', 12))
    wm_label_12.place(x=300, y=350)

    wm_label_13 = Label(window, text='X =')
    wm_label_13.place(x=300, y=380)

    # Расстояние от надписи до левой границы окна
    wm_text_x_input = Entry(window, width=10)
    wm_text_x_input.place(x=330, y=380)
    ToolTip(wm_text_x_input, 'От левой границы')

    wm_label_14 = Label(window, text='Y =')
    wm_label_14.place(x=300, y=410)

    # Расстояние от надписи до верхней границы
    wm_text_y_input = Entry(window, width=10)
    wm_text_y_input.place(x=330, y=410)
    ToolTip(wm_text_y_input, 'От верхней границы')

    # Кнопка открытия окна по введённым параметрам
    wm_create_button = Button(window, text='СОЗДАТЬ', bg='green', fg='white', width=20, font=('Times New Roman', 16),
                              command=wm_open_custom_window)
    wm_create_button.place(x=300, y=440)
    ToolTip(wm_create_button, 'Создать окно по текущим параметрам...')

    wm_save_button = Button(window, text='Сохранить', bg='#f2ac6b', width=15, command=wm_save)
    wm_save_button.place(x=450, y=10)
    ToolTip(wm_save_button, 'Сохранить текущие параметры...')

    wm_open_button = Button(window, text='Открыть', bg='#f2dc6b', width=15, command=wm_open)
    wm_open_button.place(x=300, y=10)
    ToolTip(wm_open_button, 'Создать окно с сохранёнными параметрами...')

    wm_clean_button = Button(window, text='Обновить', bg='#93bbe6', width=15, command=wm_clean)
    wm_clean_button.place(x=450, y=45)
    ToolTip(wm_clean_button, 'Стереть текущие параметры...')

    wm_delete_button = Button(window, text='Удалить', bg='#e69b93', width=15, command=wm_delete)
    wm_delete_button.place(x=300, y=45)
    ToolTip(wm_delete_button, 'Удалить файл...')

    wm_edit_button = Button(window, text='Редактировать', bg='#90d4cb', width=15, command=wm_edit)
    wm_edit_button.place(x=150, y=45)
    ToolTip(wm_edit_button, 'Подставить параметры окна для редактирования...')

    wm_off = Button(window, text='⌂', font=('Arial Bold', 15), width=2, height=1, bg='black', fg='white',
                    command=wm_to_home)
    wm_off.place(x=0, y=5)
    ToolTip(wm_off, 'На главную...')


def AccountManager():
    am = AccountManagerGlobals()

    def am_to_home():
        """
        Возвращение на главную страницу MihaSoft
        """
        try:
            am.open_window.destroy()
        except AttributeError:
            pass

        try:
            am.quest_window.destroy()
        except AttributeError:
            pass

        try:
            am.delete_window.destroy()
        except AttributeError:
            pass

        am_title.destroy()
        am_label_1.destroy()
        am_input_1.destroy()
        am_button_1.destroy()
        am_label_2.destroy()
        am_input_2.destroy()
        am_button_2.destroy()
        am_label_3.destroy()
        am_input_3.destroy()
        am_button_3.destroy()
        am_pass_but.destroy()
        am_save_db_but.destroy()
        am_open_but.destroy()
        am_del_file_but.destroy()
        am_clean_but.destroy()
        am_ch_file_but.destroy()
        am_add_but.destroy()
        am_off.destroy()
        home()
        window.configure(width=700, height=m.abs_height)
        center_window(root, 678, m.abs_height)

    def copy_service():
        copy(am_input_1.get())

    def copy_login():
        copy(am_input_2.get())

    def copy_password():
        copy(am_input_3.get())

    def password():
        def am_create_quest_window():
            def create_password():
                try:
                    am_input_3.delete(0, END)

                    password_var = ''
                    if qw_input.get():
                        numb_of_symbols = int(qw_input.get())
                    else:
                        numb_of_symbols = 15
                    p_list = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
                              'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'x',
                              'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
                              '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '!', '#', '$', '%', '&', '(', ')',
                              '*', '+', '-', '/', '<', '=', '>', '?', '@', '{', '}', '[', ']', '_']
                    for i in range(numb_of_symbols):
                        password_var += choice(p_list)
                        p_list.remove(password_var[-1])

                    am_input_3.insert(0, str(password_var))
                    copy(password_var)
                    am.quest_window.destroy()
                except IndexError:
                    messagebox.showwarning(title='Ошибка', message='Длина пароля ограничена 83 символами!',
                                           parent=am.quest_window)

            am.quest_window = Toplevel()
            center_window(am.quest_window, 200, 100)
            am.quest_window.title('Число символов')
            am.quest_window.resizable(False, False)

            qw_label = Label(am.quest_window, text='Число символов:')
            qw_label.place(x=5, y=5)

            qw_input = Entry(am.quest_window, width=10)
            qw_input.place(x=110, y=5)

            qw_but = Button(am.quest_window, text='Сгенерировать', bg='#b8b8b8', command=create_password)
            qw_but.place(x=50, y=40)

        try:
            am.quest_window.resizable(False, False)
            am.quest_window.destroy()

        except AttributeError:
            am_create_quest_window()

        except TclError:
            am_create_quest_window()

    def am_save_db():
        if am_input_1.get() and am_input_2.get() and am_input_3.get():
            save(f'MihaSoft Files/AM Files/{am_input_1.get()}', [am_input_1.get(), am_input_2.get(),
                                                                    am_input_3.get()])
            messagebox.showinfo('OK', 'Запись сохранена!')
        else:
            messagebox.showwarning('INFO', 'Заполните поля перед сохранением!')

    def am_open():
        def am_create_open_window():
            def am_open_ok():
                am_input_1.delete(0, END)
                am_input_2.delete(0, END)
                am_input_3.delete(0, END)
                am_list = load(f'MihaSoft Files/AM Files/{am_open_combobox.get()}')
                am_input_1.insert(0, am_list[0])
                am_input_2.insert(0, am_list[1])
                am_input_3.insert(0, am_list[2])
                am.open_window.destroy()

            def am_open_abort():
                am.open_window.destroy()

            am.open_window = Toplevel()
            center_window(am.open_window, 300, 100)
            am.open_window.resizable(False, False)
            am.open_window.title('Открыть')

            am_open_label = Label(am.open_window, text='Выберите запись...')
            am_open_label.place(x=5, y=5)

            # Список существующих файлов
            am_open_combobox = ttk.Combobox(am.open_window, values=os.listdir('MihaSoft Files/AM Files'),
                                            state='readonly')
            am_open_combobox.place(x=10, y=45)

            am_open_ok_button = Button(am.open_window, text='Открыть', width=10, bg='#93e6a8', command=am_open_ok)
            am_open_ok_button.place(x=200, y=53)

            am_open_close_button = Button(am.open_window, text='Отмена', bg='#b8b8b8', width=10, command=am_open_abort)
            am_open_close_button.place(x=200, y=13)

        try:
            am.open_window.resizable(False, False)

        except AttributeError:
            am_create_open_window()

        except TclError:
            am_create_open_window()

    def am_clean():
        am_input_1.delete(0, END)
        am_input_2.delete(0, END)
        am_input_3.delete(0, END)

    def am_delete():
        def am_delete_abort():
            """
            Отмена удаления
            """
            am.delete_window.destroy()

        def am_create_del_window():
            def am_delete_ok():
                """
                Удаление выбранного файла
                """
                am_delete_path = str(am_delete_combobox.get())
                os.remove('MihaSoft Files/AM Files/' + am_delete_path)
                am.delete_window.destroy()

            am.delete_window = Toplevel()
            center_window(am.delete_window, 300, 100)
            am.delete_window.resizable(False, False)
            am.delete_window.title('Удалить')

            am_delete_label = Label(am.delete_window, text='Выберите файл...')
            am_delete_label.place(x=5, y=5)

            # Список существующих файлов
            am_delete_combobox = ttk.Combobox(am.delete_window, values=os.listdir('MihaSoft Files/AM Files'),
                                              state='readonly')
            am_delete_combobox.place(x=10, y=45)

            am_delete_ok_button = Button(am.delete_window, text='Удалить', width=10, bg='#e69b93', command=am_delete_ok)
            am_delete_ok_button.place(x=200, y=53)

            am_delete_close_button = Button(am.delete_window, text='Отмена', bg='#b8b8b8', width=10,
                                            command=am_delete_abort)
            am_delete_close_button.place(x=200, y=13)

        try:
            am.delete_window.resizable(False, False)

        except AttributeError:
            am_create_del_window()

        except TclError:
            am_create_del_window()

    def default_file():
        default_name = asksaveasfilename(title='Назначить файл', filetypes=(('TXT File', '*.txt'),
                                                                            ('All files', '*.*')),
                                         defaultextension='.txt')
        if default_name:
            d_file = open(default_name, 'w')
            d_file.close()
            with open('MihaSoft Files/am-default.miha', 'w') as f:
                f.write(default_name)
                messagebox.showinfo('OK', 'Файл по умолчанию назначен.')

    def add_to_file():
        if am_input_1.get() and am_input_2.get() and am_input_3.get():
            if open('MihaSoft Files/am-default.miha').read():
                try:
                    with open(open('MihaSoft Files/am-default.miha').read(), 'r') as f:
                        am_data = f.read()
                    with open(open('MihaSoft Files/am-default.miha').read(), 'w') as f:
                        f.write(am_data + f'''\n\nСервис: {am_input_1.get()}\nЛогин: {am_input_2.get()}
Пароль: {am_input_3.get()}''')
                    messagebox.showinfo('OK', 'Запись успешно добавлена.')
                except FileNotFoundError:
                    messagebox.showwarning('INFO', 'Файл по умолчанию не найден!')
            else:
                default_file()
        else:
            messagebox.showwarning('INFO', 'Заполните поля перед сохранением!')

    if not os.path.exists('MihaSoft Files/AM Files'):
        os.mkdir('MihaSoft Files/AM Files')
    if not os.path.exists('MihaSoft Files/am-default.miha'):
        f_o = open('MihaSoft Files/am-default.miha', 'w')
        f_o.close()

    center_window(root, 540, 360)
    window.configure(width=540, height=360)
    root.title('AccountManager 2.0')
    root.minsize(540, 360)

    am_title = Label(window, text='AccountManager 2.0', font=('Times New Roman', 20), fg='red')
    am_title.place(x=50, y=5)

    am_label_1 = Label(window, text='Сервис:')
    am_label_1.place(x=30, y=70)

    am_input_1 = Entry(window, width=50)
    am_input_1.place(x=90, y=72)

    am_button_1 = Button(window, text='Копировать', bg='#b8b8b8', command=copy_service)
    am_button_1.place(x=420, y=68)

    am_label_2 = Label(window, text='Логин:')
    am_label_2.place(x=30, y=120)

    am_input_2 = Entry(window, width=50)
    am_input_2.place(x=90, y=122)

    am_button_2 = Button(window, text='Копировать', bg='#b8b8b8', command=copy_login)
    am_button_2.place(x=420, y=118)

    am_label_3 = Label(window, text='Пароль:')
    am_label_3.place(x=30, y=170)

    am_input_3 = Entry(window, width=50)
    am_input_3.place(x=90, y=172)

    am_button_3 = Button(window, text='Копировать', bg='#b8b8b8', command=copy_password)
    am_button_3.place(x=420, y=168)

    am_pass_but = Button(window, text='Сгенерировать пароль', bg='#e0d09f', width=20, command=password)
    am_pass_but.place(x=30, y=230)
    ToolTip(am_pass_but, 'Сгенерировать пароль и вставить его в соответствующую строку')

    am_save_db_but = Button(window, text='Сохранить в базу', bg='#b6f2d3', width=20, command=am_save_db)
    am_save_db_but.place(x=190, y=230)
    ToolTip(am_save_db_but, 'Сохранить данные в базе MihaSoft')

    am_open_but = Button(window, text='Открыть запись', bg='#abeaed', width=20, command=am_open)
    am_open_but.place(x=30, y=270)
    ToolTip(am_open_but, 'Подставить данные из записи в базе MIhaSoft в соответствующие строки')

    am_del_file_but = Button(window, text='Удалить запись', bg='#e69b93', width=140, command=am_delete, compound=LEFT)
    img_obj = Image.open('м.png')
    am_del_file_but.image = ImageTk.PhotoImage(img_obj)
    am_del_file_but['image'] = am_del_file_but.image
    am_del_file_but.place(x=350, y=230)
    ToolTip(am_del_file_but, 'Удалить запись из базы MihaSoft')

    am_clean_but = Button(window, text='Очистить', bg='#faeaaf', width=20, command=am_clean)
    am_clean_but.place(x=350, y=270)
    ToolTip(am_clean_but, 'Очистить все строки')

    am_ch_file_but = Button(window, text='Назначить файл', bg='#f4d7fc', width=20, command=default_file)
    am_ch_file_but.place(x=190, y=270)
    ToolTip(am_ch_file_but, 'Выбрать внешний файл для сохранения данных')

    am_add_but = Button(window, text='Добавить к файлу', bg='#d8d7fc', width=20, command=add_to_file)
    am_add_but.place(x=190, y=310)
    ToolTip(am_add_but, 'Добавить к выбранному файлу текущие данные')

    am_off = Button(window, text='⌂', font=('Arial Bold', 15), width=2, height=1, bg='black', fg='white',
                    command=am_to_home)
    am_off.place(x=0, y=5)
    ToolTip(am_off, 'На главную...')


def YourWarnings():
    """
    Приложение для создания
    фоновых уведомлений на конкретную дату
    """
    yw = YourWarningsGlobals()

    def yw_to_home():
        """
        Возвращение на главную страницу MihaSoft
        """
        try:
            yw.delete_window.destroy()
        except AttributeError:
            pass

        try:
            yw.preview_window.destroy()
        except AttributeError:
            pass

        try:
            yw.preview_ask_window.destroy()
        except AttributeError:
            pass

        yw_title.destroy()
        yw_label_1.destroy()
        yw_label_2.destroy()
        yw_label_3.destroy()
        yw_day_input.destroy()
        yw_month_input.destroy()
        yw_message_input.destroy()
        yw_create_button.destroy()
        yw_preview_button.destroy()
        yw_delete_button.destroy()
        yw_off.destroy()
        home()
        window.configure(width=700, height=m.abs_height)
        center_window(root, 678, m.abs_height)

    def yw_create():
        """
        Функция сохранения нового уведомления
        """
        # Проверка корректности введённых параметров
        if yw_month_input.get().isdigit() and yw_day_input.get().isdigit() and (
                (not yw_day_input.get().isdigit() or not yw_month_input.get().isdigit()) or 1 <= int(
                yw_day_input.get())) and int(yw_day_input.get()) <= 31 and int(
                yw_month_input.get()) >= 1:

            if int(yw_month_input.get()) <= 12:
                save('MihaSoft Files/YW Files/' + str(yw_day_input.get()) + '.' + str(yw_month_input.get()),
                     [str(yw_day_input.get()), str(yw_month_input.get()), str(yw_message_input.get('1.0', END))])
                yw_day_input.delete(0, 'end')
                yw_month_input.delete(0, 'end')
                yw_message_input.delete(1.0, END)

            else:
                messagebox.showwarning('INFO', 'Введены некорректные данные!')
        else:
            messagebox.showwarning('INFO', 'Введены некорректные данные!')

    def yw_preview():
        """
        Функция предварительного просмотра сохранённого уведомления
        """

        def yw_abort_preview():
            """
            Отмена предварительного просмотра
            """
            yw.preview_ask_window.destroy()

        try:
            yw.preview_window.destroy()
        except AttributeError:
            pass

        def yw_create_pa_window():
            def yw_open_preview():
                """
                Открытие окна с уведомлением
                """
                yw_message = load('MihaSoft Files/YW Files/' + str(yw_preview_combobox.get()))
                yw.preview_window = Toplevel()
                yw.preview_window.attributes('-topmost', 'true')
                center_window(yw.preview_window, 435, 360)
                yw.preview_window.title(yw_preview_combobox.get())

                yw_preview_message = Text(yw.preview_window, font=('Arial Bold', 20), fg='red', width=28, height=3)
                yw_preview_message.place(x=5, y=255)

                yw_preview_logo = Label(yw.preview_window, text='Ⓜ', font=('Arial Bold', 150), fg='green')
                yw_preview_logo.place(x=120, y=5)

                yw_preview_message.insert(1.0, yw_message[2])
                yw_preview_message.configure(state=DISABLED)

                yw.preview_ask_window.destroy()

            yw.preview_ask_window = Toplevel()
            center_window(yw.preview_ask_window, 300, 100)
            yw.preview_ask_window.resizable(False, False)
            yw.preview_ask_window.title('Предварительный просмотр')

            yw_preview_label = Label(yw.preview_ask_window, text='Выберите запись...')
            yw_preview_label.place(x=5, y=5)

            # Список сохранённых уведомлений
            yw_preview_combobox = ttk.Combobox(yw.preview_ask_window, values=os.listdir('MihaSoft Files/YW Files'),
                                               state='readonly')
            yw_preview_combobox.place(x=10, y=45)

            yw_preview_ok_button = Button(yw.preview_ask_window, text='Открыть', width=10, bg='#aae09f',
                                          command=yw_open_preview)
            yw_preview_ok_button.place(x=200, y=23)

            yw_preview_close_button = Button(yw.preview_ask_window, text='Отмена', width=10, bg='#b8b8b8',
                                             command=yw_abort_preview)
            yw_preview_close_button.place(x=200, y=60)

        try:
            yw.preview_ask_window.resizable(False, False)

        except AttributeError:
            yw_create_pa_window()

        except TclError:
            yw_create_pa_window()

    def yw_delete():
        """
        Функция удаления сохранённого уведомления
        """

        def yw_delete_abort():
            """
            Отмена удаления
            """
            yw.delete_window.destroy()

        def yw_create_del_window():
            def yw_delete_ok():
                """
                Удаление выбранного уведомления
                """
                os.remove('MihaSoft Files/YW Files/' + str(yw_delete_combobox.get()))
                yw.delete_window.destroy()

            yw.delete_window = Toplevel()
            center_window(yw.delete_window, 300, 100)
            yw.delete_window.resizable(False, False)
            yw.delete_window.title('Удаление')

            yw_delete_label = Label(yw.delete_window, text='Выберите запись...')
            yw_delete_label.place(x=5, y=5)

            # Список существующих уведомлений
            yw_delete_combobox = ttk.Combobox(yw.delete_window, values=os.listdir('MihaSoft Files/YW Files'),
                                              state='readonly')
            yw_delete_combobox.place(x=10, y=45)

            yw_delete_ok_button = Button(yw.delete_window, text='Удалить', width=10, bg='#e69b93', command=yw_delete_ok)
            yw_delete_ok_button.place(x=200, y=23)

            yw_delete_close_button = Button(yw.delete_window, text='Отмена', width=10, bg='#b8b8b8',
                                            command=yw_delete_abort)
            yw_delete_close_button.place(x=200, y=60)

        try:
            yw.delete_window.resizable(False, False)

        except AttributeError:
            yw_create_del_window()

        except TclError:
            yw_create_del_window()

        # Создание папки с уведомлениями в случае отсутствия таковой

    if not os.path.exists('MihaSoft Files/YW Files'):
        os.mkdir('MihaSoft Files/YW Files')

    center_window(root, 400, 400)
    window.configure(width=400, height=400)
    root.title('YourWarnings 1.0')
    root.minsize(400, 400)

    yw_title = Label(window, text='YourWarnings 1.0', font=('Times New Roman', 20), fg='red')
    yw_title.place(x=50, y=5)

    yw_label_1 = Label(window, text='Введите дату:')
    yw_label_1.place(x=20, y=70)

    # Поле ввода даты вывода уведомления
    yw_day_input = Entry(window, width=20)
    yw_day_input.place(x=20, y=100)

    yw_label_2 = Label(window, text='Введите месяц:')
    yw_label_2.place(x=20, y=140)

    # Поле ввода месяца вывода уведомления
    yw_month_input = Entry(window, width=20)
    yw_month_input.place(x=20, y=170)

    yw_label_3 = Label(window, text='Введите текст сообщения:')
    yw_label_3.place(x=20, y=210)

    # Поле ввода текста уведомления
    yw_message_input = Text(window, width=30, height=5)
    yw_message_input.place(x=20, y=240)

    yw_create_button = Button(window, text='Добавить', bg='#aae09f', width=20, command=yw_create)
    yw_create_button.place(x=20, y=350)
    ToolTip(yw_create_button, 'Добавить новое уведомление...')

    yw_preview_button = Button(window, text='Просмотреть', bg='#e0d09f', width=15, command=yw_preview)
    yw_preview_button.place(x=200, y=70)
    ToolTip(yw_preview_button, 'Предварительный просмотр уведомления...')

    yw_delete_button = Button(window, text='Удалить', bg='#e09f9f', width=15, command=yw_delete)
    yw_delete_button.place(x=200, y=120)
    ToolTip(yw_delete_button, 'Удалить файл уведомления...')

    yw_off = Button(window, text='⌂', font=('Arial Bold', 15), width=2, height=1, bg='black', fg='white',
                    command=yw_to_home)
    yw_off.place(x=0, y=5)
    ToolTip(yw_off, 'На главную...')


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
        home()
        window.configure(width=700, height=m.abs_height)
        center_window(root, 678, m.abs_height)

    def sh_to_shoot(sup=None):
        """
        Функция произведения выстрела из пушки
        """
        # Озвучка выстрела в случае наличия соответствующей настройки
        if os.path.exists('MihaSoft Files/SoundFlagFile.miha'):
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
            window.after(sh.speed_snar, odin())
            window.update()

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
            if os.path.exists('MihaSoft Files/SoundFlagFile.miha'):
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
            window.after(sh.speed_push, sh_up_one())
            window.update()

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
            window.after(sh.speed_push, sh_down_one())
            window.update()

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
    window.configure(width=600, height=640)
    root.title('Shmalyalka 1.2')
    root.minsize(600, 640)

    sh_title = Label(window, text='Shmalyalka 1.2', font=('Arial Bold', 16), fg='red')
    sh_title.place(x=40, y=20)

    sh_up_button = Button(window, text='⇧', font=('Arial Black', 20), bg='#90d69f', command=sh_up)
    sh_up_button.place(x=240, y=20)

    sh_down_button = Button(window, text='⇩', font=('Arial Black', 20), bg='#90d69f', command=sh_down)
    sh_down_button.place(x=310, y=20)

    pushka = Label(window, width=10, bg='#ff0000')
    pushka.place(x=30, y=130)

    snaryad = Label(window, width=2, bg='#11ff00')
    snaryad.place(x=100, y=130)

    cel = Label(window, width=2, bg='black')
    cel.place(x=530, y=randint(130, 530))

    sh_shoot_button = Button(window, text='ЗАЛП', bg='yellow', width=10, font=('Times New Roman', 16),
                             command=sh_to_shoot)
    sh_shoot_button.place(x=400, y=20)

    sh_label_1 = Label(window, text='Попаданий:')
    sh_label_1.place(x=30, y=70)

    sh_number_of_hits_label = Label(window, text='0')
    sh_number_of_hits_label.place(x=100, y=70)

    sh_label_2 = Label(window, text='Выстрелов:')
    sh_label_2.place(x=30, y=90)

    sh_number_of_shots_label = Label(window, text='0')
    sh_number_of_shots_label.place(x=100, y=90)

    sh_percents_label = Label(window)
    sh_percents_label.place(x=130, y=80)

    sh_stop_button = Button(window, text='ЗАНОВО', bg='#d47f7f', width=10, font=('Times New Roman', 16),
                            command=sh_stop)
    sh_stop_button.place(x=400, y=70)

    sh_parametrs_button = Button(window, text='Параметры', bg='#9be0df', width=10, font=('Times New Roman', 12),
                                 command=sh_parametrs)
    sh_parametrs_button.place(x=450, y=570)

    root.bind('<Return>', sh_to_shoot)
    root.bind('<space>', sh_to_shoot)
    root.bind('<Down>', sh_down)
    root.bind('<Up>', sh_up)

    sh_off = Button(window, text='⌂', font=('Arial Bold', 15), width=2, height=1, bg='black', fg='white',
                    command=sh_to_home)
    sh_off.place(x=0, y=5)
    ToolTip(sh_off, 'На главную...')


def Paint():
    """
    Пиксельный графический редактор
    """
    # Создание объекта с глобальными переменными
    p = PaintGlobals()

    def p_to_home():
        """
        Возвращение на главную страницу MihaSoft
        """
        try:
            p.delete_window.destroy()
        except AttributeError:
            pass

        try:
            p.open_window.destroy()
        except AttributeError:
            pass

        try:
            p.save_window.destroy()
        except AttributeError:
            pass

        p_window.destroy()
        home()
        window.configure(width=700, height=m.abs_height)
        center_window(root, 678, m.abs_height)

    def recol(pix):
        """
        Общая функция изменения цвета пикселя
        """
        pix.configure(bg=p.chosen_color)

    # Функции изменения цвета для каждого пикселя
    def r1():
        recol(a1)

    def r2():
        recol(a2)

    def r3():
        recol(a3)

    def r4():
        recol(a4)

    def r5():
        recol(a5)

    def r6():
        recol(a6)

    def r7():
        recol(a7)

    def r8():
        recol(a8)

    def r9():
        recol(a9)

    def r10():
        recol(a10)

    def r11():
        recol(a11)

    def r12():
        recol(a12)

    def r13():
        recol(a13)

    def r14():
        recol(a14)

    def r15():
        recol(a15)

    def r16():
        recol(a16)

    def r17():
        recol(a17)

    def r18():
        recol(a18)

    def r19():
        recol(a19)

    def r20():
        recol(a20)

    def r21():
        recol(a21)

    def r22():
        recol(a22)

    def r23():
        recol(a23)

    def r24():
        recol(a24)

    def r25():
        recol(a25)

    def r26():
        recol(a26)

    def r27():
        recol(a27)

    def r28():
        recol(a28)

    def r29():
        recol(a29)

    def r30():
        recol(a30)

    def s1():
        recol(b1)

    def s2():
        recol(b2)

    def s3():
        recol(b3)

    def s4():
        recol(b4)

    def s5():
        recol(b5)

    def s6():
        recol(b6)

    def s7():
        recol(b7)

    def s8():
        recol(b8)

    def s9():
        recol(b9)

    def s10():
        recol(b10)

    def s11():
        recol(b11)

    def s12():
        recol(b12)

    def s13():
        recol(b13)

    def s14():
        recol(b14)

    def s15():
        recol(b15)

    def s16():
        recol(b16)

    def s17():
        recol(b17)

    def s18():
        recol(b18)

    def s19():
        recol(b19)

    def s20():
        recol(b20)

    def s21():
        recol(b21)

    def s22():
        recol(b22)

    def s23():
        recol(b23)

    def s24():
        recol(b24)

    def s25():
        recol(b25)

    def s26():
        recol(b26)

    def s27():
        recol(b27)

    def s28():
        recol(b28)

    def s29():
        recol(b29)

    def s30():
        recol(b30)

    def t1():
        recol(c1)

    def t2():
        recol(c2)

    def t3():
        recol(c3)

    def t4():
        recol(c4)

    def t5():
        recol(c5)

    def t6():
        recol(c6)

    def t7():
        recol(c7)

    def t8():
        recol(c8)

    def t9():
        recol(c9)

    def t10():
        recol(c10)

    def t11():
        recol(c11)

    def t12():
        recol(c12)

    def t13():
        recol(c13)

    def t14():
        recol(c14)

    def t15():
        recol(c15)

    def t16():
        recol(c16)

    def t17():
        recol(c17)

    def t18():
        recol(c18)

    def t19():
        recol(c19)

    def t20():
        recol(c20)

    def t21():
        recol(c21)

    def t22():
        recol(c22)

    def t23():
        recol(c23)

    def t24():
        recol(c24)

    def t25():
        recol(c25)

    def t26():
        recol(c26)

    def t27():
        recol(c27)

    def t28():
        recol(c28)

    def t29():
        recol(c29)

    def t30():
        recol(c30)

    def u1():
        recol(d1)

    def u2():
        recol(d2)

    def u3():
        recol(d3)

    def u4():
        recol(d4)

    def u5():
        recol(d5)

    def u6():
        recol(d6)

    def u7():
        recol(d7)

    def u8():
        recol(d8)

    def u9():
        recol(d9)

    def u10():
        recol(d10)

    def u11():
        recol(d11)

    def u12():
        recol(d12)

    def u13():
        recol(d13)

    def u14():
        recol(d14)

    def u15():
        recol(d15)

    def u16():
        recol(d16)

    def u17():
        recol(d17)

    def u18():
        recol(d18)

    def u19():
        recol(d19)

    def u20():
        recol(d20)

    def u21():
        recol(d21)

    def u22():
        recol(d22)

    def u23():
        recol(d23)

    def u24():
        recol(d24)

    def u25():
        recol(d25)

    def u26():
        recol(d26)

    def u27():
        recol(d27)

    def u28():
        recol(d28)

    def u29():
        recol(d29)

    def u30():
        recol(d30)

    def v1():
        recol(e1)

    def v2():
        recol(e2)

    def v3():
        recol(e3)

    def v4():
        recol(e4)

    def v5():
        recol(e5)

    def v6():
        recol(e6)

    def v7():
        recol(e7)

    def v8():
        recol(e8)

    def v9():
        recol(e9)

    def v10():
        recol(e10)

    def v11():
        recol(e11)

    def v12():
        recol(e12)

    def v13():
        recol(e13)

    def v14():
        recol(e14)

    def v15():
        recol(e15)

    def v16():
        recol(e16)

    def v17():
        recol(e17)

    def v18():
        recol(e18)

    def v19():
        recol(e19)

    def v20():
        recol(e20)

    def v21():
        recol(e21)

    def v22():
        recol(e22)

    def v23():
        recol(e23)

    def v24():
        recol(e24)

    def v25():
        recol(e25)

    def v26():
        recol(e26)

    def v27():
        recol(e27)

    def v28():
        recol(e28)

    def v29():
        recol(e29)

    def v30():
        recol(e30)

    def w1():
        recol(f1)

    def w2():
        recol(f2)

    def w3():
        recol(f3)

    def w4():
        recol(f4)

    def w5():
        recol(f5)

    def w6():
        recol(f6)

    def w7():
        recol(f7)

    def w8():
        recol(f8)

    def w9():
        recol(f9)

    def w10():
        recol(f10)

    def w11():
        recol(f11)

    def w12():
        recol(f12)

    def w13():
        recol(f13)

    def w14():
        recol(f14)

    def w15():
        recol(f15)

    def w16():
        recol(f16)

    def w17():
        recol(f17)

    def w18():
        recol(f18)

    def w19():
        recol(f19)

    def w20():
        recol(f20)

    def w21():
        recol(f21)

    def w22():
        recol(f22)

    def w23():
        recol(f23)

    def w24():
        recol(f24)

    def w25():
        recol(f25)

    def w26():
        recol(f26)

    def w27():
        recol(f27)

    def w28():
        recol(f28)

    def w29():
        recol(f29)

    def w30():
        recol(f30)

    def x1():
        recol(g1)

    def x2():
        recol(g2)

    def x3():
        recol(g3)

    def x4():
        recol(g4)

    def x5():
        recol(g5)

    def x6():
        recol(g6)

    def x7():
        recol(g7)

    def x8():
        recol(g8)

    def x9():
        recol(g9)

    def x10():
        recol(g10)

    def x11():
        recol(g11)

    def x12():
        recol(g12)

    def x13():
        recol(g13)

    def x14():
        recol(g14)

    def x15():
        recol(g15)

    def x16():
        recol(g16)

    def x17():
        recol(g17)

    def x18():
        recol(g18)

    def x19():
        recol(g19)

    def x20():
        recol(g20)

    def x21():
        recol(g21)

    def x22():
        recol(g22)

    def x23():
        recol(g23)

    def x24():
        recol(g24)

    def x25():
        recol(g25)

    def x26():
        recol(g26)

    def x27():
        recol(g27)

    def x28():
        recol(g28)

    def x29():
        recol(g29)

    def x30():
        recol(g30)

    def y1():
        recol(h1)

    def y2():
        recol(h2)

    def y3():
        recol(h3)

    def y4():
        recol(h4)

    def y5():
        recol(h5)

    def y6():
        recol(h6)

    def y7():
        recol(h7)

    def y8():
        recol(h8)

    def y9():
        recol(h9)

    def y10():
        recol(h10)

    def y11():
        recol(h11)

    def y12():
        recol(h12)

    def y13():
        recol(h13)

    def y14():
        recol(h14)

    def y15():
        recol(h15)

    def y16():
        recol(h16)

    def y17():
        recol(h17)

    def y18():
        recol(h18)

    def y19():
        recol(h19)

    def y20():
        recol(h20)

    def y21():
        recol(h21)

    def y22():
        recol(h22)

    def y23():
        recol(h23)

    def y24():
        recol(h24)

    def y25():
        recol(h25)

    def y26():
        recol(h26)

    def y27():
        recol(h27)

    def y28():
        recol(h28)

    def y29():
        recol(h29)

    def y30():
        recol(h30)

    def p_choose_color():
        """
        Функция выбора цвета редактирования
        """
        p_colorchoose_window = colorchooser.askcolor()
        p.chosen_color = p_colorchoose_window[1]
        p_choose_button.configure(bg=str(p.chosen_color))
        p.choose_flag = True

    def eraser():
        """
        Функция включения-выключения режима ластика
        """
        # Включение ластика
        if p.choose_flag:
            p.now_color = p_choose_button['background']
            p.chosen_color = 'white'
            p_choose_button.configure(bg='white')
            p.choose_flag = False

        # Возвращение к последнему использовавшемуся цвету
        else:
            p.chosen_color = p.now_color
            p_choose_button.configure(bg=p.now_color)
            p.choose_flag = True

    def p_save():
        """
        Функция сохранения рисунка в файл
        """

        def p_save_changes():
            """
            Функция сохранения изменений в существующем файле
            """
            p_colors_list = []
            for i in range(len(p_all)):
                p_colors_list.append(p_all[i]['background'])
            save(p.file_name, p_colors_list)
            p.save_window.destroy()

        def p_abort_save():
            """
            Отмена сохранения
            """
            p.save_window.destroy()

        # Проверка значения переменной, отвечающей за состояния
        # приложения (создание нового файла или редактирование существующего)
        # и вызов соответствующего окна.
        def p_create_save_window():
            def p_save_file():
                """
                Сохранение нового файла
                """
                p_colors_list = []
                for i in range(len(p_all)):
                    p_colors_list.append(p_all[i]['background'])
                save('MihaSoft Files/P Files/' + str(p_save_input.get()), p_colors_list)
                p.save_window.destroy()

            if p.save_flag:
                p.save_window = Toplevel()
                center_window(p.save_window, 300, 100)
                p.save_window.resizable(False, False)
                p.save_window.title('Сохранение')

                p_save_label = Label(p.save_window, text='Введите название файла...')
                p_save_label.place(x=5, y=5)

                p_save_input = Entry(p.save_window, width=25)
                p_save_input.place(x=10, y=45)

                p_save_ok_button = Button(p.save_window, text='Сохранить', width=10, bg='#93e6a8', command=p_save_file)
                p_save_ok_button.place(x=200, y=23)

                p_close_button = Button(p.save_window, text='Отмена', width=10, bg='#b8b8b8', command=p_abort_save)
                p_close_button.place(x=200, y=60)

            else:
                p.save_window = Toplevel()
                center_window(p.save_window, 300, 100)
                p.save_window.resizable(False, False)
                p.save_window.title('Сохранение изменений')

                p_save_label = Label(p.save_window, text='Сохранить изменения в файле\n' + p.file_name + '?')
                p_save_label.place(x=5, y=5)

                p_save_ok_button = Button(p.save_window, text='Сохранить', width=10, bg='#93e6a8',
                                          command=p_save_changes)
                p_save_ok_button.place(x=100, y=60)

                p_close_button = Button(p.save_window, text='Отмена', width=10, bg='#b8b8b8', command=p_abort_save)
                p_close_button.place(x=200, y=60)

        try:
            p.save_window.resizable(False, False)

        except AttributeError:
            p_create_save_window()

        except TclError:
            p_create_save_window()

    def p_open():
        """
        Функция открытия сохранённого рисунка
        """

        def p_abort_open():
            """
            Отмена открытия
            """
            p.open_window.destroy()

        def p_create_open_window():
            def p_open_ok():
                """
                Считывание данных и вывод рисунка на экран
                """
                p_open_colors_list = load('MihaSoft Files/P Files/' + str(p_open_combobox.get()))
                p.file_name = 'MihaSoft Files/P Files/' + str(p_open_combobox.get())
                for i in range(len(p_all)):
                    p_all[i].configure(bg=p_open_colors_list[i])
                p.open_window.destroy()
                p.save_flag = False

            p.open_window = Toplevel()
            center_window(p.open_window, 300, 100)
            p.open_window.resizable(False, False)
            p.open_window.title('Открыть')

            p_open_label = Label(p.open_window, text='Выберите файл...')
            p_open_label.place(x=5, y=5)

            # Список существующих файлов
            p_open_combobox = ttk.Combobox(p.open_window, values=os.listdir('MihaSoft Files/P Files'),
                                           state='readonly')
            p_open_combobox.place(x=10, y=45)

            p_open_ok_button = Button(p.open_window, text='Открыть', width=10, bg='#93e6a8', command=p_open_ok)
            p_open_ok_button.place(x=200, y=23)

            p_open_abort_button = Button(p.open_window, text='Отмена', width=10, bg='#b8b8b8', command=p_abort_open)
            p_open_abort_button.place(x=200, y=60)

        try:
            p.open_window.resizable(False, False)

        except AttributeError:
            p_create_open_window()

        except TclError:
            p_create_open_window()

    def p_delete():
        """
        Функция удаления сохранённых файлов
        """

        def p_delete_abort():
            """
            Отмена удаления
            """
            p.delete_window.destroy()

        def p_create_del_window():
            def p_delete_ok():
                """
                Удаление выбранного файла
                """
                os.remove('MihaSoft Files/P Files/' + str(p_delete_combobox.get()))
                p.delete_window.destroy()

            p.delete_window = Toplevel()
            center_window(p.delete_window, 300, 100)
            p.delete_window.resizable(False, False)
            p.delete_window.title('Удаление')

            p_delete_label = Label(p.delete_window, text='Выберите файл...')
            p_delete_label.place(x=5, y=5)

            # Список существующих файлов
            p_delete_combobox = ttk.Combobox(p.delete_window, values=os.listdir('MihaSoft Files/P Files'),
                                             state='readonly')
            p_delete_combobox.place(x=10, y=45)

            p_delete_ok_button = Button(p.delete_window, text='Удалить', width=10, bg='#e69b93', command=p_delete_ok)
            p_delete_ok_button.place(x=200, y=23)

            p_delete_close_button = Button(p.delete_window, text='Отмена', width=10, bg='#b8b8b8',
                                           command=p_delete_abort)
            p_delete_close_button.place(x=200, y=60)

        try:
            p.delete_window.resizable(False, False)

        except AttributeError:
            p_create_del_window()

        except TclError:
            p_create_del_window()

    def p_clean():
        """
        Функция очистки поля для рисования
        """
        for i in range(len(p_all)):
            p_all[i].configure(bg='white')

    def p_new_pict():
        """
        Функция очистки поля для рисования
        и выхода из режима редактирования
        """
        p.save_flag = True
        p.file_name = None
        p_clean()

    # Массив для последующего добавления объектов всех
    # пикселей для последующих операций с ними
    p_all = []

    # Создание папки с файлами в случае отсутствия таковой
    if not os.path.exists('MihaSoft Files/P Files'):
        os.mkdir('MihaSoft Files/P Files')

    center_window(root, 550, 300)
    window.configure(width=550, height=300)
    p_window = Frame(window, width=550, height=300)
    root.title('Paint 1.1')
    root.minsize(550, 300)

    p_title = Label(p_window, text='Paint 1.1', font=('Arial Bold', 16), fg='red')
    p_title.place(x=50, y=10)

    p_new_picture_button = Button(p_window, text='Новый рисунок', bg='#b8b8b8', command=p_new_pict)
    p_new_picture_button.place(x=180, y=10)

    p_clean_button = Button(p_window, text='Очистить', bg='#b8b8b8', command=p_clean)
    p_clean_button.place(x=285, y=10)

    p_eraser_button = Button(p_window, text='Ластик', bg='#b8b8b8', command=eraser)
    p_eraser_button.place(x=355, y=10)
    ToolTip(p_eraser_button, 'Нажмите повторно для возвращения к последнему цвету...')

    p_choose_button = Button(p_window, text='Выбрать цвет', bg='white', command=p_choose_color)
    p_choose_button.place(x=415, y=10)

    # Пиксели
    a1 = Button(p_window, width=1, height=1, bg='white', font=("Arial Bold", 6), command=r1)
    a1.place(x=50, y=50)
    p_all.append(a1)

    a2 = Button(p_window, width=1, height=1, bg='white', font=("Arial Bold", 6), command=r2)
    a2.place(x=65, y=50)
    p_all.append(a2)

    a3 = Button(p_window, width=1, height=1, bg='white', font=("Arial Bold", 6), command=r3)
    a3.place(x=80, y=50)
    p_all.append(a3)

    a4 = Button(p_window, width=1, height=1, bg='white', font=("Arial Bold", 6), command=r4)
    a4.place(x=95, y=50)
    p_all.append(a4)

    a5 = Button(p_window, width=1, height=1, bg='white', font=("Arial Bold", 6), command=r5)
    a5.place(x=110, y=50)
    p_all.append(a5)

    a6 = Button(p_window, width=1, height=1, bg='white', font=("Arial Bold", 6), command=r6)
    a6.place(x=125, y=50)
    p_all.append(a6)

    a7 = Button(p_window, width=1, height=1, bg='white', font=("Arial Bold", 6), command=r7)
    a7.place(x=140, y=50)
    p_all.append(a7)

    a8 = Button(p_window, width=1, height=1, bg='white', font=("Arial Bold", 6), command=r8)
    a8.place(x=155, y=50)
    p_all.append(a8)

    a9 = Button(p_window, width=1, height=1, bg='white', font=("Arial Bold", 6), command=r9)
    a9.place(x=170, y=50)
    p_all.append(a9)

    a10 = Button(p_window, width=1, height=1, bg='white', font=("Arial Bold", 6), command=r10)
    a10.place(x=185, y=50)
    p_all.append(a10)

    a11 = Button(p_window, width=1, height=1, bg='white', font=("Arial Bold", 6), command=r11)
    a11.place(x=200, y=50)
    p_all.append(a11)

    a12 = Button(p_window, width=1, height=1, bg='white', font=("Arial Bold", 6), command=r12)
    a12.place(x=215, y=50)
    p_all.append(a12)

    a13 = Button(p_window, width=1, height=1, bg='white', font=("Arial Bold", 6), command=r13)
    a13.place(x=230, y=50)
    p_all.append(a13)

    a14 = Button(p_window, width=1, height=1, bg='white', font=("Arial Bold", 6), command=r14)
    a14.place(x=245, y=50)
    p_all.append(a14)

    a15 = Button(p_window, width=1, height=1, bg='white', font=("Arial Bold", 6), command=r15)
    a15.place(x=260, y=50)
    p_all.append(a15)

    a16 = Button(p_window, width=1, height=1, bg='white', font=("Arial Bold", 6), command=r16)
    a16.place(x=275, y=50)
    p_all.append(a16)

    a17 = Button(p_window, width=1, height=1, bg='white', font=("Arial Bold", 6), command=r17)
    a17.place(x=290, y=50)
    p_all.append(a17)

    a18 = Button(p_window, width=1, height=1, bg='white', font=("Arial Bold", 6), command=r18)
    a18.place(x=305, y=50)
    p_all.append(a18)

    a19 = Button(p_window, width=1, height=1, bg='white', font=("Arial Bold", 6), command=r19)
    a19.place(x=320, y=50)
    p_all.append(a19)

    a20 = Button(p_window, width=1, height=1, bg='white', font=("Arial Bold", 6), command=r20)
    a20.place(x=335, y=50)
    p_all.append(a20)

    a21 = Button(p_window, width=1, height=1, bg='white', font=("Arial Bold", 6), command=r21)
    a21.place(x=350, y=50)
    p_all.append(a21)

    a22 = Button(p_window, width=1, height=1, bg='white', font=("Arial Bold", 6), command=r22)
    a22.place(x=365, y=50)
    p_all.append(a22)

    a23 = Button(p_window, width=1, height=1, bg='white', font=("Arial Bold", 6), command=r23)
    a23.place(x=380, y=50)
    p_all.append(a23)

    a24 = Button(p_window, width=1, height=1, bg='white', font=("Arial Bold", 6), command=r24)
    a24.place(x=395, y=50)
    p_all.append(a24)

    a25 = Button(p_window, width=1, height=1, bg='white', font=("Arial Bold", 6), command=r25)
    a25.place(x=410, y=50)
    p_all.append(a25)

    a26 = Button(p_window, width=1, height=1, bg='white', font=("Arial Bold", 6), command=r26)
    a26.place(x=425, y=50)
    p_all.append(a26)

    a27 = Button(p_window, width=1, height=1, bg='white', font=("Arial Bold", 6), command=r27)
    a27.place(x=440, y=50)
    p_all.append(a27)

    a28 = Button(p_window, width=1, height=1, bg='white', font=("Arial Bold", 6), command=r28)
    a28.place(x=455, y=50)
    p_all.append(a28)

    a29 = Button(p_window, width=1, height=1, bg='white', font=("Arial Bold", 6), command=r29)
    a29.place(x=470, y=50)
    p_all.append(a29)

    a30 = Button(p_window, width=1, height=1, bg='white', font=("Arial Bold", 6), command=r30)
    a30.place(x=485, y=50)
    p_all.append(a30)

    b1 = Button(p_window, width=1, height=1, bg='white', font=("Arial Bold", 6), command=s1)
    b1.place(x=50, y=68)
    p_all.append(b1)

    b2 = Button(p_window, width=1, height=1, bg='white', font=("Arial Bold", 6), command=s2)
    b2.place(x=65, y=68)
    p_all.append(b2)

    b3 = Button(p_window, width=1, height=1, bg='white', font=("Arial Bold", 6), command=s3)
    b3.place(x=80, y=68)
    p_all.append(b3)

    b4 = Button(p_window, width=1, height=1, bg='white', font=("Arial Bold", 6), command=s4)
    b4.place(x=95, y=68)
    p_all.append(b4)

    b5 = Button(p_window, width=1, height=1, bg='white', font=("Arial Bold", 6), command=s5)
    b5.place(x=110, y=68)
    p_all.append(b5)

    b6 = Button(p_window, width=1, height=1, bg='white', font=("Arial Bold", 6), command=s6)
    b6.place(x=125, y=68)
    p_all.append(b6)

    b7 = Button(p_window, width=1, height=1, bg='white', font=("Arial Bold", 6), command=s7)
    b7.place(x=140, y=68)
    p_all.append(b7)

    b8 = Button(p_window, width=1, height=1, bg='white', font=("Arial Bold", 6), command=s8)
    b8.place(x=155, y=68)
    p_all.append(b8)

    b9 = Button(p_window, width=1, height=1, bg='white', font=("Arial Bold", 6), command=s9)
    b9.place(x=170, y=68)
    p_all.append(b9)

    b10 = Button(p_window, width=1, height=1, bg='white', font=("Arial Bold", 6), command=s10)
    b10.place(x=185, y=68)
    p_all.append(b10)

    b11 = Button(p_window, width=1, height=1, bg='white', font=("Arial Bold", 6), command=s11)
    b11.place(x=200, y=68)
    p_all.append(b11)

    b12 = Button(p_window, width=1, height=1, bg='white', font=("Arial Bold", 6), command=s12)
    b12.place(x=215, y=68)
    p_all.append(b12)

    b13 = Button(p_window, width=1, height=1, bg='white', font=("Arial Bold", 6), command=s13)
    b13.place(x=230, y=68)
    p_all.append(b13)

    b14 = Button(p_window, width=1, height=1, bg='white', font=("Arial Bold", 6), command=s14)
    b14.place(x=245, y=68)
    p_all.append(b14)

    b15 = Button(p_window, width=1, height=1, bg='white', font=("Arial Bold", 6), command=s15)
    b15.place(x=260, y=68)
    p_all.append(b15)

    b16 = Button(p_window, width=1, height=1, bg='white', font=("Arial Bold", 6), command=s16)
    b16.place(x=275, y=68)
    p_all.append(b16)

    b17 = Button(p_window, width=1, height=1, bg='white', font=("Arial Bold", 6), command=s17)
    b17.place(x=290, y=68)
    p_all.append(b17)

    b18 = Button(p_window, width=1, height=1, bg='white', font=("Arial Bold", 6), command=s18)
    b18.place(x=305, y=68)
    p_all.append(b18)

    b19 = Button(p_window, width=1, height=1, bg='white', font=("Arial Bold", 6), command=s19)
    b19.place(x=320, y=68)
    p_all.append(b19)

    b20 = Button(p_window, width=1, height=1, bg='white', font=("Arial Bold", 6), command=s20)
    b20.place(x=335, y=68)
    p_all.append(b20)

    b21 = Button(p_window, width=1, height=1, bg='white', font=("Arial Bold", 6), command=s21)
    b21.place(x=350, y=68)
    p_all.append(b21)

    b22 = Button(p_window, width=1, height=1, bg='white', font=("Arial Bold", 6), command=s22)
    b22.place(x=365, y=68)
    p_all.append(b22)

    b23 = Button(p_window, width=1, height=1, bg='white', font=("Arial Bold", 6), command=s23)
    b23.place(x=380, y=68)
    p_all.append(b23)

    b24 = Button(p_window, width=1, height=1, bg='white', font=("Arial Bold", 6), command=s24)
    b24.place(x=395, y=68)
    p_all.append(b24)

    b25 = Button(p_window, width=1, height=1, bg='white', font=("Arial Bold", 6), command=s25)
    b25.place(x=410, y=68)
    p_all.append(b25)

    b26 = Button(p_window, width=1, height=1, bg='white', font=("Arial Bold", 6), command=s26)
    b26.place(x=425, y=68)
    p_all.append(b26)

    b27 = Button(p_window, width=1, height=1, bg='white', font=("Arial Bold", 6), command=s27)
    b27.place(x=440, y=68)
    p_all.append(b27)

    b28 = Button(p_window, width=1, height=1, bg='white', font=("Arial Bold", 6), command=s28)
    b28.place(x=455, y=68)
    p_all.append(b28)

    b29 = Button(p_window, width=1, height=1, bg='white', font=("Arial Bold", 6), command=s29)
    b29.place(x=470, y=68)
    p_all.append(b29)

    b30 = Button(p_window, width=1, height=1, bg='white', font=("Arial Bold", 6), command=s30)
    b30.place(x=485, y=68)
    p_all.append(b30)

    c1 = Button(p_window, width=1, height=1, bg='white', font=("Arial Bold", 6), command=t1)
    c1.place(x=50, y=86)
    p_all.append(c1)

    c2 = Button(p_window, width=1, height=1, bg='white', font=("Arial Bold", 6), command=t2)
    c2.place(x=65, y=86)
    p_all.append(c2)

    c3 = Button(p_window, width=1, height=1, bg='white', font=("Arial Bold", 6), command=t3)
    c3.place(x=80, y=86)
    p_all.append(c3)

    c4 = Button(p_window, width=1, height=1, bg='white', font=("Arial Bold", 6), command=t4)
    c4.place(x=95, y=86)
    p_all.append(c4)

    c5 = Button(p_window, width=1, height=1, bg='white', font=("Arial Bold", 6), command=t5)
    c5.place(x=110, y=86)
    p_all.append(c5)

    c6 = Button(p_window, width=1, height=1, bg='white', font=("Arial Bold", 6), command=t6)
    c6.place(x=125, y=86)
    p_all.append(c6)

    c7 = Button(p_window, width=1, height=1, bg='white', font=("Arial Bold", 6), command=t7)
    c7.place(x=140, y=86)
    p_all.append(c7)

    c8 = Button(p_window, width=1, height=1, bg='white', font=("Arial Bold", 6), command=t8)
    c8.place(x=155, y=86)
    p_all.append(c8)

    c9 = Button(p_window, width=1, height=1, bg='white', font=("Arial Bold", 6), command=t9)
    c9.place(x=170, y=86)
    p_all.append(c9)

    c10 = Button(p_window, width=1, height=1, bg='white', font=("Arial Bold", 6), command=t10)
    c10.place(x=185, y=86)
    p_all.append(c10)

    c11 = Button(p_window, width=1, height=1, bg='white', font=("Arial Bold", 6), command=t11)
    c11.place(x=200, y=86)
    p_all.append(c11)

    c12 = Button(p_window, width=1, height=1, bg='white', font=("Arial Bold", 6), command=t12)
    c12.place(x=215, y=86)
    p_all.append(c12)

    c13 = Button(p_window, width=1, height=1, bg='white', font=("Arial Bold", 6), command=t13)
    c13.place(x=230, y=86)
    p_all.append(c13)

    c14 = Button(p_window, width=1, height=1, bg='white', font=("Arial Bold", 6), command=t14)
    c14.place(x=245, y=86)
    p_all.append(c14)

    c15 = Button(p_window, width=1, height=1, bg='white', font=("Arial Bold", 6), command=t15)
    c15.place(x=260, y=86)
    p_all.append(c15)

    c16 = Button(p_window, width=1, height=1, bg='white', font=("Arial Bold", 6), command=t16)
    c16.place(x=275, y=86)
    p_all.append(c16)

    c17 = Button(p_window, width=1, height=1, bg='white', font=("Arial Bold", 6), command=t17)
    c17.place(x=290, y=86)
    p_all.append(c17)

    c18 = Button(p_window, width=1, height=1, bg='white', font=("Arial Bold", 6), command=t18)
    c18.place(x=305, y=86)
    p_all.append(c18)

    c19 = Button(p_window, width=1, height=1, bg='white', font=("Arial Bold", 6), command=t19)
    c19.place(x=320, y=86)
    p_all.append(c19)

    c20 = Button(p_window, width=1, height=1, bg='white', font=("Arial Bold", 6), command=t20)
    c20.place(x=335, y=86)
    p_all.append(c20)

    c21 = Button(p_window, width=1, height=1, bg='white', font=("Arial Bold", 6), command=t21)
    c21.place(x=350, y=86)
    p_all.append(c21)

    c22 = Button(p_window, width=1, height=1, bg='white', font=("Arial Bold", 6), command=t22)
    c22.place(x=365, y=86)
    p_all.append(c22)

    c23 = Button(p_window, width=1, height=1, bg='white', font=("Arial Bold", 6), command=t23)
    c23.place(x=380, y=86)
    p_all.append(c23)

    c24 = Button(p_window, width=1, height=1, bg='white', font=("Arial Bold", 6), command=t24)
    c24.place(x=395, y=86)
    p_all.append(c24)

    c25 = Button(p_window, width=1, height=1, bg='white', font=("Arial Bold", 6), command=t25)
    c25.place(x=410, y=86)
    p_all.append(c25)

    c26 = Button(p_window, width=1, height=1, bg='white', font=("Arial Bold", 6), command=t26)
    c26.place(x=425, y=86)
    p_all.append(c26)

    c27 = Button(p_window, width=1, height=1, bg='white', font=("Arial Bold", 6), command=t27)
    c27.place(x=440, y=86)
    p_all.append(c27)

    c28 = Button(p_window, width=1, height=1, bg='white', font=("Arial Bold", 6), command=t28)
    c28.place(x=455, y=86)
    p_all.append(c28)

    c29 = Button(p_window, width=1, height=1, bg='white', font=("Arial Bold", 6), command=t29)
    c29.place(x=470, y=86)
    p_all.append(c29)

    c30 = Button(p_window, width=1, height=1, bg='white', font=("Arial Bold", 6), command=t30)
    c30.place(x=485, y=86)
    p_all.append(c30)

    d1 = Button(p_window, width=1, height=1, bg='white', font=("Arial Bold", 6), command=u1)
    d1.place(x=50, y=104)
    p_all.append(d1)

    d2 = Button(p_window, width=1, height=1, bg='white', font=("Arial Bold", 6), command=u2)
    d2.place(x=65, y=104)
    p_all.append(d2)

    d3 = Button(p_window, width=1, height=1, bg='white', font=("Arial Bold", 6), command=u3)
    d3.place(x=80, y=104)
    p_all.append(d3)

    d4 = Button(p_window, width=1, height=1, bg='white', font=("Arial Bold", 6), command=u4)
    d4.place(x=95, y=104)
    p_all.append(d4)

    d5 = Button(p_window, width=1, height=1, bg='white', font=("Arial Bold", 6), command=u5)
    d5.place(x=110, y=104)
    p_all.append(d5)

    d6 = Button(p_window, width=1, height=1, bg='white', font=("Arial Bold", 6), command=u6)
    d6.place(x=125, y=104)
    p_all.append(d6)

    d7 = Button(p_window, width=1, height=1, bg='white', font=("Arial Bold", 6), command=u7)
    d7.place(x=140, y=104)
    p_all.append(d7)

    d8 = Button(p_window, width=1, height=1, bg='white', font=("Arial Bold", 6), command=u8)
    d8.place(x=155, y=104)
    p_all.append(d8)

    d9 = Button(p_window, width=1, height=1, bg='white', font=("Arial Bold", 6), command=u9)
    d9.place(x=170, y=104)
    p_all.append(d9)

    d10 = Button(p_window, width=1, height=1, bg='white', font=("Arial Bold", 6), command=u10)
    d10.place(x=185, y=104)
    p_all.append(d10)

    d11 = Button(p_window, width=1, height=1, bg='white', font=("Arial Bold", 6), command=u11)
    d11.place(x=200, y=104)
    p_all.append(d11)

    d12 = Button(p_window, width=1, height=1, bg='white', font=("Arial Bold", 6), command=u12)
    d12.place(x=215, y=104)
    p_all.append(d12)

    d13 = Button(p_window, width=1, height=1, bg='white', font=("Arial Bold", 6), command=u13)
    d13.place(x=230, y=104)
    p_all.append(d13)

    d14 = Button(p_window, width=1, height=1, bg='white', font=("Arial Bold", 6), command=u14)
    d14.place(x=245, y=104)
    p_all.append(d14)

    d15 = Button(p_window, width=1, height=1, bg='white', font=("Arial Bold", 6), command=u15)
    d15.place(x=260, y=104)
    p_all.append(d15)

    d16 = Button(p_window, width=1, height=1, bg='white', font=("Arial Bold", 6), command=u16)
    d16.place(x=275, y=104)
    p_all.append(d16)

    d17 = Button(p_window, width=1, height=1, bg='white', font=("Arial Bold", 6), command=u17)
    d17.place(x=290, y=104)
    p_all.append(d17)

    d18 = Button(p_window, width=1, height=1, bg='white', font=("Arial Bold", 6), command=u18)
    d18.place(x=305, y=104)
    p_all.append(d18)

    d19 = Button(p_window, width=1, height=1, bg='white', font=("Arial Bold", 6), command=u19)
    d19.place(x=320, y=104)
    p_all.append(d19)

    d20 = Button(p_window, width=1, height=1, bg='white', font=("Arial Bold", 6), command=u20)
    d20.place(x=335, y=104)
    p_all.append(d20)

    d21 = Button(p_window, width=1, height=1, bg='white', font=("Arial Bold", 6), command=u21)
    d21.place(x=350, y=104)
    p_all.append(d21)

    d22 = Button(p_window, width=1, height=1, bg='white', font=("Arial Bold", 6), command=u22)
    d22.place(x=365, y=104)
    p_all.append(d22)

    d23 = Button(p_window, width=1, height=1, bg='white', font=("Arial Bold", 6), command=u23)
    d23.place(x=380, y=104)
    p_all.append(d23)

    d24 = Button(p_window, width=1, height=1, bg='white', font=("Arial Bold", 6), command=u24)
    d24.place(x=395, y=104)
    p_all.append(d24)

    d25 = Button(p_window, width=1, height=1, bg='white', font=("Arial Bold", 6), command=u25)
    d25.place(x=410, y=104)
    p_all.append(d25)

    d26 = Button(p_window, width=1, height=1, bg='white', font=("Arial Bold", 6), command=u26)
    d26.place(x=425, y=104)
    p_all.append(d26)

    d27 = Button(p_window, width=1, height=1, bg='white', font=("Arial Bold", 6), command=u27)
    d27.place(x=440, y=104)
    p_all.append(d27)

    d28 = Button(p_window, width=1, height=1, bg='white', font=("Arial Bold", 6), command=u28)
    d28.place(x=455, y=104)
    p_all.append(d28)

    d29 = Button(p_window, width=1, height=1, bg='white', font=("Arial Bold", 6), command=u29)
    d29.place(x=470, y=104)
    p_all.append(d29)

    d30 = Button(p_window, width=1, height=1, bg='white', font=("Arial Bold", 6), command=u30)
    d30.place(x=485, y=104)
    p_all.append(d30)

    e1 = Button(p_window, width=1, height=1, bg='white', font=("Arial Bold", 6), command=v1)
    e1.place(x=50, y=122)
    p_all.append(e1)

    e2 = Button(p_window, width=1, height=1, bg='white', font=("Arial Bold", 6), command=v2)
    e2.place(x=65, y=122)
    p_all.append(e2)

    e3 = Button(p_window, width=1, height=1, bg='white', font=("Arial Bold", 6), command=v3)
    e3.place(x=80, y=122)
    p_all.append(e3)

    e4 = Button(p_window, width=1, height=1, bg='white', font=("Arial Bold", 6), command=v4)
    e4.place(x=95, y=122)
    p_all.append(e4)

    e5 = Button(p_window, width=1, height=1, bg='white', font=("Arial Bold", 6), command=v5)
    e5.place(x=110, y=122)
    p_all.append(e5)

    e6 = Button(p_window, width=1, height=1, bg='white', font=("Arial Bold", 6), command=v6)
    e6.place(x=125, y=122)
    p_all.append(e6)

    e7 = Button(p_window, width=1, height=1, bg='white', font=("Arial Bold", 6), command=v7)
    e7.place(x=140, y=122)
    p_all.append(e7)

    e8 = Button(p_window, width=1, height=1, bg='white', font=("Arial Bold", 6), command=v8)
    e8.place(x=155, y=122)
    p_all.append(e8)

    e9 = Button(p_window, width=1, height=1, bg='white', font=("Arial Bold", 6), command=v9)
    e9.place(x=170, y=122)
    p_all.append(e9)

    e10 = Button(p_window, width=1, height=1, bg='white', font=("Arial Bold", 6), command=v10)
    e10.place(x=185, y=122)
    p_all.append(e10)

    e11 = Button(p_window, width=1, height=1, bg='white', font=("Arial Bold", 6), command=v11)
    e11.place(x=200, y=122)
    p_all.append(e11)

    e12 = Button(p_window, width=1, height=1, bg='white', font=("Arial Bold", 6), command=v12)
    e12.place(x=215, y=122)
    p_all.append(e12)

    e13 = Button(p_window, width=1, height=1, bg='white', font=("Arial Bold", 6), command=v13)
    e13.place(x=230, y=122)
    p_all.append(e13)

    e14 = Button(p_window, width=1, height=1, bg='white', font=("Arial Bold", 6), command=v14)
    e14.place(x=245, y=122)
    p_all.append(e14)

    e15 = Button(p_window, width=1, height=1, bg='white', font=("Arial Bold", 6), command=v15)
    e15.place(x=260, y=122)
    p_all.append(e15)

    e16 = Button(p_window, width=1, height=1, bg='white', font=("Arial Bold", 6), command=v16)
    e16.place(x=275, y=122)
    p_all.append(e16)

    e17 = Button(p_window, width=1, height=1, bg='white', font=("Arial Bold", 6), command=v17)
    e17.place(x=290, y=122)
    p_all.append(e17)

    e18 = Button(p_window, width=1, height=1, bg='white', font=("Arial Bold", 6), command=v18)
    e18.place(x=305, y=122)
    p_all.append(e18)

    e19 = Button(p_window, width=1, height=1, bg='white', font=("Arial Bold", 6), command=v19)
    e19.place(x=320, y=122)
    p_all.append(e19)

    e20 = Button(p_window, width=1, height=1, bg='white', font=("Arial Bold", 6), command=v20)
    e20.place(x=335, y=122)
    p_all.append(e20)

    e21 = Button(p_window, width=1, height=1, bg='white', font=("Arial Bold", 6), command=v21)
    e21.place(x=350, y=122)
    p_all.append(e21)

    e22 = Button(p_window, width=1, height=1, bg='white', font=("Arial Bold", 6), command=v22)
    e22.place(x=365, y=122)
    p_all.append(e22)

    e23 = Button(p_window, width=1, height=1, bg='white', font=("Arial Bold", 6), command=v23)
    e23.place(x=380, y=122)
    p_all.append(e23)

    e24 = Button(p_window, width=1, height=1, bg='white', font=("Arial Bold", 6), command=v24)
    e24.place(x=395, y=122)
    p_all.append(e24)

    e25 = Button(p_window, width=1, height=1, bg='white', font=("Arial Bold", 6), command=v25)
    e25.place(x=410, y=122)
    p_all.append(e25)

    e26 = Button(p_window, width=1, height=1, bg='white', font=("Arial Bold", 6), command=v26)
    e26.place(x=425, y=122)
    p_all.append(e26)

    e27 = Button(p_window, width=1, height=1, bg='white', font=("Arial Bold", 6), command=v27)
    e27.place(x=440, y=122)
    p_all.append(e27)

    e28 = Button(p_window, width=1, height=1, bg='white', font=("Arial Bold", 6), command=v28)
    e28.place(x=455, y=122)
    p_all.append(e28)

    e29 = Button(p_window, width=1, height=1, bg='white', font=("Arial Bold", 6), command=v29)
    e29.place(x=470, y=122)
    p_all.append(e29)

    e30 = Button(p_window, width=1, height=1, bg='white', font=("Arial Bold", 6), command=v30)
    e30.place(x=485, y=122)
    p_all.append(e30)

    f1 = Button(p_window, width=1, height=1, bg='white', font=("Arial Bold", 6), command=w1)
    f1.place(x=50, y=140)
    p_all.append(f1)

    f2 = Button(p_window, width=1, height=1, bg='white', font=("Arial Bold", 6), command=w2)
    f2.place(x=65, y=140)
    p_all.append(f2)

    f3 = Button(p_window, width=1, height=1, bg='white', font=("Arial Bold", 6), command=w3)
    f3.place(x=80, y=140)
    p_all.append(f3)

    f4 = Button(p_window, width=1, height=1, bg='white', font=("Arial Bold", 6), command=w4)
    f4.place(x=95, y=140)
    p_all.append(f4)

    f5 = Button(p_window, width=1, height=1, bg='white', font=("Arial Bold", 6), command=w5)
    f5.place(x=110, y=140)
    p_all.append(f5)

    f6 = Button(p_window, width=1, height=1, bg='white', font=("Arial Bold", 6), command=w6)
    f6.place(x=125, y=140)
    p_all.append(f6)

    f7 = Button(p_window, width=1, height=1, bg='white', font=("Arial Bold", 6), command=w7)
    f7.place(x=140, y=140)
    p_all.append(f7)

    f8 = Button(p_window, width=1, height=1, bg='white', font=("Arial Bold", 6), command=w8)
    f8.place(x=155, y=140)
    p_all.append(f8)

    f9 = Button(p_window, width=1, height=1, bg='white', font=("Arial Bold", 6), command=w9)
    f9.place(x=170, y=140)
    p_all.append(f9)

    f10 = Button(p_window, width=1, height=1, bg='white', font=("Arial Bold", 6), command=w10)
    f10.place(x=185, y=140)
    p_all.append(f10)

    f11 = Button(p_window, width=1, height=1, bg='white', font=("Arial Bold", 6), command=w11)
    f11.place(x=200, y=140)
    p_all.append(f11)

    f12 = Button(p_window, width=1, height=1, bg='white', font=("Arial Bold", 6), command=w12)
    f12.place(x=215, y=140)
    p_all.append(f12)

    f13 = Button(p_window, width=1, height=1, bg='white', font=("Arial Bold", 6), command=w13)
    f13.place(x=230, y=140)
    p_all.append(f13)

    f14 = Button(p_window, width=1, height=1, bg='white', font=("Arial Bold", 6), command=w14)
    f14.place(x=245, y=140)
    p_all.append(f14)

    f15 = Button(p_window, width=1, height=1, bg='white', font=("Arial Bold", 6), command=w15)
    f15.place(x=260, y=140)
    p_all.append(f15)

    f16 = Button(p_window, width=1, height=1, bg='white', font=("Arial Bold", 6), command=w16)
    f16.place(x=275, y=140)
    p_all.append(f16)

    f17 = Button(p_window, width=1, height=1, bg='white', font=("Arial Bold", 6), command=w17)
    f17.place(x=290, y=140)
    p_all.append(f17)

    f18 = Button(p_window, width=1, height=1, bg='white', font=("Arial Bold", 6), command=w18)
    f18.place(x=305, y=140)
    p_all.append(f18)

    f19 = Button(p_window, width=1, height=1, bg='white', font=("Arial Bold", 6), command=w19)
    f19.place(x=320, y=140)
    p_all.append(f19)

    f20 = Button(p_window, width=1, height=1, bg='white', font=("Arial Bold", 6), command=w20)
    f20.place(x=335, y=140)
    p_all.append(f20)

    f21 = Button(p_window, width=1, height=1, bg='white', font=("Arial Bold", 6), command=w21)
    f21.place(x=350, y=140)
    p_all.append(f21)

    f22 = Button(p_window, width=1, height=1, bg='white', font=("Arial Bold", 6), command=w22)
    f22.place(x=365, y=140)
    p_all.append(f22)

    f23 = Button(p_window, width=1, height=1, bg='white', font=("Arial Bold", 6), command=w23)
    f23.place(x=380, y=140)
    p_all.append(f23)

    f24 = Button(p_window, width=1, height=1, bg='white', font=("Arial Bold", 6), command=w24)
    f24.place(x=395, y=140)
    p_all.append(f24)

    f25 = Button(p_window, width=1, height=1, bg='white', font=("Arial Bold", 6), command=w25)
    f25.place(x=410, y=140)
    p_all.append(f25)

    f26 = Button(p_window, width=1, height=1, bg='white', font=("Arial Bold", 6), command=w26)
    f26.place(x=425, y=140)
    p_all.append(f26)

    f27 = Button(p_window, width=1, height=1, bg='white', font=("Arial Bold", 6), command=w27)
    f27.place(x=440, y=140)
    p_all.append(f27)

    f28 = Button(p_window, width=1, height=1, bg='white', font=("Arial Bold", 6), command=w28)
    f28.place(x=455, y=140)
    p_all.append(f28)

    f29 = Button(p_window, width=1, height=1, bg='white', font=("Arial Bold", 6), command=w29)
    f29.place(x=470, y=140)
    p_all.append(f29)

    f30 = Button(p_window, width=1, height=1, bg='white', font=("Arial Bold", 6), command=w30)
    f30.place(x=485, y=140)
    p_all.append(f30)

    g1 = Button(p_window, width=1, height=1, bg='white', font=("Arial Bold", 6), command=x1)
    g1.place(x=50, y=158)
    p_all.append(g1)

    g2 = Button(p_window, width=1, height=1, bg='white', font=("Arial Bold", 6), command=x2)
    g2.place(x=65, y=158)
    p_all.append(g2)

    g3 = Button(p_window, width=1, height=1, bg='white', font=("Arial Bold", 6), command=x3)
    g3.place(x=80, y=158)
    p_all.append(g3)

    g4 = Button(p_window, width=1, height=1, bg='white', font=("Arial Bold", 6), command=x4)
    g4.place(x=95, y=158)
    p_all.append(g4)

    g5 = Button(p_window, width=1, height=1, bg='white', font=("Arial Bold", 6), command=x5)
    g5.place(x=110, y=158)
    p_all.append(g5)

    g6 = Button(p_window, width=1, height=1, bg='white', font=("Arial Bold", 6), command=x6)
    g6.place(x=125, y=158)
    p_all.append(g6)

    g7 = Button(p_window, width=1, height=1, bg='white', font=("Arial Bold", 6), command=x7)
    g7.place(x=140, y=158)
    p_all.append(g7)

    g8 = Button(p_window, width=1, height=1, bg='white', font=("Arial Bold", 6), command=x8)
    g8.place(x=155, y=158)
    p_all.append(g8)

    g9 = Button(p_window, width=1, height=1, bg='white', font=("Arial Bold", 6), command=x9)
    g9.place(x=170, y=158)
    p_all.append(g9)

    g10 = Button(p_window, width=1, height=1, bg='white', font=("Arial Bold", 6), command=x10)
    g10.place(x=185, y=158)
    p_all.append(g10)

    g11 = Button(p_window, width=1, height=1, bg='white', font=("Arial Bold", 6), command=x11)
    g11.place(x=200, y=158)
    p_all.append(g11)

    g12 = Button(p_window, width=1, height=1, bg='white', font=("Arial Bold", 6), command=x12)
    g12.place(x=215, y=158)
    p_all.append(g12)

    g13 = Button(p_window, width=1, height=1, bg='white', font=("Arial Bold", 6), command=x13)
    g13.place(x=230, y=158)
    p_all.append(g13)

    g14 = Button(p_window, width=1, height=1, bg='white', font=("Arial Bold", 6), command=x14)
    g14.place(x=245, y=158)
    p_all.append(g14)

    g15 = Button(p_window, width=1, height=1, bg='white', font=("Arial Bold", 6), command=x15)
    g15.place(x=260, y=158)
    p_all.append(g15)

    g16 = Button(p_window, width=1, height=1, bg='white', font=("Arial Bold", 6), command=x16)
    g16.place(x=275, y=158)
    p_all.append(g16)

    g17 = Button(p_window, width=1, height=1, bg='white', font=("Arial Bold", 6), command=x17)
    g17.place(x=290, y=158)
    p_all.append(g17)

    g18 = Button(p_window, width=1, height=1, bg='white', font=("Arial Bold", 6), command=x18)
    g18.place(x=305, y=158)
    p_all.append(g18)

    g19 = Button(p_window, width=1, height=1, bg='white', font=("Arial Bold", 6), command=x19)
    g19.place(x=320, y=158)
    p_all.append(g19)

    g20 = Button(p_window, width=1, height=1, bg='white', font=("Arial Bold", 6), command=x20)
    g20.place(x=335, y=158)
    p_all.append(g20)

    g21 = Button(p_window, width=1, height=1, bg='white', font=("Arial Bold", 6), command=x21)
    g21.place(x=350, y=158)
    p_all.append(g21)

    g22 = Button(p_window, width=1, height=1, bg='white', font=("Arial Bold", 6), command=x22)
    g22.place(x=365, y=158)
    p_all.append(g22)

    g23 = Button(p_window, width=1, height=1, bg='white', font=("Arial Bold", 6), command=x23)
    g23.place(x=380, y=158)
    p_all.append(g23)

    g24 = Button(p_window, width=1, height=1, bg='white', font=("Arial Bold", 6), command=x24)
    g24.place(x=395, y=158)
    p_all.append(g24)

    g25 = Button(p_window, width=1, height=1, bg='white', font=("Arial Bold", 6), command=x25)
    g25.place(x=410, y=158)
    p_all.append(g25)

    g26 = Button(p_window, width=1, height=1, bg='white', font=("Arial Bold", 6), command=x26)
    g26.place(x=425, y=158)
    p_all.append(g26)

    g27 = Button(p_window, width=1, height=1, bg='white', font=("Arial Bold", 6), command=x27)
    g27.place(x=440, y=158)
    p_all.append(g27)

    g28 = Button(p_window, width=1, height=1, bg='white', font=("Arial Bold", 6), command=x28)
    g28.place(x=455, y=158)
    p_all.append(g28)

    g29 = Button(p_window, width=1, height=1, bg='white', font=("Arial Bold", 6), command=x29)
    g29.place(x=470, y=158)
    p_all.append(g29)

    g30 = Button(p_window, width=1, height=1, bg='white', font=("Arial Bold", 6), command=x30)
    g30.place(x=485, y=158)
    p_all.append(g30)

    h1 = Button(p_window, width=1, height=1, bg='white', font=("Arial Bold", 6), command=y1)
    h1.place(x=50, y=176)
    p_all.append(h1)

    h2 = Button(p_window, width=1, height=1, bg='white', font=("Arial Bold", 6), command=y2)
    h2.place(x=65, y=176)
    p_all.append(h2)

    h3 = Button(p_window, width=1, height=1, bg='white', font=("Arial Bold", 6), command=y3)
    h3.place(x=80, y=176)
    p_all.append(h3)

    h4 = Button(p_window, width=1, height=1, bg='white', font=("Arial Bold", 6), command=y4)
    h4.place(x=95, y=176)
    p_all.append(h4)

    h5 = Button(p_window, width=1, height=1, bg='white', font=("Arial Bold", 6), command=y5)
    h5.place(x=110, y=176)
    p_all.append(h5)

    h6 = Button(p_window, width=1, height=1, bg='white', font=("Arial Bold", 6), command=y6)
    h6.place(x=125, y=176)
    p_all.append(h6)

    h7 = Button(p_window, width=1, height=1, bg='white', font=("Arial Bold", 6), command=y7)
    h7.place(x=140, y=176)
    p_all.append(h7)

    h8 = Button(p_window, width=1, height=1, bg='white', font=("Arial Bold", 6), command=y8)
    h8.place(x=155, y=176)
    p_all.append(h8)

    h9 = Button(p_window, width=1, height=1, bg='white', font=("Arial Bold", 6), command=y9)
    h9.place(x=170, y=176)
    p_all.append(h9)

    h10 = Button(p_window, width=1, height=1, bg='white', font=("Arial Bold", 6), command=y10)
    h10.place(x=185, y=176)
    p_all.append(h10)

    h11 = Button(p_window, width=1, height=1, bg='white', font=("Arial Bold", 6), command=y11)
    h11.place(x=200, y=176)
    p_all.append(h11)

    h12 = Button(p_window, width=1, height=1, bg='white', font=("Arial Bold", 6), command=y12)
    h12.place(x=215, y=176)
    p_all.append(h12)

    h13 = Button(p_window, width=1, height=1, bg='white', font=("Arial Bold", 6), command=y13)
    h13.place(x=230, y=176)
    p_all.append(h13)

    h14 = Button(p_window, width=1, height=1, bg='white', font=("Arial Bold", 6), command=y14)
    h14.place(x=245, y=176)
    p_all.append(h14)

    h15 = Button(p_window, width=1, height=1, bg='white', font=("Arial Bold", 6), command=y15)
    h15.place(x=260, y=176)
    p_all.append(h15)

    h16 = Button(p_window, width=1, height=1, bg='white', font=("Arial Bold", 6), command=y16)
    h16.place(x=275, y=176)
    p_all.append(h16)

    h17 = Button(p_window, width=1, height=1, bg='white', font=("Arial Bold", 6), command=y17)
    h17.place(x=290, y=176)
    p_all.append(h17)

    h18 = Button(p_window, width=1, height=1, bg='white', font=("Arial Bold", 6), command=y18)
    h18.place(x=305, y=176)
    p_all.append(h18)

    h19 = Button(p_window, width=1, height=1, bg='white', font=("Arial Bold", 6), command=y19)
    h19.place(x=320, y=176)
    p_all.append(h19)

    h20 = Button(p_window, width=1, height=1, bg='white', font=("Arial Bold", 6), command=y20)
    h20.place(x=335, y=176)
    p_all.append(h20)

    h21 = Button(p_window, width=1, height=1, bg='white', font=("Arial Bold", 6), command=y21)
    h21.place(x=350, y=176)
    p_all.append(h21)

    h22 = Button(p_window, width=1, height=1, bg='white', font=("Arial Bold", 6), command=y22)
    h22.place(x=365, y=176)
    p_all.append(h22)

    h23 = Button(p_window, width=1, height=1, bg='white', font=("Arial Bold", 6), command=y23)
    h23.place(x=380, y=176)
    p_all.append(h23)

    h24 = Button(p_window, width=1, height=1, bg='white', font=("Arial Bold", 6), command=y24)
    h24.place(x=395, y=176)
    p_all.append(h24)

    h25 = Button(p_window, width=1, height=1, bg='white', font=("Arial Bold", 6), command=y25)
    h25.place(x=410, y=176)
    p_all.append(h25)

    h26 = Button(p_window, width=1, height=1, bg='white', font=("Arial Bold", 6), command=y26)
    h26.place(x=425, y=176)
    p_all.append(h26)

    h27 = Button(p_window, width=1, height=1, bg='white', font=("Arial Bold", 6), command=y27)
    h27.place(x=440, y=176)
    p_all.append(h27)

    h28 = Button(p_window, width=1, height=1, bg='white', font=("Arial Bold", 6), command=y28)
    h28.place(x=455, y=176)
    p_all.append(h28)

    h29 = Button(p_window, width=1, height=1, bg='white', font=("Arial Bold", 6), command=y29)
    h29.place(x=470, y=176)
    p_all.append(h29)

    h30 = Button(p_window, width=1, height=1, bg='white', font=("Arial Bold", 6), command=y30)
    h30.place(x=485, y=176)
    p_all.append(h30)

    p_save_button = Button(p_window, text='Сохранить', bg='#9be0b4', width=10, font=('Times New Roman', 16),
                           command=p_save)
    p_save_button.place(x=50, y=220)

    p_delete_button = Button(p_window, text='Удалить', bg='#e69b93', width=10, font=('Times New Roman', 16),
                             command=p_delete)
    p_delete_button.place(x=210, y=220)

    p_open_button = Button(p_window, text='Открыть', bg='#e0dc9b', width=10, font=('Times New Roman', 16),
                           command=p_open)
    p_open_button.place(x=370, y=220)

    p_off = Button(p_window, text='⌂', font=('Arial Bold', 15), width=2, height=1, bg='black', fg='white',
                   command=p_to_home)
    p_off.place(x=0, y=5)
    ToolTip(p_off, 'На главную...')

    p_window.pack()


def Saper():
    s = SaperGlobals()

    def Return():
        try:
            s.stat_window.destroy()
        except AttributeError:
            pass

        try:
            s.params_window.destroy()
        except AttributeError:
            pass

        s_title.destroy()
        restart_button.destroy()
        info_label.destroy()
        off.destroy()
        s_box_a1.destroy()
        s_box_a2.destroy()
        s_box_a3.destroy()
        s_box_a4.destroy()
        s_box_a5.destroy()
        s_box_b1.destroy()
        s_box_b2.destroy()
        s_box_b3.destroy()
        s_box_b4.destroy()
        s_box_b5.destroy()
        s_box_c1.destroy()
        s_box_c2.destroy()
        s_box_c3.destroy()
        s_box_c4.destroy()
        s_box_c5.destroy()
        s_box_d1.destroy()
        s_box_d2.destroy()
        s_box_d3.destroy()
        s_box_d4.destroy()
        s_box_d5.destroy()
        s_box_e1.destroy()
        s_box_e2.destroy()
        s_box_e3.destroy()
        s_box_e4.destroy()
        s_box_e5.destroy()
        stat_button.destroy()
        param_button.destroy()
        home()
        window.configure(width=700, height=m.abs_height)
        center_window(root, 678, m.abs_height)

    def NewGame():
        s.start_flag = True
        s.to_flags_list = [False, False, False, False, False, False, False, False, False, False, False, False, False,
                           False, False, False, False, False, False, False, False, False, False, False, False]
        s.box_list = [s_box_a1, s_box_a2, s_box_a3, s_box_a4, s_box_a5, s_box_b1, s_box_b2, s_box_b3, s_box_b4,
                      s_box_b5, s_box_c1, s_box_c2, s_box_c3, s_box_c4, s_box_c5, s_box_d1, s_box_d2, s_box_d3,
                      s_box_d4, s_box_d5, s_box_e1, s_box_e2, s_box_e3, s_box_e4, s_box_e5]
        s_flags_list = [False, False, False, False, False, False, False, False, False, False, False, False, False,
                        False, False, False, False, False, False, False, False, False, False, False, False]
        s_numbers_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24]
        s.bomb_list = []
        for i in range(1, s.number_of_mines + 1):
            s_bomb_loc = choice(s_numbers_list)
            s_numbers_list.remove(s_bomb_loc)
            s_flags_list[s_bomb_loc] = True
            s.bomb_list.append(s.box_list[s_bomb_loc])
        for i in range(len(s.bomb_list)):
            s.box_list.remove(s.bomb_list[i])
        s.global_flag = True
        s.flag_a1, s.flag_a2, s.flag_a3, s.flag_a4, s.flag_a5, s.flag_b1, s.flag_b2, s.flag_b3, s.flag_b4, s.flag_b5, \
            s.flag_c1, s.flag_c2, s.flag_c3, s.flag_c4, s.flag_c5, s.flag_d1, s.flag_d2, s.flag_d3, s.flag_d4, \
            s.flag_d5, s.flag_e1, s.flag_e2, s.flag_e3, s.flag_e4, s.flag_e5 = \
            s_flags_list[0], s_flags_list[1], s_flags_list[2], s_flags_list[3], s_flags_list[4], s_flags_list[5], \
            s_flags_list[6], s_flags_list[7], s_flags_list[8], s_flags_list[9], s_flags_list[10], s_flags_list[11], \
            s_flags_list[12], s_flags_list[13], s_flags_list[14], s_flags_list[15], s_flags_list[16], s_flags_list[17],\
            s_flags_list[18], s_flags_list[19], s_flags_list[20], s_flags_list[21], s_flags_list[22], s_flags_list[23],\
            s_flags_list[24]

        s.flags_array = [s.flag_a1, s.flag_a2, s.flag_a3, s.flag_a4, s.flag_a5, s.flag_b1, s.flag_b2, s.flag_b3,
                         s.flag_b4, s.flag_b5,
                         s.flag_c1, s.flag_c2, s.flag_c3, s.flag_c4, s.flag_c5, s.flag_d1, s.flag_d2, s.flag_d3,
                         s.flag_d4,
                         s.flag_d5, s.flag_e1, s.flag_e2, s.flag_e3, s.flag_e4, s.flag_e5]

    def GameOver():
        if s.global_flag:
            for i in range(len(s.bomb_list)):
                s.bomb_list[i].configure(bg='red')
            for i in range(len(s.box_list)):
                s.box_list[i].configure(bg='white')
            info_label.configure(text='Вы проиграли!', fg='red')
            s.global_flag = False
            stat_list = load('MihaSoft Files/SaperStat.npy')
            numb_of_games = stat_list[0] + 1
            new_stat_list = [numb_of_games, stat_list[1]]
            save('MihaSoft Files/SaperStat', new_stat_list)
            if os.path.exists('MihaSoft Files/SoundFlagFile.miha'):
                Beep(1000, 500)

    def CheckWin():
        k = 0
        for i in range(len(s.box_list)):
            if s.box_list[i]['background'] != 'white':
                k += 1
        if k == 0:
            for i in range(len(s.box_list)):
                s.box_list[i].configure(bg='white')
            for i in range(len(s.bomb_list)):
                s.bomb_list[i].configure(bg='green')
            s.global_flag = False
            info_label.configure(text='Вы выиграли!', fg='green')
            stat_list = load('MihaSoft Files/SaperStat.npy')
            numb_of_games = stat_list[0] + 1
            numb_of_wins = stat_list[1] + 1
            new_stat_list = [numb_of_games, numb_of_wins]
            save('MihaSoft Files/SaperStat', new_stat_list)
            if os.path.exists('MihaSoft Files/SoundFlagFile.miha'):
                Beep(500, 400)
                window.after(30, Beep(500, 400))
                window.after(30, Beep(500, 400))

    def RestartGame():
        NewGame()
        info_label.configure(text='')
        s_box_list_2 = [s_box_a1, s_box_a2, s_box_a3, s_box_a4, s_box_a5, s_box_b1, s_box_b2, s_box_b3, s_box_b4,
                        s_box_b5,
                        s_box_c1, s_box_c2, s_box_c3, s_box_c4, s_box_c5, s_box_d1, s_box_d2, s_box_d3, s_box_d4,
                        s_box_d5,
                        s_box_e1, s_box_e2, s_box_e3, s_box_e4, s_box_e5]
        for i in range(len(s_box_list_2)):
            s_box_list_2[i].configure(bg='#7a9cd6', text='')

    def to_flag_1(full=None):
        if s_box_a1['background'] != 'white':
            if not s.to_flags_list[0]:
                s.to_flags_list[0] = True
                s_box_a1.configure(bg='yellow')
            else:
                s.to_flags_list[0] = False
                s_box_a1.configure(bg='#7a9cd6')
        return full

    def to_flag_2(full=None):
        if s_box_a2['background'] != 'white':
            if not s.to_flags_list[1]:
                s.to_flags_list[1] = True
                s_box_a2.configure(bg='yellow')
            else:
                s.to_flags_list[1] = False
                s_box_a2.configure(bg='#7a9cd6')
        return full

    def to_flag_3(full=None):
        if s_box_a3['background'] != 'white':
            if not s.to_flags_list[2]:
                s.to_flags_list[2] = True
                s_box_a3.configure(bg='yellow')
            else:
                s.to_flags_list[2] = False
                s_box_a3.configure(bg='#7a9cd6')
        return full

    def to_flag_4(full=None):
        if s_box_a4['background'] != 'white':
            if not s.to_flags_list[3]:
                s.to_flags_list[3] = True
                s_box_a4.configure(bg='yellow')
            else:
                s.to_flags_list[3] = False
                s_box_a4.configure(bg='#7a9cd6')
        return full

    def to_flag_5(full=None):
        if s_box_a5['background'] != 'white':
            if not s.to_flags_list[4]:
                s.to_flags_list[4] = True
                s_box_a5.configure(bg='yellow')
            else:
                s.to_flags_list[4] = False
                s_box_a5.configure(bg='#7a9cd6')
        return full

    def to_flag_6(full=None):
        if s_box_b1['background'] != 'white':
            if not s.to_flags_list[5]:
                s.to_flags_list[5] = True
                s_box_b1.configure(bg='yellow')
            else:
                s.to_flags_list[5] = False
                s_box_b1.configure(bg='#7a9cd6')
        return full

    def to_flag_7(full=None):
        if s_box_b2['background'] != 'white':
            if not s.to_flags_list[6]:
                s.to_flags_list[6] = True
                s_box_b2.configure(bg='yellow')
            else:
                s.to_flags_list[6] = False
                s_box_b2.configure(bg='#7a9cd6')
        return full

    def to_flag_8(full=None):
        if s_box_b3['background'] != 'white':
            if not s.to_flags_list[7]:
                s.to_flags_list[7] = True
                s_box_b3.configure(bg='yellow')
            else:
                s.to_flags_list[7] = False
                s_box_b3.configure(bg='#7a9cd6')
        return full

    def to_flag_9(full=None):
        if s_box_b4['background'] != 'white':
            if not s.to_flags_list[8]:
                s.to_flags_list[8] = True
                s_box_b4.configure(bg='yellow')
            else:
                s.to_flags_list[8] = False
                s_box_b4.configure(bg='#7a9cd6')
        return full

    def to_flag_10(full=None):
        if s_box_b5['background'] != 'white':
            if not s.to_flags_list[9]:
                s.to_flags_list[9] = True
                s_box_b5.configure(bg='yellow')
            else:
                s.to_flags_list[9] = False
                s_box_b5.configure(bg='#7a9cd6')
        return full

    def to_flag_11(full=None):
        if s_box_c1['background'] != 'white':
            if not s.to_flags_list[10]:
                s.to_flags_list[10] = True
                s_box_c1.configure(bg='yellow')
            else:
                s.to_flags_list[10] = False
                s_box_c1.configure(bg='#7a9cd6')
        return full

    def to_flag_12(full=None):
        if s_box_c2['background'] != 'white':
            if not s.to_flags_list[11]:
                s.to_flags_list[11] = True
                s_box_c2.configure(bg='yellow')
            else:
                s.to_flags_list[11] = False
                s_box_c2.configure(bg='#7a9cd6')
        return full

    def to_flag_13(full=None):
        if s_box_c3['background'] != 'white':
            if not s.to_flags_list[12]:
                s.to_flags_list[12] = True
                s_box_c3.configure(bg='yellow')
            else:
                s.to_flags_list[12] = False
                s_box_c3.configure(bg='#7a9cd6')
        return full

    def to_flag_14(full=None):
        if s_box_c4['background'] != 'white':
            if not s.to_flags_list[13]:
                s.to_flags_list[13] = True
                s_box_c4.configure(bg='yellow')
            else:
                s.to_flags_list[13] = False
                s_box_c4.configure(bg='#7a9cd6')
        return full

    def to_flag_15(full=None):
        if s_box_c5['background'] != 'white':
            if not s.to_flags_list[14]:
                s.to_flags_list[14] = True
                s_box_c5.configure(bg='yellow')
            else:
                s.to_flags_list[14] = False
                s_box_c5.configure(bg='#7a9cd6')
        return full

    def to_flag_16(full=None):
        if s_box_d1['background'] != 'white':
            if not s.to_flags_list[15]:
                s.to_flags_list[15] = True
                s_box_d1.configure(bg='yellow')
            else:
                s.to_flags_list[15] = False
                s_box_d1.configure(bg='#7a9cd6')
        return full

    def to_flag_17(full=None):
        if s_box_d2['background'] != 'white':
            if not s.to_flags_list[16]:
                s.to_flags_list[16] = True
                s_box_d2.configure(bg='yellow')
            else:
                s.to_flags_list[16] = False
                s_box_d2.configure(bg='#7a9cd6')
        return full

    def to_flag_18(full=None):
        if s_box_d3['background'] != 'white':
            if not s.to_flags_list[17]:
                s.to_flags_list[17] = True
                s_box_d3.configure(bg='yellow')
            else:
                s.to_flags_list[17] = False
                s_box_d3.configure(bg='#7a9cd6')
        return full

    def to_flag_19(full=None):
        if s_box_d4['background'] != 'white':
            if not s.to_flags_list[18]:
                s.to_flags_list[18] = True
                s_box_d4.configure(bg='yellow')
            else:
                s.to_flags_list[18] = False
                s_box_d4.configure(bg='#7a9cd6')
        return full

    def to_flag_20(full=None):
        if s_box_d5['background'] != 'white':
            if not s.to_flags_list[19]:
                s.to_flags_list[19] = True
                s_box_d5.configure(bg='yellow')
            else:
                s.to_flags_list[19] = False
                s_box_d5.configure(bg='#7a9cd6')
        return full

    def to_flag_21(full=None):
        if s_box_e1['background'] != 'white':
            if not s.to_flags_list[20]:
                s.to_flags_list[20] = True
                s_box_e1.configure(bg='yellow')
            else:
                s.to_flags_list[20] = False
                s_box_e1.configure(bg='#7a9cd6')
        return full

    def to_flag_22(full=None):
        if s_box_e2['background'] != 'white':
            if not s.to_flags_list[21]:
                s.to_flags_list[21] = True
                s_box_e2.configure(bg='yellow')
            else:
                s.to_flags_list[21] = False
                s_box_e2.configure(bg='#7a9cd6')
        return full

    def to_flag_23(full=None):
        if s_box_e3['background'] != 'white':
            if not s.to_flags_list[22]:
                s.to_flags_list[22] = True
                s_box_e3.configure(bg='yellow')
            else:
                s.to_flags_list[22] = False
                s_box_e3.configure(bg='#7a9cd6')
        return full

    def to_flag_24(full=None):
        if s_box_e4['background'] != 'white':
            if not s.to_flags_list[23]:
                s.to_flags_list[23] = True
                s_box_e4.configure(bg='yellow')
            else:
                s.to_flags_list[23] = False
                s_box_e4.configure(bg='#7a9cd6')
        return full

    def to_flag_25(full=None):
        if s_box_e5['background'] != 'white':
            if not s.to_flags_list[24]:
                s.to_flags_list[24] = True
                s_box_e5.configure(bg='yellow')
            else:
                s.to_flags_list[24] = False
                s_box_e5.configure(bg='#7a9cd6')
        return full

    def s_open_box_1(box, flag_1, flag_2, flag_3):
        k = 0
        listok = [flag_1, flag_2, flag_3]
        for j in range(len(listok)):
            if listok[j]:
                k += 1
        box.configure(text=k, bg='white')
        CheckWin()

    def on_a1():
        if os.path.exists('MihaSoft Files/SoundFlagFile.miha'):
            Beep(300, 50)
        if s.global_flag and not s.to_flags_list[0]:
            if not s.flag_a1:
                if s.start_flag:
                    s.start_flag = False
                s_open_box_1(s_box_a1, s.flag_a2, s.flag_b2, s.flag_b1)
            else:
                if s.start_flag:
                    while s.flag_a1:
                        RestartGame()
                    s_open_box_1(s_box_a1, s.flag_a2, s.flag_b2, s.flag_b1)
                    s.start_flag = False
                else:
                    GameOver()

    def on_a5():
        if os.path.exists('MihaSoft Files/SoundFlagFile.miha'):
            Beep(300, 50)
        if s.global_flag and not s.to_flags_list[4]:
            if not s.flag_a5:
                if s.start_flag:
                    s.start_flag = False
                s_open_box_1(s_box_a5, s.flag_a4, s.flag_b4, s.flag_b5)
            else:
                if s.start_flag:
                    while s.flag_a5:
                        RestartGame()
                    s_open_box_1(s_box_a5, s.flag_a4, s.flag_b4, s.flag_b5)
                    s.start_flag = False
                else:
                    GameOver()

    def on_e1():
        if os.path.exists('MihaSoft Files/SoundFlagFile.miha'):
            Beep(300, 50)
        if s.global_flag and not s.to_flags_list[20]:
            if not s.flag_e1:
                if s.start_flag:
                    s.start_flag = False

                s_open_box_1(s_box_e1, s.flag_d1, s.flag_d2, s.flag_e2)
            else:
                if s.start_flag:
                    while s.flag_e1:
                        RestartGame()
                    s_open_box_1(s_box_e1, s.flag_d1, s.flag_d2, s.flag_e2)
                    s.start_flag = False
                else:
                    GameOver()

    def on_e5():
        if os.path.exists('MihaSoft Files/SoundFlagFile.miha'):
            Beep(300, 50)
        if s.global_flag and not s.to_flags_list[24]:
            if not s.flag_e5:
                if s.start_flag:
                    s.start_flag = False
                s_open_box_1(s_box_e5, s.flag_e4, s.flag_d4, s.flag_d5)

            else:
                if s.start_flag:
                    while s.flag_e5:
                        RestartGame()
                    s_open_box_1(s_box_e5, s.flag_e4, s.flag_d4, s.flag_d5)
                    s.start_flag = False
                else:
                    GameOver()

    def s_open_box_2(box, flag_1, flag_2, flag_3, flag_4, flag_5):
        k = 0
        listok = [flag_1, flag_2, flag_3, flag_4, flag_5]
        for j in range(len(listok)):
            if listok[j]:
                k += 1
        box.configure(text=k, bg='white')
        CheckWin()

    def on_a2():
        if os.path.exists('MihaSoft Files/SoundFlagFile.miha'):
            Beep(300, 50)
        if s.global_flag and not s.to_flags_list[1]:
            if not s.flag_a2:
                if s.start_flag:
                    s.start_flag = False
                s_open_box_2(s_box_a2, s.flag_a1, s.flag_b1, s.flag_b2, s.flag_b3, s.flag_a3)

            else:
                if s.start_flag:
                    while s.flag_a2:
                        RestartGame()
                    s_open_box_2(s_box_a2, s.flag_a1, s.flag_b1, s.flag_b2, s.flag_b3, s.flag_a3)
                    s.start_flag = False
                else:
                    GameOver()

    def on_a3():
        if os.path.exists('MihaSoft Files/SoundFlagFile.miha'):
            Beep(300, 50)
        if s.global_flag and not s.to_flags_list[2]:
            if not s.flag_a3:
                if s.start_flag:
                    s.start_flag = False
                s_open_box_2(s_box_a3, s.flag_a2, s.flag_b2, s.flag_b3, s.flag_b4, s.flag_a4)

            else:
                if s.start_flag:
                    while s.flag_a3:
                        RestartGame()
                    s_open_box_2(s_box_a3, s.flag_a2, s.flag_b2, s.flag_b3, s.flag_b4, s.flag_a4)
                    s.start_flag = False
                else:
                    GameOver()

    def on_a4():
        if os.path.exists('MihaSoft Files/SoundFlagFile.miha'):
            Beep(300, 50)
        if s.global_flag and not s.to_flags_list[3]:
            if not s.flag_a4:
                if s.start_flag:
                    s.start_flag = False
                s_open_box_2(s_box_a4, s.flag_a3, s.flag_b3, s.flag_b4, s.flag_b5, s.flag_a5)

            else:
                if s.start_flag:
                    while s.flag_a4:
                        RestartGame()
                    s_open_box_2(s_box_a4, s.flag_a3, s.flag_b3, s.flag_b4, s.flag_b5, s.flag_a5)
                    s.start_flag = False
                else:
                    GameOver()

    def on_b1():
        if os.path.exists('MihaSoft Files/SoundFlagFile.miha'):
            Beep(300, 50)
        if s.global_flag and not s.to_flags_list[5]:
            if not s.flag_b1:
                if s.start_flag:
                    s.start_flag = False
                s_open_box_2(s_box_b1, s.flag_a1, s.flag_a2, s.flag_b2, s.flag_c2, s.flag_c1)

            else:
                if s.start_flag:
                    while s.flag_b1:
                        RestartGame()
                    s_open_box_2(s_box_b1, s.flag_a1, s.flag_a2, s.flag_b2, s.flag_c2, s.flag_c1)
                    s.start_flag = False
                else:
                    GameOver()

    def on_c1():
        if os.path.exists('MihaSoft Files/SoundFlagFile.miha'):
            Beep(300, 50)
        if s.global_flag and not s.to_flags_list[10]:
            if not s.flag_c1:
                if s.start_flag:
                    s.start_flag = False
                s_open_box_2(s_box_c1, s.flag_b1, s.flag_b2, s.flag_c2, s.flag_d2, s.flag_d1)

            else:
                if s.start_flag:
                    while s.flag_c1:
                        RestartGame()
                    s_open_box_2(s_box_c1, s.flag_b1, s.flag_b2, s.flag_c2, s.flag_d2, s.flag_d1)
                    s.start_flag = False
                else:
                    GameOver()

    def on_d1():
        if os.path.exists('MihaSoft Files/SoundFlagFile.miha'):
            Beep(300, 50)
        if s.global_flag and not s.to_flags_list[15]:
            if not s.flag_d1:
                if s.start_flag:
                    s.start_flag = False
                s_open_box_2(s_box_d1, s.flag_c1, s.flag_c2, s.flag_d2, s.flag_e2, s.flag_e1)

            else:
                if s.start_flag:
                    while s.flag_d1:
                        RestartGame()
                    s_open_box_2(s_box_d1, s.flag_c1, s.flag_c2, s.flag_d2, s.flag_e2, s.flag_e1)
                    s.start_flag = False
                else:
                    GameOver()

    def on_e2():
        if os.path.exists('MihaSoft Files/SoundFlagFile.miha'):
            Beep(300, 50)
        if s.global_flag and not s.to_flags_list[21]:
            if not s.flag_e2:
                if s.start_flag:
                    s.start_flag = False
                s_open_box_2(s_box_e2, s.flag_e1, s.flag_d1, s.flag_d2, s.flag_d3, s.flag_e3)

            else:
                if s.start_flag:
                    while s.flag_e2:
                        RestartGame()
                    s_open_box_2(s_box_e2, s.flag_e1, s.flag_d1, s.flag_d2, s.flag_d3, s.flag_e3)
                    s.start_flag = False
                else:
                    GameOver()

    def on_e3():
        if os.path.exists('MihaSoft Files/SoundFlagFile.miha'):
            Beep(300, 50)
        if s.global_flag and not s.to_flags_list[22]:
            if not s.flag_e3:
                if s.start_flag:
                    s.start_flag = False
                s_open_box_2(s_box_e3, s.flag_e2, s.flag_d2, s.flag_d3, s.flag_d4, s.flag_e4)

            else:
                if s.start_flag:
                    while s.flag_e3:
                        RestartGame()
                    s_open_box_2(s_box_e3, s.flag_e2, s.flag_d2, s.flag_d3, s.flag_d4, s.flag_e4)
                    s.start_flag = False
                else:
                    GameOver()

    def on_e4():
        if os.path.exists('MihaSoft Files/SoundFlagFile.miha'):
            Beep(300, 50)
        if s.global_flag and not s.to_flags_list[23]:
            if not s.flag_e4:
                if s.start_flag:
                    s.start_flag = False
                s_open_box_2(s_box_e4, s.flag_e3, s.flag_d3, s.flag_d4, s.flag_d5, s.flag_e5)

            else:
                if s.start_flag:
                    while s.flag_e4:
                        RestartGame()
                    s_open_box_2(s_box_e4, s.flag_e3, s.flag_d3, s.flag_d4, s.flag_d5, s.flag_e5)
                    s.start_flag = False
                else:
                    GameOver()

    def on_b5():
        if os.path.exists('MihaSoft Files/SoundFlagFile.miha'):
            Beep(300, 50)
        if s.global_flag and not s.to_flags_list[9]:
            if not s.flag_b5:
                if s.start_flag:
                    s.start_flag = False
                s_open_box_2(s_box_b5, s.flag_a5, s.flag_a4, s.flag_b4, s.flag_c4, s.flag_c5)

            else:
                if s.start_flag:
                    while s.flag_b5:
                        RestartGame()
                    s_open_box_2(s_box_b5, s.flag_a5, s.flag_a4, s.flag_b4, s.flag_c4, s.flag_c5)
                    s.start_flag = False
                else:
                    GameOver()

    def on_c5():
        if os.path.exists('MihaSoft Files/SoundFlagFile.miha'):
            Beep(300, 50)
        if s.global_flag and not s.to_flags_list[14]:
            if not s.flag_c5:
                if s.start_flag:
                    s.start_flag = False
                s_open_box_2(s_box_c5, s.flag_b5, s.flag_b4, s.flag_c4, s.flag_d4, s.flag_d5)

            else:
                if s.start_flag:
                    while s.flag_c5:
                        RestartGame()
                    s_open_box_2(s_box_c5, s.flag_b5, s.flag_b4, s.flag_c4, s.flag_d4, s.flag_d5)
                    s.start_flag = False
                else:
                    GameOver()

    def on_d5():
        if os.path.exists('MihaSoft Files/SoundFlagFile.miha'):
            Beep(300, 50)
        if s.global_flag and not s.to_flags_list[19]:
            if not s.flag_d5:
                if s.start_flag:
                    s.start_flag = False
                s_open_box_2(s_box_d5, s.flag_c5, s.flag_c4, s.flag_d4, s.flag_e4, s.flag_e5)

            else:
                if s.start_flag:
                    while s.flag_d5:
                        RestartGame()
                    s_open_box_2(s_box_d5, s.flag_c5, s.flag_c4, s.flag_d4, s.flag_e4, s.flag_e5)
                    s.start_flag = False
                else:
                    GameOver()

    def s_open_box_3(box, flag_1, flag_2, flag_3, flag_4, flag_5, flag_6, flag_7, flag_8):
        k = 0
        listok = [flag_1, flag_2, flag_3, flag_4, flag_5, flag_6, flag_7, flag_8]
        for j in range(len(listok)):
            if listok[j]:
                k += 1
        box.configure(text=k, bg='white')
        CheckWin()

    def on_b2():
        if os.path.exists('MihaSoft Files/SoundFlagFile.miha'):
            Beep(300, 50)
        if s.global_flag and not s.to_flags_list[6]:
            if not s.flag_b2:
                if s.start_flag:
                    s.start_flag = False
                s_open_box_3(s_box_b2, s.flag_a1, s.flag_a2, s.flag_a3, s.flag_b3, s.flag_c3, s.flag_c2,
                             s.flag_c1, s.flag_b1)

            else:
                if s.start_flag:
                    while s.flag_b2:
                        RestartGame()
                    s_open_box_3(s_box_b2, s.flag_a1, s.flag_a2, s.flag_a3, s.flag_b3, s.flag_c3, s.flag_c2,
                                 s.flag_c1, s.flag_b1)
                    s.start_flag = False
                else:
                    GameOver()

    def on_b3():
        if os.path.exists('MihaSoft Files/SoundFlagFile.miha'):
            Beep(300, 50)
        if s.global_flag and not s.to_flags_list[7]:
            if not s.flag_b3:
                if s.start_flag:
                    s.start_flag = False
                s_open_box_3(s_box_b3, s.flag_a2, s.flag_a3, s.flag_a4, s.flag_b4, s.flag_c4, s.flag_c3, s.flag_c2,
                             s.flag_b2)

            else:
                if s.start_flag:
                    while s.flag_b3:
                        RestartGame()
                    s_open_box_3(s_box_b3, s.flag_a2, s.flag_a3, s.flag_a4, s.flag_b4, s.flag_c4, s.flag_c3, s.flag_c2,
                                 s.flag_b2)
                    s.start_flag = False
                else:
                    GameOver()

    def on_b4():
        if os.path.exists('MihaSoft Files/SoundFlagFile.miha'):
            Beep(300, 50)
        if s.global_flag and not s.to_flags_list[8]:
            if not s.flag_b4:
                if s.start_flag:
                    s.start_flag = False
                s_open_box_3(s_box_b4, s.flag_a3, s.flag_a4, s.flag_a5, s.flag_b5, s.flag_c5, s.flag_c4, s.flag_c3,
                             s.flag_b3)

            else:
                if s.start_flag:
                    while s.flag_b4:
                        RestartGame()
                    s_open_box_3(s_box_b4, s.flag_a3, s.flag_a4, s.flag_a5, s.flag_b5, s.flag_c5, s.flag_c4, s.flag_c3,
                                 s.flag_b3)
                    s.start_flag = False
                else:
                    GameOver()

    def on_c2():
        if os.path.exists('MihaSoft Files/SoundFlagFile.miha'):
            Beep(300, 50)
        if s.global_flag and not s.to_flags_list[11]:
            if not s.flag_c2:
                if s.start_flag:
                    s.start_flag = False
                s_open_box_3(s_box_c2, s.flag_b1, s.flag_b2, s.flag_b3, s.flag_c3, s.flag_d3, s.flag_d2, s.flag_d1,
                             s.flag_c1)

            else:
                if s.start_flag:
                    while s.flag_c2:
                        RestartGame()
                    s_open_box_3(s_box_c2, s.flag_b1, s.flag_b2, s.flag_b3, s.flag_c3, s.flag_d3, s.flag_d2, s.flag_d1,
                                 s.flag_c1)
                    s.start_flag = False
                else:
                    GameOver()

    def on_c3():
        if os.path.exists('MihaSoft Files/SoundFlagFile.miha'):
            Beep(300, 50)
        if s.global_flag and not s.to_flags_list[12]:
            if not s.flag_c3:
                if s.start_flag:
                    s.start_flag = False
                s_open_box_3(s_box_c3, s.flag_b2, s.flag_b3, s.flag_b4, s.flag_c4, s.flag_d4, s.flag_d3, s.flag_d2,
                             s.flag_c2)

            else:
                if s.start_flag:
                    while s.flag_c3:
                        RestartGame()
                    s_open_box_3(s_box_c3, s.flag_b2, s.flag_b3, s.flag_b4, s.flag_c4, s.flag_d4, s.flag_d3, s.flag_d2,
                                 s.flag_c2)
                    s.start_flag = False
                else:
                    GameOver()

    def on_c4():
        if os.path.exists('MihaSoft Files/SoundFlagFile.miha'):
            Beep(300, 50)
        if s.global_flag and not s.to_flags_list[13]:
            if not s.flag_c4:
                if s.start_flag:
                    s.start_flag = False
                s_open_box_3(s_box_c4, s.flag_b3, s.flag_b4, s.flag_b5, s.flag_c5, s.flag_d5, s.flag_d4, s.flag_d3,
                             s.flag_c3)

            else:
                if s.start_flag:
                    while s.flag_c4:
                        RestartGame()
                    s_open_box_3(s_box_c4, s.flag_b3, s.flag_b4, s.flag_b5, s.flag_c5, s.flag_d5, s.flag_d4, s.flag_d3,
                                 s.flag_c3)
                    s.start_flag = False
                else:
                    GameOver()

    def on_d2():
        if os.path.exists('MihaSoft Files/SoundFlagFile.miha'):
            Beep(300, 50)
        if s.global_flag and not s.to_flags_list[16]:
            if not s.flag_d2:
                if s.start_flag:
                    s.start_flag = False
                s_open_box_3(s_box_d2, s.flag_c1, s.flag_c2, s.flag_c3, s.flag_d3, s.flag_e3, s.flag_e2, s.flag_e1,
                             s.flag_d1)

            else:
                if s.start_flag:
                    while s.flag_d2:
                        RestartGame()
                    s_open_box_3(s_box_d2, s.flag_c1, s.flag_c2, s.flag_c3, s.flag_d3, s.flag_e3, s.flag_e2, s.flag_e1,
                                 s.flag_d1)
                    s.start_flag = False
                else:
                    GameOver()

    def on_d3():
        if os.path.exists('MihaSoft Files/SoundFlagFile.miha'):
            Beep(300, 50)
        if s.global_flag and not s.to_flags_list[17]:
            if not s.flag_d3:
                if s.start_flag:
                    s.start_flag = False
                s_open_box_3(s_box_d3, s.flag_c2, s.flag_c3, s.flag_c4, s.flag_d4, s.flag_e4, s.flag_e3, s.flag_e2,
                             s.flag_d2)

            else:
                if s.start_flag:
                    while s.flag_d3:
                        RestartGame()
                    s_open_box_3(s_box_d3, s.flag_c2, s.flag_c3, s.flag_c4, s.flag_d4, s.flag_e4, s.flag_e3, s.flag_e2,
                                 s.flag_d2)
                    s.start_flag = False
                else:
                    GameOver()

    def on_d4():
        if os.path.exists('MihaSoft Files/SoundFlagFile.miha'):
            Beep(300, 50)
        if s.global_flag and not s.to_flags_list[18]:
            if not s.flag_d4:
                if s.start_flag:
                    s.start_flag = False
                s_open_box_3(s_box_d4, s.flag_c3, s.flag_c4, s.flag_c5, s.flag_d5, s.flag_e5, s.flag_e4, s.flag_e3,
                             s.flag_d3)

            else:
                if s.start_flag:
                    while s.flag_d4:
                        RestartGame()
                    s_open_box_3(s_box_d4, s.flag_c3, s.flag_c4, s.flag_c5, s.flag_d5, s.flag_e5, s.flag_e4, s.flag_e3,
                                 s.flag_d3)
                    s.start_flag = False
                else:
                    GameOver()

    def Statistics():
        def CleanStat():
            s_stats_start_list = [0, 0]
            save('MihaSoft Files/SaperStat', s_stats_start_list)
            s.stat_window.destroy()

        def Close():
            s.stat_window.destroy()

        def s_create_stat_window():
            s.stat_window = Toplevel()
            center_window(s.stat_window, 200, 220)
            s.stat_window.resizable(False, False)
            s.stat_window.title('Статистика')

            first_label = Label(s.stat_window, text='Побед:')
            first_label.place(x=5, y=5)

            second_label = Label(s.stat_window, text='Всего игр:')
            second_label.place(x=5, y=50)

            third_label = Label(s.stat_window, text='Процент выигрышей:')
            third_label.place(x=5, y=95)

            s_stat_list = load('MihaSoft Files/SaperStat.npy')

            if s_stat_list[0] == 0:
                percent = '0%'

            else:
                percent = str(int((s_stat_list[1] / s_stat_list[0]) * 100)) + '%'

            wins = Label(s.stat_window, text=s_stat_list[1])
            wins.place(x=150, y=5)

            games = Label(s.stat_window, text=s_stat_list[0])
            games.place(x=150, y=50)

            percents = Label(s.stat_window, text=percent)
            percents.place(x=150, y=95)

            clean_button = Button(s.stat_window, text='Очистить статистику', bg='#db9c9c', command=CleanStat)
            clean_button.place(x=30, y=135)

            close_button = Button(s.stat_window, text='ОК', bg='#b6e0e0', width=16, command=Close)
            close_button.place(x=32, y=170)

        try:
            s.stat_window.resizable(False, False)

        except AttributeError:
            s_create_stat_window()

        except TclError:
            s_create_stat_window()

    def s_params():
        def s_params_abort():
            s.params_window.destroy()

        def s_create_par_window():
            def s_params_ok():
                s.number_of_mines = int(s_params_combobox.get())
                RestartGame()
                s.params_window.destroy()

            s.params_window = Toplevel()
            center_window(s.params_window, 180, 100)
            s.params_window.resizable(False, False)
            s.params_window.title('Параметры')

            s_p_m = []
            for i in range(1, 24):
                s_p_m.append(str(i))

            s_params_label = Label(s.params_window, text='Выберите число мин:')
            s_params_label.place(x=5, y=5)

            s_params_combobox = ttk.Combobox(s.params_window, values=s_p_m, state='readonly')
            s_params_combobox.place(x=10, y=30)

            s_params_ok_button = Button(s.params_window, text='OK', width=6, command=s_params_ok)
            s_params_ok_button.place(x=10, y=60)

            s_params_abort_button = Button(s.params_window, text='Отмена', width=6, command=s_params_abort)
            s_params_abort_button.place(x=95, y=60)

        try:
            s.params_window.resizable(False, False)

        except AttributeError:
            s_create_par_window()

        except TclError:
            s_create_par_window()

    if not os.path.exists('MihaSoft Files/SaperStat.npy'):
        s_stat_start_list = [0, 0]
        save('MihaSoft Files/SaperStat', s_stat_start_list)

    center_window(root, 430, 450)
    window.configure(width=430, height=450)
    root.title('Saper 2.0')
    root.minsize(430, 450)

    s_title = Label(window, text='Saper 2.0', font=('Arial Bold', 16), fg='red')
    s_title.place(x=50, y=10)

    s_box_a1 = Button(window, width=6, height=3, bg='#7a9cd6', command=on_a1)
    s_box_a1.place(x=80, y=100)

    s_box_a2 = Button(window, width=6, height=3, bg='#7a9cd6', command=on_a2)
    s_box_a2.place(x=132, y=100)

    s_box_a3 = Button(window, width=6, height=3, bg='#7a9cd6', command=on_a3)
    s_box_a3.place(x=184, y=100)

    s_box_a4 = Button(window, width=6, height=3, bg='#7a9cd6', command=on_a4)
    s_box_a4.place(x=236, y=100)

    s_box_a5 = Button(window, width=6, height=3, bg='#7a9cd6', command=on_a5)
    s_box_a5.place(x=288, y=100)

    s_box_b1 = Button(window, width=6, height=3, bg='#7a9cd6', command=on_b1)
    s_box_b1.place(x=80, y=156)

    s_box_b2 = Button(window, width=6, height=3, bg='#7a9cd6', command=on_b2)
    s_box_b2.place(x=132, y=156)

    s_box_b3 = Button(window, width=6, height=3, bg='#7a9cd6', command=on_b3)
    s_box_b3.place(x=184, y=156)

    s_box_b4 = Button(window, width=6, height=3, bg='#7a9cd6', command=on_b4)
    s_box_b4.place(x=236, y=156)

    s_box_b5 = Button(window, width=6, height=3, bg='#7a9cd6', command=on_b5)
    s_box_b5.place(x=288, y=156)

    s_box_c1 = Button(window, width=6, height=3, bg='#7a9cd6', command=on_c1)
    s_box_c1.place(x=80, y=212)

    s_box_c2 = Button(window, width=6, height=3, bg='#7a9cd6', command=on_c2)
    s_box_c2.place(x=132, y=212)

    s_box_c3 = Button(window, width=6, height=3, bg='#7a9cd6', command=on_c3)
    s_box_c3.place(x=184, y=212)

    s_box_c4 = Button(window, width=6, height=3, bg='#7a9cd6', command=on_c4)
    s_box_c4.place(x=236, y=212)

    s_box_c5 = Button(window, width=6, height=3, bg='#7a9cd6', command=on_c5)
    s_box_c5.place(x=288, y=212)

    s_box_d1 = Button(window, width=6, height=3, bg='#7a9cd6', command=on_d1)
    s_box_d1.place(x=80, y=268)

    s_box_d2 = Button(window, width=6, height=3, bg='#7a9cd6', command=on_d2)
    s_box_d2.place(x=132, y=268)

    s_box_d3 = Button(window, width=6, height=3, bg='#7a9cd6', command=on_d3)
    s_box_d3.place(x=184, y=268)

    s_box_d4 = Button(window, width=6, height=3, bg='#7a9cd6', command=on_d4)
    s_box_d4.place(x=236, y=268)

    s_box_d5 = Button(window, width=6, height=3, bg='#7a9cd6', command=on_d5)
    s_box_d5.place(x=288, y=268)

    s_box_e1 = Button(window, width=6, height=3, bg='#7a9cd6', command=on_e1)
    s_box_e1.place(x=80, y=324)

    s_box_e2 = Button(window, width=6, height=3, bg='#7a9cd6', command=on_e2)
    s_box_e2.place(x=132, y=324)

    s_box_e3 = Button(window, width=6, height=3, bg='#7a9cd6', command=on_e3)
    s_box_e3.place(x=184, y=324)

    s_box_e4 = Button(window, width=6, height=3, bg='#7a9cd6', command=on_e4)
    s_box_e4.place(x=236, y=324)

    s_box_e5 = Button(window, width=6, height=3, bg='#7a9cd6', command=on_e5)
    s_box_e5.place(x=288, y=324)

    restart_button = Button(window, text='Новая игра', width=10, bg='#93e6a8', font=('Arial Bold', 12),
                            command=RestartGame)
    restart_button.place(x=300, y=10)

    info_label = Label(window, font=('Arial Bold', 16))
    info_label.place(x=138, y=400)

    stat_button = Button(window, text='Статистика', width=10, bg='#d9c786', font=('Arial Bold', 12), command=Statistics)
    stat_button.place(x=180, y=10)

    param_button = Button(window, text='Параметры', width=10, bg='#a8a8a8', font=('Arial Bold', 12), command=s_params)
    param_button.place(x=300, y=50)

    NewGame()

    s_box_a1.bind('<Button-3>', to_flag_1)
    s_box_a2.bind('<Button-3>', to_flag_2)
    s_box_a3.bind('<Button-3>', to_flag_3)
    s_box_a4.bind('<Button-3>', to_flag_4)
    s_box_a5.bind('<Button-3>', to_flag_5)
    s_box_b1.bind('<Button-3>', to_flag_6)
    s_box_b2.bind('<Button-3>', to_flag_7)
    s_box_b3.bind('<Button-3>', to_flag_8)
    s_box_b4.bind('<Button-3>', to_flag_9)
    s_box_b5.bind('<Button-3>', to_flag_10)
    s_box_c1.bind('<Button-3>', to_flag_11)
    s_box_c2.bind('<Button-3>', to_flag_12)
    s_box_c3.bind('<Button-3>', to_flag_13)
    s_box_c4.bind('<Button-3>', to_flag_14)
    s_box_c5.bind('<Button-3>', to_flag_15)
    s_box_d1.bind('<Button-3>', to_flag_16)
    s_box_d2.bind('<Button-3>', to_flag_17)
    s_box_d3.bind('<Button-3>', to_flag_18)
    s_box_d4.bind('<Button-3>', to_flag_19)
    s_box_d5.bind('<Button-3>', to_flag_20)
    s_box_e1.bind('<Button-3>', to_flag_21)
    s_box_e2.bind('<Button-3>', to_flag_22)
    s_box_e3.bind('<Button-3>', to_flag_23)
    s_box_e4.bind('<Button-3>', to_flag_24)
    s_box_e5.bind('<Button-3>', to_flag_25)
    off = Button(window, text='⌂', font=('Arial Bold', 15), width=2, height=1, bg='black', fg='white',
                 command=Return)
    off.place(x=0, y=5)
    ToolTip(off, 'На главную...')


def TurtlePaint():
    def tp_help():
        def tp_help_ok():
            tp.help_window.destroy()

        def tp_create_help_window():
            tp.help_window = Toplevel()
            center_window(tp.help_window, 470, 190)
            tp.help_window.resizable(False, False)
            tp.help_window.title('TurtlePaint - справка')

            paint_help_text = '''
При опущенном пере:
Левая кнопка мыши - провести линию;
Правая кнопка мыши - закрасить последнюю начертанную фигуру,
поднять перо.

При поднятом пере:
Левая кнопка мыши - переместить перо;
Правая кнопка мыши - опустить перо.
                        '''
            paint_help_label = Label(tp.help_window, text=paint_help_text)
            paint_help_label.pack()

            tp_help_button = Button(tp.help_window, text='ОK', bg='#b8b8b8', command=tp_help_ok, width=10)
            tp_help_button.place(x=335, y=150)

        try:
            tp.help_window.resizable(False, False)

        except AttributeError:
            tp_create_help_window()

        except TclError:
            tp_create_help_window()

    def paint_save():
        paint_window.setup(width=1.0, height=1.0)
        root.state('iconic')
        sleep(0.3)
        paint_image = capture_screen()
        sleep(0.3)
        root.state('normal')
        paint_window.setup(800, 600)
        paint_file = asksaveasfile(title='Сохранить файл', defaultextension='.png',
                                   filetypes=(('PNG file', '*.png'), ('All Files', '*.*')))
        if paint_file:
            paint_image.save(paint_file.name)

    def paint_destroy():
        try:
            paint_window.bye()
        finally:
            try:
                tp.help_window.destroy()
            except AttributeError:
                pass

            paint_off.destroy()
            paint_save_button.destroy()
            paint_help_button.destroy()
            paint_color_button.destroy()
            paint_label.destroy()
            home()
            window.configure(width=700, height=m.abs_height)
            center_window(root, 678, m.abs_height)

    def tp_choose_color():
        tp_colorchoose_window = colorchooser.askcolor()
        tp.now_color = tp_colorchoose_window[1]
        paint_main()
        up()
        paint_label.configure(text='Перо поднято...')
        paint_color_button.configure(bg=str(tp.now_color))

    root.geometry('530x80+0+0')
    window.configure(width=520, height=100)
    root.title('TurtlePaint')
    root.minsize(520, 100)

    paint_help_button = Button(window, text='СПРАВКА', bg='#b8b8b8', font=('Arial Bold', 12),
                               command=tp_help)
    paint_help_button.place(x=60, y=10)

    paint_save_button = Button(window, text='СОХРАНИТЬ РИСУНОК', bg='#93e6a8', font=('Arial Bold', 12),
                               command=paint_save)
    paint_save_button.place(x=160, y=10)

    paint_color_button = Button(window, text='ВЫБРАТЬ ЦВЕТ', bg='white', font=('Arial Bold', 12),
                                command=tp_choose_color)
    paint_color_button.place(x=360, y=10)

    paint_label = Label(window, text='Перо поднято...')
    paint_label.place(x=60, y=50)

    paint_off = Button(window, text='⌂', font=('Arial Bold', 15), width=2, height=1, bg='black', fg='white',
                       command=paint_destroy)
    paint_off.place(x=0, y=5)
    ToolTip(paint_off, 'На главную...')

    TurtleScreen._RUNNING = True
    tp = TurtlePaintGlobal()

    def paint_switchupdown(xx=0.0, yy=0.0):
        if pen()['pendown']:
            end_fill()
            up()
            paint_label.configure(text='Перо поднято...')
        else:
            down()
            begin_fill()
            paint_label.configure(text='Перо опущено...')
        return xx, yy

    def paint_main():
        shape('circle')
        resizemode('user')
        shapesize(.5)
        width(3)
        tp.colors = ['red', 'green', 'blue', 'yellow', 'grey', 'black']
        color(tp.now_color)
        paint_switchupdown()
        onscreenclick(goto, 1)
        onscreenclick(paint_switchupdown, 3)

    paint_window = Screen()
    paint_window.title('TurtlePaint')
    paint_window.setup(800, 600)

    paint_main()


def WaterMarks():
    def ws_destroy():
        try:
            ws.save_window.destroy()
        except AttributeError:
            pass

        try:
            ws.delete_window.destroy()
        except AttributeError:
            pass

        try:
            ws.edit_window.destroy()
        except AttributeError:
            pass

        try:
            ws.view_window.destroy()
        except AttributeError:
            pass

        ws_title.destroy()
        ws_search_button.destroy()
        ws_file_label.destroy()
        ws_color_button.destroy()
        ws_label_1.destroy()
        ws_text.destroy()
        ws_color_demo.destroy()
        ws_label_2.destroy()
        ws_label_3.destroy()
        ws_input_1.destroy()
        ws_label_6.destroy()
        ws_input_2.destroy()
        ws_choose_button.destroy()
        ws_label_4.destroy()
        ws_input_3.destroy()
        ws_label_5.destroy()
        ws_font_combobox.destroy()
        ws_preview_button.destroy()
        ws_save_button.destroy()
        ws_off.destroy()
        m.enu.delete('Проект')
        home()
        window.configure(width=700, height=m.abs_height)
        center_window(root, 678, m.abs_height)

    def ws_open_file():
        ws.file = askopenfilename()
        if ws.file:
            ws_file_label.configure(state=NORMAL)
            ws_file_label.delete(1.0, END)
            ws_file_label.insert(1.0, ws.file)
            ws_file_label.configure(state=DISABLED)
        else:
            ws.file = None

    def ws_choose_color():
        ws_colorchoose_window = colorchooser.askcolor()
        ws.color = ws_colorchoose_window[0]
        if ws.color is not None:
            ws.color = (int(ws.color[0]), int(ws.color[1]), int(ws.color[2]))
            ws_color_demo.configure(bg=str(ws_colorchoose_window[1]))

    def ws_open_preview():
        try:
            if ws.file is not None and ws.color is not None and ws_text.get(1.0, END) and ws_input_1.get().isdigit() \
                    and ws_input_2.get().isdigit() and ws_input_3.get().isdigit() and ws_font_combobox.get():
                try:
                    photo = Image.open(ws.file)
                    drawing = ImageDraw.Draw(photo)
                    ws_font = ImageFont.truetype('fonts/' + ws_font_combobox.get(), int(ws_input_3.get()))
                    drawing.text((int(ws_input_1.get()), int(ws_input_2.get())), ws_text.get(1.0, END), fill=ws.color,
                                 font=ws_font)
                    photo.save('MihaSoft Files/Temp/ws.png')
                    os.startfile('MihaSoft Files/Temp/ws.png')

                except UnidentifiedImageError:
                    messagebox.showerror('Ошибка!', 'Выбранный файл не является изображением!')
            else:
                messagebox.showwarning('INFO', 'Введены некорректные данные!')
        except FileNotFoundError:
            messagebox.showerror('Ошибка!', 'Файл изображения перемещён или утрачен!')

    def ws_save():
        try:
            ws_file = asksaveasfilename(title='Сохранить файл', defaultextension='.png',
                                        filetypes=(('PNG file', '*.png'), ('All Files', '*.*')))
            if ws_file:
                if ws.file is not None and ws.color is not None and ws_text.get(1.0, END) \
                        and ws_input_1.get().isdigit() and ws_input_2.get().isdigit() and ws_input_3.get().isdigit() \
                        and ws_font_combobox.get():
                    try:
                        photo = Image.open(ws.file)
                        drawing = ImageDraw.Draw(photo)
                        ws_font = ImageFont.truetype('fonts/' + ws_font_combobox.get(), int(ws_input_3.get()))
                        drawing.text((int(ws_input_1.get()), int(ws_input_2.get())), ws_text.get(1.0, END),
                                     fill=ws.color,
                                     font=ws_font)
                        photo.save(ws_file)
                    except UnidentifiedImageError:
                        messagebox.showerror('Ошибка!', 'Выбранный файл не является изображением!')
                else:
                    messagebox.showwarning('INFO', 'Введены некорректные данные!')
        except FileNotFoundError:
            messagebox.showerror('Ошибка!', 'Файл изображения перемещён или утрачен!')

    def choose_place():
        def ws_create_view_window():
            def ws_ok_place(event):
                ws_input_1.delete(0, END)
                ws_input_2.delete(0, END)
                ws_input_1.insert(0, event.x)
                ws_input_2.insert(0, event.y)
                ws.view_window.destroy()

            if ws.file is not None:
                ws.view_window = Toplevel()
                ws.view_window.title('Укажите точку...')
                img_label = Label(ws.view_window, cursor='hand2')
                img_obj = Image.open(ws.file)
                im_width, im_height = img_obj.size
                img_label.image = ImageTk.PhotoImage(img_obj)
                img_label['image'] = img_label.image

                img_label.pack()
                center_window(ws.view_window, im_width, im_height)
                ws.view_window.resizable(False, False)
                ws.view_window.bind('<Button-1>', ws_ok_place)

            else:
                messagebox.showwarning('INFO', 'Выберите файл!')

        try:
            ws.view_window.resizable(False, False)

        except AttributeError:
            ws_create_view_window()

        except TclError:
            ws_create_view_window()

    def ws_save_project():
        """
        Функция сохранения параметров
        проекта в файл
        """

        def ws_save_changes():
            """
            Функция сохранения изменений в
            открытом для редактирования файла
            """
            save(ws.open_path,
                 [ws.file, ws.color, ws_text.get(1.0, END), ws_input_1.get(), ws_input_2.get(), ws_input_3.get(),
                  ws_font_combobox.get()])

            ws.flag = True
            ws.save_window.destroy()

        def ws_save_abort():
            """
            Отмена сохранения
            """
            ws.save_window.destroy()

        # Проверка значения переменной, отвечающей за состояние
        # приложения (создание нового файла или редактирование существующего)
        # и вызов соответствующего окна.

        # Проверка правильности заполнения полей с параметрами
        def ws_create_save_window():
            def ws_save_file():
                """
                Функция сохранения нового файла
                """
                save('MihaSoft Files/WS Files/' + str(ws_save_input.get()),
                     [ws.file, ws.color, ws_text.get(1.0, END), ws_input_1.get(), ws_input_2.get(), ws_input_3.get(),
                      ws_font_combobox.get()])

                ws.save_window.destroy()

            if ws.file is not None and ws.color is not None and ws_text.get(1.0, END) and ws_input_1.get().isdigit() \
                    and ws_input_2.get().isdigit() and ws_input_3.get().isdigit() and ws_font_combobox.get():
                if not ws.flag:
                    ws.save_window = Toplevel()
                    center_window(ws.save_window, 300, 100)
                    ws.save_window.resizable(False, False)
                    ws.save_window.title('Сохранение')

                    ws_save_label = Label(ws.save_window, text='Сохранить изменения?')
                    ws_save_label.place(x=5, y=5)

                    ws_save_ok_button = Button(ws.save_window, text='ОК', width=10, bg='#93e6a8',
                                               command=ws_save_changes)
                    ws_save_ok_button.place(x=200, y=43)

                    ws_close_button = Button(ws.save_window, text='Отмена', bg='#b8b8b8', width=10,
                                             command=ws_save_abort)
                    ws_close_button.place(x=100, y=43)

                else:
                    ws.save_window = Toplevel()
                    center_window(ws.save_window, 300, 100)
                    ws.save_window.resizable(False, False)
                    ws.save_window.title('Сохранение')

                    ws_save_label = Label(ws.save_window, text='Введите название файла...')
                    ws_save_label.place(x=5, y=5)

                    # Поле ввода названия нового файла
                    ws_save_input = Entry(ws.save_window, width=25)
                    ws_save_input.place(x=10, y=45)

                    ws_save_ok_button = Button(ws.save_window, text='Сохранить', width=10, bg='#93e6a8',
                                               command=ws_save_file)
                    ws_save_ok_button.place(x=200, y=53)

                    ws_save_close_button = Button(ws.save_window, text='Отмена', bg='#b8b8b8', width=10,
                                                  command=ws_save_abort)
                    ws_save_close_button.place(x=200, y=13)
            else:
                messagebox.showwarning('INFO', 'Проверьте корректность введённых данных!')

        try:
            ws.save_window.resizable(False, False)

        except AttributeError:
            ws_create_save_window()

        except TclError:
            ws_create_save_window()

    def ws_clean():
        ws_file_label.configure(state=NORMAL)
        ws_file_label.delete(1.0, END)
        ws_file_label.configure(state=DISABLED)
        ws_text.delete(1.0, END)
        ws_input_1.delete(0, END)
        ws_input_2.delete(0, END)
        ws_input_3.delete(0, END)
        ws_font_combobox.delete(0, END)
        ws_color_demo.configure(bg='white')
        ws.flag = True

    def ws_edit():
        """
        Функция редактирования существующего файла
        (подстановка параметров из существующего файла
        в соответствующие поля
        """

        def ws_edit_abort():
            """
            Отмена редактирования
            """
            ws.edit_window.destroy()

        def ws_create_edit_window():
            def ws_edit_ok():
                """
                Функция вывода параметров в соответствующие поля
                из выбранного файла
                """
                ws_clean()
                ws_edit_path = str(ws_edit_combobox.get())
                ws_data_list = load('MihaSoft Files/WS Files/' + ws_edit_path, allow_pickle=True)
                ws.open_path = 'MihaSoft Files/WS Files/' + ws_edit_path
                ws.file = ws_data_list[0]
                ws.color = eval(str(ws_data_list[1]))
                ws_file_label.configure(state=NORMAL)
                ws_file_label.delete(1.0, END)
                ws_file_label.insert(1.0, ws.file)
                ws_file_label.configure(state=DISABLED)
                ws_color_demo.configure(bg='#%02x%02x%02x' % tuple(ws.color))
                ws_text.insert(1.0, ws_data_list[2])
                ws_input_1.insert(0, ws_data_list[3])
                ws_input_2.insert(0, ws_data_list[4])
                ws_input_3.insert(0, ws_data_list[5])
                ws_font_combobox.configure(state='normal')
                ws_font_combobox.insert(0, ws_data_list[6])
                ws_font_combobox.configure(state='readonly')
                ws.flag = False
                ws.edit_window.destroy()

            ws.edit_window = Toplevel()
            center_window(ws.edit_window, 300, 100)
            ws.edit_window.resizable(False, False)
            ws.edit_window.title('Открыть')

            ws_edit_label = Label(ws.edit_window, text='Выберите файл...')
            ws_edit_label.place(x=5, y=5)

            # Список существующих файлов
            ws_edit_combobox = ttk.Combobox(ws.edit_window, values=os.listdir('MihaSoft Files/WS Files'),
                                            state='readonly')
            ws_edit_combobox.place(x=10, y=45)

            ws_edit_ok_button = Button(ws.edit_window, text='Открыть', width=13, bg='#93e6a8', command=ws_edit_ok)
            ws_edit_ok_button.place(x=180, y=53)

            ws_edit_close_button = Button(ws.edit_window, text='Отмена', bg='#b8b8b8', width=13, command=ws_edit_abort)
            ws_edit_close_button.place(x=180, y=13)

        try:
            ws.edit_window.resizable(False, False)

        except AttributeError:
            ws_create_edit_window()

        except TclError:
            ws_create_edit_window()

    def ws_delete():
        """
        Функция удаления сохранённых файлов
        """

        def ws_delete_abort():
            """
            Отмена удаления
            """
            ws.delete_window.destroy()

        def ws_create_del_window():
            def ws_delete_ok():
                """
                Удаление выбранного файла
                """
                os.remove('MihaSoft Files/WS Files/' + str(ws_delete_combobox.get()))
                ws.delete_window.destroy()

            ws.delete_window = Toplevel()
            center_window(ws.delete_window, 300, 100)
            ws.delete_window.resizable(False, False)
            ws.delete_window.title('Удаление')

            ws_delete_label = Label(ws.delete_window, text='Выберите файл...')
            ws_delete_label.place(x=5, y=5)

            # Список существующих файлов
            ws_delete_combobox = ttk.Combobox(ws.delete_window, values=os.listdir('MihaSoft Files/WS Files'),
                                              state='readonly')
            ws_delete_combobox.place(x=10, y=45)

            ws_delete_ok_button = Button(ws.delete_window, text='Удалить', width=10, bg='#e69b93', command=ws_delete_ok)
            ws_delete_ok_button.place(x=200, y=23)

            ws_delete_close_button = Button(ws.delete_window, text='Отмена', width=10, bg='#b8b8b8',
                                            command=ws_delete_abort)
            ws_delete_close_button.place(x=200, y=60)

        try:
            ws.delete_window.resizable(False, False)

        except AttributeError:
            ws_create_del_window()

        except TclError:
            ws_create_del_window()

    if not os.path.exists('MihaSoft Files/WS Files'):
        os.mkdir('MihaSoft Files/WS Files')

    center_window(root, 430, 400)
    window.configure(width=430, height=400)
    root.title('WaterMarks 2.0')
    root.minsize(430, 400)

    ws = WaterMarksGlobals()
    menu = Menu(m.enu, tearoff=0)
    menu.add_command(label='Сохранить', command=ws_save_project)
    menu.add_command(label='Открыть', command=ws_edit)
    menu.add_command(label='Удалить', command=ws_delete)
    menu.add_command(label='Новый проект', command=ws_clean)
    m.enu.add_cascade(label='Проект', menu=menu)

    ws_title = Label(window, text='WaterMarks 2.0', font=('Arial Bold', 16), fg='red')
    ws_title.place(x=50, y=10)

    ws_search_button = Button(window, text='Выбрать файл', width=12, height=1, font=('Times New Roman', 12),
                              bg='yellow', command=ws_open_file)
    ws_search_button.place(x=50, y=60)
    ToolTip(ws_search_button, 'Выбрать картинку для редактирования...')

    ws_file_label = Text(window, width=23, height=2, state=DISABLED)
    ws_file_label.place(x=220, y=10)

    ws_color_button = Button(window, text='Выбрать цвет', width=22, height=1, font=('Times New Roman', 12),
                             bg='#f5ba53', command=ws_choose_color)
    ws_color_button.place(x=200, y=60)
    ToolTip(ws_color_button, 'Выбрать цвет надписи...')

    ws_label_1 = Label(window, text='Tекст водяного знака:')
    ws_label_1.place(x=50, y=100)

    ws_text = Text(window, width=35, height=5)
    ws_text.place(x=50, y=120)

    ws_color_demo = Label(window, bg='white', width=7, height=5)
    ws_color_demo.place(x=350, y=121)

    ws_label_2 = Label(window, text='Расположение текста на картинке:')
    ws_label_2.place(x=50, y=220)

    ws_label_3 = Label(window, text='X =')
    ws_label_3.place(x=50, y=250)

    ws_input_1 = Entry(window, width=6)
    ws_input_1.place(x=80, y=250)

    ws_label_4 = Label(window, text='Y =')
    ws_label_4.place(x=130, y=250)

    ws_input_2 = Entry(window, width=6)
    ws_input_2.place(x=160, y=250)

    ws_choose_button = Button(window, bg='#b0eef7', text='Указать', command=choose_place)
    ws_choose_button.place(x=215, y=245)

    ws_label_5 = Label(window, text='Размер шрифта:')
    ws_label_5.place(x=290, y=220)

    ws_input_3 = Entry(window, width=18)
    ws_input_3.place(x=290, y=250)

    ws_label_6 = Label(window, text='Шрифт:')
    ws_label_6.place(x=50, y=290)

    ws_font_combobox = ttk.Combobox(window, width=45, values=os.listdir('fonts'), state='readonly')
    ws_font_combobox.place(x=110, y=290)

    ws_preview_button = Button(window, text='Предварительный просмотр', width=22, height=1,
                               font=('Times New Roman', 12),
                               bg='#abf0a1', command=ws_open_preview)
    ws_preview_button.place(x=200, y=330)
    ToolTip(ws_preview_button, 'Открыть полученную картинку в программе просмотра изображений...')

    ws_save_button = Button(window, text='Сохранить', width=12, height=1, font=('Times New Roman', 12),
                            bg='#93e6a8', command=ws_save)
    ws_save_button.place(x=50, y=330)
    ToolTip(ws_save_button, 'Сохранить полученную картинку в новом месте...')

    ws_off = Button(window, text='⌂', font=('Arial Bold', 15), width=2, height=1, bg='black', fg='white',
                    command=ws_destroy)
    ws_off.place(x=0, y=5)
    ToolTip(ws_off, 'На главную...')


def HyperText():
    htt = HyperTextGlobals()
    ht_view_list = []
    ht_list = []

    def ht_destroy():
        try:
            htt.req_win.destroy()
        except AttributeError:
            pass

        try:
            htt.i_i.destroy()
        except AttributeError:
            pass

        try:
            htt.resp_window.destroy()
        except AttributeError:
            pass

        ht_title.destroy()
        ht_preview_button.destroy()
        ht_del_button.destroy()
        ht_save_button.destroy()
        ht_frame_1.destroy()
        ht_frame_2.destroy()
        ht_info.destroy()
        ht_off.destroy()
        ht_frame_3.destroy()
        ht_send_button.destroy()
        ht_new.destroy()
        ht_check.destroy()

        home()
        window.configure(width=700, height=m.abs_height)
        center_window(root, 678, m.abs_height)

    def ht_choose_background():
        ht_ch = colorchooser.askcolor()
        htt.background = ht_ch[1]
        ht_color_button.configure(bg=str(htt.background))

    def ht_choose_color():
        ht_ch_1 = colorchooser.askcolor()
        htt.color = ht_ch_1[1]
        ht_color_button_2.configure(bg=str(htt.color))

    def ht_del_block():
        if ht_list:
            def ht_create_req_window():
                def ht_ok():
                    ht_list.pop(int(ht_comb.get()[0] + ht_comb.get()[1]) - 1)
                    ht_view_list.pop(int(ht_comb.get()[0] + ht_comb.get()[1]) - 1)
                    htt.key -= 1
                    htt.req_win.destroy()

                htt.req_win = Toplevel()
                htt.req_win.title('Удаление')
                center_window(htt.req_win, 300, 100)
                htt.req_win.resizable(False, False)
                h_v = []
                for z in range(1, htt.key + 1):
                    h_v.append(str(z) + ' .' + ht_view_list[z - 1])
                ht_comb = ttk.Combobox(htt.req_win, values=h_v, width=45, state='readonly')
                ht_comb.place(x=5, y=5)

                ht_but = Button(htt.req_win, text='OK', width=10, command=ht_ok)
                ht_but.place(x=110, y=50)

            try:
                htt.req_win.resizable(False, False)

            except AttributeError:
                ht_create_req_window()

            except TclError:
                ht_create_req_window()
        else:
            messagebox.showinfo('INFO', 'Элементы отсутствуют!')

    def ht_preview():
        document = f'''<!DOCTYPE html><html><head><title>{ht_tit_input.get()}</title>
</head><body bgcolor="{htt.background}">''' + ''.join(ht_list) + '''</body></html>'''
        ht_num = str(randint(0, 10000))
        ht_html = open(f'MihaSoft Files/Temp/{ht_num}.html', 'w')
        ht_html.write(document)
        ht_html.close()
        open_new(f'file:///MihaSoft Files/Temp/{ht_num}.html')

    def ht_append():
        if (not ht_1_input.get().isdigit() and ht_1_input.get()) or (not ht_width.get().isdigit() and ht_width.get()) \
                or (not ht_height.get().isdigit() and ht_height.get()):
            messagebox.showwarning('INFO', 'Некорректные числовые параметры!')
        else:
            ht_center = ht_center_end = ''
            if var_center.get():
                ht_center = '<center>'
                ht_center_end = '</center>'

            if ht_combobox_1.get() == 'Жирный':
                ht_type = 'bold'
            else:
                ht_type = 'normal'
            if ht_combobox_2.get() == 'Блок':
                htt.block = f'''{ht_center}<div style="color: {htt.color}; font-size: {ht_1_input.get()}px;
                font-weight: {ht_type}; margin: {ht_input_x.get()}px; background: {htt.all_color};
                width: {ht_width.get()}px; height: {ht_height.get()}px;">
                {ht_text.get(1.0, END)}</div>{ht_center_end}'''

            elif ht_combobox_2.get() == 'Ссылка':
                htt.block = f'''{ht_center}<a style="color: {htt.color}; font-size: {ht_1_input.get()}px;
                             font-weight: {ht_type}; margin: {ht_input_x.get()}px;"
                             href="{ht_but_href.get()}">{ht_text.get(1.0, END)}</a>{ht_center_end}'''

            elif ht_combobox_2.get() == 'Кнопка':
                htt.block = f'''{ht_center}<button style="color: {htt.color}; font-size: {ht_1_input.get()}px;
                             font-weight: {ht_type}; margin: {ht_input_x.get()}px; background: {htt.all_color};
                             width: {ht_width.get()}px; height: {ht_height.get()}px;" 
                             onclick="window.location.href = '{ht_but_href.get()}'">{ht_text.get(1.0, END)}</button>
                             {ht_center_end}'''
            ht_list.append(htt.block)
            ht_view_list.append(f'{ht_combobox_2.get()} : {ht_text.get(1.0, END)}')
            htt.key += 1
            ht_text.delete(1.0, END)
            ht_input_x.delete(0, END)
            ht_but_href.delete(0, END)
            ht_height.delete(0, END)
            ht_width.delete(0, END)

    def add_image():
        if (not ht_but_width.get().isdigit() and ht_but_width.get()) or (not ht_but_height.get().isdigit()
                                                                         and ht_but_height.get()):
            messagebox.showwarning('INFO', 'Некорректные числовые параметры!')
        elif htt.image is None and not ht_img_href.get():
            messagebox.showwarning('INFO', 'Выберите изображение для вставки!')
        else:
            ht_center = ht_center_end = ''
            if var_center.get():
                ht_center = '<center>'
                ht_center_end = '</center>'
            if not ht_img_href.get():
                src = 'file:///' + str(htt.image)
            else:
                src = ht_img_href.get()
            ht_block = f'''{ht_center}<img src="{src}" width="{ht_but_width.get()}px" height="{ht_but_height.get()}px"
            style="margin: {ht_input_x.get()}">{ht_center_end}'''
            ht_list.append(ht_block)
            ht_view_list.append(f'Изображение: {src}')
            htt.key += 1
            ht_img_href.delete(0, END)
            ht_but_height.delete(0, END)
            ht_but_width.delete(0, END)

    def ht_save():
        ht_file = asksaveasfilename(title='Сохранить файл', defaultextension='.html',
                                    filetypes=(('HTML file', '*.html'), ('All Files', '*.*')))
        if ht_file:
            _document = f'''<!DOCTYPE html><html><head><title>{ht_tit_input.get()}</title>
            </head><body bgcolor="{htt.background}">''' + ''.join(ht_list) + '''</body></html>'''
            file = open(ht_file, 'w')
            file.write(_document)
            file.close()

    def ht_info_i():
        def ht_create_info_window():
            htt.i_i = Toplevel()
            center_window(htt.i_i, 1100, 700)
            htt.i_i.resizable(False, False)
            htt.i_i.title('INFO')
            ht_box = Listbox(htt.i_i, width=180, height=40)
            for xz in ht_view_list:
                ht_box.insert(END, xz)
            ht_box.pack()

        try:
            htt.i_i.resizable(False, False)

        except AttributeError:
            ht_create_info_window()

        except TclError:
            ht_create_info_window()

    def ht_choose_img():
        hh_file = askopenfilename()
        if hh_file:
            htt.image = hh_file
            ht_now_image.configure(text=f'Текущий файл: {htt.image}')

    def ht_choose_bg_all():
        abg = colorchooser.askcolor()
        htt.all_color = abg[1]
        ht_colora_button.configure(bg=str(htt.all_color))

    def ht_send():
        def write_to_mihnote():
            copy(f'https://otziv-mihasoft.glitch.me/page?id={response.text}')
            if ht_tit_input.get():
                ht_til = ht_tit_input.get()
            else:
                ht_til = 'url'
            url_file = open('MihaSoft Files/MihNote Files/' + ht_til + '.miha', 'w')
            url_file.write(f'https://otziv-mihasoft.glitch.me/page?id={response.text}')
            url_file.close()
            htt.resp_window.destroy()

        def copy_url():
            copy(f'https://otziv-mihasoft.glitch.me/page?id={response.text}')
            htt.resp_window.destroy()

        try:
            abstr_inp = Entry(window)
            abstr_inp.insert(0, str(randint(10000, 1000000)))
            ht_list_x = []
            for lol in range(len(ht_list)):
                ht_list_x.append(ht_list[lol].replace('#', '%23').replace('&', '%26'))

            document_send = f'''<!DOCTYPE html><html><head><title>{ht_tit_input.get()}</title>
            </head><body bgcolor="{htt.background.replace('#', '%23').replace('&', '%26')}">''' + ''.join(ht_list_x) + \
                            '''</body></html>'''
            response = requests.get(f'https://otziv-mihasoft.glitch.me/regis?name={document_send}&id={abstr_inp.get()}')
            if response.text:
                htt.resp_window = Toplevel()
                htt.resp_window.title('Успешно!')
                center_window(htt.resp_window, 400, 140)
                htt.resp_window.resizable(False, False)
                label_res = Label(htt.resp_window, font=('Times New Roman', 13), text=f'''Ваша страница опубликована
и доступна по адресу:

https://otziv-mihasoft.glitch.me/page?id={response.text}''')
                label_res.pack()
                res_but_1 = Button(htt.resp_window, text='Добавить в MihNote', font=('Times New Roman', 11), bg='white',
                                   command=write_to_mihnote)
                res_but_1.place(x=30, y=100)
                res_but_2 = Button(htt.resp_window, text='Копировать', font=('Times New Roman', 11), bg='white',
                                   command=copy_url)
                res_but_2.place(x=280, y=100)

            else:
                messagebox.showerror('Ошибка!', 'Ошибка на сервере! Попробуйте позже или свяжитесь с разработчиком.')
        except requests.exceptions.ConnectionError:
            messagebox.showerror('Ошибка!', 'Нет доступа к сети!')

    def ht_new():
        ht_list.clear()
        ht_view_list.clear()

    if not os.path.exists('MihaSoft Files/Temp'):
        os.mkdir('MihaSoft Files/Temp')
    if os.listdir('MihaSoft Files/Temp'):
        for i in os.listdir('MihaSoft Files/Temp'):
            os.remove('MihaSoft Files/Temp/' + i)

    center_window(root, 850, 480)
    window.configure(width=850, height=480)
    root.title('HyperText 3.0')
    root.minsize(850, 480)

    ht_title = Label(window, text='HyperText 3.0', font=('Arial Bold', 16), fg='red')
    ht_title.place(x=50, y=10)

    ht_preview_button = Button(window, text='Предварительный просмотр', width=23, font=('Times New Roman', 13),
                               bg='#fff7ab',
                               command=ht_preview)
    ht_preview_button.place(x=620, y=165)
    ToolTip(ht_preview_button, 'Открыть страницу в браузере без сохранения')

    ht_del_button = Button(window, text='Удалить элемент', width=23, font=('Times New Roman', 13), bg='#ffb6ab',
                           command=ht_del_block)
    ht_del_button.place(x=620, y=210)
    ToolTip(ht_del_button, 'Удалить ранее добавленный элемент с макета страницы')

    ht_save_button = Button(window, text='Сохранить', font=('Times New Roman', 13), bg='#c7ffda', width=23,
                            command=ht_save)
    ht_save_button.place(x=620, y=255)
    ToolTip(ht_save_button, 'Сохранить страницу, как локальный файл')

    ht_send_button = Button(window, text='Опубликовать', font=('Times New Roman', 13), bg='#93e6a8', width=23,
                            command=ht_send)
    ht_send_button.place(x=620, y=300)
    ToolTip(ht_send_button, 'Загрузить страницу на сервер MihaSoft и получить ссылку')

    ht_info = Button(window, text='Список блоков', width=23, font=('Times New Roman', 13), bg='#b8b8b8',
                     command=ht_info_i)
    ht_info.place(x=620, y=345)
    ToolTip(ht_info, 'Вывести список всех добавленных html-элементов')

    ht_new = Button(window, text='Новый проект', width=23, font=('Times New Roman', 13), bg='#c9c9c9',
                    command=ht_new)
    ht_new.place(x=620, y=390)
    ToolTip(ht_new, 'Удалить все элементы из текущей конструируемой страницы')

    ht_frame_1 = LabelFrame(window, width=300, height=100, text='Общее')
    ht_frame_1.place(x=50, y=45)

    ht_label_1 = Label(ht_frame_1, text='Заголовок:')
    ht_label_1.place(x=0, y=0)

    ht_tit_input = Entry(ht_frame_1, width=35)
    ht_tit_input.place(x=70, y=0)

    ht_label_2 = Label(ht_frame_1, text='Цвет фона:')
    ht_label_2.place(x=0, y=30)

    ht_color_button = Button(ht_frame_1, text='Выбрать', font=('Times New Roman', 11), bg='white',
                             command=ht_choose_background)
    ht_color_button.place(x=70, y=30)

    ht_label_x = Label(ht_frame_1, text='Отступы:')
    ht_label_x.place(x=160, y=35)

    ht_input_x = Entry(ht_frame_1, width=10)
    ht_input_x.place(x=220, y=35)

    ht_frame_2 = LabelFrame(window, width=550, height=320, text='Элементы')
    ht_frame_2.place(x=50, y=145)

    ht_label_3 = Label(ht_frame_2, text='Цвет текста:')
    ht_label_3.place(x=0, y=0)

    ht_color_button_2 = Button(ht_frame_2, text='Выбрать', font=('Times New Roman', 11), bg='white',
                               command=ht_choose_color)
    ht_color_button_2.place(x=90, y=0)

    ht_label_4 = Label(ht_frame_2, text='Тип текста:')
    ht_label_4.place(x=180, y=0)

    ht_combobox_1 = ttk.Combobox(ht_frame_2, values=['Жирный', 'Нормальный'], state='readonly', width=11)
    ht_combobox_1.place(x=250, y=0)

    ht_label_5 = Label(ht_frame_2, text='Размер текста:')
    ht_label_5.place(x=350, y=0)

    ht_1_input = Entry(ht_frame_2, width=10)
    ht_1_input.place(x=450, y=0)

    ht_label_6 = Label(ht_frame_2, text='Текст:')
    ht_label_6.place(x=0, y=40)

    ht_text = Text(ht_frame_2, width=60, height=10)
    ht_text.place(x=50, y=40)

    ht_label_7x = Label(ht_frame_2, text='Высота:')
    ht_label_7x.place(x=410, y=215)

    ht_height = Entry(ht_frame_2, width=5)
    ht_height.place(x=470, y=215)

    ht_label_8x = Label(ht_frame_2, text='Длина:')
    ht_label_8x.place(x=410, y=235)

    ht_width = Entry(ht_frame_2, width=5)
    ht_width.place(x=470, y=235)

    ht_add_button = Button(ht_frame_2, text='Добавить', font=('Times New Roman', 12), bg='#93e6a8', command=ht_append)
    ht_add_button.place(x=50, y=260)

    ht_label_4x = Label(ht_frame_2, text='Тип элемента:')
    ht_label_4x.place(x=180, y=260)

    ht_combobox_2 = ttk.Combobox(ht_frame_2, values=['Блок', 'Кнопка', 'Ссылка'], width=11)
    ht_combobox_2.place(x=280, y=260)
    ht_combobox_2.insert(0, 'Блок')
    ht_combobox_2.configure(state='readonly')

    ht_frame_3 = LabelFrame(window, width=457, height=130, text='Изображение')
    ht_frame_3.place(x=380, y=15)

    ht_label_7 = Label(ht_frame_3, text='Высота:')
    ht_label_7.place(x=5, y=5)

    ht_but_height = Entry(ht_frame_3, width=5)
    ht_but_height.place(x=70, y=5)

    ht_label_8 = Label(ht_frame_3, text='Длина:')
    ht_label_8.place(x=5, y=25)

    ht_but_width = Entry(ht_frame_3, width=5)
    ht_but_width.place(x=70, y=25)

    ht_label_9 = Label(ht_frame_2, text='Цвет:')
    ht_label_9.place(x=300, y=220)

    ht_colora_button = Button(ht_frame_2, text='Выбрать', font=('Times New Roman', 9), bg='white',
                              command=ht_choose_bg_all)
    ht_colora_button.place(x=340, y=215)

    ht_label_10 = Label(ht_frame_3, text='Файл:')
    ht_label_10.place(x=170, y=5)

    ht_img_button = Button(ht_frame_3, text='Выбрать', font=('Times New Roman', 9), bg='white',
                           command=ht_choose_img)
    ht_img_button.place(x=220, y=5)

    ht_label_11x = Label(ht_frame_3, text='Ссылка:')
    ht_label_11x.place(x=35, y=50)

    ht_img_href = Entry(ht_frame_3, width=46)
    ht_img_href.place(x=100, y=50)

    ht_now_image = Label(ht_frame_3)
    ht_now_image.place(x=35, y=80)

    ht_label_11 = Label(ht_frame_2, text='Ссылка:')
    ht_label_11.place(x=5, y=220)

    ht_but_href = Entry(ht_frame_2, width=36)
    ht_but_href.place(x=70, y=220)

    ht_add_button_2 = Button(ht_frame_3, text='Добавить', font=('Times New Roman', 12), bg='#93e6a8',
                             command=add_image)
    ht_add_button_2.place(x=300, y=3)

    var_center = BooleanVar()
    var_center.set(False)

    ht_check = Checkbutton(window, text='Центрировать', variable=var_center, onvalue=1, offvalue=0)
    ht_check.place(x=240, y=25)

    ht_off = Button(window, text='⌂', font=('Arial Bold', 15), width=2, height=1, bg='black', fg='white',
                    command=ht_destroy)
    ht_off.place(x=0, y=5)
    ToolTip(ht_off, 'На главную...')


def Morse():
    def mr_destroy():
        mr_title.destroy()
        translate_label.destroy()
        translate_paste_1.destroy()
        translate_copy_1.destroy()
        translate_save_1.destroy()
        translate_open_1.destroy()
        translate_help.destroy()
        translate_input.destroy()
        translate_output.destroy()
        translate_paste_2.destroy()
        translate_copy_2.destroy()
        translate_save_2.destroy()
        translate_open_2.destroy()
        translate_label_2.destroy()
        rtm_listen.destroy()
        listen_speed.destroy()
        listen_speed_input.destroy()
        rtm_button.destroy()
        mtr_button.destroy()
        mte_button.destroy()
        mr_off.destroy()

        home()
        window.configure(width=700, height=m.abs_height)
        center_window(root, 678, m.abs_height)

    def rtm_main():
        if translate_input.get(1.0, END) == '' or translate_input.get(1.0, END) == '\n':
            messagebox.showwarning('INFO', 'Введите текст для перевода!')
            print(translate_input.get(1.0, END))
        content = translate_input.get(1.0, END)
        if translate_output.get(1.0, END):
            translate_output.delete(1.0, END)

        result = ''
        k = 0
        ban_list = ['~', '`', '#', '№', '%', '^', '*', '/', '|', '<', '>', '{', '}', '[', ']']
        extra_ban = '\ '
        extra_ban = extra_ban.replace(' ', '')
        for zix in range(len(ban_list)):
            if (ban_list[zix] in content or extra_ban in content) and k == 0:
                messagebox.showinfo('INFO', 'Символы ~ ` # № % ^ * / \ | < > { } [ ]\nне \
переводятся в азбуку морзе! Посторонние символы будут автоматически удалены.')
                k += 1

        for i in content:
            if 1040 <= ord(i) <= 1103 or i == ' ' or ord(i) == 1105 or 43 <= ord(i) <= 46 \
                    or 63 <= ord(i) <= 90 or 97 <= ord(i) <= 122 or 48 <= ord(i) <= 59 \
                    or 32 <= ord(i) <= 34 or 38 <= ord(i) <= 41 or ord(i) == 61 \
                    or i == '\n':
                result += i
        result = result[::-1].replace('\n', '', 1)[::-1]
        translate_input.delete('1.0', 'end')
        translate_input.insert('end', result)
        content = str(result).lower()

        rus_to_morse = {'а': '.-',
                        'б': '-...',
                        'в': '.--',
                        'г': '--.',
                        'д': '-..',
                        'е': '.',
                        'ё': '.',
                        'ж': '...-',
                        'з': '--..',
                        'и': '..',
                        'й': '.---',
                        'к': '-.-',
                        'л': '.-..',
                        'м': '--',
                        'н': '-.',
                        'о': '---',
                        'п': '.--.',
                        'р': '.-.',
                        'с': '...',
                        'т': '-',
                        'у': '..-',
                        'ф': '..-.',
                        'х': '....',
                        'ц': '-.-.',
                        'ч': '---.',
                        'ш': '----',
                        'щ': '--.-',
                        'ъ': '.--.-.',
                        'ы': '-.--',
                        'ь': '-..-',
                        'э': '..-..',
                        'ю': '..--',
                        'я': '.-.-',
                        'a': '.-',
                        'b': '-...',
                        'c': '-.-.',
                        'd': '-..',
                        'e': '.',
                        'f': '..-.',
                        'g': '--.',
                        'h': '....',
                        'i': '..',
                        'j': '.---',
                        'k': '-.-',
                        'l': '.-..',
                        'm': '--',
                        'n': '-.',
                        'o': '---',
                        'p': '.--.',
                        'q': '--.-',
                        'r': '.-.',
                        's': '...',
                        't': '-',
                        'u': '..-',
                        'v': '...-',
                        'w': '.--',
                        'x': '-..-',
                        'y': '-.--',
                        'z': '--..',
                        '0': '-----',
                        '1': '.----',
                        '2': '..---',
                        '3': '...--',
                        '4': '....-',
                        '5': '.....',
                        '6': '-....',
                        '7': '--...',
                        '8': '---..',
                        '9': '----.',
                        '-': '-....-',
                        '.': '......',
                        ',': '.-.-.-',
                        ';': '-.-.-.',
                        ':': '---...',
                        '!': '--..--',
                        '?': '..--..',
                        '\n': '\n',
                        '$': '...-..-',
                        '@': '.--.-.',
                        ''': '.-..-.',
                        ''': '.----.',
                        '&': '.-...',
                        '+': '.-.-.',
                        '=': '-...-',
                        '(': '-.--.',
                        ')': '-.--.-',
                        ' ': ' ',
                        '"': '',
                        "'": ''}

        result = ''

        for x in content:
            if rus_to_morse[x] == '\n' or rus_to_morse[x] == ' ':
                result += (rus_to_morse[x])
            else:
                result += (rus_to_morse[x] + ' ')

        if '.' in result or '-' in result:
            translate_output.insert(1.0, result[::-1].replace(' ', '', 1)[::-1])
            copy(result[::-1].replace(' ', '', 1)[::-1])

    def open_any():
        file_types = [('Текстовые файлы', '*.txt'), ('PY файлы', '*.py'), ('PYW файлы', '*.pyw')]
        fl = askopenfilename(filetypes=file_types)
        if fl:
            text = open(fl).read()
            translate_input.insert(END, text)

    def open_any_1():
        file_types = [('MORSE файлы', '*.mrs'), ('Текстовые файлы', '*.txt')]
        fl = askopenfilename(filetypes=file_types)
        if fl:
            text = open(fl).read()
            translate_output.insert(END, text)

    def play():
        def speed_check(sp):
            k = 0
            alphabet = '1234567890.,'
            for ia in range(len(sp)):
                if sp[ia] not in alphabet:
                    k += 1
                    if k == 1:
                        return 0
            if k == 0:
                return 1

        def speed_change(x, speeds):
            if (100 * x / speeds) % 1 >= 0.5:
                return ceil(100 * x / speeds)
            else:
                return int(100 * x / speeds)

        frequency = 500
        content = translate_output.get(1.0, END)
        content_check = content
        content_check = content_check.replace('.', '')
        content_check = content_check.replace('-', '')
        content_check = content_check.replace(' ', '')
        content_check = content_check.replace('\n', '')
        if content_check != '':
            messagebox.showwarning('INFO',
                                   'Отсутствует код морзе для воспроизведения или он содержит посторонние символы.')
        else:
            if content == '' or ('.' not in content and '-' not in content):
                messagebox.showwarning('INFO', 'Отсутствует код морзе для воспроизведения!')
            else:
                a = 0
                b = 0
                speeder = listen_speed_input.get()
                speeder = speeder.replace('\n', '', 1)
                if not (speeder.count('0') != 0 and speeder.count('1') == 0 and speeder.count('2') == 0 and
                        speeder.count('3') == 0 and speeder.count('4') == 0 and speeder.count('5') == 0 and
                        speeder.count('6') == 0 and speeder.count('7') == 0 and speeder.count('8') == 0 and
                        speeder.count('9') == 0):
                    speed_check_2 = speeder.split(',')
                    speed_check_3 = speeder.split('.')
                    while a < len(speed_check_2):
                        if speed_check_2[a] == '' or speed_check_3[b] == '.':
                            speed_check_2.pop(a)
                        else:
                            a += 1
                    while b < len(speed_check_3):
                        if speed_check_3[b] == '' or speed_check_3[b] == ',':
                            speed_check_3.pop(b)
                        else:
                            b += 1
                    if speed_check(speeder) == 0 or len(speed_check_2) == 0 or len(speed_check_3) == 0 or \
                            speeder.count('.') > 1 or speeder.count(',') > 1 \
                            or speeder.count('.') + speeder.count(',') > 1:
                        messagebox.showwarning('INFO', 'Некорректное значение скорости!')
                    else:
                        if speeder.count('0') == 0 and speeder.count('1') == 0 and speeder.count('2') == 0 and \
                                speeder.count('3') == 0 and speeder.count('4') == 0 and speeder.count('5') == 0 and \
                                speeder.count('6') == 0 and speeder.count('7') == 0 and speeder.count('8') == 0 and \
                                speeder.count('9') == 0:
                            speeder = 1
                        else:
                            speeder = speeder.replace(',', '.')
                            if speeder.count('.') == 0:
                                speeder = int(speeder)
                            else:
                                speeder = float(speeder)
                        with open('flag', 'w'):
                            pass
                        os.startfile('morse.exe')
                        for i in content:
                            mr_flag = True
                            for symbol in i:
                                if symbol == '.':
                                    Beep(frequency, speed_change(1, speeder))
                                    sleep(0.1 / speeder)
                                elif symbol == '-':
                                    Beep(frequency, speed_change(3, speeder))
                                    sleep(0.1 / speeder)
                                elif symbol == ' ':
                                    sleep(0.3 / speeder)
                                if not os.path.exists('flag'):
                                    mr_flag = False
                                    break
                            if not mr_flag:
                                break
                        Popen('taskkill /im morse.exe /f')
                else:
                    messagebox.showwarning('INFO', 'Некорректное значение скорости!')

    def paste_0():
        translate_input.delete(1.0, END)
        translate_input.insert(1.0, str(paste()))

    def paste_1():
        translate_output.delete(1.0, END)
        translate_output.insert(1.0, str(paste()))

    def mtr_main():
        if translate_input.get(1.0, END):
            translate_input.delete(1.0, END)
        rez = ''
        content = translate_output.get(1.0, END)
        if content[-1] != ' ':
            content = content + ' '
        k = 0
        clean_content = ''
        content_check = content
        content_check = content_check.replace(' ', '')
        content_check = content_check.replace('\n', '')
        content_check = content_check.replace('-', '')
        content_check = content_check.replace('.', '')

        if content_check == '':
            content = content[::-1].replace('\n', '', 1)[::-1]
            clean_content = content
        else:
            if '.' not in content and '-' not in content:
                messagebox.showwarning('INFO', 'Введите код для перевода!')
            elif k == 0:
                messagebox.showinfo('INFO',
                                    'Недопустимые символы или их сочетания будут автоматически удалены!')
                k += 1
            for mih in range(len(content)):
                if content[mih] == '.' or content[mih] == '-' or content[mih] == ' ' or content[mih] == '\n':
                    clean_content += content[mih]
            clean_content = clean_content[::-1].replace('\n', '', 1)[::-1]
            translate_input.delete(1.0, END)
            translate_input.insert(1.0, clean_content)
        clean_content = clean_content.replace('\n', ' \n ')
        clean_content = clean_content.split(' ')
        clean_content[-1] = clean_content[-1].replace('\n', '', 1)

        def translator_mtr(content_piece):
            if content_piece == '':
                return ' '
            if content_piece == '\n':
                return '\n'
            if content_piece == '-.--.-':
                return ')'
            if content_piece == '-.--.':
                return '('
            if content_piece == '-...-':
                return '='
            if content_piece == '.-.-.':
                return '+'
            if content_piece == '.-...':
                return '&'
            if content_piece == '.----.':
                return "'"
            if content_piece == '.-..-.':
                return '"'
            if content_piece == '.--.-.':
                return '@'
            if content_piece == '...-..-':
                return '$'
            if content_piece == '..--..':
                return '?'
            if content_piece == '--..--':
                return '!'
            if content_piece == '---...':
                return ':'
            if content_piece == '-.-.-.':
                return ';'
            if content_piece == '.-.-.-':
                return ','
            if content_piece == '......':
                return '.'
            if content_piece == '-....-':
                return '-'
            if content_piece == '----.':
                return '9'
            if content_piece == '---..':
                return '8'
            if content_piece == '--...':
                return '7'
            if content_piece == '-....':
                return '6'
            if content_piece == '.....':
                return '5'
            if content_piece == '....-':
                return '4'
            if content_piece == '...--':
                return '3'
            if content_piece == '..---':
                return '2'
            if content_piece == '.----':
                return '1'
            if content_piece == '-----':
                return '0'
            if content_piece == '.-.-':
                return 'я'
            if content_piece == '..--':
                return 'ю'
            if content_piece == '..-..':
                return 'э'
            if content_piece == '-..-':
                return 'ь'
            if content_piece == '-.--':
                return 'ы'
            if content_piece == '.--.-.':
                return 'ъ'
            if content_piece == '--.-':
                return 'щ'
            if content_piece == '----':
                return 'ш'
            if content_piece == '---.':
                return 'ч'
            if content_piece == '-.-.':
                return 'ц'
            if content_piece == '....':
                return 'х'
            if content_piece == '..-.':
                return 'ф'
            if content_piece == '..-':
                return 'у'
            if content_piece == '-':
                return 'т'
            if content_piece == '...':
                return 'с'
            if content_piece == '.-.':
                return 'р'
            if content_piece == '.--.':
                return 'п'
            if content_piece == '---':
                return 'о'
            if content_piece == '-.':
                return 'н'
            if content_piece == '--':
                return 'м'
            if content_piece == '.-..':
                return 'л'
            if content_piece == '-.-':
                return 'к'
            if content_piece == '.---':
                return 'й'
            if content_piece == '..':
                return 'и'
            if content_piece == '--..':
                return 'з'
            if content_piece == '...-':
                return 'ж'
            if content_piece == '.':
                return 'е'
            if content_piece == '-..':
                return 'д'
            if content_piece == '--.':
                return 'г'
            if content_piece == '.--':
                return 'в'
            if content_piece == '-...':
                return 'б'
            if content_piece == '.-':
                return 'а'
            else:
                messagebox.showwarning('INFO',
                                       'Введённое сочетание символов имеет буквы из другого языка или не имеет смысла!')
                return '#'

        for zix in range(len(clean_content)):
            rez_temp = translator_mtr(clean_content[zix])
            rez += rez_temp
        if rez.count('#') == 0:
            translate_input.insert(1.0, rez[::-1].replace(' ', '', 1)[::-1])
            copy(rez[::-1].replace(' ', '', 1)[::-1])

    def mte_main():
        if translate_input.get(1.0, END):
            translate_input.delete(1.0, END)
        rez = ''
        content = translate_output.get(1.0, END)
        if content[-1] != ' ':
            content = content + ' '
        k = 0
        clean_content = ''
        content_check = content
        content_check = content_check.replace(' ', '')
        content_check = content_check.replace('\n', '')
        content_check = content_check.replace('-', '')
        content_check = content_check.replace('.', '')

        if content_check == '':
            content = content[::-1].replace('\n', '', 1)[::-1]
            clean_content = content
        else:
            if '.' not in content and '-' not in content:
                messagebox.showwarning('INFO', 'Введите код для перевода!')
            elif k == 0:
                messagebox.showinfo('INFO',
                                    'Недопустимые символы или их сочетания будут автоматически удалены!')
                k += 1
            for mih in range(len(content)):
                if content[mih] == '.' or content[mih] == '-' or content[mih] == ' ' or content[mih] == '\n':
                    clean_content += content[mih]
            clean_content = clean_content[::-1].replace('\n', '', 1)[::-1]
            translate_input.delete(1.0, END)
            translate_input.insert(1.0, clean_content)
        clean_content = clean_content.replace('\n', ' \n ')
        clean_content = clean_content.split(' ')
        clean_content[-1] = clean_content[-1].replace('\n', '', 1)

        def translator_mte(content_piece):
            if content_piece == '':
                return ' '
            if content_piece == '\n':
                return '\n'
            if content_piece == '-.--.-':
                return ')'
            if content_piece == '-.--.':
                return '('
            if content_piece == '-...-':
                return '='
            if content_piece == '.-.-.':
                return '+'
            if content_piece == '.-...':
                return '&'
            if content_piece == '.----.':
                return "'"
            if content_piece == '.-..-.':
                return '"'
            if content_piece == '.--.-.':
                return '@'
            if content_piece == '...-..-':
                return '$'
            if content_piece == '..--..':
                return '?'
            if content_piece == '--..--':
                return '!'
            if content_piece == '---...':
                return ':'
            if content_piece == '-.-.-.':
                return ';'
            if content_piece == '.-.-.-':
                return ','
            if content_piece == '......':
                return '.'
            if content_piece == '-....-':
                return '-'
            if content_piece == '----.':
                return '9'
            if content_piece == '---..':
                return '8'
            if content_piece == '--...':
                return '7'
            if content_piece == '-....':
                return '6'
            if content_piece == '.....':
                return '5'
            if content_piece == '....-':
                return '4'
            if content_piece == '...--':
                return '3'
            if content_piece == '..---':
                return '2'
            if content_piece == '.----':
                return '1'
            if content_piece == '-----':
                return '0'
            if content_piece == '--..':
                return 'z'
            if content_piece == '-.--':
                return 'y'
            if content_piece == '-..-':
                return 'x'
            if content_piece == '.--':
                return 'w'
            if content_piece == '...-':
                return 'v'
            if content_piece == '..-':
                return 'u'
            if content_piece == '-':
                return 't'
            if content_piece == '...':
                return 's'
            if content_piece == '.-.':
                return 'r'
            if content_piece == '--.-':
                return 'q'
            if content_piece == '.--.':
                return 'p'
            if content_piece == '---':
                return 'o'
            if content_piece == '-.':
                return 'n '
            if content_piece == '--':
                return 'm'
            if content_piece == '.-..':
                return 'l'
            if content_piece == '-.-':
                return 'k'
            if content_piece == '.---':
                return 'j'
            if content_piece == '..':
                return 'i'
            if content_piece == '....':
                return 'h'
            if content_piece == '--.':
                return 'g'
            if content_piece == '..-.':
                return 'f'
            if content_piece == '.':
                return 'e'
            if content_piece == '-..':
                return 'd'
            if content_piece == '-.-.':
                return 'c'
            if content_piece == '-...':
                return 'b'
            if content_piece == '.-':
                return 'a'
            else:
                messagebox.showwarning('INFO',
                                       'Введённое сочетание символов имеет буквы из другого языка или не имеет смысла!')
                return '#'

        for zix in range(len(clean_content)):
            rez_temp = translator_mte(clean_content[zix])
            rez += rez_temp
        if rez.count('#') == 0:
            translate_input.insert(1.0, rez[::-1].replace(' ', '', 1)[::-1])
            copy(rez[::-1].replace(' ', '', 1)[::-1])

    def mr_help():
        messagebox.showinfo('Справка', 'Некоторые сочетания символов в Азбуке Морзе можно перевести сразу на \
несколько языков\n\nПри переводе из Морзе все символы будут преобразованы только в один из языков.')

    def mr_copy():
        copy(translate_input.get(1.0, END))

    def mr_copy_1():
        copy(translate_output.get(1.0, END))

    def mr_save():
        mr_name = asksaveasfilename(title='Сохранить', filetypes=(('TXT File', '*.txt'),
                                                                  ('All files', '*.*')),
                                    defaultextension='.txt')
        if mr_name:
            d_file = open(mr_name, 'w')
            d_file.close()
            with open(mr_name, 'w') as f:
                f.write(translate_input.get(1.0, END))

    def mr_save_1():
        mr_name = asksaveasfilename(title='Сохранить', filetypes=(('MORSE File', '*.mrs'),
                                                                  ('TXT File', '*.txt'),
                                                                  ('All files', '*.*')),
                                    defaultextension='.mrs')
        if mr_name:
            d_file = open(mr_name, 'w')
            d_file.close()
            with open(mr_name, 'w') as f:
                f.write(translate_output.get(1.0, END))

    center_window(root, 550, 420)
    root.title('Morse 1.0')
    window.configure(width=550, height=420)
    root.minsize(550, 420)

    mr_title = Label(window, text='Morse 1.0', font=('Arial Bold', 16), fg='red')
    mr_title.place(x=50, y=10)

    translate_label = Label(window, text='Текст:', height=1)
    translate_label.place(x=50, y=129)

    translate_paste_1 = Button(window, text='Вставить', bg='#fab1b1', width=12,
                               command=paste_0, font=('Calibri', 10))
    translate_paste_1.place(x=100, y=125)

    translate_copy_1 = Button(window, text='Копировать', bg='#facab1', width=12,
                              command=mr_copy, font=('Calibri', 10))
    translate_copy_1.place(x=200, y=125)

    translate_save_1 = Button(window, text='Сохранить', bg='#b3fab1', width=12,
                              command=mr_save, font=('Calibri', 10))
    translate_save_1.place(x=300, y=125)

    translate_open_1 = Button(window, text='Открыть', bg='#b1e5fa', width=12,
                              command=open_any, font=('Calibri', 10))
    translate_open_1.place(x=400, y=125)

    translate_help = Button(window, text='Справка', bg='#dedede', width=21, command=mr_help,
                            font=('Calibri', 10))
    translate_help.place(x=340, y=10)

    translate_input = Text(window, width=55, height=5)
    translate_input.place(x=50, y=159)

    translate_output = Text(window, width=55, height=5)
    translate_output.place(x=50, y=297)

    translate_paste_2 = Button(window, text='Вставить', bg='#fab1b1', width=12,
                               command=paste_1, font=('Calibri', 10))
    translate_paste_2.place(x=100, y=263)

    translate_copy_2 = Button(window, text='Копировать', bg='#facab1', width=12,
                              command=mr_copy_1, font=('Calibri', 10))
    translate_copy_2.place(x=200, y=263)

    translate_save_2 = Button(window, text='Сохранить', bg='#b3fab1', width=12,
                              command=mr_save_1, font=('Calibri', 10))
    translate_save_2.place(x=300, y=263)

    translate_open_2 = Button(window, text='Открыть', bg='#b1e5fa', width=12,
                              command=open_any_1, font=('Calibri', 10))
    translate_open_2.place(x=400, y=263)

    translate_label_2 = Label(window, text='Код:', height=1)
    translate_label_2.place(x=50, y=267)

    rtm_listen = Button(window, text='Воспроизвести', bg='#ffdab3', fg='black', width=21,
                        command=play, font=('Calibri', 10))
    rtm_listen.place(x=340, y=50)

    listen_speed = Label(window, text='Скорость воспроизведения:', height=1)
    listen_speed.place(x=155, y=90)

    listen_speed_input = Entry(window, width=10)
    listen_speed_input.place(x=320, y=90)

    rtm_button = Button(window, text='Перевести в Морзе', bg='#80fff7', width=15,
                        command=rtm_main, font=('Calibri', 10))
    rtm_button.place(x=50, y=50)

    mtr_button = Button(window, text='Перевести на Русский', bg='#80fff7', width=21, command=mtr_main,
                        font=('Calibri', 10))
    mtr_button.place(x=175, y=10)

    mte_button = Button(window, text='Перевести на Английский', bg='#80fff7', width=21, command=mte_main,
                        font=('Calibri', 10))
    mte_button.place(x=175, y=50)

    listen_speed_input.insert(0, '1')

    mr_off = Button(window, text='⌂', font=('Arial Bold', 15), width=2, height=1, bg='black', fg='white',
                    command=mr_destroy)
    mr_off.place(x=0, y=5)
    ToolTip(mr_off, 'На главную...')


# def PythonCompiler():
#     def pc_destroy():
#         pc_title.destroy()
#         pc_compile_button.destroy()
#         pc_input.destroy()
#         pc_choose.destroy()
#         pc_open_button.destroy()
#         pc_off.destroy()
#
#         home()
#         window.configure(width=700, height=m.abs_height)
#         center_window(root, 678, m.abs_height)
#
#     def pc_open():
#         file_n = askopenfilename(filetypes=[('PY файлы', '*.py'), ('Текстовые файлы', '*.txt')])
#         if file_n:
#             with open(file_n) as f:
#                 pc_input.insert(1.0, f.read())
#
#     def pc_compile():
#         pc_name = asksaveasfilename(title='Имя программы')
#         if pc_name:
#             info_w = Toplevel()
#             info_w.attributes('-topmost', 'true')
#             info_w.overrideredirect(True)
#             center_window(info_w, 200, 40)
#             info_l = Label(info_w, text='Идёт процесс компиляции...')
#             info_l.pack()
#
#             def pc_go():
#                 pc_name_iter = os.path.basename(pc_name)
#                 try:
#                     with open('MihaSoft Files/Compile/' + pc_name_iter + '.py', 'w') as f:
#                         f.write(pc_input.get(1.0, END))
#
#                     if pc_choose.get() == 'Один файл':
#                         PyInstaller.__main__.run([
#                             'MihaSoft Files/Compile/' + pc_name_iter + '.py',
#                             '--onefile',
#                         ])
#                     else:
#                         PyInstaller.__main__.run([
#                             'MihaSoft Files/Compile/' + pc_name_iter + '.py'
#                         ])
#                     os.remove(pc_name_iter + '.spec')
#                     if pc_choose.get() == 'Один файл':
#                         os.replace('dist/' + pc_name_iter + '.exe', pc_name + '.exe')
#                     else:
#                         os.replace('dist/' + pc_name_iter, pc_name)
#                     rmtree('dist')
#                     info_w.destroy()
#                     messagebox.showinfo('INFO', 'Компиляция успешно завершена')
#                 except UnicodeDecodeError:
#                     info_w.destroy()
#                     try:
#                         os.remove(pc_name_iter + '.spec')
#                     except FileNotFoundError:
#                         pass
#                     messagebox.showerror('Ошибка!', 'Некорректный тип файла!')
#
#             root.after(1000, pc_go)
#
#     if not os.path.exists('MihaSoft Files/Compile'):
#         os.mkdir('MihaSoft Files/Compile')

     # center_window(root, 450, 320)
     # root.title('PythonCompiler 1.0')
     # window.configure(width=450, height=320)
     # root.minsize(450, 320)
     #
     # pc_title = Label(window, text='PythonCompiler 1.0', font=('Arial Bold', 16), fg='red')
     # pc_title.place(x=50, y=10)
     #
     # pc_compile_button = Button(window, text='Компилировать', bg='#ffdab3', fg='black', font=('Calibri', 12),
     #                            command=pc_compile)
     # pc_compile_button.place(x=293, y=10)
     #
     # pc_input = Text(window, width=45, height=11)
     # pc_input.place(x=50, y=60)
     #
     # pc_choose = ttk.Combobox(window, values=['Один файл', 'Пакет'])
     # pc_choose.place(x=50, y=260)
     # pc_choose.insert(0, 'Один файл')
     # pc_choose.configure(state='readonly')
     #
     # pc_open_button = Button(window, text='Открыть', bg='#80ff95', width=17, font=('Calibri', 12), command=pc_open)
     # pc_open_button.place(x=267, y=260)
     #
     # pc_off = Button(window, text='⌂', font=('Arial Bold', 15), width=2, height=1, bg='black', fg='white',
     #                 command=pc_destroy)
     # pc_off.place(x=0, y=5)
     # ToolTip(pc_off, 'На главную...')


def Clock():
    def timing():
        current_time = strftime('%H:%M:%S')
        clock.config(text=current_time)
        clock.after(200, timing)

    root_z = Toplevel()
    root_z.resizable(False, False)
    root_z.attributes('-topmost', 'true')
    root_z.title('Часы')
    clock = Label(root_z, font=('times', 60, 'bold'))
    clock.pack()
    timing()


def LoadingLine():
    lola = LoadingLineGlobals()

    lola.line_height = 1
    lola.logo_size = 1

    def LoadingLineCycle():
        line_1.configure(height=lola.line_height)
        line_2.configure(height=lola.line_height)
        lola.line_height += 1
        r1.configure(font=('Arial Bold', lola.logo_size))
        lola.logo_size += 9

    def destroying():
        line_1.destroy()
        line_2.destroy()

    line_1 = Label(window, height=1, width=8, bg='red')
    line_1.place(x=20, y=20)
    line_2 = Label(window, height=1, width=8, bg='red')
    line_2.place(x=595, y=20)

    root.title('MihaSoft 15.0')
    center_window(root, 678, 730)
    root.minsize(678, 730)

    r1 = Label(window, text='Ⓜ', font=('Arial Bold', 1), fg='red')
    r1.place(x=160, y=0)

    for i in range(1, 30):
        window.after(20, LoadingLineCycle())
        window.update()

    line_1.configure(bg='green')
    line_2.configure(bg='green')
    window.update()
    window.after(800, destroying())
    r1.destroy()
    root.attributes('-topmost', 'false')


def YourWarningsDo():
    if not os.path.exists('MihaSoft Files/YW Files'):
        os.mkdir('MihaSoft Files/YW Files')
    now = datetime.datetime.now()

    for i in range(len(os.listdir('MihaSoft Files/YW Files'))):
        if os.listdir('MihaSoft Files/YW Files')[i] == (str(now.day) + '.' + str(now.month) + '.npy'):
            yw_data = load('MihaSoft Files/YW Files/' + os.listdir('MihaSoft Files/YW Files')[i])

            yw_window = Toplevel()
            yw_window.attributes('-topmost', 'true')
            center_window(yw_window, 435, 360)
            yw_window.title(os.listdir('MihaSoft Files/YW Files')[i] + ': Уведомление!')

            yw_message = Text(yw_window, font=('Arial Bold', 20), fg='red', width=28, height=3)
            yw_message.place(x=5, y=255)

            yw_message.insert(1.0, yw_data[2], 'center')
            yw_message.configure(state=DISABLED)

            yw_logo = Label(yw_window, text='Ⓜ', font=('Arial Bold', 150), fg='green')
            yw_logo.place(x=120, y=5)


def HolidayWarningsDo():
    now = datetime.datetime.now()

    def okno(text):
        hw_window = Toplevel()
        hw_window.attributes('-topmost', 'true')
        center_window(hw_window, 440, 330)
        hw_window.title(str(now))

        hw_do_message = Label(hw_window, text=('ПОЗДРАВЛЯЕМ!!!\n' + text), font=('Times New Roman', 20), fg='red')
        hw_do_message.pack(side=BOTTOM)

        hw_do_logo = Label(hw_window, text='Ⓜ', font=("Arial Bold", 150), fg='red')
        hw_do_logo.pack()

    if os.path.exists('MihaSoft Files/FlagHW.miha'):

        if now.day == 1 and now.month == 1:
            okno('Сегодня наступил новый\n    ' + str(now.year) + ' год!')

        if now.day == 7 and now.month == 1:
            okno('Сегодня отмечается\n      Рождество Христово! ')

        if now.day == 12 and now.month == 1:
            okno('Сегодня отмечается День\n Работника прокуратуры РФ!')

        if now.day == 13 and now.month == 1:
            okno('Сегодня День Российской\n печати!')

        if now.day == 14 and now.month == 1:
            okno('Сегодня День\n Трубопроводных войск!')

        if now.day == 21 and now.month == 1:
            okno('Сегодня День\n Инженерных войск!')

        if now.day == 25 and now.month == 1:
            okno('Сегодня День\n Российского студенчества!')

        if now.day == 27 and now.month == 1:
            okno('Сегодня День Снятия\n блокады Ленинграда!')

        if now.day == 2 and now.month == 2:
            okno('Сегодня День победы\n в Сталинградской битве!')

        if now.day == 8 and now.month == 2:
            okno('Сегодня День\n Российской науки!')

        if now.day == 9 and now.month == 2:
            okno('Сегодня День Работника\n гражданской авиации!')

        if now.day == 10 and now.month == 2:
            okno('Сегодня День\n Дипломатического работника!')

        if now.day == 15 and now.month == 2:
            okno('Сегодня День Памяти\n воинов-интернационалистов!')

        if now.day == 17 and now.month == 2:
            okno('Сегодня День Российских\n студенческих отрядов!')

        if now.day == 23 and now.month == 2:
            okno('Сегодня День\n Защитника Отечества!')

        if now.day == 24 and now.month == 2:
            okno('Сегодня день, когда\n Земля остановилась...')

        if now.day == 27 and now.month == 2:
            okno('Сегодня День Сил\n специальных операций!')

        if now.day == 1 and now.month == 3:
            okno('Сегодня Всемирный\n день Гражданской обороны!')

        if now.day == 8 and now.month == 3:
            okno('Сегодня Международный\n Женский день!')

        if now.day == 11 and now.month == 3:
            okno('Сегодня День\n Работников наркоконтроля!')

        if now.day == 12 and now.month == 3:
            okno('Сегодня День работников\n уголовно-исполнительной системы!')

        if now.day == 18 and now.month == 3:
            okno('Сегодня День\n Воссоединения Крыма и России!')

        if now.day == 19 and now.month == 3:
            okno('Сегодня День \nМоряка-подводника!')

        if now.day == 23 and now.month == 3:
            okno('Сегодня День Гидрометеоролога!')

        if now.day == 25 and now.month == 3:
            okno('Сегодня День\n Работника культуры России!')

        if now.day == 27 and now.month == 3:
            okno('Сегодня День Войск\n национальной гвардии РФ!')

        if now.day == 29 and now.month == 3:
            okno('Сегодня День Специалиста\n юридической службы!')

        if now.day == 1 and now.month == 4:
            okno('Сегодня День Смеха!')

        if now.day == 2 and now.month == 4:
            okno('Сегодня День Единения народов!')

        if now.day == 8 and now.month == 4:
            okno('Сегодня День\n Сотрудников военкоматов!')

        if now.day == 12 and now.month == 4:
            okno('Сегодня День Космонавтики!')

        if now.day == 15 and now.month == 4:
            okno('Сегодня День специалиста по\n радиоэлектронной борьбе!')

        if now.day == 18 and now.month == 4:
            okno('Сегодня День Победы\n на Чудском озере!')

        if now.day == 19 and now.month == 4:
            okno('Сегодня День\n Российской полиграфии!')

        if now.day == 21 and now.month == 4:
            okno('Сегодня День\n Местного самоуправления!')

        if now.day == 26 and now.month == 4:
            okno('Сегодня День Нотариата!')

        if now.day == 27 and now.month == 4:
            okno('Сегодня День\n Российского парламентаризма!')

        if now.day == 28 and now.month == 4:
            okno('Сегодня Международный\n день Охраны Труда!')

        if now.day == 30 and now.month == 4:
            okno('Сегодня День Пожарной охраны!')

        if now.day == 1 and now.month == 5:
            okno('Сегодня Праздник\n Весны и Труда!')

        if now.day == 7 and now.month == 5:
            okno('Сегодня День Радио!')

        if now.day == 9 and now.month == 5:
            okno('Сегодня День Победы!')

        if now.day == 21 and now.month == 5:
            okno('Сегодня День Полярника!')

        if now.day == 24 and now.month == 5:
            okno('Сегодня День Славянской\n письменности и культуры!')

        if now.day == 25 and now.month == 5:
            okno('Сегодня День Филолога!')

        if now.day == 26 and now.month == 5:
            okno('Сегодня День\n Российского предпринимательства!')

        if now.day == 27 and now.month == 5:
            okno('Сегодня Общероссийский\n день библиотек!')

        if now.day == 28 and now.month == 5:
            okno('Сегодня День Пограничника!')

        if now.day == 29 and now.month == 5:
            okno('Сегодня День\n Военного автомобилиста!')

        if now.day == 31 and now.month == 5:
            okno('Сегодня День\n Российской адвокатуры!')

        if now.day == 1 and now.month == 6:
            okno('Сегодня Международный День\n защиты детей!')

        if now.day == 2 and now.month == 6:
            okno('Сегодня День Спутникового\n мониторинга и навигации!')

        if now.day == 5 and now.month == 6:
            okno('Сегодня День Эколога!')

        if now.day == 6 and now.month == 6:
            okno('Сегодня День Русского языка!')

        if now.day == 8 and now.month == 6:
            okno('Сегодня День\n Социального работника!')

        if now.day == 12 and now.month == 6:
            okno('Сегодня День России!')

        if now.day == 14 and now.month == 6:
            okno('Сегодня День Работников\n миграционной службы!')

        if now.day == 18 and now.month == 6:
            okno('Сегодня День Службы\n военных сообщений!')

        if now.day == 25 and now.month == 6:
            okno('Сегодня День Работника\n статистики!')

        if now.day == 27 and now.month == 6:
            okno('Сегодня День Молодёжи!')

        if now.day == 29 and now.month == 6:
            okno('Сегодня День Партизан\n и подпольщиков!')

        if now.day == 30 and now.month == 6:
            okno('Сегодня День Экономиста!')

        if now.day == 3 and now.month == 7:
            okno('Сегодня День ГИБДД!')

        if now.day == 7 and now.month == 7:
            okno('Сегодня День Победы\n в Чесменском сражении!')

        if now.day == 8 and now.month == 7:
            okno('Сегодня День Семьи, любви и\n верности!')

        if now.day == 10 and now.month == 7:
            okno('Сегодня День Победы\n в Полтавской битве!')

        if now.day == 17 and now.month == 7:
            okno('Сегодня День Этнографа')

        if now.day == 25 and now.month == 7:
            okno('Сегодня День Следователя!')

        if now.day == 28 and now.month == 7:
            okno('Сегодня День Крещения Руси!')

        if now.day == 31 and now.month == 7:
            okno('Сегодня День ВМФ России!')

        if now.day == 1 and now.month == 8:
            okno('Сегодня День Тыла ВС РФ!')

        if now.day == 2 and now.month == 8:
            okno('Сегодня День ВДВ!')

        if now.day == 6 and now.month == 8:
            okno('Сегодня День\n Железнодорожных войск!')

        if now.day == 9 and now.month == 8:
            okno('Сегодня День Победы\n в Гангутском сражении!')

        if now.day == 12 and now.month == 8:
            okno('Сегодня День\n Военно-воздушных сил!')

        if now.day == 15 and now.month == 8:
            okno('Сегодня День Археолога!')

        if now.day == 18 and now.month == 8:
            okno('Сегодня День Географа!')

        if now.day == 22 and now.month == 8:
            okno('Сегодня День\n Государственного флага РФ!')

        if now.day == 23 and now.month == 8:
            okno('Сегодня День \nПобеды в Курской битве!')

        if now.day == 27 and now.month == 8:
            okno('Сегодня День Кино!')

        if now.day == 31 and now.month == 8:
            okno('Сегодня День\n Ветеринарного Работника!')

        if now.day == 1 and now.month == 9:
            okno('Сегодня День Знаний!')

        if now.day == 2 and now.month == 9:
            okno('Сегодня День \nРоссийской гвардии!')

        if now.day == 3 and now.month == 9:
            okno('Сегодня День\n Окончания Второй Мировой войны!')

        if now.day == 4 and now.month == 9:
            okno('Сегодня День Специалиста\n по ядерному обеспечению!')

        if now.day == 8 and now.month == 9:
            okno('Сегодня День\n Бородинского сражения!')

        if now.day == 9 and now.month == 9:
            okno('Сегодня День Тестировщика!')

        if now.day == 11 and now.month == 9:
            okno('Сегодня День\n Победы у мыса Тендра!')

        if now.day == 13 and now.month == 9:
            okno('Сегодня День Программиста!')

        if now.day == 19 and now.month == 9:
            okno('Сегодня День Оружейника!')

        if now.day == 21 and now.month == 9:
            okno('Сегодня День\n Победы в Куликовской битве!')

        if now.day == 24 and now.month == 9:
            okno('Сегодня День\n Системного аналитика!')

        if now.day == 27 and now.month == 9:
            okno('Сегодня Всемирный\n день Туризма!')

        if now.day == 28 and now.month == 9:
            okno('Сегодня День Работника\n атомной промышленности!')

        if now.day == 30 and now.month == 9:
            okno('Сегодня День Переводчика!')

        if now.day == 1 and now.month == 10:
            okno('Сегодня День Сухопутных войск!')

        if now.day == 4 and now.month == 10:
            okno('Сегодня День Космических войск!')

        if now.day == 5 and now.month == 10:
            okno('Сегодня День Учителя!')

        if now.day == 9 and now.month == 10:
            okno('День Победы в Битве за Кавказ!')

        if now.day == 19 and now.month == 10:
            okno('Сегодня Всероссийский\n день Лицеиста!')

        if now.day == 20 and now.month == 10:
            okno('Сегодня День\n Военного связиста!')

        if now.day == 22 and now.month == 10:
            okno('Сегодня День \nФинансово-экономической службы!')

        if now.day == 23 and now.month == 10:
            okno('Сегодня День Работников рекламы!')

        if now.day == 25 and now.month == 10:
            okno('Сегодня День Таможенника РФ!')

        if now.day == 29 and now.month == 10:
            okno('Сегодня День\n Вневедомственной охраны!')

        if now.day == 30 and now.month == 10:
            okno('Сегодня День Инженера-механика!')

        if now.day == 31 and now.month == 10:
            okno('Сегодня День\n Работника СИЗО и тюрем!')

        if now.day == 1 and now.month == 11:
            okno('Сегодня День\n Судебного пристава РФ!')

        if now.day == 4 and now.month == 11:
            okno('Сегодня День Народного Единства!')

        if now.day == 5 and now.month == 11:
            okno('Сегодня День Военного разведчика!')

        if now.day == 7 and now.month == 11:
            okno('Сегодня Годовщина\n Великой Октябрьской революции!')

        if now.day == 9 and now.month == 11:
            okno('Сегодня День Специального\n отряда быстрого реагирования!')

        if now.day == 10 and now.month == 11:
            okno('Сегодня День Сотрудника ОВД РФ!')

        if now.day == 11 and now.month == 11:
            okno('Сегодня День Экономиста!')

        if now.day == 13 and now.month == 11:
            okno('Сегодня День войск РХБЗ!')

        if now.day == 14 and now.month == 11:
            okno('Сегодня День Социолога!')

        if now.day == 19 and now.month == 11:
            okno('Сегодня Международный Мужской день')

        if now.day == 20 and now.month == 11:
            okno('Сегодня День Работника транспорта!')

        if now.day == 21 and now.month == 11:
            okno('Сегодня День Работника\n налоговых органов РФ!')

        if now.day == 27 and now.month == 11:
            okno('Сегодня День Морской пехоты!')

        if now.day == 30 and now.month == 11:
            okno('Сегодня Международный\n день Защиты информации!')

        if now.day == 1 and now.month == 12:
            okno('Сегодня День Победы \nв Синопском сражении!')

        if now.day == 3 and now.month == 12:
            okno('Сегодня День Неизвестного солдата!')

        if now.day == 5 and now.month == 12:
            okno('Сегодня День Волонтёра!')

        if now.day == 9 and now.month == 12:
            okno('Сегодня День Героев Отечества!')

        if now.day == 12 and now.month == 12:
            okno('Сегодня День Конституции РФ!')

        if now.day == 17 and now.month == 12:
            okno('Сегодня День Ракетных\n войск стратегического назначения!')

        if now.day == 18 and now.month == 12:
            okno('Сегодня День Работников ЗАГС!')

        if now.day == 19 and now.month == 12:
            okno('Сегодня День Работников\n военной контрразведки РФ!')

        if now.day == 20 and now.month == 12:
            okno('Сегодня День Работников\n органов безопасности РФ!')

        if now.day == 22 and now.month == 12:
            okno('Сегодня День Энергетика!')

        if now.day == 24 and now.month == 12:
            okno('Сегодня День Взятия\n турецкой крепости Измаил!')

        if now.day == 27 and now.month == 12:
            okno('Сегодня День Спасателя РФ!')

        if now.day == 31 and now.month == 12:
            okno('Сегодня Последний день ' + str(now.year) + ' года!')


def Settings():
    def create_Settings():
        def click_an_but():
            if not os.path.exists('MihaSoft Files/AnimationFlagFile.miha'):
                f = open('MihaSoft Files/AnimationFlagFile.miha', 'w')
                f.close()
                animation_button.configure(text='ВЫКЛЮЧИТЬ', bg='red')
            else:
                os.remove('MihaSoft Files/AnimationFlagFile.miha')
                animation_button.configure(text='ВКЛЮЧИТЬ', bg='green')

        def click_so_but():
            if not os.path.exists('MihaSoft Files/SoundFlagFile.miha'):
                f = open('MihaSoft Files/SoundFlagFile.miha', 'w')
                f.close()
                sound_button.configure(text='ВЫКЛЮЧИТЬ', bg='red')
            else:
                os.remove('MihaSoft Files/SoundFlagFile.miha')
                sound_button.configure(text='ВКЛЮЧИТЬ', bg='green')

        def click_ti_but():
            if not os.path.exists('MihaSoft Files/TintFlagFile.miha'):
                f = open('MihaSoft Files/TintFlagFile.miha', 'w')
                f.close()
                third_button.configure(text='ВЫКЛЮЧИТЬ', bg='red')
            else:
                os.remove('MihaSoft Files/TintFlagFile.miha')
                third_button.configure(text='ВКЛЮЧИТЬ', bg='green')

        def click_up_but():
            if not os.path.exists('MihaSoft Files/UpdateFlag.miha'):
                fl = open('MihaSoft Files/UpdateFlag.miha', 'w')
                fl.close()
                fourth_button.configure(text='ВКЛЮЧИТЬ', bg='green')
            else:
                os.remove('MihaSoft Files/UpdateFlag.miha')
                fourth_button.configure(text='ВЫКЛЮЧИТЬ', bg='red')

        def click_am_but():
            if not os.path.exists('MihaSoft Files/FlagHW.miha'):
                fl = open('MihaSoft Files/FlagHW.miha', 'w')
                fl.close()
                fifth_button.configure(text='ВЫКЛЮЧИТЬ', bg='red')
            else:
                os.remove('MihaSoft Files/FlagHW.miha')
                fifth_button.configure(text='ВКЛЮЧИТЬ', bg='green')

        def set_exit():
            m.set_window.destroy()

        m.set_window = Toplevel()
        center_window(m.set_window, 400, 430)
        m.set_window.resizable(False, False)
        m.set_window.title('Настройки')

        first_label = Label(m.set_window, text='Анимация запуска программы:')
        first_label.place(x=10, y=10)

        animation_button = Button(m.set_window, font=("Arial Bold", 11), width=13, fg='white', command=click_an_but)
        animation_button.place(x=220, y=10)

        if not os.path.exists('MihaSoft Files/AnimationFlagFile.miha'):
            animation_button.configure(text='ВКЛЮЧИТЬ', bg='green')
        else:
            animation_button.configure(text='ВЫКЛЮЧИТЬ', bg='red')

        second_label = Label(m.set_window, text='Звук:')
        second_label.place(x=10, y=90)

        sound_button = Button(m.set_window, font=('Arial Bold', 11), width=13, fg='white', command=click_so_but)
        sound_button.place(x=220, y=90)

        if not os.path.exists('MihaSoft Files/SoundFlagFile.miha'):
            sound_button.configure(text='ВКЛЮЧИТЬ', bg='green')
        else:
            sound_button.configure(text='ВЫКЛЮЧИТЬ', bg='red')

        third_label = Label(m.set_window, text='Всплывающие подсказки\n к кнопкам:')
        third_label.place(x=10, y=165)

        third_button = Button(m.set_window, font=('Arial Bold', 11), width=13, fg='white', command=click_ti_but)
        third_button.place(x=220, y=170)

        if not os.path.exists('MihaSoft Files/TintFlagFile.miha'):
            third_button.configure(text='ВКЛЮЧИТЬ', bg='green')
        else:
            third_button.configure(text='ВЫКЛЮЧИТЬ', bg='red')

        fourth_label = Label(m.set_window, text='Уведомления о выходе \nобновлений:')
        fourth_label.place(x=10, y=245)

        fourth_button = Button(m.set_window, font=('Arial Bold', 11), width=13, fg='white', command=click_up_but)
        fourth_button.place(x=220, y=250)

        if not os.path.exists('MihaSoft Files/UpdateFlag.miha'):
            fourth_button.configure(text='ВЫКЛЮЧИТЬ', bg='red')
        else:
            fourth_button.configure(text='ВКЛЮЧИТЬ', bg='green')

        fifth_label = Label(m.set_window, text='HolidayWarnings:')
        fifth_label.place(x=10, y=325)

        fifth_button = Button(m.set_window, font=('Arial Bold', 11), width=13, fg='white', command=click_am_but)
        fifth_button.place(x=220, y=330)

        if not os.path.exists('MihaSoft Files/FlagHW.miha'):
            fifth_button.configure(text='ВКЛЮЧИТЬ', bg='green')
        else:
            fifth_button.configure(text='ВЫКЛЮЧИТЬ', bg='red')

        exit_button = Button(m.set_window, text='OK', bg='#b8b8b8', font=('Arial Bold', 11), width=13, command=set_exit)
        exit_button.place(x=220, y=380)

    try:
        m.set_window.resizable(False, False)

    except AttributeError:
        create_Settings()

    except TclError:
        create_Settings()


def Music():
    Beep(300, 900)
    for i in range(1, 4):
        window.after(50, Beep(300, 100))


def AuthorList():
    def create_AuthorList():
        def mess_exit():
            m.mess_window.destroy()

        m.mess_window = Toplevel()
        center_window(m.mess_window, 435, 280)
        m.mess_window.title('Сообщение от автора')
        m.mess_window.resizable(False, False)

        mess_ground = Text(m.mess_window, width=52, height=13)
        mess_ground.place(x=5, y=5)

        try:
            response = requests.get('https://mihasoft.glitch.me/api.txt')
            mess_ground.insert(1.0, response.text)
            mess_ground.configure(state='disabled')

        except requests.exceptions.ConnectionError:
            mess_ground.configure(fg='red')
            mess_ground.insert(1.0, 'НЕТ ДОСТУПА К СЕТИ!')

        exit_button = Button(m.mess_window, text='OK', bg='#b8b8b8', font=('Arial Bold', 11), width=13,
                             command=mess_exit)
        exit_button.place(x=270, y=230)

    try:
        m.mess_window.resizable(False, False)

    except AttributeError:
        create_AuthorList()

    except TclError:
        create_AuthorList()


def valute():
    def create_valute():
        def valute_exit():
            m.valute_window.destroy()

        m.valute_window = Toplevel()
        center_window(m.valute_window, 460, 280)
        m.valute_window.resizable(False, False)
        m.valute_window.title('Курсы валют')

        def translate_val():
            val_dict = {
                'Белорусский рубль': valute_json['Valute']['BYN']['Value'],
                'Фунт стерлингов': valute_json['Valute']['GBP']['Value'],
                'Евро': valute_json['Valute']['EUR']['Value'],
                'Доллар США': valute_json['Valute']['USD']['Value'],
                'Российский рубль': '1'
            }
            try:
                val_course = float(val_dict[val_combobox.get()]) / float(val_dict[val_combobox_1.get()])
                val_one = val_res_place.get()
                val_res_place.delete(0, END)
                val_res_place.insert(0, str(float(val_one) * val_course))
            except KeyError:
                messagebox.showwarning(title='Ошибка', message='Выберите валюты для перевода!', parent=m.valute_window)
            except ValueError:
                messagebox.showwarning(title='Ошибка', message='Введено некорректное значение!', parent=m.valute_window)

        def copy_val():
            copy(val_res_place.get())

        try:
            response = requests.get('https://www.cbr-xml-daily.ru/daily_json.js')
            valute_json = response.json()

            date_string = ''
            for i in range(0, 10):
                date_string += valute_json['Date'][i]
            date_string += ' '
            for i in range(11, 16):
                date_string += valute_json['Date'][i]
            m.valute_window.title('Курсы валют - ' + date_string)

            val_label_1 = Label(m.valute_window, text='Доллар США:', font=('Times New Roman', 14))
            val_label_1.place(x=10, y=10)

            val_label_1_2 = Label(m.valute_window, text=valute_json['Valute']['USD']['Value'],
                                  font=('Times New Roman', 14))
            val_label_1_2.place(x=180, y=10)

            val_label_2 = Label(m.valute_window, text='Евро:', font=('Times New Roman', 14))
            val_label_2.place(x=10, y=50)

            val_label_2_2 = Label(m.valute_window, text=valute_json['Valute']['EUR']['Value'],
                                  font=('Times New Roman', 14))
            val_label_2_2.place(x=180, y=50)

            val_label_3 = Label(m.valute_window, text='Фунт стерлингов:', font=('Times New Roman', 14))
            val_label_3.place(x=10, y=90)

            val_label_3_2 = Label(m.valute_window, text=valute_json['Valute']['GBP']['Value'],
                                  font=('Times New Roman', 14))
            val_label_3_2.place(x=180, y=90)

            val_label_3 = Label(m.valute_window, text='Белорусский рубль:', font=('Times New Roman', 14))
            val_label_3.place(x=10, y=130)

            val_label_3_2 = Label(m.valute_window, text=valute_json['Valute']['BYN']['Value'],
                                  font=('Times New Roman', 14))
            val_label_3_2.place(x=180, y=130)

            val_label_x_1 = Label(m.valute_window, text='Перевести из:')
            val_label_x_1.place(x=280, y=5)

            val_combobox = ttk.Combobox(m.valute_window,
                                        values=['Белорусский рубль', 'Фунт стерлингов', 'Евро', 'Доллар США',
                                                'Российский рубль'],
                                        state='readonly')
            val_combobox.place(x=280, y=40)

            val_label_x_2 = Label(m.valute_window, text='Перевести в:')
            val_label_x_2.place(x=280, y=70)

            val_combobox_1 = ttk.Combobox(m.valute_window,
                                          values=['Белорусский рубль', 'Фунт стерлингов', 'Евро', 'Доллар США',
                                                  'Российский рубль'],
                                          state='readonly')
            val_combobox_1.place(x=280, y=105)

            val_res_place = Entry(m.valute_window, width=23)
            val_res_place.place(x=280, y=145)

            valute_go_button = Button(m.valute_window, text='Перевести', width=16, font=('Times New Roman', 11),
                                      bg='#87e6a2',
                                      command=translate_val)
            valute_go_button.place(x=280, y=180)

            valute_copy_button = Button(m.valute_window, text='Копировать', width=16, font=('Times New Roman', 11),
                                        bg='#e6df87',
                                        command=copy_val)
            valute_copy_button.place(x=280, y=220)

        except requests.exceptions.ConnectionError:
            center_window(m.valute_window, 330, 280)

            err_label = Label(m.valute_window, text='НЕТ ДОСТУПА К СЕТИ!', font=('Times New Roman', 14), fg='red')
            err_label.place(x=10, y=10)

        valute_exit_button = Button(m.valute_window, text='ОК', width=16, font=('Times New Roman', 14), bg='#b8b8b8',
                                    command=valute_exit)
        valute_exit_button.place(x=40, y=200)

    try:
        m.valute_window.resizable(False, False)

    except AttributeError:
        create_valute()

    except TclError:
        create_valute()


def CleanTemp():
    def create_CleanTemp():
        def ct_clean():
            delete_size = 0
            number_of_del_files = 0
            no_del_files = ''
            user_name = os.environ.get('USERNAME')
            ct_report_ground.configure(state=NORMAL)
            ct_report_ground.insert('1.0', 'Идёт процесс удаления...\n\n')
            for i in os.listdir('Users/' + user_name + '/AppData/Local/Temp'):
                try:
                    d_size = os.path.getsize('Users/' + user_name + '/AppData/Local/Temp/' + i)
                    if os.path.isdir('Users/' + user_name + '/AppData/Local/Temp/' + i):
                        rmtree('Users/' + user_name + '/AppData/Local/Temp/' + i)
                    else:
                        os.remove('Users/' + user_name + '/AppData/Local/Temp/' + i)
                    number_of_del_files += 1
                    delete_size += d_size
                except PermissionError:
                    no_del_files += (i + '\n')

            delete_size = round(delete_size / (1024 * 1024), 5)

            ct_report_ground.insert('2.0', 'Всего удалено ' + str(number_of_del_files) + ' объектов размером\n')
            ct_report_ground.insert('3.0', str(delete_size) + ' мегабайт\n')
            ct_report_ground.insert('4.0', 'Не удалось удалить следующие файлы:\n' + no_del_files)
            ct_report_ground.configure(state=DISABLED)

        def ct_ok():
            m.ct_window.destroy()

        m.ct_window = Toplevel()
        center_window(m.ct_window, 415, 460)
        m.ct_window.resizable(False, False)
        m.ct_window.title('Очистить папку Temp')

        ct_clean_button = Button(m.ct_window, text='Очистить', bg='green', fg='white', width=20,
                                 font=('Times New Roman', 16),
                                 command=ct_clean)
        ct_clean_button.place(x=80, y=10)

        ct_report_ground = Text(m.ct_window, width=50, height=20, state=DISABLED)
        ct_report_ground.place(x=5, y=60)

        ct_ok_button = Button(m.ct_window, text='ОK', bg='#b8b8b8', width=20, font=('Times New Roman', 16),
                              command=ct_ok)
        ct_ok_button.place(x=80, y=400)

    try:
        m.ct_window.resizable(False, False)

    except AttributeError:
        create_CleanTemp()

    except TclError:
        create_CleanTemp()


def bulls_and_cows():
    def create_bulls_and_cows():
        bac = BACGlobals()
        stop_list = []
        for i in range(0, 10):
            for j in range(0, 10):
                stop_list.append(str(i) + str(j) + str(i))
        for i in range(0, 10):
            for j in range(0, 10):
                stop_list.append(str(i) + str(i) + str(j))
                stop_list.append(str(i) + str(j) + str(j))
        for i in range(0, 10):
            for j in range(0, 10):
                stop_list.append(str(i) + str(j) + str(j))

        def bac_new_game():
            bac.k = 0
            bac.flag = True
            bac_input.delete(0, END)
            bac_num_label.configure(text='0 х.')
            bac_ground.configure(bg='#b8b8b8')

            bac.number = randint(100, 999)
            if str(bac.number) in stop_list:
                while str(bac.number) in stop_list:
                    bac.number = randint(100, 999)
            bac_res_label.configure(text='')

        def bac_answer():
            K = 0
            B = 0
            Z = False
            if bac.flag:
                for ZOV in bac_input.get():
                    if ZOV not in '0123456789':
                        Z = True
                        break
                if Z:
                    messagebox.showwarning(parent=m.bac_window, title='INFO',
                                           message='Введены посторонние символы!')
                elif len(bac_input.get()) != 3 or bac_input.get()[0] == '0':
                    messagebox.showwarning(parent=m.bac_window, title='INFO',
                                           message='Введено не трёхзначное число!')
                elif bac_input.get() in stop_list:
                    messagebox.showwarning(parent=m.bac_window, title='INFO',
                                           message='Введено число с повторяющимися числами!')
                else:
                    bac.k += 1
                    bac_num_label.configure(text='{} х.'.format(bac.k))
                    if bac_input.get()[0] not in str(bac.number) and bac_input.get()[1] not in str(bac.number) and \
                            bac_input.get()[2] not in str(bac.number):
                        bac_ground.configure(bg='#d49f9f')
                        bac_res_label.configure(text='НЕВЕРНО!', fg='red')
                    elif bac_input.get()[0] == str(bac.number)[0] and bac_input.get()[1] == str(bac.number)[1] and \
                            bac_input.get()[2] == str(bac.number)[2]:
                        bac_ground.configure(bg='#a2d49f')
                        if os.path.exists('MihaSoft Files/BACFlag.miha'):
                            bac_mess = 'С КАЙФОМ, ПОН!'
                            on_M()
                        else:
                            bac_mess = 'ВЫ ВЫИГРАЛИ!'
                        bac_res_label.configure(text=bac_mess, fg='green')
                        bac.flag = False

                    else:
                        if bac_input.get()[0] == str(bac.number)[0]:
                            B += 1
                        if bac_input.get()[1] == str(bac.number)[1]:
                            B += 1
                        if bac_input.get()[2] == str(bac.number)[2]:
                            B += 1
                        if (bac_input.get()[0] in str(bac.number)) and (bac_input.get()[0] != str(bac.number)[0]):
                            K += 1
                        if (bac_input.get()[1] in str(bac.number)) and (bac_input.get()[1] != str(bac.number)[1]):
                            K += 1
                        if (bac_input.get()[2] in str(bac.number)) and (bac_input.get()[2] != str(bac.number)[2]):
                            K += 1
                        res_1 = 'а'
                        res_2 = 'ы'
                        if B == 0:
                            res_1 = 'ов'
                        elif B == 1:
                            res_1 = ''
                        if K == 0:
                            res_2 = ''
                        elif K == 1:
                            res_2 = 'а'
                        bac_ground.configure(bg='#e6d47c')
                        bac_res_label.configure(text='{} бык{}, {} коров{}.'.format(str(B), res_1, str(K), res_2),
                                                fg='#d68233')

        def bac_destroy(event):
            try:
                bac.s_window.destroy()
            except AttributeError:
                pass
            return event

        def bac_settings():
            def ht_ok():
                if bac_s_comb.get() == 'Вы выиграли!':
                    try:
                        os.remove('MihaSoft Files/BACFlag.miha')
                    except FileNotFoundError:
                        pass

                else:
                    fil = open('MihaSoft Files/BACFlag.miha', 'w')
                    fil.close()
                bac.s_window.destroy()

            bac.s_window = Toplevel()
            center_window(bac.s_window, 200, 100)
            bac.s_window.resizable(False, False)
            bac.s_window.title('Настройки')

            bac_s_label = Label(bac.s_window, text='Текст сообщения о победе:')
            bac_s_label.place(x=5, y=5)

            bac_s_comb = ttk.Combobox(bac.s_window, values=['Вы выиграли!', 'С кайфом, пон!'], state='readonly')
            bac_s_comb.place(x=10, y=30)

            bac_s_but = Button(bac.s_window, text='OK', width=10, command=ht_ok)
            bac_s_but.place(x=40, y=60)

        m.bac_window = Toplevel()
        center_window(m.bac_window, 300, 240)
        m.bac_window.resizable(False, False)
        m.bac_window.title('Быки и коровы')
        m.bac_window.bind('<Destroy>', bac_destroy)

        enu = Menu(m.bac_window)
        m.bac_window.config(menu=enu)
        enu.add_command(label='Настройки', command=bac_settings)

        bac_title = Label(m.bac_window, text='Bulls&Cows', font=('Arial Bold', 16), fg='red')
        bac_title.place(x=15, y=5)

        bac_num_label = Label(m.bac_window)
        bac_num_label.place(x=140, y=10)

        bac_new_button = Button(m.bac_window, text='Новая игра', bg='green', fg='white', width=10,
                                font=('Times New Roman', 12), command=bac_new_game)
        bac_new_button.place(x=185, y=5)

        bac_ground = Label(m.bac_window, width=38, height=5, bg='#b8b8b8')
        bac_ground.place(x=15, y=50)

        bac_label = Label(m.bac_window, text='Ваш ответ:')
        bac_label.place(x=65, y=72)

        bac_input = Entry(m.bac_window, width=4, font=('Times New Roman', 12))
        bac_input.place(x=185, y=70)

        bac_ans_button = Button(m.bac_window, text='Ответить', bg='yellow', width=10, font=('Times New Roman', 12),
                                command=bac_answer)
        bac_ans_button.place(x=100, y=140)

        bac_res_label = Label(m.bac_window, font=('Arial Bold', 16))
        bac_res_label.pack(side=BOTTOM)
        bac_new_game()

    try:
        m.bac_window.resizable(False, False)

    except AttributeError:
        create_bulls_and_cows()

    except TclError:
        create_bulls_and_cows()


def makeQR():
    def create_makeQR():
        def qr_make():
            try:
                code = make(qr_input.get(1.0, END))
                qr_file_name = asksaveasfilename(title='Сохранить файл', defaultextension='.png',
                                                 filetypes=(('PNG file', '*.png'), ('All Files', '*.*')))
                if qr_file_name:
                    code.save(qr_file_name)
                    messagebox.showinfo(parent=m.qr_window, title='Успешно!', message='QR-код создан!')
            except DataOverflowError:
                messagebox.showerror(parent=m.qr_window, title='Ошибка!', message='Слишком большой объём данных!')

        def qr_view():
            try:
                code = make(qr_input.get(1.0, END))
                code.save('MihaSoft Files/Temp/temp.png')
                os.startfile('MihaSoft Files/Temp/temp.png')
            except DataOverflowError:
                messagebox.showerror(parent=m.qr_window, title='Ошибка!', message='Слишком большой объём данных!')

        def qr_destroy():
            m.qr_window.destroy()

        m.qr_window = Toplevel()
        center_window(m.qr_window, 390, 190)
        m.qr_window.title('QR-код')
        m.qr_window.resizable(False, False)

        qr_label = Label(m.qr_window, text='Введите текст:')
        qr_label.place(x=10, y=10)

        qr_input = Text(m.qr_window, width=45, height=4)
        qr_input.place(x=10, y=40)

        qr_ok_button = Button(m.qr_window, text='СОЗДАТЬ', bg='green', fg='white', width=10,
                              font=('Times New Roman', 12), command=qr_make)
        qr_ok_button.place(x=275, y=130)

        qr_ab_button = Button(m.qr_window, text='ВЫХОД', bg='#b8b8b8', width=10,
                              font=('Times New Roman', 12), command=qr_destroy)
        qr_ab_button.place(x=142, y=130)

        qr_view_button = Button(m.qr_window, text='ПОКАЗАТЬ', bg='yellow', width=10,
                                font=('Times New Roman', 12), command=qr_view)
        qr_view_button.place(x=10, y=130)

    try:
        m.qr_window.resizable(False, False)

    except AttributeError:
        create_makeQR()

    except TclError:
        create_makeQR()


def english_dict():
    def create_english_dict():
        def ed_exit():
            m.dict_window.destroy()

        def ed_translate(hi=None):
            with open('dict.json', encoding='utf8') as fi:
                verbs = fi.read()
            verbs = loads(verbs)
            ed_res_str = ''
            ed_en = False
            ed_en_big = False
            ed_ru = False
            ed_ru_big = False
            ed_all = False
            ed_this = False
            if not ed_input.get():
                ed_this = True
            if ed_input.get()[0] in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
                ed_en_big = True
            if ed_input.get()[0] in 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЭЮЯ':
                ed_ru_big = True
            for i in ed_input.get():
                if i in 'abcdefghijklmnopqrstuvwxyz':
                    ed_en = True
                elif i in 'абвгдеёжзийклмнопрстуфхцчшщьыъэюя':
                    ed_ru = True
                elif not ed_ru_big and not ed_en_big:
                    ed_all = True
            if ed_en and not ed_ru and not ed_all:
                for i in verbs:
                    if i['word'] == ed_input.get():
                        for j in i['translates']:
                            ed_res_str += (j + '\n')
                        break
                if not ed_res_str:
                    messagebox.showinfo(title='INFO', message='Слово не найдено!', parent=m.dict_window)
                else:
                    ed_output.delete(1.0, END)
                    ed_output.insert(1.0, ed_res_str)

            elif ed_ru and not ed_en and not ed_all:
                for i in verbs:
                    for j in i['translates']:
                        if j == ed_input.get():
                            ed_res_str += (i['word'] + '\n')
                        break
                if not ed_res_str:
                    messagebox.showinfo(title='INFO', message='Слово не найдено!', parent=m.dict_window)
                else:
                    ed_output.delete(1.0, END)
                    ed_output.insert(1.0, ed_res_str)

            elif ed_ru and ed_en and not ed_all:
                messagebox.showwarning(title='Ошибка', message='Буквы разных алфавитов в слове!', parent=m.dict_window)
            elif ed_all:
                messagebox.showwarning(title='Ошибка', message='Введены посторонние символы!', parent=m.dict_window)
            elif ed_this:
                messagebox.showwarning(title='Ошибка', message='Введите слово для перевода!', parent=m.dict_window)
            return hi

        m.dict_window = Toplevel()
        center_window(m.dict_window, 420, 350)
        m.dict_window.title('Англо-русский словарь')
        m.dict_window.resizable(False, False)

        ed_label = Label(m.dict_window, text='Слово:')
        ed_label.place(x=5, y=15)

        ed_input = Entry(m.dict_window, width=55)
        ed_input.place(x=60, y=15)

        ed_output = Text(m.dict_window, width=47, height=13)
        ed_output.place(x=15, y=60)

        ed_transl_but = Button(m.dict_window, text='ПЕРЕВЕСТИ', bg='green', fg='white', width=15,
                               font=('Times New Roman', 13), command=ed_translate)
        ed_transl_but.place(x=15, y=290)

        ed_exit_but = Button(m.dict_window, text='ВЫХОД', bg='#b8b8b8', width=15,
                             font=('Times New Roman', 13), command=ed_exit)
        ed_exit_but.place(x=250, y=290)

        ed_input.bind('<Return>', ed_translate)

    try:
        m.dict_window.resizable(False, False)

    except AttributeError:
        create_english_dict()

    except TclError:
        create_english_dict()


def about_ms(par=None):
    def create_about_ms():
        def inf_close():
            m.info_window.destroy()

        m.info_window = Toplevel()
        center_window(m.info_window, 220, 320)
        m.info_window.resizable(False, False)
        m.info_window.title('О программе')

        info_title = Label(m.info_window, text='Ⓜ', font=("Arial Bold", 100), fg='red')
        info_title.pack()

        info_string_1 = Label(m.info_window, text='Универсальная программа для\n домашнего использования')
        info_string_1.place(x=20, y=140)

        info_string_2 = Label(m.info_window, text='Версия:   15.0')
        info_string_2.place(x=70, y=190)

        info_string_3 = Label(m.info_window, text='Лицензия:   MIT License')
        info_string_3.place(x=40, y=210)

        info_string_4 = Label(m.info_window, text='Copyright © 2022 Власко М. М.')
        info_string_4.place(x=25, y=240)

        inf_close_button = Button(m.info_window, text='OK', bg='#b8b8b8', width=8, font=('Times New Roman', 10),
                                  command=inf_close)
        inf_close_button.place(x=80, y=270)

    try:
        m.info_window.resizable(False, False)

    except AttributeError:
        create_about_ms()

    except TclError:
        create_about_ms()

    return par


def check_update():
    def cu_abort():
        fl = open('MihaSoft Files/UpdateFlag.miha', 'w')
        fl.close()
        cu_window.destroy()

    def cu_open():
        cu_window.destroy()
        open_new('https://mihasoft.glitch.me/#zov')

    if not os.path.exists('MihaSoft Files/UpdateFlag.miha'):
        try:
            cu_response = requests.get('https://mihasoft.glitch.me/vers.txt')
            if cu_response.text != VERSION:
                cu_window = Toplevel()
                center_window(cu_window, 410, 150)
                cu_window.resizable(False, False)
                cu_window.title('Обновление')

                cu_label = Label(cu_window,
                                 text='''Внимание! Ваша версия MihaSoft устарела. 
Вы можете скачать последнюю версию {}
на официальном сайте.'''.format(cu_response.text), font=('Times New Roman', 13), fg='red')
                cu_label.pack()

                site_button = Button(cu_window, text='Перейти на сайт', bg='green', fg='white', width=18,
                                     font=('Times New Roman', 12), command=cu_open)
                site_button.place(x=25, y=70)

                ab_button = Button(cu_window, text='Больше не показывать', bg='#b8b8b8', width=18,
                                   font=('Times New Roman', 12), command=cu_abort)
                ab_button.place(x=215, y=70)
        except requests.exceptions.ConnectionError:
            pass


def blackout(button):
    """
    Затемнение кнопок главной страницы
    при наведении на них курсора.
    """

    bg = button['background']
    fg = button['foreground']

    def on_enter(e):
        button['background'] = '#6e6e6e'
        button['foreground'] = 'white'
        return e

    def on_leave(e):
        button['background'] = bg
        button['foreground'] = fg
        return e

    button.bind('<Enter>', on_enter)
    button.bind('<Leave>', on_leave)


def help_show(h_title, message, url):
    def help_destroy():
        m.help_window.destroy()

    def help_more():
        open_new(url)
        m.help_window.destroy()

    def create_help_window():
        m.help_window = Toplevel()
        center_window(m.help_window, 500, 300)
        m.help_window.title(h_title)
        m.help_window.resizable(False, False)

        help_text = Text(m.help_window, width=60, height=12)
        help_text.insert(1.0, message)
        help_text.configure(state=DISABLED)
        help_text.place(x=5, y=5)

        h_exit_but = Button(m.help_window, text='OK', bg='#b8b8b8', width=12,
                            font=('Times New Roman', 12), command=help_destroy)
        h_exit_but.place(x=10, y=250)

        h_more_but = Button(m.help_window, text='ПОДРОБНЕЕ', bg='green', fg='white', width=12,
                            font=('Times New Roman', 12), command=help_more)
        h_more_but.place(x=370, y=250)

    try:
        m.help_window.resizable(False, False)

    except AttributeError:
        create_help_window()

    except TclError:
        create_help_window()


def about_yourwarnings(her):
    help_show('YourWarnings', 'Приложение для создания пользовательских уведомлений. Сохраняет текст и дату \
уведомления в файл и автоматически выводит уведомление при запуске MihaSoft в указанную дату.',
              'https://mihasoft.glitch.me/yw.html')
    return her


def about_accountmanager(her):
    help_show('AccountManager', 'Приложение для генерации паролей, сохранения данных о регистрации на конкретном '
                                'сервисе (логина и пароля), их демонстрации.',
              'https://mihasoft.glitch.me/')
    return her


def about_windowmanager(her):
    help_show('WindowManager', 'Приложение для создание кастомизированных окон с надписями. \
Поддерживает сохранение, редактирование, удаление и демонстрацию таких окон.',
              'https://mihasoft.glitch.me/wm.html')
    return her


def about_mihnote(her):
    help_show('MihNote', 'Приложение для работы с текстовыми заметками. \
Поддерживает создание, редактирование, удаление и просмотр заметок.',
              'https://mihasoft.glitch.me/mn.html')
    return her


def about_crosszero(her):
    help_show('CrossZero', 'Классическая игра «Крестики-нолики» 3х3 клетки. Поддерживает использование \
собственных имён игроков и автоматическую запись отчётов о проведённых играх.',
              'https://mihasoft.glitch.me/cz.html')
    return her


def about_paint(her):
    help_show('Paint', 'Графический пиксельный редактор с полем редактирование 30х10 клеток. \
Использует оригинальный формат изображения. Поддерживает сохранение, редактирование и удаление файлов.',
              'https://mihasoft.glitch.me/p.html')
    return her


def about_turtlepaint(her):
    help_show('TurtlePaint', 'Графический векторный редактор. Поддерживает сохранение файлов методом скриншотирования, \
а также изменение цвета редактирования.',
              'https://mihasoft.glitch.me/tp.html')
    return her


def about_yourage(her):
    help_show('YourAge', 'Приложение для определения промежутка времени между двумя датами. \
Поддерживает подстановку системной даты, сохранение и подстановку исходных дат, вывод времени в двух форматах.',
              'https://mihasoft.glitch.me/yao.html')
    return her


def about_middlescore(her):
    help_show('MiddleScore', 'Приложение для расчёта среднего балла оценок. \
Поддерживает оценки с двойным индексом и игнорирование чисел, не являющихся оценками..',
              'https://mihasoft.glitch.me/mso.html')
    return her


def about_saper(her):
    help_show('Saper', 'Классическая игра «Сапёр» с полем 5х5 клеток. Поддерживает сохранение статистики, \
изменение количества мин в пределах от 1 до 23 и установку флажков.',
              'https://mihasoft.glitch.me/s.html')
    return her


def about_watermarks(her):
    help_show('WaterMarks', 'Приложение для нанесения текстовых водяных знаков на изображение. \
Поддерживает выбор шрифта, размера, местоположения и цвета текста, предварительный просмотр результата..',
              'https://mihasoft.glitch.me/')
    return her


def about_hypertext(her):
    help_show('HyperText', 'Приложение для создания, сохранения и публикации в Интернете html-страниц. \
Поддерживает добавление блоков, кнопок, ссылок и изображений, изменение цвета текста и фона, предварительный \
просмотр страниц и публикацию на сервере MihaSoft.',
              'https://mihasoft.glitch.me/')
    return her


def about_sml(her):
    help_show('The SML - IDE & Interpreter', 'Редактор и интерпретатор кода на простейшем языке программирования. \
Поддерживает сохранение файлов с кодом и вывод сообщений об ошибках при запуске программ.',
              'https://mihasoft.glitch.me/sml.html')
    return her


def about_numbersystems(her):
    help_show('NumberSystems', 'Перевод чисел из систем счисления вплоть до миллионеричной. \
Поддерживает копирование результата перевода в буфер обмена.',
              'https://mihasoft.glitch.me/tns.html')
    return her


def about_shmalyalka(her):
    help_show('Shmalyalka', 'Динамическая игра-шутер. Поддерживает запись статистики.',
              'https://mihasoft.glitch.me/sml.html')
    return her


def on_M(par=None):
    m.monk_window.append(Toplevel())
    m.monk_window[-1].title('monkey...')
    center_window(m.monk_window[-1], 240, 178)
    m.monk_window[-1].resizable(False, False)
    monk_gif = Gif(m.monk_window[-1], path='monkey.gif')
    monk_gif.pack()
    root.bind('<KeyPress-BackSpace>', M_out)
    return par


def M_out(param=None):
    try:
        m.monk_window[-1].destroy()
        m.monk_window.pop(-1)
    except IndexError:
        pass
    return param


def home():
    def home_to_yao():
        home_destroying()
        YourAge()

    def home_to_mso():
        home_destroying()
        MiddleScore()

    def home_to_sml():
        home_destroying()
        SML()

    def home_to_ns():
        home_destroying()
        NumberSystems()

    def home_to_cz():
        home_destroying()
        CrossZero()

    def home_to_mn():
        home_destroying()
        MihNote()

    def home_to_wm():
        home_destroying()
        WindowManager()

    def home_to_hw():
        home_destroying()
        AccountManager()

    def home_to_yw():
        home_destroying()
        YourWarnings()

    def home_to_sh():
        home_destroying()
        Shmalyalka()

    def home_to_p():
        home_destroying()
        Paint()

    def home_to_s():
        home_destroying()
        Saper()

    def home_to_tp():
        home_destroying()
        TurtlePaint()

    def home_to_ws():
        home_destroying()
        WaterMarks()

    def home_to_ht():
        home_destroying()
        HyperText()

    def home_to_mr():
        home_destroying()
        Morse()

    # def home_to_pc():
    #     home_destroying()
    #     PythonCompiler()

    def home_destroying():
        try:
            MIHA_SOFT_LOGOTYPE.destroy()
        except AttributeError:
            pass

        ms_frame.destroy()

    def main_exit(fuck):
        root.quit()
        return fuck

    root.title('MihaSoft 15.0')
    center_window(root, 678, m.abs_height)
    root.minsize(678, m.abs_height - 20)
    root.tk.call('wm', 'iconphoto', '.', PhotoImage(file='icon.png'))

    m.enu = Menu(root)
    root.config(menu=m.enu)
    m.enu.add_command(label='Настройки', command=Settings)
    menu_2 = Menu(m.enu, tearoff=0)
    menu_2.add_command(label='Очистить папку Temp', command=CleanTemp)
    menu_2.add_command(label='Сообщение от автора', command=AuthorList)
    menu_2.add_command(label='Курсы валют', command=valute)
    menu_2.add_command(label='Словарь', command=english_dict)
    menu_2.add_command(label='QR-код', command=makeQR)
    menu_2.add_command(label='Часы', command=Clock)
    menu_3 = Menu(m.enu, tearoff=0)
    menu_3.add_command(label='Быки и коровы', command=bulls_and_cows)
    m.enu.add_cascade(label='Дополнительно', menu=menu_2)
    m.enu.add_cascade(label='Игры', menu=menu_3)
    m.enu.add_command(label='О программе', command=about_ms)

    root.bind('<Double-Escape>', main_exit)
    root.bind('<F1>', about_ms)

    MIHA_SOFT_LOGOTYPE = None

    if root.winfo_screenheight() > 770:
        MIHA_SOFT_LOGOTYPE = Label(window, text='Ⓜ', font=('Arial Bold', 265), fg='red')
        MIHA_SOFT_LOGOTYPE.place(x=160, y=0)
        ms_frame = Label(window, width=90, height=25)
        ms_frame.place(x=20, y=380)
    else:
        ms_frame = Label(window, width=90, height=25)
        ms_frame.place(x=20, y=20)

    ms_ground = Label(ms_frame, width=90, height=25, bg='#e0b6b6')
    ms_ground.place(x=0, y=0)

    ms_yao_button = Button(ms_frame, text='YourAge', font=('Arial Bold', 13), width=25, height=2, bg='#0039A6',
                           fg='white',
                           command=home_to_yao)
    ms_yao_button.place(x=20, y=250)
    blackout(ms_yao_button)

    ms_mso_button = Button(ms_frame, text='MiddleScore', font=('Arial Bold', 13), width=25, height=2, bg='#FF0000',
                           fg='white', command=home_to_mso)
    ms_mso_button.place(x=380, y=250)
    blackout(ms_mso_button)

    ms_sml_button = Button(ms_frame, text='The SML - IDE & Interpreter', font=('Arial Bold', 13), width=25, height=2,
                           bg='#D52B1E',
                           fg='white', command=home_to_sml)
    ms_sml_button.place(x=20, y=310)
    blackout(ms_sml_button)

    ms_tns_button = Button(ms_frame, text='NumberSystems', font=('Arial Bold', 13), width=25, height=2, bg='#ffdf00',
                           command=home_to_ns)
    ms_tns_button.place(x=380, y=310)
    blackout(ms_tns_button)

    ms_cz_button = Button(ms_frame, text='CrossZero', font=('Arial Bold', 13), width=25, height=2, bg='#FFFFFF',
                          command=home_to_cz)
    ms_cz_button.place(x=20, y=190)
    blackout(ms_cz_button)

    ms_mn_button = Button(ms_frame, text='MihNote', font=('Arial Bold', 13), width=10, height=2, bg='#a9e866',
                          command=home_to_mn)
    ms_mn_button.place(x=267, y=70)
    blackout(ms_mn_button)

    ms_wm_button = Button(ms_frame, text='WindowManager', font=('Arial Bold', 13), width=25, height=2, bg='#93e6a1',
                          command=home_to_wm)
    ms_wm_button.place(x=20, y=130)
    blackout(ms_wm_button)

    ms_am_button = Button(ms_frame, text='AccountManager', font=('Arial Bold', 13), width=25, height=2, bg='#93e6a1',
                          command=home_to_hw)
    ms_am_button.place(x=380, y=130)
    blackout(ms_am_button)

    ms_yw_button = Button(ms_frame, text='YourWarnings', font=('Arial Bold', 13), width=25, height=2, bg='#9ae3de',
                          command=home_to_yw)
    ms_yw_button.place(x=20, y=70)
    blackout(ms_yw_button)

    ms_sh_button = Button(ms_frame, text='Shmalyalka', font=('Arial Bold', 13), width=25, height=2, bg='#9ae3de',
                          command=home_to_sh)
    ms_sh_button.place(x=380, y=70)
    blackout(ms_sh_button)

    ms_p_button = Button(ms_frame, text='Paint', font=('Arial Bold', 13), width=10, height=2, bg='#a9e866',
                         command=home_to_p)
    ms_p_button.place(x=267, y=190)
    blackout(ms_p_button)

    ms_s_button = Button(ms_frame, text='Saper', font=('Arial Bold', 13), width=10, height=2, bg='#d67ab4',
                         command=home_to_s)
    ms_s_button.place(x=267, y=130)
    blackout(ms_s_button)

    ms_tp_button = Button(ms_frame, text='TurtlePaint', font=('Arial Bold', 13), width=10, height=2, bg='#9ae3de',
                          command=home_to_tp)
    ms_tp_button.place(x=267, y=250)
    blackout(ms_tp_button)

    ms_ht_button = Button(ms_frame, text='HyperText', font=('Arial Bold', 13), width=10, height=2, bg='white',
                          command=home_to_ht)
    ms_ht_button.place(x=267, y=310)
    blackout(ms_ht_button)

    ms_ws_button = Button(ms_frame, text='WaterMarks', font=('Arial Bold', 13), width=25, height=2, bg='white',
                          command=home_to_ws)
    ms_ws_button.place(x=380, y=190)
    blackout(ms_ws_button)

    ms_mr_button = Button(ms_frame, text='Morse', font=('Arial Bold', 13), width=10, height=2, bg='#93e6a1',
                          command=home_to_mr)
    ms_mr_button.place(x=267, y=10)
    blackout(ms_mr_button)

    # ms_pc_button = Button(ms_frame, text='PythonCompiler', font=('Arial Bold', 13), width=25, height=2, bg='#93e6a1',
    #                       command=home_to_pc)
    # ms_pc_button.place(x=380, y=10)
    # blackout(ms_pc_button)

    ms_yw_button.bind('<Button-3>', about_yourwarnings)
    ms_am_button.bind('<Button-3>', about_accountmanager)
    ms_wm_button.bind('<Button-3>', about_windowmanager)
    ms_mn_button.bind('<Button-3>', about_mihnote)
    ms_cz_button.bind('<Button-3>', about_crosszero)
    ms_p_button.bind('<Button-3>', about_paint)
    ms_s_button.bind('<Button-3>', about_saper)
    ms_tp_button.bind('<Button-3>', about_turtlepaint)
    ms_yao_button.bind('<Button-3>', about_yourage)
    ms_mso_button.bind('<Button-3>', about_middlescore)
    ms_ht_button.bind('<Button-3>', about_hypertext)
    ms_ws_button.bind('<Button-3>', about_watermarks)
    ms_sh_button.bind('<Button-3>', about_shmalyalka)
    ms_sml_button.bind('<Button-3>', about_sml)
    ms_tns_button.bind('<Button-3>', about_numbersystems)

    root.bind('<Control-KeyPress-m>', on_M)


def start():
    text_1 = '''
    Вас приветствуют разработчики MihaSoft! Для корректного продолжения работы
    программы необходимо разрешение на создание системных папок на диске C:
    '''

    text_2 = '''
    На диске C: будет создана папка MihaSoft Files, в которой будут 
    размещаться новые папки и файлы, создаваемые в процессе работы программы
    '''

    def sss_exit():
        root.quit()

    def sss_welcome():
        os.mkdir('MihaSoft Files')
        well_label.destroy()
        well_button.destroy()
        bye_button.destroy()
        window.configure(width=700, height=m.abs_height)
        home()
        center_window(root, 678, m.abs_height)

    if not os.path.exists('MihaSoft Files'):
        center_window(root, 500, 100)
        window.configure(width=500, height=100)
        root.title('Добро пожаловать!')
        root.minsize(500, 100)

        well_label = Label(window, text=text_1)
        well_label.place(x=5, y=5)

        well_button = Button(window, text='РАЗРЕШИТЬ', font=('Times New Roman', 10), width=13, command=sss_welcome)
        well_button.place(x=230, y=60)
        ToolTip(well_button, text_2)

        bye_button = Button(window, text='ОТМЕНА', font=('Times New Roman', 10), width=13, command=sss_exit)
        bye_button.place(x=350, y=60)

    else:
        def do_it():
            if os.path.exists('MihaSoft Files/AnimationFlagFile.miha') and root.winfo_screenheight() >= 730:
                LoadingLine()
            if os.path.exists('MihaSoft Files/SoundFlagFile.miha'):
                Music()

            home()
            HolidayWarningsDo()
            YourWarningsDo()
            check_update()

        if os.path.exists('MihaSoft Files/AnimationFlagFile.miha') and root.winfo_screenheight() >= 770:
            root.after(4000, do_it)
        else:
            do_it()


VERSION = '15.0'

if __name__ == '__main__':
    m = Main()
    root = Tk()

    if root.winfo_screenheight() < 820:
        m.abs_height = 390
    else:
        m.abs_height = 790

    if os.path.exists('MihaSoft Files') and os.path.exists('MihaSoft Files/AnimationFlagFile.miha'):
        root.attributes('-topmost', 'true')


        def hello_end():
            root.overrideredirect(False)
            root.configure(bg=root_c)
            m_img_label.destroy()


        root.overrideredirect(True)
        root_c = root['background']
        root.configure(bg='red')
        center_window(root, 583, 404)
        m_img_label = Label(root)
        m_img_obj = Image.open('image-m.png')
        m_img_label.image = ImageTk.PhotoImage(m_img_obj)
        m_img_label['image'] = m_img_label.image
        m_img_label.pack()
        root.after(4000, hello_end)

    window = Frame(root, width=700, height=m.abs_height)
    window.pack(expand=1)
    start()
    root.mainloop()
