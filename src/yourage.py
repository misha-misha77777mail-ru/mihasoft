import datetime
from tkinter import messagebox
from tkinter import ttk
from tkinter.ttk import Radiobutton
from main import root, m

from src.center import center_window
from src.classes import *
from src.homex import *


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
        homes()
        m.window.configure(width=788, height=m.abs_height)
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
                text_file = open('C:/MihaSoft Files/YAO Files/' + str(yao_save_name_input.get()), 'w')
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
                    yao_open_file = open('C:/MihaSoft Files/YAO Files/' + str(yao_open_combobox.get()), 'r')
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
            yao_open_combobox = ttk.Combobox(yao.open_window, values=os.listdir('C:/MihaSoft Files/YAO Files'),
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
                    os.remove('C:/MihaSoft Files/YAO Files/' + str(yao_del_combobox.get()))
                    yao.delete_window.destroy()

            yao.delete_window = Toplevel()
            yao.delete_window.geometry('300x150+70+70')
            center_window(yao.delete_window, 300, 150)
            yao.delete_window.resizable(False, False)
            yao.delete_window.title('Удаление записи')

            yao_del_label = Label(yao.delete_window, text='Выберите запись для удаления...')
            yao_del_label.place(x=5, y=5)

            # Выпадающий список имеющихся файлов
            yao_del_combobox = ttk.Combobox(yao.delete_window, values=os.listdir('C:/MihaSoft Files/YAO Files'),
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
    if not os.path.exists('C:/MihaSoft Files/YAO Files'):
        os.mkdir('C:/MihaSoft Files/YAO Files')

    yao_files_list = os.listdir('C:/MihaSoft Files/YAO Files')
    center_window(root, 620, 250)
    root.title('YourAge 3.0')
    m.window.configure(width=620, height=250)
    root.minsize(620, 250)

    yao_title = Label(m.window, text='YourAge 3.0', font=('Arial Bold', 16), fg='red')
    yao_title.place(x=40, y=20)

    yao_label_1 = Label(m.window, text='Дата рождения:', font=('Times New Roman', 12))
    yao_label_1.place(x=40, y=60)

    # Поле ввода исходного дня
    yao_day_input = Entry(m.window, width=4)
    yao_day_input.place(x=40, y=100)
    ToolTip(yao_day_input, 'День')

    yao_label_2 = Label(m.window, text='.', font=('Times New Roman', 12))
    yao_label_2.place(x=73, y=103)

    # Поле ввода исходного месяца
    yao_month_input = Entry(m.window, width=4)
    yao_month_input.place(x=90, y=100)
    ToolTip(yao_month_input, 'Месяц')

    yao_label_3 = Label(m.window, text='.', font=('Times New Roman', 12))
    yao_label_3.place(x=124, y=100)

    # Поле ввода исходного года
    yao_year_input = Entry(m.window, width=9)
    yao_year_input.place(x=140, y=100)
    ToolTip(yao_year_input, 'Год')

    yao_sysdate_button = Button(m.window, text='Подставить т. д.', width=13, height=1, bg='#eef5b3',
                                command=yao_Now_Date)
    yao_sysdate_button.place(x=250, y=20)
    ToolTip(yao_sysdate_button, 'Подставить системную дату...')

    yao_save_button = Button(m.window, text='Сохранить зап.', width=92, height=20, bg='#8ceb8a',
                             command=yao_Save, compound=LEFT)
    s_img_obj = Image.open('images/у.png')
    yao_save_button.image = ImageTk.PhotoImage(s_img_obj)
    yao_save_button['image'] = yao_save_button.image
    yao_save_button.place(x=490, y=120)
    ToolTip(yao_save_button, 'Сохранить данные о дате рождения...')

    yao_birthday_button = Button(m.window, text='Подставить д. р.', width=13, height=1, bg='#b3f5ec',
                                 command=yao_Open)
    yao_birthday_button.place(x=370, y=20)
    ToolTip(yao_birthday_button, 'Подставить сохранённую дату рождения...')

    yao_delete_button = Button(m.window, text='Удалить зап.', width=92, height=20, bg='#eb8a8a', fg='black',
                               command=yao_Delete, compound=LEFT)
    d_img_obj = Image.open('images/м.png')
    yao_delete_button.image = ImageTk.PhotoImage(d_img_obj)
    yao_delete_button['image'] = yao_delete_button.image
    yao_delete_button.place(x=490, y=70)
    ToolTip(yao_delete_button, 'Удалить запись о дате рождения...')

    yao_clean_button = Button(m.window, text='Очистить', width=13, height=1, bg='#ebd38a', command=yao_Clean)
    yao_clean_button.place(x=490, y=20)
    ToolTip(yao_clean_button, 'Очистить поля ввода...')

    yao_label_4 = Label(m.window, text='Текущая дата:', font=('Times New Roman', 12))
    yao_label_4.place(x=300, y=60)

    # Поле ввода текущего дня
    yao_now_day_input = Entry(m.window, width=4)
    yao_now_day_input.place(x=300, y=100)
    ToolTip(yao_now_day_input, 'День')

    yao_label_5 = Label(m.window, text='.', font=('Times New Roman', 12))
    yao_label_5.place(x=333, y=100)

    # Поле ввода текущего месяца
    yao_now_month_input = Entry(m.window, width=4)
    yao_now_month_input.place(x=350, y=100)
    ToolTip(yao_now_month_input, 'Месяц')

    yao_label_6 = Label(m.window, text='.', font=('Times New Roman', 12))
    yao_label_6.place(x=384, y=100)

    # Поле ввода текущего года
    yao_now_year_input = Entry(m.window, width=9)
    yao_now_year_input.place(x=400, y=100)
    ToolTip(yao_now_year_input, 'Год')

    # Получение выбранного способа вывода данных
    yao_choice_def = IntVar()

    # Кнопки выбора одного из двух способов вывода данных:
    yao_choice_radbut_1 = Radiobutton(m.window, text='Вывести возраст в годах, месяцах и днях', variable=yao_choice_def,
                                      value=1)
    yao_choice_radbut_1.place(x=40, y=150)

    yao_choice_radbut_2 = Radiobutton(m.window, text='Вывести возраст в днях', variable=yao_choice_def, value=2)
    yao_choice_radbut_2.place(x=300, y=150)

    yao_result_button = Button(m.window, text='РАССЧИТАТЬ', width=19, height=2, bg='black', fg='white',
                               command=yao_begin)
    yao_result_button.place(x=40, y=190)

    yao_label_7 = Label(m.window, text='Ваш возраст: ', font=('Times New Roman', 16))
    yao_label_7.place(x=220, y=190)

    yao_label_8 = Label(m.window, font=('Times New Roman', 16))
    yao_label_8.place(x=350, y=190)

    yao_off = Button(m.window, text='⌂', font=('Arial Bold', 15), width=2, height=1, bg='black', fg='white',
                     command=yao_to_home)
    yao_off.place(x=0, y=5)
    ToolTip(yao_off, 'На главную...')
