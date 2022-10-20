from src.also_apps import *


def hom():
    def home_to_yao():
        from src.yourage import YourAge
        home_destroying()
        YourAge()

    def home_to_mso():
        from src.middlescore import MiddleScore
        home_destroying()
        MiddleScore()

    def home_to_sml():
        from src.sml import SML
        home_destroying()
        SML()

    def home_to_ns():
        from src.numbersystems import NumberSystems
        home_destroying()
        NumberSystems()

    def home_to_cz():
        from src.crosszero import CrossZero
        home_destroying()
        CrossZero()

    def home_to_mn():
        from src.mihnote import MihNote
        home_destroying()
        MihNote()

    def home_to_wm():
        from src.windowmanager import WindowManager
        home_destroying()
        WindowManager()

    def home_to_hw():
        from src.accountmanager import AccountManager
        home_destroying()
        AccountManager()

    def home_to_yw():
        from src.yourwarnings import YourWarnings
        home_destroying()
        YourWarnings()

    def home_to_sh():
        from src.shmalyalka import Shmalyalka
        home_destroying()
        Shmalyalka()

    def home_to_p():
        from src.paint import Paint
        home_destroying()
        Paint()

    def home_to_s():
        from src.saper import Saper
        home_destroying()
        Saper()

    def home_to_tp():
        from src.turtlepaint import TurtlePaint
        home_destroying()
        TurtlePaint()

    def home_to_ws():
        from src.watermarks import WaterMarks
        home_destroying()
        WaterMarks()

    def home_to_ht():
        from src.hypertext import HyperText
        home_destroying()
        HyperText()

    def home_to_mr():
        from src.morse import Morse
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

    root.title('MihaSoft ' + VERSION)
    center_window(root, 788, m.abs_height)
    root.minsize(788, m.abs_height - 20)
    root.tk.call('wm', 'iconphoto', '.', PhotoImage(file='images/icon.png'))

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
        MIHA_SOFT_LOGOTYPE = Label(m.window, text='Ⓜ', font=('Arial Bold', 265), fg='red')
        MIHA_SOFT_LOGOTYPE.place(x=217, y=0)
        ms_frame = Label(m.window, width=106, height=18)
        ms_frame.place(x=20, y=380)
    else:
        ms_frame = Label(m.window, width=106, height=18)
        ms_frame.place(x=20, y=20)

    ms_ground = Label(ms_frame, width=106, height=18, bg='#e0b6b6')
    ms_ground.place(x=0, y=0)

    ms_yao_button = Button(ms_frame, text='YourAge', font=('Arial Bold', 13), width=10, height=2, bg='#93e6a1',
                           command=home_to_yao)
    ms_yao_button.place(x=380, y=20)
    blackout(ms_yao_button)

    ms_mso_button = Button(ms_frame, text='MiddleScore', font=('Arial Bold', 13), width=25, height=2, bg='#FF0000',
                           fg='white', command=home_to_mso)
    ms_mso_button.place(x=492, y=140)
    blackout(ms_mso_button)

    ms_sml_button = Button(ms_frame, text='The SML - IDE & Interpreter', font=('Arial Bold', 13), width=25, height=2,
                           bg='#D52B1E',
                           fg='white', command=home_to_sml)
    ms_sml_button.place(x=20, y=200)
    blackout(ms_sml_button)

    ms_tns_button = Button(ms_frame, text='NumberSystems', font=('Arial Bold', 13), width=25, height=2, bg='#ffdf00',
                           command=home_to_ns)
    ms_tns_button.place(x=492, y=200)
    blackout(ms_tns_button)

    ms_cz_button = Button(ms_frame, text='CrossZero', font=('Arial Bold', 13), width=10, height=2, bg='#d67ab4',
                          command=home_to_cz)
    ms_cz_button.place(x=380, y=80)
    blackout(ms_cz_button)

    ms_mn_button = Button(ms_frame, text='MihNote', font=('Arial Bold', 13), width=10, height=2, bg='#a9e866',
                          command=home_to_mn)
    ms_mn_button.place(x=380, y=140)
    blackout(ms_mn_button)

    ms_wm_button = Button(ms_frame, text='WindowManager', font=('Arial Bold', 13), width=25, height=2, bg='#0039A6',
                          fg='white', command=home_to_wm)
    ms_wm_button.place(x=20, y=140)
    blackout(ms_wm_button)

    ms_am_button = Button(ms_frame, text='AccountManager', font=('Arial Bold', 13), width=25, height=2, bg='#9ae3de',
                          command=home_to_hw)
    ms_am_button.place(x=492, y=20)
    blackout(ms_am_button)

    ms_yw_button = Button(ms_frame, text='YourWarnings', font=('Arial Bold', 13), width=25, height=2, bg='white',
                          command=home_to_yw)
    ms_yw_button.place(x=20, y=80)
    blackout(ms_yw_button)

    ms_sh_button = Button(ms_frame, text='Shmalyalka', font=('Arial Bold', 13), width=25, height=2, bg='#9ae3de',
                          command=home_to_sh)
    ms_sh_button.place(x=20, y=20)
    blackout(ms_sh_button)

    ms_p_button = Button(ms_frame, text='Paint', font=('Arial Bold', 13), width=10, height=2, bg='#a9e866',
                         command=home_to_p)
    ms_p_button.place(x=267, y=80)
    blackout(ms_p_button)

    ms_s_button = Button(ms_frame, text='Saper', font=('Arial Bold', 13), width=10, height=2, bg='#e0a7fc',
                         command=home_to_s)
    ms_s_button.place(x=267, y=20)
    blackout(ms_s_button)

    ms_tp_button = Button(ms_frame, text='TurtlePaint', font=('Arial Bold', 13), width=10, height=2, bg='#d67ab4',
                          command=home_to_tp)
    ms_tp_button.place(x=267, y=140)
    blackout(ms_tp_button)

    ms_ht_button = Button(ms_frame, text='HyperText', font=('Arial Bold', 13), width=10, height=2, bg='#93e6a1',
                          command=home_to_ht)
    ms_ht_button.place(x=267, y=200)
    blackout(ms_ht_button)

    ms_ws_button = Button(ms_frame, text='WaterMarks', font=('Arial Bold', 13), width=25, height=2, bg='white',
                          command=home_to_ws)
    ms_ws_button.place(x=492, y=80)
    blackout(ms_ws_button)

    ms_mr_button = Button(ms_frame, text='Morse', font=('Arial Bold', 13), width=10, height=2, bg='#e0a7fc',
                          command=home_to_mr)
    ms_mr_button.place(x=380, y=200)
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
    # ms_tp_button.bind('<Button-3>', about_turtlepaint)
    ms_yao_button.bind('<Button-3>', about_yourage)
    ms_mso_button.bind('<Button-3>', about_middlescore)
    ms_ht_button.bind('<Button-3>', about_hypertext)
    ms_ws_button.bind('<Button-3>', about_watermarks)
    ms_sh_button.bind('<Button-3>', about_shmalyalka)
    ms_sml_button.bind('<Button-3>', about_sml)
    ms_tns_button.bind('<Button-3>', about_numbersystems)

    root.bind('<Control-KeyPress-m>', on_M)
