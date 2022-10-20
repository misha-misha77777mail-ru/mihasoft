from time import strftime
from tkinter import messagebox, ttk
from pyperclip import copy
from shutil import rmtree
from random import randint
from qrcode import make
from qrcode.exceptions import DataOverflowError
from json import loads
from tkinter.filedialog import asksaveasfilename

from src.functions import *
from src.init import m


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


def Settings():
    def create_Settings():
        def click_an_but():
            if not os.path.exists('C:/MihaSoft Files/AnimationFlagFile.miha'):
                f = open('C:/MihaSoft Files/AnimationFlagFile.miha', 'w')
                f.close()
                animation_button.configure(text='ВЫКЛЮЧИТЬ', bg='red')
            else:
                os.remove('C:/MihaSoft Files/AnimationFlagFile.miha')
                animation_button.configure(text='ВКЛЮЧИТЬ', bg='green')

        def click_so_but():
            if not os.path.exists('C:/MihaSoft Files/SoundFlagFile.miha'):
                f = open('C:/MihaSoft Files/SoundFlagFile.miha', 'w')
                f.close()
                sound_button.configure(text='ВЫКЛЮЧИТЬ', bg='red')
            else:
                os.remove('C:/MihaSoft Files/SoundFlagFile.miha')
                sound_button.configure(text='ВКЛЮЧИТЬ', bg='green')

        def click_ti_but():
            if not os.path.exists('C:/MihaSoft Files/TintFlagFile.miha'):
                f = open('C:/MihaSoft Files/TintFlagFile.miha', 'w')
                f.close()
                third_button.configure(text='ВЫКЛЮЧИТЬ', bg='red')
            else:
                os.remove('C:/MihaSoft Files/TintFlagFile.miha')
                third_button.configure(text='ВКЛЮЧИТЬ', bg='green')

        def click_up_but():
            if not os.path.exists('C:/MihaSoft Files/UpdateFlag.miha'):
                fl = open('C:/MihaSoft Files/UpdateFlag.miha', 'w')
                fl.close()
                fourth_button.configure(text='ВКЛЮЧИТЬ', bg='green')
            else:
                os.remove('C:/MihaSoft Files/UpdateFlag.miha')
                fourth_button.configure(text='ВЫКЛЮЧИТЬ', bg='red')

        def click_am_but():
            if not os.path.exists('C:/MihaSoft Files/FlagHW.miha'):
                fl = open('C:/MihaSoft Files/FlagHW.miha', 'w')
                fl.close()
                fifth_button.configure(text='ВЫКЛЮЧИТЬ', bg='red')
            else:
                os.remove('C:/MihaSoft Files/FlagHW.miha')
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

        if not os.path.exists('C:/MihaSoft Files/AnimationFlagFile.miha'):
            animation_button.configure(text='ВКЛЮЧИТЬ', bg='green')
        else:
            animation_button.configure(text='ВЫКЛЮЧИТЬ', bg='red')

        second_label = Label(m.set_window, text='Звук:')
        second_label.place(x=10, y=90)

        sound_button = Button(m.set_window, font=('Arial Bold', 11), width=13, fg='white', command=click_so_but)
        sound_button.place(x=220, y=90)

        if not os.path.exists('C:/MihaSoft Files/SoundFlagFile.miha'):
            sound_button.configure(text='ВКЛЮЧИТЬ', bg='green')
        else:
            sound_button.configure(text='ВЫКЛЮЧИТЬ', bg='red')

        third_label = Label(m.set_window, text='Всплывающие подсказки\n к кнопкам:')
        third_label.place(x=10, y=165)

        third_button = Button(m.set_window, font=('Arial Bold', 11), width=13, fg='white', command=click_ti_but)
        third_button.place(x=220, y=170)

        if not os.path.exists('C:/MihaSoft Files/TintFlagFile.miha'):
            third_button.configure(text='ВКЛЮЧИТЬ', bg='green')
        else:
            third_button.configure(text='ВЫКЛЮЧИТЬ', bg='red')

        fourth_label = Label(m.set_window, text='Уведомления о выходе \nобновлений:')
        fourth_label.place(x=10, y=245)

        fourth_button = Button(m.set_window, font=('Arial Bold', 11), width=13, fg='white', command=click_up_but)
        fourth_button.place(x=220, y=250)

        if not os.path.exists('C:/MihaSoft Files/UpdateFlag.miha'):
            fourth_button.configure(text='ВЫКЛЮЧИТЬ', bg='red')
        else:
            fourth_button.configure(text='ВКЛЮЧИТЬ', bg='green')

        fifth_label = Label(m.set_window, text='HolidayWarnings:')
        fifth_label.place(x=10, y=325)

        fifth_button = Button(m.set_window, font=('Arial Bold', 11), width=13, fg='white', command=click_am_but)
        fifth_button.place(x=220, y=330)

        if not os.path.exists('C:/MihaSoft Files/FlagHW.miha'):
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
            for i in os.listdir('C:/Users/' + user_name + '/AppData/Local/Temp'):
                try:
                    d_size = os.path.getsize('C:/Users/' + user_name + '/AppData/Local/Temp/' + i)
                    if os.path.isdir('C:/Users/' + user_name + '/AppData/Local/Temp/' + i):
                        rmtree('C:/Users/' + user_name + '/AppData/Local/Temp/' + i)
                    else:
                        os.remove('C:/Users/' + user_name + '/AppData/Local/Temp/' + i)
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
                        if os.path.exists('C:/MihaSoft Files/BACFlag.miha'):
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
                        os.remove('C:/MihaSoft Files/BACFlag.miha')
                    except FileNotFoundError:
                        pass

                else:
                    fil = open('C:/MihaSoft Files/BACFlag.miha', 'w')
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
                code.save('C:/MihaSoft Files/Temp/temp.png')
                os.startfile('C:/MihaSoft Files/Temp/temp.png')
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
            with open('res/dict.json', encoding='utf8') as fi:
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

        info_string_2 = Label(m.info_window, text='Версия:   ' + VERSION)
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
