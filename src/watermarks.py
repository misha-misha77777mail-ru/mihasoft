from tkinter.filedialog import askopenfilename, asksaveasfilename
from tkinter import messagebox, ttk, colorchooser
from PIL import ImageDraw, ImageFont, UnidentifiedImageError
from numpy import save

from src.functions import *
from src.init import m, root
from src.homex import *


def WaterMarks():
    def ws_destroy():
        try:
            ws.save_window.destroy()
        except AttributeError:
            pass

        try:
            ws.delete_window.destroy()
        except AttributeError:
            pass

        try:
            ws.edit_window.destroy()
        except AttributeError:
            pass

        try:
            ws.view_window.destroy()
        except AttributeError:
            pass

        ws_title.destroy()
        ws_search_button.destroy()
        ws_file_label.destroy()
        ws_color_button.destroy()
        ws_label_1.destroy()
        ws_text.destroy()
        ws_color_demo.destroy()
        ws_label_2.destroy()
        ws_label_3.destroy()
        ws_input_1.destroy()
        ws_label_6.destroy()
        ws_input_2.destroy()
        ws_choose_button.destroy()
        ws_label_4.destroy()
        ws_input_3.destroy()
        ws_label_5.destroy()
        ws_font_combobox.destroy()
        ws_preview_button.destroy()
        ws_save_button.destroy()
        ws_off.destroy()
        m.enu.delete('Проект')
        homes()
        m.window.configure(width=788, height=m.abs_height)
        center_window(root, 678, m.abs_height)

    def ws_open_file():
        ws.file = askopenfilename()
        if ws.file:
            ws_file_label.configure(state=NORMAL)
            ws_file_label.delete(1.0, END)
            ws_file_label.insert(1.0, ws.file)
            ws_file_label.configure(state=DISABLED)
        else:
            ws.file = None

    def ws_choose_color():
        ws_colorchoose_window = colorchooser.askcolor()
        ws.color = ws_colorchoose_window[0]
        if ws.color is not None:
            ws.color = (int(ws.color[0]), int(ws.color[1]), int(ws.color[2]))
            ws_color_demo.configure(bg=str(ws_colorchoose_window[1]))

    def ws_open_preview():
        try:
            if ws.file is not None and ws.color is not None and ws_text.get(1.0, END) and ws_input_1.get().isdigit() \
                    and ws_input_2.get().isdigit() and ws_input_3.get().isdigit() and ws_font_combobox.get():
                try:
                    photo = Image.open(ws.file)
                    drawing = ImageDraw.Draw(photo)
                    ws_font = ImageFont.truetype('fonts/' + ws_font_combobox.get(), int(ws_input_3.get()))
                    drawing.text((int(ws_input_1.get()), int(ws_input_2.get())), ws_text.get(1.0, END), fill=ws.color,
                                 font=ws_font)
                    photo.save('C:/MihaSoft Files/Temp/ws.png')
                    os.startfile('C:/MihaSoft Files/Temp/ws.png')

                except UnidentifiedImageError:
                    messagebox.showerror('Ошибка!', 'Выбранный файл не является изображением!')
            else:
                messagebox.showwarning('INFO', 'Введены некорректные данные!')
        except FileNotFoundError:
            messagebox.showerror('Ошибка!', 'Файл изображения перемещён или утрачен!')

    def ws_save():
        try:
            ws_file = asksaveasfilename(title='Сохранить файл', defaultextension='.png',
                                        filetypes=(('PNG file', '*.png'), ('All Files', '*.*')))
            if ws_file:
                if ws.file is not None and ws.color is not None and ws_text.get(1.0, END) \
                        and ws_input_1.get().isdigit() and ws_input_2.get().isdigit() and ws_input_3.get().isdigit() \
                        and ws_font_combobox.get():
                    try:
                        photo = Image.open(ws.file)
                        drawing = ImageDraw.Draw(photo)
                        ws_font = ImageFont.truetype('fonts/' + ws_font_combobox.get(), int(ws_input_3.get()))
                        drawing.text((int(ws_input_1.get()), int(ws_input_2.get())), ws_text.get(1.0, END),
                                     fill=ws.color,
                                     font=ws_font)
                        photo.save(ws_file)
                    except UnidentifiedImageError:
                        messagebox.showerror('Ошибка!', 'Выбранный файл не является изображением!')
                else:
                    messagebox.showwarning('INFO', 'Введены некорректные данные!')
        except FileNotFoundError:
            messagebox.showerror('Ошибка!', 'Файл изображения перемещён или утрачен!')

    def choose_place():
        def ws_create_view_window():
            def ws_ok_place(event):
                ws_input_1.delete(0, END)
                ws_input_2.delete(0, END)
                ws_input_1.insert(0, event.x)
                ws_input_2.insert(0, event.y)
                ws.view_window.destroy()

            if ws.file is not None:
                ws.view_window = Toplevel()
                ws.view_window.title('Укажите точку...')
                img_label = Label(ws.view_window, cursor='hand2')
                img_obj = Image.open(ws.file)
                im_width, im_height = img_obj.size
                img_label.image = ImageTk.PhotoImage(img_obj)
                img_label['image'] = img_label.image

                img_label.pack()
                center_window(ws.view_window, im_width, im_height)
                ws.view_window.resizable(False, False)
                ws.view_window.bind('<Button-1>', ws_ok_place)

            else:
                messagebox.showwarning('INFO', 'Выберите файл!')

        try:
            ws.view_window.resizable(False, False)

        except AttributeError:
            ws_create_view_window()

        except TclError:
            ws_create_view_window()

    def ws_save_project():
        """
        Функция сохранения параметров
        проекта в файл
        """

        def ws_save_changes():
            """
            Функция сохранения изменений в
            открытом для редактирования файла
            """
            save(ws.open_path,
                 [ws.file, ws.color, ws_text.get(1.0, END), ws_input_1.get(), ws_input_2.get(), ws_input_3.get(),
                  ws_font_combobox.get()])

            ws.flag = True
            ws.save_window.destroy()

        def ws_save_abort():
            """
            Отмена сохранения
            """
            ws.save_window.destroy()

        # Проверка значения переменной, отвечающей за состояние
        # приложения (создание нового файла или редактирование существующего)
        # и вызов соответствующего окна.

        # Проверка правильности заполнения полей с параметрами
        def ws_create_save_window():
            def ws_save_file():
                """
                Функция сохранения нового файла
                """
                save('C:/MihaSoft Files/WS Files/' + str(ws_save_input.get()),
                     [ws.file, ws.color, ws_text.get(1.0, END), ws_input_1.get(), ws_input_2.get(), ws_input_3.get(),
                      ws_font_combobox.get()])

                ws.save_window.destroy()

            if ws.file is not None and ws.color is not None and ws_text.get(1.0, END) and ws_input_1.get().isdigit() \
                    and ws_input_2.get().isdigit() and ws_input_3.get().isdigit() and ws_font_combobox.get():
                if not ws.flag:
                    ws.save_window = Toplevel()
                    center_window(ws.save_window, 300, 100)
                    ws.save_window.resizable(False, False)
                    ws.save_window.title('Сохранение')

                    ws_save_label = Label(ws.save_window, text='Сохранить изменения?')
                    ws_save_label.place(x=5, y=5)

                    ws_save_ok_button = Button(ws.save_window, text='ОК', width=10, bg='#93e6a8',
                                               command=ws_save_changes)
                    ws_save_ok_button.place(x=200, y=43)

                    ws_close_button = Button(ws.save_window, text='Отмена', bg='#b8b8b8', width=10,
                                             command=ws_save_abort)
                    ws_close_button.place(x=100, y=43)

                else:
                    ws.save_window = Toplevel()
                    center_window(ws.save_window, 300, 100)
                    ws.save_window.resizable(False, False)
                    ws.save_window.title('Сохранение')

                    ws_save_label = Label(ws.save_window, text='Введите название файла...')
                    ws_save_label.place(x=5, y=5)

                    # Поле ввода названия нового файла
                    ws_save_input = Entry(ws.save_window, width=25)
                    ws_save_input.place(x=10, y=45)

                    ws_save_ok_button = Button(ws.save_window, text='Сохранить', width=10, bg='#93e6a8',
                                               command=ws_save_file)
                    ws_save_ok_button.place(x=200, y=53)

                    ws_save_close_button = Button(ws.save_window, text='Отмена', bg='#b8b8b8', width=10,
                                                  command=ws_save_abort)
                    ws_save_close_button.place(x=200, y=13)
            else:
                messagebox.showwarning('INFO', 'Проверьте корректность введённых данных!')

        try:
            ws.save_window.resizable(False, False)

        except AttributeError:
            ws_create_save_window()

        except TclError:
            ws_create_save_window()

    def ws_clean():
        ws_file_label.configure(state=NORMAL)
        ws_file_label.delete(1.0, END)
        ws_file_label.configure(state=DISABLED)
        ws_text.delete(1.0, END)
        ws_input_1.delete(0, END)
        ws_input_2.delete(0, END)
        ws_input_3.delete(0, END)
        ws_font_combobox.delete(0, END)
        ws_color_demo.configure(bg='white')
        ws.flag = True

    def ws_edit():
        """
        Функция редактирования существующего файла
        (подстановка параметров из существующего файла
        в соответствующие поля
        """

        def ws_edit_abort():
            """
            Отмена редактирования
            """
            ws.edit_window.destroy()

        def ws_create_edit_window():
            def ws_edit_ok():
                """
                Функция вывода параметров в соответствующие поля
                из выбранного файла
                """
                ws_clean()
                ws_edit_path = str(ws_edit_combobox.get())
                ws_data_list = load('C:/MihaSoft Files/WS Files/' + ws_edit_path, allow_pickle=True)
                ws.open_path = 'C:/MihaSoft Files/WS Files/' + ws_edit_path
                ws.file = ws_data_list[0]
                ws.color = eval(str(ws_data_list[1]))
                ws_file_label.configure(state=NORMAL)
                ws_file_label.delete(1.0, END)
                ws_file_label.insert(1.0, ws.file)
                ws_file_label.configure(state=DISABLED)
                ws_color_demo.configure(bg='#%02x%02x%02x' % tuple(ws.color))
                ws_text.insert(1.0, ws_data_list[2])
                ws_input_1.insert(0, ws_data_list[3])
                ws_input_2.insert(0, ws_data_list[4])
                ws_input_3.insert(0, ws_data_list[5])
                ws_font_combobox.configure(state='normal')
                ws_font_combobox.insert(0, ws_data_list[6])
                ws_font_combobox.configure(state='readonly')
                ws.flag = False
                ws.edit_window.destroy()

            ws.edit_window = Toplevel()
            center_window(ws.edit_window, 300, 100)
            ws.edit_window.resizable(False, False)
            ws.edit_window.title('Открыть')

            ws_edit_label = Label(ws.edit_window, text='Выберите файл...')
            ws_edit_label.place(x=5, y=5)

            # Список существующих файлов
            ws_edit_combobox = ttk.Combobox(ws.edit_window, values=os.listdir('C:/MihaSoft Files/WS Files'),
                                            state='readonly')
            ws_edit_combobox.place(x=10, y=45)

            ws_edit_ok_button = Button(ws.edit_window, text='Открыть', width=13, bg='#93e6a8', command=ws_edit_ok)
            ws_edit_ok_button.place(x=180, y=53)

            ws_edit_close_button = Button(ws.edit_window, text='Отмена', bg='#b8b8b8', width=13, command=ws_edit_abort)
            ws_edit_close_button.place(x=180, y=13)

        try:
            ws.edit_window.resizable(False, False)

        except AttributeError:
            ws_create_edit_window()

        except TclError:
            ws_create_edit_window()

    def ws_delete():
        """
        Функция удаления сохранённых файлов
        """

        def ws_delete_abort():
            """
            Отмена удаления
            """
            ws.delete_window.destroy()

        def ws_create_del_window():
            def ws_delete_ok():
                """
                Удаление выбранного файла
                """
                os.remove('C:/MihaSoft Files/WS Files/' + str(ws_delete_combobox.get()))
                ws.delete_window.destroy()

            ws.delete_window = Toplevel()
            center_window(ws.delete_window, 300, 100)
            ws.delete_window.resizable(False, False)
            ws.delete_window.title('Удаление')

            ws_delete_label = Label(ws.delete_window, text='Выберите файл...')
            ws_delete_label.place(x=5, y=5)

            # Список существующих файлов
            ws_delete_combobox = ttk.Combobox(ws.delete_window, values=os.listdir('C:/MihaSoft Files/WS Files'),
                                              state='readonly')
            ws_delete_combobox.place(x=10, y=45)

            ws_delete_ok_button = Button(ws.delete_window, text='Удалить', width=10, bg='#e69b93', command=ws_delete_ok)
            ws_delete_ok_button.place(x=200, y=23)

            ws_delete_close_button = Button(ws.delete_window, text='Отмена', width=10, bg='#b8b8b8',
                                            command=ws_delete_abort)
            ws_delete_close_button.place(x=200, y=60)

        try:
            ws.delete_window.resizable(False, False)

        except AttributeError:
            ws_create_del_window()

        except TclError:
            ws_create_del_window()

    if not os.path.exists('C:/MihaSoft Files/WS Files'):
        os.mkdir('C:/MihaSoft Files/WS Files')

    center_window(root, 430, 400)
    m.window.configure(width=430, height=400)
    root.title('WaterMarks 2.0')
    root.minsize(430, 400)

    ws = WaterMarksGlobals()
    menu = Menu(m.enu, tearoff=0)
    menu.add_command(label='Сохранить', command=ws_save_project)
    menu.add_command(label='Открыть', command=ws_edit)
    menu.add_command(label='Удалить', command=ws_delete)
    menu.add_command(label='Новый проект', command=ws_clean)
    m.enu.add_cascade(label='Проект', menu=menu)

    ws_title = Label(m.window, text='WaterMarks 2.0', font=('Arial Bold', 16), fg='red')
    ws_title.place(x=50, y=10)

    ws_search_button = Button(m.window, text='Выбрать файл', width=12, height=1, font=('Times New Roman', 12),
                              bg='yellow', command=ws_open_file)
    ws_search_button.place(x=50, y=60)
    ToolTip(ws_search_button, 'Выбрать картинку для редактирования...')

    ws_file_label = Text(m.window, width=23, height=2, state=DISABLED)
    ws_file_label.place(x=220, y=10)

    ws_color_button = Button(m.window, text='Выбрать цвет', width=22, height=1, font=('Times New Roman', 12),
                             bg='#f5ba53', command=ws_choose_color)
    ws_color_button.place(x=200, y=60)
    ToolTip(ws_color_button, 'Выбрать цвет надписи...')

    ws_label_1 = Label(m.window, text='Tекст водяного знака:')
    ws_label_1.place(x=50, y=100)

    ws_text = Text(m.window, width=35, height=5)
    ws_text.place(x=50, y=120)

    ws_color_demo = Label(m.window, bg='white', width=7, height=5)
    ws_color_demo.place(x=350, y=121)

    ws_label_2 = Label(m.window, text='Расположение текста на картинке:')
    ws_label_2.place(x=50, y=220)

    ws_label_3 = Label(m.window, text='X =')
    ws_label_3.place(x=50, y=250)

    ws_input_1 = Entry(m.window, width=6)
    ws_input_1.place(x=80, y=250)

    ws_label_4 = Label(m.window, text='Y =')
    ws_label_4.place(x=130, y=250)

    ws_input_2 = Entry(m.window, width=6)
    ws_input_2.place(x=160, y=250)

    ws_choose_button = Button(m.window, bg='#b0eef7', text='Указать', command=choose_place)
    ws_choose_button.place(x=215, y=245)

    ws_label_5 = Label(m.window, text='Размер шрифта:')
    ws_label_5.place(x=290, y=220)

    ws_input_3 = Entry(m.window, width=18)
    ws_input_3.place(x=290, y=250)

    ws_label_6 = Label(m.window, text='Шрифт:')
    ws_label_6.place(x=50, y=290)

    ws_font_combobox = ttk.Combobox(m.window, width=45, values=os.listdir('fonts'), state='readonly')
    ws_font_combobox.place(x=110, y=290)

    ws_preview_button = Button(m.window, text='Предварительный просмотр', width=22, height=1,
                               font=('Times New Roman', 12),
                               bg='#abf0a1', command=ws_open_preview)
    ws_preview_button.place(x=200, y=330)
    ToolTip(ws_preview_button, 'Открыть полученную картинку в программе просмотра изображений...')

    ws_save_button = Button(m.window, text='Сохранить', width=12, height=1, font=('Times New Roman', 12),
                            bg='#93e6a8', command=ws_save)
    ws_save_button.place(x=50, y=330)
    ToolTip(ws_save_button, 'Сохранить полученную картинку в новом месте...')

    ws_off = Button(m.window, text='⌂', font=('Arial Bold', 15), width=2, height=1, bg='black', fg='white',
                    command=ws_destroy)
    ws_off.place(x=0, y=5)
    ToolTip(ws_off, 'На главную...')
