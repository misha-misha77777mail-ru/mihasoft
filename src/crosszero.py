from tkinter import messagebox, ttk

from src.functions import *
from src.init import m, root
from src.homex import *


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
        homes()
        m.window.configure(width=788, height=m.abs_height)
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

            if os.path.exists('C:/MihaSoft Files/CzReportFlag.miha'):
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
        if os.path.exists('C:/MihaSoft Files/SoundFlagFile.miha'):
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
            if os.path.exists('C:/MihaSoft Files/SoundFlagFile.miha'):
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
            if os.path.exists('C:/MihaSoft Files/SoundFlagFile.miha'):
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
            if os.path.exists('C:/MihaSoft Files/SoundFlagFile.miha'):
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
        if os.path.exists('C:/MihaSoft Files/CzReportFlag.miha'):
            os.remove('C:/MihaSoft Files/CzReportFlag.miha')
            cz_save_button.configure(text='Сохранять\n отчёты')
            messagebox.showinfo('ОК', 'Функция сохранения отчётов отключена.')
        else:
            cz_flag_file = open('C:/MihaSoft Files/CzReportFlag.miha', 'w')
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
            'C:/MihaSoft Files/CZ Files/Log_' + str(cz_now.strftime('%d-%m-%Y %H.%M.%S')) + '.miha', 'w')
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
                    cz_report_file = open("C:/MihaSoft Files/CZ Files/" + cz_report_name, "r")
                    cz_report.configure(text=str(cz_report_file.readline()))
                    cz_report_file.close()

            cz.open_window = Toplevel()
            cz.open_window.title('Открыть отчёт')
            center_window(cz.open_window, 385, 140)
            cz.open_window.resizable(False, False)

            cz_open_label = Label(cz.open_window, text='Выберите запись...')
            cz_open_label.place(x=5, y=5)

            # Список существующих отчётов
            cz_open_combobox = ttk.Combobox(cz.open_window, values=os.listdir('C:/MihaSoft Files/CZ Files'),
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
                os.remove('C:/MihaSoft Files/CZ Files/' + str(cz_delete_combobox.get()))
                cz.delete_window.destroy()

            cz.delete_window = Toplevel()
            cz.delete_window.title('Удалить отчёт')
            center_window(cz.delete_window, 385, 140)
            cz.delete_window.resizable(False, False)

            cz_delete_label = Label(cz.delete_window, text='Выберите запись...')
            cz_delete_label.place(x=5, y=5)

            # Список существующих отчётов
            cz_delete_combobox = ttk.Combobox(cz.delete_window, values=os.listdir('C:/MihaSoft Files/CZ Files'),
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
    if not os.path.exists('C:/MihaSoft Files/CZ Files'):
        os.mkdir('C:/MihaSoft Files/CZ Files')

    center_window(root, 600, 440)
    m.window.configure(width=600, height=440)
    root.title('CrossZero 2.1')
    root.minsize(600, 440)

    cz_title = Label(m.window, text='CrossZero', font=('Times New Roman', 26), fg='red')
    cz_title.place(x=50, y=65)

    # Клетки
    cz_box_1 = Button(m.window, font=('Arial Black', 21), fg='red', bg='#b1d4e6', width=5, height=2,
                      command=cz_on_click_1)
    cz_box_1.place(x=250, y=80)

    cz_box_2 = Button(m.window, font=('Arial Black', 21), fg='red', bg='#b1d4e6', width=5, height=2,
                      command=cz_on_click_2)
    cz_box_2.place(x=360, y=80)

    cz_box_3 = Button(m.window, font=('Arial Black', 21), fg='red', bg='#b1d4e6', width=5, height=2,
                      command=cz_on_click_3)
    cz_box_3.place(x=470, y=80)

    cz_box_4 = Button(m.window, font=('Arial Black', 21), fg='red', bg='#b1d4e6', width=5, height=2,
                      command=cz_on_click_4)
    cz_box_4.place(x=250, y=195)

    cz_box_5 = Button(m.window, font=('Arial Black', 21), fg='red', bg='#b1d4e6', width=5, height=2,
                      command=cz_on_click_5)
    cz_box_5.place(x=360, y=195)

    cz_box_6 = Button(m.window, font=('Arial Black', 21), fg='red', bg='#b1d4e6', width=5, height=2,
                      command=cz_on_click_6)
    cz_box_6.place(x=470, y=195)

    cz_box_7 = Button(m.window, font=('Arial Black', 21), fg='red', bg='#b1d4e6', width=5, height=2,
                      command=cz_on_click_7)
    cz_box_7.place(x=250, y=310)

    cz_box_8 = Button(m.window, font=('Arial Black', 21), fg='red', bg='#b1d4e6', width=5, height=2,
                      command=cz_on_click_8)
    cz_box_8.place(x=360, y=310)

    cz_box_9 = Button(m.window, font=('Arial Black', 21), fg='red', bg='#b1d4e6', width=5, height=2,
                      command=cz_on_click_9)
    cz_box_9.place(x=470, y=310)

    cz_parametrs_button = Button(m.window, text='Параметры', font=('Times New Roman', 11), fg='blue', bg='#ddc0eb',
                                 command=cz_parametrs, width=10, height=2)
    cz_parametrs_button.place(x=50, y=10)
    ToolTip(cz_parametrs_button, 'Присвоить игрокам произвольные имена...')

    cz_new_game_button = Button(m.window, text='Новая игра', font=('Times New Roman', 11), fg='blue', bg='#c0ebcb',
                                command=cz_new_game, width=10, height=2)
    cz_new_game_button.place(x=160, y=10)
    ToolTip(cz_new_game_button, 'Обновить поле и начать новую игру...')

    if not os.path.exists('C:/MihaSoft Files/CzReportFlag.miha'):
        cz_text = 'Сохранять\n отчёты'
    else:
        cz_text = 'Не сохранять\n отчёты'

    cz_save_button = Button(m.window, text=cz_text, font=('Times New Roman', 11), fg='blue', bg='#e0cf92',
                            command=cz_save_report_set, width=10)
    cz_save_button.place(x=270, y=10)
    ToolTip(cz_save_button, 'Сохранить отчёт о последней игре...')

    cz_open_button = Button(m.window, text='Открыть\n отчёт', font=('Times New Roman', 11), fg='blue', bg='#87e6ad',
                            command=cz_open_report, width=10)
    cz_open_button.place(x=380, y=10)
    ToolTip(cz_open_button, 'Открыть отчёт в новом окне...')

    cz_delete_button = Button(m.window, text='Удалить\n отчёт', font=('Times New Roman', 11), fg='blue', bg='#eb9898',
                              command=cz_delete_report, width=10)
    cz_delete_button.place(x=490, y=10)
    ToolTip(cz_delete_button, 'Удалить существующий отчёт...')

    # Строки вывода информации о результате игры
    cz_game_condition_label = Label(m.window, font=('Times New Roman', 20), fg='blue')
    cz_game_condition_label.place(x=50, y=180)

    cz_name_of_winner_label = Label(m.window, font=('Times New Roman', 20), fg='blue')
    cz_name_of_winner_label.place(x=50, y=240)

    cz_numb_of_moves_label = Label(m.window, text='1', font=('Times New Roman', 20), fg='blue')
    cz_numb_of_moves_label.place(x=50, y=120)

    cz_info_label = Label(m.window, text='ХОД', font=('Times New Roman', 20), fg='blue')
    cz_info_label.place(x=90, y=120)

    cz_off = Button(m.window, text='⌂', font=('Arial Bold', 15), width=2, height=1, bg='black', fg='white',
                    command=cz_to_home)
    cz_off.place(x=0, y=5)
    ToolTip(cz_off, 'На главную...')
