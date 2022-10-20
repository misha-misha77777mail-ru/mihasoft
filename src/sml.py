from tkinter import ttk

from src.functions import *
from src.init import m, root
from src.homex import *


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
        homes()
        m.window.configure(width=788, height=m.abs_height)
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
            center_window(sml.help_window, 800, 540)
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
            3 строка - если using input;: method=x;, где x это + (сложение), - (вычитание), * (умножение), / (деление), 
            // (целочисленное деление), % (деление с остатком)  
                       если using const;: const1=x;, где x - первое значение  
               _____________  
            4 строка - если using input;: окончание программы: end;  
                       если using const;: const2=y, где y - второе значение
               _____________  
            5 строка - если using const;: method=x;, где x это + (сложение), - (вычитание), * (умножение), / (деление), 
            // (целочисленное деление), % (деление с остатком)  
               _____________  
            6 строка - если using const;: окончание программы: end;

            ПРИМЕР:  
              program miha;
              using const;
              const1=5;
              const2=5;
              method=+;
              end;
            '''
            sml_help_field.insert(1.0, sml_help_text)
            sml_help_field.configure(state='disabled')

            sml_show_example_button = Button(sml.help_window, text='ВЫПОЛНИТЬ', bg='white', command=sml_Help_Example)
            sml_show_example_button.place(x=153, y=450)

            sml_exit_help_button = Button(sml.help_window, text='ЗАКРЫТЬ', bg='#e6bebe', command=sml_Help_Exit)
            sml_exit_help_button.place(x=700, y=450)

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
                                if sml_code_input.get('5.7') == '+':
                                    sml.flag = '+'
                                elif sml_code_input.get('5.7') == '-':
                                    sml.flag = '-'
                                elif sml_code_input.get('5.7') == '*':
                                    sml.flag = '*'
                                elif sml_code_input.get('5.7') == '/':
                                    sml.flag = '/'
                                elif sml_code_input.get('5.7') == '//':
                                    sml.flag = '//'
                                elif sml_code_input.get('5.7') == '%':
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
                            if sml_code_input.get('3.7') == '+':
                                sml.flag_1 = '+'
                            elif sml_code_input.get('3.7') == '-':
                                sml.flag_1 = '-'
                            elif sml_code_input.get('3.7') == '*':
                                sml.flag_1 = '*'
                            elif sml_code_input.get('3.7') == '/':
                                sml.flag_1 = '/'
                            elif sml_code_input.get('3.7') == '//':
                                sml.flag_1 = '//'
                            elif sml_code_input.get('3.7') == '%':
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
                sml_text_file = open('C:/MihaSoft Files/SML Files/' + str(sml_save_input.get()) + '.miha', "w")
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
                sml_text_file = open('C:/MihaSoft Files/SML Files/' + str(sml_open_combobox.get()), "r")
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
            sml_open_combobox = ttk.Combobox(sml.open_window, values=os.listdir('C:/MihaSoft Files/SML Files'),
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
                os.remove('C:/MihaSoft Files/SML Files/' + str(sml_delete_combobox.get()))
                sml.delete_window.destroy()

            sml.delete_window = Toplevel()
            sml.delete_window.title('Удалить')
            center_window(sml.delete_window, 350, 120)
            sml.delete_window.resizable(False, False)

            sml_delete_label = Label(sml.delete_window, text='Выберите файл...')
            sml_delete_label.place(x=5, y=5)

            # Список существующих файлов
            sml_delete_combobox = ttk.Combobox(sml.delete_window, values=os.listdir('C:/MihaSoft Files/SML Files'),
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
    if not os.path.exists('C:/MihaSoft Files/SML Files'):
        os.mkdir('C:/MihaSoft Files/SML Files')

    center_window(root, 830, 320)
    m.window.configure(width=830, height=320)
    root.title('The Simplest Mihail’s Language - IDE & Interpreter')
    root.minsize(830, 320)

    sml_title = Label(m.window, text='The Simplest Mihail’s Language - IDE & Interpreter', font=('Arial Bold', 24),
                      fg='red')
    sml_title.place(x=35, y=15)

    sml_help_button = Button(m.window, text='Справка', bg='red', fg="white", command=sml_Help)
    sml_help_button.place(x=15, y=70)

    # Поле ввода исходного кода
    sml_code_input = Text(m.window, width=75, height=12)
    sml_code_input.place(x=15, y=110)
    ToolTip(sml_code_input, 'Ваш код...')

    sml_begin_button = Button(m.window, text='ВЫПОЛНИТЬ', bg='green', fg='white', width=15, command=sml_Begin)
    sml_begin_button.place(x=90, y=70)
    ToolTip(sml_begin_button, 'Запустить программу...')

    sml_save_button = Button(m.window, text='СОХРАНИТЬ', bg='yellow', width=15, command=sml_Save)
    sml_save_button.place(x=220, y=70)
    ToolTip(sml_save_button, 'Сохранить введённый код...')

    sml_open_button = Button(m.window, text='ОТКРЫТЬ', bg='grey', width=15, command=sml_Open)
    sml_open_button.place(x=350, y=70)
    ToolTip(sml_open_button, 'Подставить сохранённый код...')

    sml_delete_button = Button(m.window, text='УДАЛИТЬ', bg='#eb9898', width=15, command=sml_Delete)
    sml_delete_button.place(x=480, y=70)
    ToolTip(sml_delete_button, 'Удалить сохранённый код...')

    # Область вывода сообщений об ошибках на соответствующих строках
    sml_error_1 = Label(m.window, fg='red')
    sml_error_1.place(x=640, y=110)

    sml_error_2 = Label(m.window, fg='red')
    sml_error_2.place(x=640, y=140)

    sml_error_3 = Label(m.window, fg='red')
    sml_error_3.place(x=640, y=170)

    sml_error_4 = Label(m.window, fg='red')
    sml_error_4.place(x=640, y=200)

    sml_error_5 = Label(m.window, fg='red')
    sml_error_5.place(x=640, y=230)

    sml_error_6 = Label(m.window, fg='red')
    sml_error_6.place(x=640, y=260)

    sml_off = Button(m.window, text='⌂', font=('Arial Bold', 15), width=2, height=1, bg='black', fg='white',
                     command=sml_to_home)
    sml_off.place(x=0, y=5)
    ToolTip(sml_off, 'На главную...')
