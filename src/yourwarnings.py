from tkinter import messagebox, ttk
from numpy import save

from src.functions import *
from src.init import m, root
from src.homex import *


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
        homes()
        m.window.configure(width=788, height=m.abs_height)
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
                save('C:/MihaSoft Files/YW Files/' + str(yw_day_input.get()) + '.' + str(yw_month_input.get()),
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
                yw_message = load('C:/MihaSoft Files/YW Files/' + str(yw_preview_combobox.get()))
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
            yw_preview_combobox = ttk.Combobox(yw.preview_ask_window, values=os.listdir('C:/MihaSoft Files/YW Files'),
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
                os.remove('C:/MihaSoft Files/YW Files/' + str(yw_delete_combobox.get()))
                yw.delete_window.destroy()

            yw.delete_window = Toplevel()
            center_window(yw.delete_window, 300, 100)
            yw.delete_window.resizable(False, False)
            yw.delete_window.title('Удаление')

            yw_delete_label = Label(yw.delete_window, text='Выберите запись...')
            yw_delete_label.place(x=5, y=5)

            # Список существующих уведомлений
            yw_delete_combobox = ttk.Combobox(yw.delete_window, values=os.listdir('C:/MihaSoft Files/YW Files'),
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

    if not os.path.exists('C:/MihaSoft Files/YW Files'):
        os.mkdir('C:/MihaSoft Files/YW Files')

    center_window(root, 400, 400)
    m.window.configure(width=400, height=400)
    root.title('YourWarnings 1.0')
    root.minsize(400, 400)

    yw_title = Label(m.window, text='YourWarnings 1.0', font=('Times New Roman', 20), fg='red')
    yw_title.place(x=50, y=5)

    yw_label_1 = Label(m.window, text='Введите дату:')
    yw_label_1.place(x=20, y=70)

    # Поле ввода даты вывода уведомления
    yw_day_input = Entry(m.window, width=20)
    yw_day_input.place(x=20, y=100)

    yw_label_2 = Label(m.window, text='Введите месяц:')
    yw_label_2.place(x=20, y=140)

    # Поле ввода месяца вывода уведомления
    yw_month_input = Entry(m.window, width=20)
    yw_month_input.place(x=20, y=170)

    yw_label_3 = Label(m.window, text='Введите текст сообщения:')
    yw_label_3.place(x=20, y=210)

    # Поле ввода текста уведомления
    yw_message_input = Text(m.window, width=30, height=5)
    yw_message_input.place(x=20, y=240)

    yw_create_button = Button(m.window, text='Добавить', bg='#aae09f', width=20, command=yw_create)
    yw_create_button.place(x=20, y=350)
    ToolTip(yw_create_button, 'Добавить новое уведомление...')

    yw_preview_button = Button(m.window, text='Просмотреть', bg='#e0d09f', width=15, command=yw_preview)
    yw_preview_button.place(x=200, y=70)
    ToolTip(yw_preview_button, 'Предварительный просмотр уведомления...')

    yw_delete_button = Button(m.window, text='Удалить', bg='#e09f9f', width=15, command=yw_delete)
    yw_delete_button.place(x=200, y=120)
    ToolTip(yw_delete_button, 'Удалить файл уведомления...')

    yw_off = Button(m.window, text='⌂', font=('Arial Bold', 15), width=2, height=1, bg='black', fg='white',
                    command=yw_to_home)
    yw_off.place(x=0, y=5)
    ToolTip(yw_off, 'На главную...')
