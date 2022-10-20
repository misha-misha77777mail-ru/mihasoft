import os
from tkinter import *
from PIL import Image, ImageTk


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

    if os.path.exists('C:/MihaSoft Files/TintFlagFile.miha'):
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
        self.window = None
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
