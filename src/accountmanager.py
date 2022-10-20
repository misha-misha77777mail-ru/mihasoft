from pyperclip import copy
from tkinter import messagebox, ttk
from tkinter.filedialog import asksaveasfilename
from random import choice

from src.functions import *
from src.init import m, root
from src.homex import *


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
        homes()
        m.window.configure(width=788, height=m.abs_height)
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
            save(f'C:/MihaSoft Files/AM Files/{am_input_1.get()}', [am_input_1.get(), am_input_2.get(),
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
                am_list = load(f'C:/MihaSoft Files/AM Files/{am_open_combobox.get()}')
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
            am_open_combobox = ttk.Combobox(am.open_window, values=os.listdir('C:/MihaSoft Files/AM Files'),
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
                os.remove('C:/MihaSoft Files/AM Files/' + am_delete_path)
                am.delete_window.destroy()

            am.delete_window = Toplevel()
            center_window(am.delete_window, 300, 100)
            am.delete_window.resizable(False, False)
            am.delete_window.title('Удалить')

            am_delete_label = Label(am.delete_window, text='Выберите файл...')
            am_delete_label.place(x=5, y=5)

            # Список существующих файлов
            am_delete_combobox = ttk.Combobox(am.delete_window, values=os.listdir('C:/MihaSoft Files/AM Files'),
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
            with open('C:/MihaSoft Files/am-default.miha', 'w') as f:
                f.write(default_name)
                messagebox.showinfo('OK', 'Файл по умолчанию назначен.')

    def add_to_file():
        if am_input_1.get() and am_input_2.get() and am_input_3.get():
            if open('C:/MihaSoft Files/am-default.miha').read():
                try:
                    with open(open('C:/MihaSoft Files/am-default.miha').read(), 'r') as f:
                        am_data = f.read()
                    with open(open('C:/MihaSoft Files/am-default.miha').read(), 'w') as f:
                        f.write(am_data + f'''\n\nСервис: {am_input_1.get()}\nЛогин: {am_input_2.get()}
Пароль: {am_input_3.get()}''')
                    messagebox.showinfo('OK', 'Запись успешно добавлена.')
                except FileNotFoundError:
                    messagebox.showwarning('INFO', 'Файл по умолчанию не найден!')
            else:
                default_file()
        else:
            messagebox.showwarning('INFO', 'Заполните поля перед сохранением!')

    if not os.path.exists('C:/MihaSoft Files/AM Files'):
        os.mkdir('C:/MihaSoft Files/AM Files')
    if not os.path.exists('C:/MihaSoft Files/am-default.miha'):
        f_o = open('C:/MihaSoft Files/am-default.miha', 'w')
        f_o.close()

    center_window(root, 540, 360)
    m.window.configure(width=540, height=360)
    root.title('AccountManager 2.0')
    root.minsize(540, 360)

    am_title = Label(m.window, text='AccountManager 2.0', font=('Times New Roman', 20), fg='red')
    am_title.place(x=50, y=5)

    am_label_1 = Label(m.window, text='Сервис:')
    am_label_1.place(x=30, y=70)

    am_input_1 = Entry(m.window, width=50)
    am_input_1.place(x=90, y=72)

    am_button_1 = Button(m.window, text='Копировать', bg='#b8b8b8', command=copy_service)
    am_button_1.place(x=420, y=68)

    am_label_2 = Label(m.window, text='Логин:')
    am_label_2.place(x=30, y=120)

    am_input_2 = Entry(m.window, width=50)
    am_input_2.place(x=90, y=122)

    am_button_2 = Button(m.window, text='Копировать', bg='#b8b8b8', command=copy_login)
    am_button_2.place(x=420, y=118)

    am_label_3 = Label(m.window, text='Пароль:')
    am_label_3.place(x=30, y=170)

    am_input_3 = Entry(m.window, width=50)
    am_input_3.place(x=90, y=172)

    am_button_3 = Button(m.window, text='Копировать', bg='#b8b8b8', command=copy_password)
    am_button_3.place(x=420, y=168)

    am_pass_but = Button(m.window, text='Сгенерировать пароль', bg='#e0d09f', width=20, command=password)
    am_pass_but.place(x=30, y=230)
    ToolTip(am_pass_but, 'Сгенерировать пароль и вставить его в соответствующую строку')

    am_save_db_but = Button(m.window, text='Сохранить в базу', bg='#b6f2d3', width=20, command=am_save_db)
    am_save_db_but.place(x=190, y=230)
    ToolTip(am_save_db_but, 'Сохранить данные в базе MihaSoft')

    am_open_but = Button(m.window, text='Открыть запись', bg='#abeaed', width=20, command=am_open)
    am_open_but.place(x=30, y=270)
    ToolTip(am_open_but, 'Подставить данные из записи в базе MIhaSoft в соответствующие строки')

    am_del_file_but = Button(m.window, text='Удалить запись', bg='#e69b93', width=140, command=am_delete, compound=LEFT)
    img_obj = Image.open('images/м.png')
    am_del_file_but.image = ImageTk.PhotoImage(img_obj)
    am_del_file_but['image'] = am_del_file_but.image
    am_del_file_but.place(x=350, y=230)
    ToolTip(am_del_file_but, 'Удалить запись из базы MihaSoft')

    am_clean_but = Button(m.window, text='Очистить', bg='#faeaaf', width=20, command=am_clean)
    am_clean_but.place(x=350, y=270)
    ToolTip(am_clean_but, 'Очистить все строки')

    am_ch_file_but = Button(m.window, text='Назначить файл', bg='#f4d7fc', width=20, command=default_file)
    am_ch_file_but.place(x=190, y=270)
    ToolTip(am_ch_file_but, 'Выбрать внешний файл для сохранения данных')

    am_add_but = Button(m.window, text='Добавить к файлу', bg='#d8d7fc', width=20, command=add_to_file)
    am_add_but.place(x=190, y=310)
    ToolTip(am_add_but, 'Добавить к выбранному файлу текущие данные')

    am_off = Button(m.window, text='⌂', font=('Arial Bold', 15), width=2, height=1, bg='black', fg='white',
                    command=am_to_home)
    am_off.place(x=0, y=5)
    ToolTip(am_off, 'На главную...')
