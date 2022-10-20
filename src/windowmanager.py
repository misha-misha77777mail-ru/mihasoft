from tkinter import messagebox, colorchooser, ttk
from tkinter.font import families
from numpy import save

from src.functions import *
from src.init import m, root
from src.homex import *


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
        homes()
        m.window.configure(width=788, height=m.abs_height)
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
                save('C:/MihaSoft Files/WM Files/' + str(wm_save_input.get()),
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
                wm_data_list = load('C:/MihaSoft Files/WM Files/' + wm_edit_path)
                wm.open_path = 'C:/MihaSoft Files/WM Files/' + wm_edit_path
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
            wm_edit_combobox = ttk.Combobox(wm.edit_window, values=os.listdir('C:/MihaSoft Files/WM Files'),
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
                wm_open_data_list = load('C:/MihaSoft Files/WM Files/' + wm_op_path)

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
            wm_open_combobox = ttk.Combobox(wm.open_window, values=os.listdir('C:/MihaSoft Files/WM Files'),
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
                os.remove('C:/MihaSoft Files/WM Files/' + wm_delete_path)
                wm.delete_window.destroy()

            wm.delete_window = Toplevel()
            center_window(wm.delete_window, 300, 100)
            wm.delete_window.resizable(False, False)
            wm.delete_window.title('Удалить')

            wm_delete_label = Label(wm.delete_window, text='Выберите файл...')
            wm_delete_label.place(x=5, y=5)

            # Список существующих файлов
            wm_delete_combobox = ttk.Combobox(wm.delete_window, values=os.listdir('C:/MihaSoft Files/WM Files'),
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
    if not os.path.exists('C:/MihaSoft Files/WM Files'):
        os.mkdir('C:/MihaSoft Files/WM Files')

    center_window(root, 600, 500)
    m.window.configure(width=600, height=500)
    root.title('WindowManager 1.3')
    root.minsize(600, 500)

    wm_title = Label(m.window, text='WindowManager 1.3', font=('Times New Roman', 20), fg='red')
    wm_title.place(x=50, y=5)

    wm_label_1 = Label(m.window, text='Размеры окна:', font=('Times New Roman', 12))
    wm_label_1.place(x=20, y=60)

    # Поле ввода ширины окна
    wm_width_input = Entry(m.window, width=12)
    wm_width_input.place(x=30, y=100)
    ToolTip(wm_width_input, 'Ширина')

    wm_label_2 = Label(m.window, text='X')
    wm_label_2.place(x=110, y=100)

    # Поле ввода высоты окна
    wm_height_input = Entry(m.window, width=12)
    wm_height_input.place(x=125, y=100)
    ToolTip(wm_height_input, 'Высота')

    wm_label_3 = Label(m.window, text='Расстояние от границ экрана:', font=('Times New Roman', 12))
    wm_label_3.place(x=20, y=130)

    wm_label_4 = Label(m.window, text='X =')
    wm_label_4.place(x=20, y=170)

    # Поле ввода расстояния от верхнего левого угла окна до левой границы экрана
    wm_x_cord_input = Entry(m.window, width=10)
    wm_x_cord_input.place(x=50, y=170)
    ToolTip(wm_x_cord_input, 'От левой границы')

    wm_label_5 = Label(m.window, text='Y =')
    wm_label_5.place(x=20, y=200)

    # Поле ввода расстояния от левого верхнего угла окна до верхней границы экрана
    wm_y_cord_input = Entry(m.window, width=10)
    wm_y_cord_input.place(x=50, y=200)
    ToolTip(wm_y_cord_input, 'От верхней границы')

    wm_label_6 = Label(m.window, text='Заголовок:', font=('Times New Roman', 12))
    wm_label_6.place(x=20, y=230)

    # Поле ввода заголовка окна
    wm_cust_title_input = Entry(m.window, width=28)
    wm_cust_title_input.place(x=30, y=260)

    wm_label_8 = Label(m.window, text='Введите текст:', font=('Times New Roman', 12))
    wm_label_8.place(x=300, y=80)

    # Поле ввода текста надписи, выводимой в окне
    wm_text_ground = Text(m.window, width=30, height=3)
    wm_text_ground.place(x=300, y=110)

    wm_label_9 = Label(m.window, text='Шрифт текста:', font=('Times New Roman', 12))
    wm_label_9.place(x=300, y=170)

    wm_font_ground = Entry(m.window, width=22, bg='white', state='readonly')
    wm_font_ground.place(x=300, y=200)

    wm_label_10 = Label(m.window, text='Размер шрифта:', font=('Times New Roman', 12))
    wm_label_10.place(x=300, y=230)

    # Поле ввода размера шрифта надписи
    wm_fsize_input = Entry(m.window, width=22)
    wm_fsize_input.place(x=300, y=260)

    wm_font_button = Button(m.window, text='Выбрать', bg='#93bbe6', command=wm_font_chooser)
    wm_font_button.place(x=460, y=200)

    wm_label_11 = Label(m.window, text='Цвет текста:', font=('Times New Roman', 12))
    wm_label_11.place(x=300, y=290)

    wm_choose_button = Button(m.window, text='Выбрать', bg='yellow', width=15, command=wm_choose_color)
    wm_choose_button.place(x=300, y=320)

    # Поле демонстрации выбранного цвета надписи
    wm_demo_ground = Label(m.window, text='', width=30, height=10)
    wm_demo_ground.place(x=30, y=320)

    wm_label_12 = Label(m.window, text='Расположение текста в окне:', font=('Times New Roman', 12))
    wm_label_12.place(x=300, y=350)

    wm_label_13 = Label(m.window, text='X =')
    wm_label_13.place(x=300, y=380)

    # Расстояние от надписи до левой границы окна
    wm_text_x_input = Entry(m.window, width=10)
    wm_text_x_input.place(x=330, y=380)
    ToolTip(wm_text_x_input, 'От левой границы')

    wm_label_14 = Label(m.window, text='Y =')
    wm_label_14.place(x=300, y=410)

    # Расстояние от надписи до верхней границы
    wm_text_y_input = Entry(m.window, width=10)
    wm_text_y_input.place(x=330, y=410)
    ToolTip(wm_text_y_input, 'От верхней границы')

    # Кнопка открытия окна по введённым параметрам
    wm_create_button = Button(m.window, text='СОЗДАТЬ', bg='green', fg='white', width=20, font=('Times New Roman', 16),
                              command=wm_open_custom_window)
    wm_create_button.place(x=300, y=440)
    ToolTip(wm_create_button, 'Создать окно по текущим параметрам...')

    wm_save_button = Button(m.window, text='Сохранить', bg='#f2ac6b', width=15, command=wm_save)
    wm_save_button.place(x=450, y=10)
    ToolTip(wm_save_button, 'Сохранить текущие параметры...')

    wm_open_button = Button(m.window, text='Открыть', bg='#f2dc6b', width=15, command=wm_open)
    wm_open_button.place(x=300, y=10)
    ToolTip(wm_open_button, 'Создать окно с сохранёнными параметрами...')

    wm_clean_button = Button(m.window, text='Обновить', bg='#93bbe6', width=15, command=wm_clean)
    wm_clean_button.place(x=450, y=45)
    ToolTip(wm_clean_button, 'Стереть текущие параметры...')

    wm_delete_button = Button(m.window, text='Удалить', bg='#e69b93', width=15, command=wm_delete)
    wm_delete_button.place(x=300, y=45)
    ToolTip(wm_delete_button, 'Удалить файл...')

    wm_edit_button = Button(m.window, text='Редактировать', bg='#90d4cb', width=15, command=wm_edit)
    wm_edit_button.place(x=150, y=45)
    ToolTip(wm_edit_button, 'Подставить параметры окна для редактирования...')

    wm_off = Button(m.window, text='⌂', font=('Arial Bold', 15), width=2, height=1, bg='black', fg='white',
                    command=wm_to_home)
    wm_off.place(x=0, y=5)
    ToolTip(wm_off, 'На главную...')
