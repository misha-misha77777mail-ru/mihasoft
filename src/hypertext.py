from tkinter import colorchooser, ttk, messagebox
from random import randint
from tkinter.filedialog import asksaveasfilename, askopenfilename
from pyperclip import copy

from src.functions import *
from src.init import m, root
from src.homex import *


def HyperText():
    htt = HyperTextGlobals()
    ht_view_list = []
    ht_list = []

    def ht_destroy():
        try:
            htt.req_win.destroy()
        except AttributeError:
            pass

        try:
            htt.i_i.destroy()
        except AttributeError:
            pass

        try:
            htt.resp_window.destroy()
        except AttributeError:
            pass

        ht_title.destroy()
        ht_preview_button.destroy()
        ht_del_button.destroy()
        ht_save_button.destroy()
        ht_frame_1.destroy()
        ht_frame_2.destroy()
        ht_info.destroy()
        ht_off.destroy()
        ht_frame_3.destroy()
        ht_send_button.destroy()
        ht_new.destroy()
        ht_check.destroy()

        homes()
        m.window.configure(width=788, height=m.abs_height)
        center_window(root, 678, m.abs_height)

    def ht_choose_background():
        ht_ch = colorchooser.askcolor()
        htt.background = ht_ch[1]
        ht_color_button.configure(bg=str(htt.background))

    def ht_choose_color():
        ht_ch_1 = colorchooser.askcolor()
        htt.color = ht_ch_1[1]
        ht_color_button_2.configure(bg=str(htt.color))

    def ht_del_block():
        if ht_list:
            def ht_create_req_window():
                def ht_ok():
                    ht_list.pop(int(ht_comb.get()[0] + ht_comb.get()[1]) - 1)
                    ht_view_list.pop(int(ht_comb.get()[0] + ht_comb.get()[1]) - 1)
                    htt.key -= 1
                    htt.req_win.destroy()

                htt.req_win = Toplevel()
                htt.req_win.title('Удаление')
                center_window(htt.req_win, 300, 100)
                htt.req_win.resizable(False, False)
                h_v = []
                for z in range(1, htt.key + 1):
                    h_v.append(str(z) + ' .' + ht_view_list[z - 1])
                ht_comb = ttk.Combobox(htt.req_win, values=h_v, width=45, state='readonly')
                ht_comb.place(x=5, y=5)

                ht_but = Button(htt.req_win, text='OK', width=10, command=ht_ok)
                ht_but.place(x=110, y=50)

            try:
                htt.req_win.resizable(False, False)

            except AttributeError:
                ht_create_req_window()

            except TclError:
                ht_create_req_window()
        else:
            messagebox.showinfo('INFO', 'Элементы отсутствуют!')

    def ht_preview():
        document = f'''<!DOCTYPE html><html><head><title>{ht_tit_input.get()}</title>
</head><body bgcolor="{htt.background}">''' + ''.join(ht_list) + '''</body></html>'''
        ht_num = str(randint(0, 10000))
        ht_html = open(f'C:/MihaSoft Files/Temp/{ht_num}.html', 'w')
        ht_html.write(document)
        ht_html.close()
        open_new(f'file:///C:/MihaSoft Files/Temp/{ht_num}.html')

    def ht_append():
        if (not ht_1_input.get().isdigit() and ht_1_input.get()) or (not ht_width.get().isdigit() and ht_width.get()) \
                or (not ht_height.get().isdigit() and ht_height.get()):
            messagebox.showwarning('INFO', 'Некорректные числовые параметры!')
        else:
            ht_center = ht_center_end = ''
            if var_center.get():
                ht_center = '<center>'
                ht_center_end = '</center>'

            if ht_combobox_1.get() == 'Жирный':
                ht_type = 'bold'
            else:
                ht_type = 'normal'
            if ht_combobox_2.get() == 'Блок':
                htt.block = f'''{ht_center}<div style="color: {htt.color}; font-size: {ht_1_input.get()}px;
                font-weight: {ht_type}; margin: {ht_input_x.get()}px; background: {htt.all_color};
                width: {ht_width.get()}px; height: {ht_height.get()}px;">
                {ht_text.get(1.0, END)}</div>{ht_center_end}'''

            elif ht_combobox_2.get() == 'Ссылка':
                htt.block = f'''{ht_center}<a style="color: {htt.color}; font-size: {ht_1_input.get()}px;
                             font-weight: {ht_type}; margin: {ht_input_x.get()}px;"
                             href="{ht_but_href.get()}">{ht_text.get(1.0, END)}</a>{ht_center_end}'''

            elif ht_combobox_2.get() == 'Кнопка':
                htt.block = f'''{ht_center}<button style="color: {htt.color}; font-size: {ht_1_input.get()}px;
                             font-weight: {ht_type}; margin: {ht_input_x.get()}px; background: {htt.all_color};
                             width: {ht_width.get()}px; height: {ht_height.get()}px;" 
                             onclick="m.window.location.href = '{ht_but_href.get()}'">{ht_text.get(1.0, END)}</button>
                             {ht_center_end}'''
            ht_list.append(htt.block)
            ht_view_list.append(f'{ht_combobox_2.get()} : {ht_text.get(1.0, END)}')
            htt.key += 1
            ht_text.delete(1.0, END)
            ht_input_x.delete(0, END)
            ht_but_href.delete(0, END)
            ht_height.delete(0, END)
            ht_width.delete(0, END)

    def add_image():
        if (not ht_but_width.get().isdigit() and ht_but_width.get()) or (not ht_but_height.get().isdigit()
                                                                         and ht_but_height.get()):
            messagebox.showwarning('INFO', 'Некорректные числовые параметры!')
        elif htt.image is None and not ht_img_href.get():
            messagebox.showwarning('INFO', 'Выберите изображение для вставки!')
        else:
            ht_center = ht_center_end = ''
            if var_center.get():
                ht_center = '<center>'
                ht_center_end = '</center>'
            if not ht_img_href.get():
                src = 'file:///' + str(htt.image)
            else:
                src = ht_img_href.get()
            ht_block = f'''{ht_center}<img src="{src}" width="{ht_but_width.get()}px" height="{ht_but_height.get()}px"
            style="margin: {ht_input_x.get()}">{ht_center_end}'''
            ht_list.append(ht_block)
            ht_view_list.append(f'Изображение: {src}')
            htt.key += 1
            ht_img_href.delete(0, END)
            ht_but_height.delete(0, END)
            ht_but_width.delete(0, END)

    def ht_save():
        ht_file = asksaveasfilename(title='Сохранить файл', defaultextension='.html',
                                    filetypes=(('HTML file', '*.html'), ('All Files', '*.*')))
        if ht_file:
            _document = f'''<!DOCTYPE html><html><head><title>{ht_tit_input.get()}</title>
            </head><body bgcolor="{htt.background}">''' + ''.join(ht_list) + '''</body></html>'''
            file = open(ht_file, 'w')
            file.write(_document)
            file.close()

    def ht_info_i():
        def ht_create_info_window():
            htt.i_i = Toplevel()
            center_window(htt.i_i, 1100, 788)
            htt.i_i.resizable(False, False)
            htt.i_i.title('INFO')
            ht_box = Listbox(htt.i_i, width=180, height=40)
            for xz in ht_view_list:
                ht_box.insert(END, xz)
            ht_box.pack()

        try:
            htt.i_i.resizable(False, False)

        except AttributeError:
            ht_create_info_window()

        except TclError:
            ht_create_info_window()

    def ht_choose_img():
        hh_file = askopenfilename()
        if hh_file:
            htt.image = hh_file
            ht_now_image.configure(text=f'Текущий файл: {htt.image}')

    def ht_choose_bg_all():
        abg = colorchooser.askcolor()
        htt.all_color = abg[1]
        ht_colora_button.configure(bg=str(htt.all_color))

    def ht_send():
        def write_to_mihnote():
            copy(f'https://otziv-mihasoft.glitch.me/page?id={response.text}')
            if ht_tit_input.get():
                ht_til = ht_tit_input.get()
            else:
                ht_til = 'url'
            url_file = open('C:/MihaSoft Files/MihNote Files/' + ht_til + '.miha', 'w')
            url_file.write(f'https://otziv-mihasoft.glitch.me/page?id={response.text}')
            url_file.close()
            htt.resp_window.destroy()

        def copy_url():
            copy(f'https://otziv-mihasoft.glitch.me/page?id={response.text}')
            htt.resp_window.destroy()

        try:
            abstr_inp = Entry(m.window)
            abstr_inp.insert(0, str(randint(10000, 1000000)))
            ht_list_x = []
            for lol in range(len(ht_list)):
                ht_list_x.append(ht_list[lol].replace('#', '%23').replace('&', '%26'))

            document_send = f'''<!DOCTYPE html><html><head><title>{ht_tit_input.get()}</title>
            </head><body bgcolor="{htt.background.replace('#', '%23').replace('&', '%26')}">''' + ''.join(ht_list_x) + \
                            '''</body></html>'''
            response = requests.get(f'https://otziv-mihasoft.glitch.me/regis?name={document_send}&id={abstr_inp.get()}')
            if response.text:
                htt.resp_window = Toplevel()
                htt.resp_window.title('Успешно!')
                center_window(htt.resp_window, 400, 140)
                htt.resp_window.resizable(False, False)
                label_res = Label(htt.resp_window, font=('Times New Roman', 13), text=f'''Ваша страница опубликована
и доступна по адресу:

https://otziv-mihasoft.glitch.me/page?id={response.text}''')
                label_res.pack()
                res_but_1 = Button(htt.resp_window, text='Добавить в MihNote', font=('Times New Roman', 11), bg='white',
                                   command=write_to_mihnote)
                res_but_1.place(x=30, y=100)
                res_but_2 = Button(htt.resp_window, text='Копировать', font=('Times New Roman', 11), bg='white',
                                   command=copy_url)
                res_but_2.place(x=280, y=100)

            else:
                messagebox.showerror('Ошибка!', 'Ошибка на сервере! Попробуйте позже или свяжитесь с разработчиком.')
        except requests.exceptions.ConnectionError:
            messagebox.showerror('Ошибка!', 'Нет доступа к сети!')

    def ht_new():
        ht_list.clear()
        ht_view_list.clear()

    if not os.path.exists('C:/MihaSoft Files/Temp'):
        os.mkdir('C:/MihaSoft Files/Temp')
    if os.listdir('C:/MihaSoft Files/Temp'):
        for i in os.listdir('C:/MihaSoft Files/Temp'):
            os.remove('C:/MihaSoft Files/Temp/' + i)

    center_window(root, 850, 480)
    m.window.configure(width=850, height=480)
    root.title('HyperText 3.0')
    root.minsize(850, 480)

    ht_title = Label(m.window, text='HyperText 3.0', font=('Arial Bold', 16), fg='red')
    ht_title.place(x=50, y=10)

    ht_preview_button = Button(m.window, text='Предварительный просмотр', width=23, font=('Times New Roman', 13),
                               bg='#fff7ab',
                               command=ht_preview)
    ht_preview_button.place(x=620, y=165)
    ToolTip(ht_preview_button, 'Открыть страницу в браузере без сохранения')

    ht_del_button = Button(m.window, text='Удалить элемент', width=23, font=('Times New Roman', 13), bg='#ffb6ab',
                           command=ht_del_block)
    ht_del_button.place(x=620, y=210)
    ToolTip(ht_del_button, 'Удалить ранее добавленный элемент с макета страницы')

    ht_save_button = Button(m.window, text='Сохранить', font=('Times New Roman', 13), bg='#c7ffda', width=23,
                            command=ht_save)
    ht_save_button.place(x=620, y=255)
    ToolTip(ht_save_button, 'Сохранить страницу, как локальный файл')

    ht_send_button = Button(m.window, text='Опубликовать', font=('Times New Roman', 13), bg='#93e6a8', width=23,
                            command=ht_send)
    ht_send_button.place(x=620, y=300)
    ToolTip(ht_send_button, 'Загрузить страницу на сервер MihaSoft и получить ссылку')

    ht_info = Button(m.window, text='Список блоков', width=23, font=('Times New Roman', 13), bg='#b8b8b8',
                     command=ht_info_i)
    ht_info.place(x=620, y=345)
    ToolTip(ht_info, 'Вывести список всех добавленных html-элементов')

    ht_new = Button(m.window, text='Новый проект', width=23, font=('Times New Roman', 13), bg='#c9c9c9',
                    command=ht_new)
    ht_new.place(x=620, y=390)
    ToolTip(ht_new, 'Удалить все элементы из текущей конструируемой страницы')

    ht_frame_1 = LabelFrame(m.window, width=300, height=100, text='Общее')
    ht_frame_1.place(x=50, y=45)

    ht_label_1 = Label(ht_frame_1, text='Заголовок:')
    ht_label_1.place(x=0, y=0)

    ht_tit_input = Entry(ht_frame_1, width=35)
    ht_tit_input.place(x=70, y=0)

    ht_label_2 = Label(ht_frame_1, text='Цвет фона:')
    ht_label_2.place(x=0, y=30)

    ht_color_button = Button(ht_frame_1, text='Выбрать', font=('Times New Roman', 11), bg='white',
                             command=ht_choose_background)
    ht_color_button.place(x=70, y=30)

    ht_label_x = Label(ht_frame_1, text='Отступы:')
    ht_label_x.place(x=160, y=35)

    ht_input_x = Entry(ht_frame_1, width=10)
    ht_input_x.place(x=220, y=35)

    ht_frame_2 = LabelFrame(m.window, width=550, height=320, text='Элементы')
    ht_frame_2.place(x=50, y=145)

    ht_label_3 = Label(ht_frame_2, text='Цвет текста:')
    ht_label_3.place(x=0, y=0)

    ht_color_button_2 = Button(ht_frame_2, text='Выбрать', font=('Times New Roman', 11), bg='white',
                               command=ht_choose_color)
    ht_color_button_2.place(x=90, y=0)

    ht_label_4 = Label(ht_frame_2, text='Тип текста:')
    ht_label_4.place(x=180, y=0)

    ht_combobox_1 = ttk.Combobox(ht_frame_2, values=['Жирный', 'Нормальный'], state='readonly', width=11)
    ht_combobox_1.place(x=250, y=0)

    ht_label_5 = Label(ht_frame_2, text='Размер текста:')
    ht_label_5.place(x=350, y=0)

    ht_1_input = Entry(ht_frame_2, width=10)
    ht_1_input.place(x=450, y=0)

    ht_label_6 = Label(ht_frame_2, text='Текст:')
    ht_label_6.place(x=0, y=40)

    ht_text = Text(ht_frame_2, width=60, height=10)
    ht_text.place(x=50, y=40)

    ht_label_7x = Label(ht_frame_2, text='Высота:')
    ht_label_7x.place(x=410, y=215)

    ht_height = Entry(ht_frame_2, width=5)
    ht_height.place(x=470, y=215)

    ht_label_8x = Label(ht_frame_2, text='Длина:')
    ht_label_8x.place(x=410, y=235)

    ht_width = Entry(ht_frame_2, width=5)
    ht_width.place(x=470, y=235)

    ht_add_button = Button(ht_frame_2, text='Добавить', font=('Times New Roman', 12), bg='#93e6a8', command=ht_append)
    ht_add_button.place(x=50, y=260)

    ht_label_4x = Label(ht_frame_2, text='Тип элемента:')
    ht_label_4x.place(x=180, y=260)

    ht_combobox_2 = ttk.Combobox(ht_frame_2, values=['Блок', 'Кнопка', 'Ссылка'], width=11)
    ht_combobox_2.place(x=280, y=260)
    ht_combobox_2.insert(0, 'Блок')
    ht_combobox_2.configure(state='readonly')

    ht_frame_3 = LabelFrame(m.window, width=457, height=130, text='Изображение')
    ht_frame_3.place(x=380, y=15)

    ht_label_7 = Label(ht_frame_3, text='Высота:')
    ht_label_7.place(x=5, y=5)

    ht_but_height = Entry(ht_frame_3, width=5)
    ht_but_height.place(x=70, y=5)

    ht_label_8 = Label(ht_frame_3, text='Длина:')
    ht_label_8.place(x=5, y=25)

    ht_but_width = Entry(ht_frame_3, width=5)
    ht_but_width.place(x=70, y=25)

    ht_label_9 = Label(ht_frame_2, text='Цвет:')
    ht_label_9.place(x=300, y=220)

    ht_colora_button = Button(ht_frame_2, text='Выбрать', font=('Times New Roman', 9), bg='white',
                              command=ht_choose_bg_all)
    ht_colora_button.place(x=340, y=215)

    ht_label_10 = Label(ht_frame_3, text='Файл:')
    ht_label_10.place(x=170, y=5)

    ht_img_button = Button(ht_frame_3, text='Выбрать', font=('Times New Roman', 9), bg='white',
                           command=ht_choose_img)
    ht_img_button.place(x=220, y=5)

    ht_label_11x = Label(ht_frame_3, text='Ссылка:')
    ht_label_11x.place(x=35, y=50)

    ht_img_href = Entry(ht_frame_3, width=46)
    ht_img_href.place(x=100, y=50)

    ht_now_image = Label(ht_frame_3)
    ht_now_image.place(x=35, y=80)

    ht_label_11 = Label(ht_frame_2, text='Ссылка:')
    ht_label_11.place(x=5, y=220)

    ht_but_href = Entry(ht_frame_2, width=36)
    ht_but_href.place(x=70, y=220)

    ht_add_button_2 = Button(ht_frame_3, text='Добавить', font=('Times New Roman', 12), bg='#93e6a8',
                             command=add_image)
    ht_add_button_2.place(x=300, y=3)

    var_center = BooleanVar()
    var_center.set(False)

    ht_check = Checkbutton(m.window, text='Центрировать', variable=var_center, onvalue=1, offvalue=0)
    ht_check.place(x=240, y=25)

    ht_off = Button(m.window, text='⌂', font=('Arial Bold', 15), width=2, height=1, bg='black', fg='white',
                    command=ht_destroy)
    ht_off.place(x=0, y=5)
    ToolTip(ht_off, 'На главную...')
