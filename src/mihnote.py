from tkinter import ttk
from functions import *

from src.init import m, root
from src.homex import *


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

        homes()
        m.window.configure(width=788, height=m.abs_height)
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
                        mn_text_file = open('C:/MihaSoft Files/MihNote Files/' + str(mn_save_input.get()) + '.miha',
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
            if os.listdir('C:/MihaSoft Files/MihNote Files') and mn.open_combobox.get():
                mn_file_name = str(mn.open_combobox.get())
                # Удаление виджетов открытия
                mn.open_combobox.destroy()
                mn.open_ok_button.destroy()
                mn.open_flag = False
                mn_open_text_file = open('C:/MihaSoft Files/MihNote Files/' + mn_file_name, 'r')
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
            mn.open_combobox = ttk.Combobox(m.window, values=os.listdir('C:/MihaSoft Files/MihNote Files'),
                                            font=('Arial Bold', 16), state='readonly')
            mn.open_combobox.place(x=20, y=60)

            mn.open_ok_button = Button(m.window, text='Открыть', font=('Arial Bold', 10), bg='#7bd491', width=14,
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
            if os.listdir('C:/MihaSoft Files/MihNote Files') and mn.delete_combobox.get():
                def mn_delete_ok():
                    mn_delete_file_name = str(mn.delete_combobox.get())
                    # Удаление виджетов удаления
                    mn.delete_combobox.destroy()
                    mn.delete_ask_button.destroy()
                    mn.del_flag = False
                    os.remove('C:/MihaSoft Files/MihNote Files/' + mn_delete_file_name)
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

            mn.delete_combobox = ttk.Combobox(m.window, values=os.listdir('C:/MihaSoft Files/MihNote Files'),
                                              font=('Arial Bold', 16), state='readonly')
            mn.delete_combobox.place(x=20, y=60)

            mn.delete_ask_button = Button(m.window, text='Удалить', font=('Arial Bold', 10), fg="black", bg='#c97979',
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
            if os.listdir('C:/MihaSoft Files/MihNote Files') and mn.edit_combobox.get():

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
                        mn_edit_file = open('C:/MihaSoft Files/MihNote Files/' + mn_edit_file_name, 'w')
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
                    mn_edit_open_file = open('C:/MihaSoft Files/MihNote Files/' + mn_edit_file_name, 'r')
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
            mn.edit_combobox = ttk.Combobox(m.window, values=os.listdir('C:/MihaSoft Files/MihNote Files'),
                                            font=('Arial Bold', 16), state='readonly')
            mn.edit_combobox.place(x=20, y=60)

            mn.edit_ok_button = Button(m.window, text='Редактировать', font=('Arial Bold', 10), bg='#79a7c9', width=14,
                                       command=mn_edit_ok)
            mn.edit_ok_button.place(x=300, y=60)

    # Создание папки для заметок в случае отсутствия таковой
    if not os.path.exists('C:/MihaSoft Files/MihNote Files'):
        os.mkdir('C:/MihaSoft Files/MihNote Files')

    center_window(root, 810, 390)
    m.window.configure(width=810, height=390)
    root.title('MihNote 1.1')
    root.minsize(810, 390)

    mn_title = Label(m.window, text='MihNote 1.1', font=('Arial Bold', 16), fg='red')
    mn_title.place(x=80, y=10)

    mn_open_button = Button(m.window, text='Открыть', font=('Arial Bold', 12), bg='#e6aeae', width=13,
                            command=mn_open_note)
    mn_open_button.place(x=210, y=10)
    ToolTip(mn_open_button, 'Открыть файл...')

    mn_edit_button = Button(m.window, text='Редактировать', font=('Arial Bold', 12), bg='#aeb4e6', width=13,
                            command=mn_edit_note)
    mn_edit_button.place(x=350, y=10)
    ToolTip(mn_edit_button, 'Редактировать существующий файл...')

    mn_new_note_button = Button(m.window, text='Создать', font=('Arial Bold', 12), bg='#aee6c9', width=13,
                                command=mn_new_note)
    mn_new_note_button.place(x=490, y=10)
    ToolTip(mn_new_note_button, 'Создать новый файл...')

    mn_delete_button = Button(m.window, text='Удалить', font=('Arial Bold', 12), bg='#e6e2ae', width=13,
                              command=mn_delete_note)
    mn_delete_button.place(x=630, y=10)
    ToolTip(mn_delete_button, 'Удалить файл...')

    # Линия, ограждающая кнопок от области вывода заметок
    mn_line = Label(m.window,
                    text='_' * 154)
    mn_line.place(x=10, y=90)

    # Область вывода заметок
    mn_note_ground = Text(m.window, font=('Times New Roman', 14), width=80, height=12, state='disabled')
    mn_note_ground.place(x=35, y=120)

    mn_off = Button(m.window, text='⌂', font=('Arial Bold', 15), width=2, height=1, bg='black', fg="white",
                    command=mn_to_home)

    mn_off.place(x=0, y=5)
    ToolTip(mn_off, 'На главную...')
