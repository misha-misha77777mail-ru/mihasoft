from tkinter import colorchooser, ttk
from numpy import save

from src.functions import *
from src.init import m, root
from src.homex import *


def Paint():
    """
    Пиксельный графический редактор
    """
    # Создание объекта с глобальными переменными
    p = PaintGlobals()

    def p_to_home():
        """
        Возвращение на главную страницу MihaSoft
        """
        try:
            p.delete_window.destroy()
        except AttributeError:
            pass

        try:
            p.open_window.destroy()
        except AttributeError:
            pass

        try:
            p.save_window.destroy()
        except AttributeError:
            pass

        p_window.destroy()
        homes()
        m.window.configure(width=788, height=m.abs_height)
        center_window(root, 678, m.abs_height)

    def recol(pix):
        """
        Общая функция изменения цвета пикселя
        """
        pix.configure(bg=p.chosen_color)

    # Функции изменения цвета для каждого пикселя
    def r1():
        recol(a1)

    def r2():
        recol(a2)

    def r3():
        recol(a3)

    def r4():
        recol(a4)

    def r5():
        recol(a5)

    def r6():
        recol(a6)

    def r7():
        recol(a7)

    def r8():
        recol(a8)

    def r9():
        recol(a9)

    def r10():
        recol(a10)

    def r11():
        recol(a11)

    def r12():
        recol(a12)

    def r13():
        recol(a13)

    def r14():
        recol(a14)

    def r15():
        recol(a15)

    def r16():
        recol(a16)

    def r17():
        recol(a17)

    def r18():
        recol(a18)

    def r19():
        recol(a19)

    def r20():
        recol(a20)

    def r21():
        recol(a21)

    def r22():
        recol(a22)

    def r23():
        recol(a23)

    def r24():
        recol(a24)

    def r25():
        recol(a25)

    def r26():
        recol(a26)

    def r27():
        recol(a27)

    def r28():
        recol(a28)

    def r29():
        recol(a29)

    def r30():
        recol(a30)

    def s1():
        recol(b1)

    def s2():
        recol(b2)

    def s3():
        recol(b3)

    def s4():
        recol(b4)

    def s5():
        recol(b5)

    def s6():
        recol(b6)

    def s7():
        recol(b7)

    def s8():
        recol(b8)

    def s9():
        recol(b9)

    def s10():
        recol(b10)

    def s11():
        recol(b11)

    def s12():
        recol(b12)

    def s13():
        recol(b13)

    def s14():
        recol(b14)

    def s15():
        recol(b15)

    def s16():
        recol(b16)

    def s17():
        recol(b17)

    def s18():
        recol(b18)

    def s19():
        recol(b19)

    def s20():
        recol(b20)

    def s21():
        recol(b21)

    def s22():
        recol(b22)

    def s23():
        recol(b23)

    def s24():
        recol(b24)

    def s25():
        recol(b25)

    def s26():
        recol(b26)

    def s27():
        recol(b27)

    def s28():
        recol(b28)

    def s29():
        recol(b29)

    def s30():
        recol(b30)

    def t1():
        recol(c1)

    def t2():
        recol(c2)

    def t3():
        recol(c3)

    def t4():
        recol(c4)

    def t5():
        recol(c5)

    def t6():
        recol(c6)

    def t7():
        recol(c7)

    def t8():
        recol(c8)

    def t9():
        recol(c9)

    def t10():
        recol(c10)

    def t11():
        recol(c11)

    def t12():
        recol(c12)

    def t13():
        recol(c13)

    def t14():
        recol(c14)

    def t15():
        recol(c15)

    def t16():
        recol(c16)

    def t17():
        recol(c17)

    def t18():
        recol(c18)

    def t19():
        recol(c19)

    def t20():
        recol(c20)

    def t21():
        recol(c21)

    def t22():
        recol(c22)

    def t23():
        recol(c23)

    def t24():
        recol(c24)

    def t25():
        recol(c25)

    def t26():
        recol(c26)

    def t27():
        recol(c27)

    def t28():
        recol(c28)

    def t29():
        recol(c29)

    def t30():
        recol(c30)

    def u1():
        recol(d1)

    def u2():
        recol(d2)

    def u3():
        recol(d3)

    def u4():
        recol(d4)

    def u5():
        recol(d5)

    def u6():
        recol(d6)

    def u7():
        recol(d7)

    def u8():
        recol(d8)

    def u9():
        recol(d9)

    def u10():
        recol(d10)

    def u11():
        recol(d11)

    def u12():
        recol(d12)

    def u13():
        recol(d13)

    def u14():
        recol(d14)

    def u15():
        recol(d15)

    def u16():
        recol(d16)

    def u17():
        recol(d17)

    def u18():
        recol(d18)

    def u19():
        recol(d19)

    def u20():
        recol(d20)

    def u21():
        recol(d21)

    def u22():
        recol(d22)

    def u23():
        recol(d23)

    def u24():
        recol(d24)

    def u25():
        recol(d25)

    def u26():
        recol(d26)

    def u27():
        recol(d27)

    def u28():
        recol(d28)

    def u29():
        recol(d29)

    def u30():
        recol(d30)

    def v1():
        recol(e1)

    def v2():
        recol(e2)

    def v3():
        recol(e3)

    def v4():
        recol(e4)

    def v5():
        recol(e5)

    def v6():
        recol(e6)

    def v7():
        recol(e7)

    def v8():
        recol(e8)

    def v9():
        recol(e9)

    def v10():
        recol(e10)

    def v11():
        recol(e11)

    def v12():
        recol(e12)

    def v13():
        recol(e13)

    def v14():
        recol(e14)

    def v15():
        recol(e15)

    def v16():
        recol(e16)

    def v17():
        recol(e17)

    def v18():
        recol(e18)

    def v19():
        recol(e19)

    def v20():
        recol(e20)

    def v21():
        recol(e21)

    def v22():
        recol(e22)

    def v23():
        recol(e23)

    def v24():
        recol(e24)

    def v25():
        recol(e25)

    def v26():
        recol(e26)

    def v27():
        recol(e27)

    def v28():
        recol(e28)

    def v29():
        recol(e29)

    def v30():
        recol(e30)

    def w1():
        recol(f1)

    def w2():
        recol(f2)

    def w3():
        recol(f3)

    def w4():
        recol(f4)

    def w5():
        recol(f5)

    def w6():
        recol(f6)

    def w7():
        recol(f7)

    def w8():
        recol(f8)

    def w9():
        recol(f9)

    def w10():
        recol(f10)

    def w11():
        recol(f11)

    def w12():
        recol(f12)

    def w13():
        recol(f13)

    def w14():
        recol(f14)

    def w15():
        recol(f15)

    def w16():
        recol(f16)

    def w17():
        recol(f17)

    def w18():
        recol(f18)

    def w19():
        recol(f19)

    def w20():
        recol(f20)

    def w21():
        recol(f21)

    def w22():
        recol(f22)

    def w23():
        recol(f23)

    def w24():
        recol(f24)

    def w25():
        recol(f25)

    def w26():
        recol(f26)

    def w27():
        recol(f27)

    def w28():
        recol(f28)

    def w29():
        recol(f29)

    def w30():
        recol(f30)

    def x1():
        recol(g1)

    def x2():
        recol(g2)

    def x3():
        recol(g3)

    def x4():
        recol(g4)

    def x5():
        recol(g5)

    def x6():
        recol(g6)

    def x7():
        recol(g7)

    def x8():
        recol(g8)

    def x9():
        recol(g9)

    def x10():
        recol(g10)

    def x11():
        recol(g11)

    def x12():
        recol(g12)

    def x13():
        recol(g13)

    def x14():
        recol(g14)

    def x15():
        recol(g15)

    def x16():
        recol(g16)

    def x17():
        recol(g17)

    def x18():
        recol(g18)

    def x19():
        recol(g19)

    def x20():
        recol(g20)

    def x21():
        recol(g21)

    def x22():
        recol(g22)

    def x23():
        recol(g23)

    def x24():
        recol(g24)

    def x25():
        recol(g25)

    def x26():
        recol(g26)

    def x27():
        recol(g27)

    def x28():
        recol(g28)

    def x29():
        recol(g29)

    def x30():
        recol(g30)

    def y1():
        recol(h1)

    def y2():
        recol(h2)

    def y3():
        recol(h3)

    def y4():
        recol(h4)

    def y5():
        recol(h5)

    def y6():
        recol(h6)

    def y7():
        recol(h7)

    def y8():
        recol(h8)

    def y9():
        recol(h9)

    def y10():
        recol(h10)

    def y11():
        recol(h11)

    def y12():
        recol(h12)

    def y13():
        recol(h13)

    def y14():
        recol(h14)

    def y15():
        recol(h15)

    def y16():
        recol(h16)

    def y17():
        recol(h17)

    def y18():
        recol(h18)

    def y19():
        recol(h19)

    def y20():
        recol(h20)

    def y21():
        recol(h21)

    def y22():
        recol(h22)

    def y23():
        recol(h23)

    def y24():
        recol(h24)

    def y25():
        recol(h25)

    def y26():
        recol(h26)

    def y27():
        recol(h27)

    def y28():
        recol(h28)

    def y29():
        recol(h29)

    def y30():
        recol(h30)

    def p_choose_color():
        """
        Функция выбора цвета редактирования
        """
        p_colorchoose_window = colorchooser.askcolor()
        p.chosen_color = p_colorchoose_window[1]
        p_choose_button.configure(bg=str(p.chosen_color))
        p.choose_flag = True

    def eraser():
        """
        Функция включения-выключения режима ластика
        """
        # Включение ластика
        if p.choose_flag:
            p.now_color = p_choose_button['background']
            p.chosen_color = 'white'
            p_choose_button.configure(bg='white')
            p.choose_flag = False

        # Возвращение к последнему использовавшемуся цвету
        else:
            p.chosen_color = p.now_color
            p_choose_button.configure(bg=p.now_color)
            p.choose_flag = True

    def p_save():
        """
        Функция сохранения рисунка в файл
        """

        def p_save_changes():
            """
            Функция сохранения изменений в существующем файле
            """
            p_colors_list = []
            for i in range(len(p_all)):
                p_colors_list.append(p_all[i]['background'])
            save(p.file_name, p_colors_list)
            p.save_window.destroy()

        def p_abort_save():
            """
            Отмена сохранения
            """
            p.save_window.destroy()

        # Проверка значения переменной, отвечающей за состояния
        # приложения (создание нового файла или редактирование существующего)
        # и вызов соответствующего окна.
        def p_create_save_window():
            def p_save_file():
                """
                Сохранение нового файла
                """
                p_colors_list = []
                for i in range(len(p_all)):
                    p_colors_list.append(p_all[i]['background'])
                save('C:/MihaSoft Files/P Files/' + str(p_save_input.get()), p_colors_list)
                p.save_window.destroy()

            if p.save_flag:
                p.save_window = Toplevel()
                center_window(p.save_window, 300, 100)
                p.save_window.resizable(False, False)
                p.save_window.title('Сохранение')

                p_save_label = Label(p.save_window, text='Введите название файла...')
                p_save_label.place(x=5, y=5)

                p_save_input = Entry(p.save_window, width=25)
                p_save_input.place(x=10, y=45)

                p_save_ok_button = Button(p.save_window, text='Сохранить', width=10, bg='#93e6a8', command=p_save_file)
                p_save_ok_button.place(x=200, y=23)

                p_close_button = Button(p.save_window, text='Отмена', width=10, bg='#b8b8b8', command=p_abort_save)
                p_close_button.place(x=200, y=60)

            else:
                p.save_window = Toplevel()
                center_window(p.save_window, 300, 100)
                p.save_window.resizable(False, False)
                p.save_window.title('Сохранение изменений')

                p_save_label = Label(p.save_window, text='Сохранить изменения в файле\n' + p.file_name + '?')
                p_save_label.place(x=5, y=5)

                p_save_ok_button = Button(p.save_window, text='Сохранить', width=10, bg='#93e6a8',
                                          command=p_save_changes)
                p_save_ok_button.place(x=100, y=60)

                p_close_button = Button(p.save_window, text='Отмена', width=10, bg='#b8b8b8', command=p_abort_save)
                p_close_button.place(x=200, y=60)

        try:
            p.save_window.resizable(False, False)

        except AttributeError:
            p_create_save_window()

        except TclError:
            p_create_save_window()

    def p_open():
        """
        Функция открытия сохранённого рисунка
        """

        def p_abort_open():
            """
            Отмена открытия
            """
            p.open_window.destroy()

        def p_create_open_window():
            def p_open_ok():
                """
                Считывание данных и вывод рисунка на экран
                """
                p_open_colors_list = load('C:/MihaSoft Files/P Files/' + str(p_open_combobox.get()))
                p.file_name = 'C:/MihaSoft Files/P Files/' + str(p_open_combobox.get())
                for i in range(len(p_all)):
                    p_all[i].configure(bg=p_open_colors_list[i])
                p.open_window.destroy()
                p.save_flag = False

            p.open_window = Toplevel()
            center_window(p.open_window, 300, 100)
            p.open_window.resizable(False, False)
            p.open_window.title('Открыть')

            p_open_label = Label(p.open_window, text='Выберите файл...')
            p_open_label.place(x=5, y=5)

            # Список существующих файлов
            p_open_combobox = ttk.Combobox(p.open_window, values=os.listdir('C:/MihaSoft Files/P Files'),
                                           state='readonly')
            p_open_combobox.place(x=10, y=45)

            p_open_ok_button = Button(p.open_window, text='Открыть', width=10, bg='#93e6a8', command=p_open_ok)
            p_open_ok_button.place(x=200, y=23)

            p_open_abort_button = Button(p.open_window, text='Отмена', width=10, bg='#b8b8b8', command=p_abort_open)
            p_open_abort_button.place(x=200, y=60)

        try:
            p.open_window.resizable(False, False)

        except AttributeError:
            p_create_open_window()

        except TclError:
            p_create_open_window()

    def p_delete():
        """
        Функция удаления сохранённых файлов
        """

        def p_delete_abort():
            """
            Отмена удаления
            """
            p.delete_window.destroy()

        def p_create_del_window():
            def p_delete_ok():
                """
                Удаление выбранного файла
                """
                os.remove('C:/MihaSoft Files/P Files/' + str(p_delete_combobox.get()))
                p.delete_window.destroy()

            p.delete_window = Toplevel()
            center_window(p.delete_window, 300, 100)
            p.delete_window.resizable(False, False)
            p.delete_window.title('Удаление')

            p_delete_label = Label(p.delete_window, text='Выберите файл...')
            p_delete_label.place(x=5, y=5)

            # Список существующих файлов
            p_delete_combobox = ttk.Combobox(p.delete_window, values=os.listdir('C:/MihaSoft Files/P Files'),
                                             state='readonly')
            p_delete_combobox.place(x=10, y=45)

            p_delete_ok_button = Button(p.delete_window, text='Удалить', width=10, bg='#e69b93', command=p_delete_ok)
            p_delete_ok_button.place(x=200, y=23)

            p_delete_close_button = Button(p.delete_window, text='Отмена', width=10, bg='#b8b8b8',
                                           command=p_delete_abort)
            p_delete_close_button.place(x=200, y=60)

        try:
            p.delete_window.resizable(False, False)

        except AttributeError:
            p_create_del_window()

        except TclError:
            p_create_del_window()

    def p_clean():
        """
        Функция очистки поля для рисования
        """
        for i in range(len(p_all)):
            p_all[i].configure(bg='white')

    def p_new_pict():
        """
        Функция очистки поля для рисования
        и выхода из режима редактирования
        """
        p.save_flag = True
        p.file_name = None
        p_clean()

    # Массив для последующего добавления объектов всех
    # пикселей для последующих операций с ними
    p_all = []

    # Создание папки с файлами в случае отсутствия таковой
    if not os.path.exists('C:/MihaSoft Files/P Files'):
        os.mkdir('C:/MihaSoft Files/P Files')

    center_window(root, 550, 300)
    m.window.configure(width=550, height=300)
    p_window = Frame(m.window, width=550, height=300)
    root.title('Paint 1.1')
    root.minsize(550, 300)

    p_title = Label(p_window, text='Paint 1.1', font=('Arial Bold', 16), fg='red')
    p_title.place(x=50, y=10)

    p_new_picture_button = Button(p_window, text='Новый рисунок', bg='#b8b8b8', command=p_new_pict)
    p_new_picture_button.place(x=180, y=10)

    p_clean_button = Button(p_window, text='Очистить', bg='#b8b8b8', command=p_clean)
    p_clean_button.place(x=285, y=10)

    p_eraser_button = Button(p_window, text='Ластик', bg='#b8b8b8', command=eraser)
    p_eraser_button.place(x=355, y=10)
    ToolTip(p_eraser_button, 'Нажмите повторно для возвращения к последнему цвету...')

    p_choose_button = Button(p_window, text='Выбрать цвет', bg='white', command=p_choose_color)
    p_choose_button.place(x=415, y=10)

    # Пиксели
    a1 = Button(p_window, width=1, height=1, bg='white', font=("Arial Bold", 6), command=r1)
    a1.place(x=50, y=50)
    p_all.append(a1)

    a2 = Button(p_window, width=1, height=1, bg='white', font=("Arial Bold", 6), command=r2)
    a2.place(x=65, y=50)
    p_all.append(a2)

    a3 = Button(p_window, width=1, height=1, bg='white', font=("Arial Bold", 6), command=r3)
    a3.place(x=80, y=50)
    p_all.append(a3)

    a4 = Button(p_window, width=1, height=1, bg='white', font=("Arial Bold", 6), command=r4)
    a4.place(x=95, y=50)
    p_all.append(a4)

    a5 = Button(p_window, width=1, height=1, bg='white', font=("Arial Bold", 6), command=r5)
    a5.place(x=110, y=50)
    p_all.append(a5)

    a6 = Button(p_window, width=1, height=1, bg='white', font=("Arial Bold", 6), command=r6)
    a6.place(x=125, y=50)
    p_all.append(a6)

    a7 = Button(p_window, width=1, height=1, bg='white', font=("Arial Bold", 6), command=r7)
    a7.place(x=140, y=50)
    p_all.append(a7)

    a8 = Button(p_window, width=1, height=1, bg='white', font=("Arial Bold", 6), command=r8)
    a8.place(x=155, y=50)
    p_all.append(a8)

    a9 = Button(p_window, width=1, height=1, bg='white', font=("Arial Bold", 6), command=r9)
    a9.place(x=170, y=50)
    p_all.append(a9)

    a10 = Button(p_window, width=1, height=1, bg='white', font=("Arial Bold", 6), command=r10)
    a10.place(x=185, y=50)
    p_all.append(a10)

    a11 = Button(p_window, width=1, height=1, bg='white', font=("Arial Bold", 6), command=r11)
    a11.place(x=200, y=50)
    p_all.append(a11)

    a12 = Button(p_window, width=1, height=1, bg='white', font=("Arial Bold", 6), command=r12)
    a12.place(x=215, y=50)
    p_all.append(a12)

    a13 = Button(p_window, width=1, height=1, bg='white', font=("Arial Bold", 6), command=r13)
    a13.place(x=230, y=50)
    p_all.append(a13)

    a14 = Button(p_window, width=1, height=1, bg='white', font=("Arial Bold", 6), command=r14)
    a14.place(x=245, y=50)
    p_all.append(a14)

    a15 = Button(p_window, width=1, height=1, bg='white', font=("Arial Bold", 6), command=r15)
    a15.place(x=260, y=50)
    p_all.append(a15)

    a16 = Button(p_window, width=1, height=1, bg='white', font=("Arial Bold", 6), command=r16)
    a16.place(x=275, y=50)
    p_all.append(a16)

    a17 = Button(p_window, width=1, height=1, bg='white', font=("Arial Bold", 6), command=r17)
    a17.place(x=290, y=50)
    p_all.append(a17)

    a18 = Button(p_window, width=1, height=1, bg='white', font=("Arial Bold", 6), command=r18)
    a18.place(x=305, y=50)
    p_all.append(a18)

    a19 = Button(p_window, width=1, height=1, bg='white', font=("Arial Bold", 6), command=r19)
    a19.place(x=320, y=50)
    p_all.append(a19)

    a20 = Button(p_window, width=1, height=1, bg='white', font=("Arial Bold", 6), command=r20)
    a20.place(x=335, y=50)
    p_all.append(a20)

    a21 = Button(p_window, width=1, height=1, bg='white', font=("Arial Bold", 6), command=r21)
    a21.place(x=350, y=50)
    p_all.append(a21)

    a22 = Button(p_window, width=1, height=1, bg='white', font=("Arial Bold", 6), command=r22)
    a22.place(x=365, y=50)
    p_all.append(a22)

    a23 = Button(p_window, width=1, height=1, bg='white', font=("Arial Bold", 6), command=r23)
    a23.place(x=380, y=50)
    p_all.append(a23)

    a24 = Button(p_window, width=1, height=1, bg='white', font=("Arial Bold", 6), command=r24)
    a24.place(x=395, y=50)
    p_all.append(a24)

    a25 = Button(p_window, width=1, height=1, bg='white', font=("Arial Bold", 6), command=r25)
    a25.place(x=410, y=50)
    p_all.append(a25)

    a26 = Button(p_window, width=1, height=1, bg='white', font=("Arial Bold", 6), command=r26)
    a26.place(x=425, y=50)
    p_all.append(a26)

    a27 = Button(p_window, width=1, height=1, bg='white', font=("Arial Bold", 6), command=r27)
    a27.place(x=440, y=50)
    p_all.append(a27)

    a28 = Button(p_window, width=1, height=1, bg='white', font=("Arial Bold", 6), command=r28)
    a28.place(x=455, y=50)
    p_all.append(a28)

    a29 = Button(p_window, width=1, height=1, bg='white', font=("Arial Bold", 6), command=r29)
    a29.place(x=470, y=50)
    p_all.append(a29)

    a30 = Button(p_window, width=1, height=1, bg='white', font=("Arial Bold", 6), command=r30)
    a30.place(x=485, y=50)
    p_all.append(a30)

    b1 = Button(p_window, width=1, height=1, bg='white', font=("Arial Bold", 6), command=s1)
    b1.place(x=50, y=68)
    p_all.append(b1)

    b2 = Button(p_window, width=1, height=1, bg='white', font=("Arial Bold", 6), command=s2)
    b2.place(x=65, y=68)
    p_all.append(b2)

    b3 = Button(p_window, width=1, height=1, bg='white', font=("Arial Bold", 6), command=s3)
    b3.place(x=80, y=68)
    p_all.append(b3)

    b4 = Button(p_window, width=1, height=1, bg='white', font=("Arial Bold", 6), command=s4)
    b4.place(x=95, y=68)
    p_all.append(b4)

    b5 = Button(p_window, width=1, height=1, bg='white', font=("Arial Bold", 6), command=s5)
    b5.place(x=110, y=68)
    p_all.append(b5)

    b6 = Button(p_window, width=1, height=1, bg='white', font=("Arial Bold", 6), command=s6)
    b6.place(x=125, y=68)
    p_all.append(b6)

    b7 = Button(p_window, width=1, height=1, bg='white', font=("Arial Bold", 6), command=s7)
    b7.place(x=140, y=68)
    p_all.append(b7)

    b8 = Button(p_window, width=1, height=1, bg='white', font=("Arial Bold", 6), command=s8)
    b8.place(x=155, y=68)
    p_all.append(b8)

    b9 = Button(p_window, width=1, height=1, bg='white', font=("Arial Bold", 6), command=s9)
    b9.place(x=170, y=68)
    p_all.append(b9)

    b10 = Button(p_window, width=1, height=1, bg='white', font=("Arial Bold", 6), command=s10)
    b10.place(x=185, y=68)
    p_all.append(b10)

    b11 = Button(p_window, width=1, height=1, bg='white', font=("Arial Bold", 6), command=s11)
    b11.place(x=200, y=68)
    p_all.append(b11)

    b12 = Button(p_window, width=1, height=1, bg='white', font=("Arial Bold", 6), command=s12)
    b12.place(x=215, y=68)
    p_all.append(b12)

    b13 = Button(p_window, width=1, height=1, bg='white', font=("Arial Bold", 6), command=s13)
    b13.place(x=230, y=68)
    p_all.append(b13)

    b14 = Button(p_window, width=1, height=1, bg='white', font=("Arial Bold", 6), command=s14)
    b14.place(x=245, y=68)
    p_all.append(b14)

    b15 = Button(p_window, width=1, height=1, bg='white', font=("Arial Bold", 6), command=s15)
    b15.place(x=260, y=68)
    p_all.append(b15)

    b16 = Button(p_window, width=1, height=1, bg='white', font=("Arial Bold", 6), command=s16)
    b16.place(x=275, y=68)
    p_all.append(b16)

    b17 = Button(p_window, width=1, height=1, bg='white', font=("Arial Bold", 6), command=s17)
    b17.place(x=290, y=68)
    p_all.append(b17)

    b18 = Button(p_window, width=1, height=1, bg='white', font=("Arial Bold", 6), command=s18)
    b18.place(x=305, y=68)
    p_all.append(b18)

    b19 = Button(p_window, width=1, height=1, bg='white', font=("Arial Bold", 6), command=s19)
    b19.place(x=320, y=68)
    p_all.append(b19)

    b20 = Button(p_window, width=1, height=1, bg='white', font=("Arial Bold", 6), command=s20)
    b20.place(x=335, y=68)
    p_all.append(b20)

    b21 = Button(p_window, width=1, height=1, bg='white', font=("Arial Bold", 6), command=s21)
    b21.place(x=350, y=68)
    p_all.append(b21)

    b22 = Button(p_window, width=1, height=1, bg='white', font=("Arial Bold", 6), command=s22)
    b22.place(x=365, y=68)
    p_all.append(b22)

    b23 = Button(p_window, width=1, height=1, bg='white', font=("Arial Bold", 6), command=s23)
    b23.place(x=380, y=68)
    p_all.append(b23)

    b24 = Button(p_window, width=1, height=1, bg='white', font=("Arial Bold", 6), command=s24)
    b24.place(x=395, y=68)
    p_all.append(b24)

    b25 = Button(p_window, width=1, height=1, bg='white', font=("Arial Bold", 6), command=s25)
    b25.place(x=410, y=68)
    p_all.append(b25)

    b26 = Button(p_window, width=1, height=1, bg='white', font=("Arial Bold", 6), command=s26)
    b26.place(x=425, y=68)
    p_all.append(b26)

    b27 = Button(p_window, width=1, height=1, bg='white', font=("Arial Bold", 6), command=s27)
    b27.place(x=440, y=68)
    p_all.append(b27)

    b28 = Button(p_window, width=1, height=1, bg='white', font=("Arial Bold", 6), command=s28)
    b28.place(x=455, y=68)
    p_all.append(b28)

    b29 = Button(p_window, width=1, height=1, bg='white', font=("Arial Bold", 6), command=s29)
    b29.place(x=470, y=68)
    p_all.append(b29)

    b30 = Button(p_window, width=1, height=1, bg='white', font=("Arial Bold", 6), command=s30)
    b30.place(x=485, y=68)
    p_all.append(b30)

    c1 = Button(p_window, width=1, height=1, bg='white', font=("Arial Bold", 6), command=t1)
    c1.place(x=50, y=86)
    p_all.append(c1)

    c2 = Button(p_window, width=1, height=1, bg='white', font=("Arial Bold", 6), command=t2)
    c2.place(x=65, y=86)
    p_all.append(c2)

    c3 = Button(p_window, width=1, height=1, bg='white', font=("Arial Bold", 6), command=t3)
    c3.place(x=80, y=86)
    p_all.append(c3)

    c4 = Button(p_window, width=1, height=1, bg='white', font=("Arial Bold", 6), command=t4)
    c4.place(x=95, y=86)
    p_all.append(c4)

    c5 = Button(p_window, width=1, height=1, bg='white', font=("Arial Bold", 6), command=t5)
    c5.place(x=110, y=86)
    p_all.append(c5)

    c6 = Button(p_window, width=1, height=1, bg='white', font=("Arial Bold", 6), command=t6)
    c6.place(x=125, y=86)
    p_all.append(c6)

    c7 = Button(p_window, width=1, height=1, bg='white', font=("Arial Bold", 6), command=t7)
    c7.place(x=140, y=86)
    p_all.append(c7)

    c8 = Button(p_window, width=1, height=1, bg='white', font=("Arial Bold", 6), command=t8)
    c8.place(x=155, y=86)
    p_all.append(c8)

    c9 = Button(p_window, width=1, height=1, bg='white', font=("Arial Bold", 6), command=t9)
    c9.place(x=170, y=86)
    p_all.append(c9)

    c10 = Button(p_window, width=1, height=1, bg='white', font=("Arial Bold", 6), command=t10)
    c10.place(x=185, y=86)
    p_all.append(c10)

    c11 = Button(p_window, width=1, height=1, bg='white', font=("Arial Bold", 6), command=t11)
    c11.place(x=200, y=86)
    p_all.append(c11)

    c12 = Button(p_window, width=1, height=1, bg='white', font=("Arial Bold", 6), command=t12)
    c12.place(x=215, y=86)
    p_all.append(c12)

    c13 = Button(p_window, width=1, height=1, bg='white', font=("Arial Bold", 6), command=t13)
    c13.place(x=230, y=86)
    p_all.append(c13)

    c14 = Button(p_window, width=1, height=1, bg='white', font=("Arial Bold", 6), command=t14)
    c14.place(x=245, y=86)
    p_all.append(c14)

    c15 = Button(p_window, width=1, height=1, bg='white', font=("Arial Bold", 6), command=t15)
    c15.place(x=260, y=86)
    p_all.append(c15)

    c16 = Button(p_window, width=1, height=1, bg='white', font=("Arial Bold", 6), command=t16)
    c16.place(x=275, y=86)
    p_all.append(c16)

    c17 = Button(p_window, width=1, height=1, bg='white', font=("Arial Bold", 6), command=t17)
    c17.place(x=290, y=86)
    p_all.append(c17)

    c18 = Button(p_window, width=1, height=1, bg='white', font=("Arial Bold", 6), command=t18)
    c18.place(x=305, y=86)
    p_all.append(c18)

    c19 = Button(p_window, width=1, height=1, bg='white', font=("Arial Bold", 6), command=t19)
    c19.place(x=320, y=86)
    p_all.append(c19)

    c20 = Button(p_window, width=1, height=1, bg='white', font=("Arial Bold", 6), command=t20)
    c20.place(x=335, y=86)
    p_all.append(c20)

    c21 = Button(p_window, width=1, height=1, bg='white', font=("Arial Bold", 6), command=t21)
    c21.place(x=350, y=86)
    p_all.append(c21)

    c22 = Button(p_window, width=1, height=1, bg='white', font=("Arial Bold", 6), command=t22)
    c22.place(x=365, y=86)
    p_all.append(c22)

    c23 = Button(p_window, width=1, height=1, bg='white', font=("Arial Bold", 6), command=t23)
    c23.place(x=380, y=86)
    p_all.append(c23)

    c24 = Button(p_window, width=1, height=1, bg='white', font=("Arial Bold", 6), command=t24)
    c24.place(x=395, y=86)
    p_all.append(c24)

    c25 = Button(p_window, width=1, height=1, bg='white', font=("Arial Bold", 6), command=t25)
    c25.place(x=410, y=86)
    p_all.append(c25)

    c26 = Button(p_window, width=1, height=1, bg='white', font=("Arial Bold", 6), command=t26)
    c26.place(x=425, y=86)
    p_all.append(c26)

    c27 = Button(p_window, width=1, height=1, bg='white', font=("Arial Bold", 6), command=t27)
    c27.place(x=440, y=86)
    p_all.append(c27)

    c28 = Button(p_window, width=1, height=1, bg='white', font=("Arial Bold", 6), command=t28)
    c28.place(x=455, y=86)
    p_all.append(c28)

    c29 = Button(p_window, width=1, height=1, bg='white', font=("Arial Bold", 6), command=t29)
    c29.place(x=470, y=86)
    p_all.append(c29)

    c30 = Button(p_window, width=1, height=1, bg='white', font=("Arial Bold", 6), command=t30)
    c30.place(x=485, y=86)
    p_all.append(c30)

    d1 = Button(p_window, width=1, height=1, bg='white', font=("Arial Bold", 6), command=u1)
    d1.place(x=50, y=104)
    p_all.append(d1)

    d2 = Button(p_window, width=1, height=1, bg='white', font=("Arial Bold", 6), command=u2)
    d2.place(x=65, y=104)
    p_all.append(d2)

    d3 = Button(p_window, width=1, height=1, bg='white', font=("Arial Bold", 6), command=u3)
    d3.place(x=80, y=104)
    p_all.append(d3)

    d4 = Button(p_window, width=1, height=1, bg='white', font=("Arial Bold", 6), command=u4)
    d4.place(x=95, y=104)
    p_all.append(d4)

    d5 = Button(p_window, width=1, height=1, bg='white', font=("Arial Bold", 6), command=u5)
    d5.place(x=110, y=104)
    p_all.append(d5)

    d6 = Button(p_window, width=1, height=1, bg='white', font=("Arial Bold", 6), command=u6)
    d6.place(x=125, y=104)
    p_all.append(d6)

    d7 = Button(p_window, width=1, height=1, bg='white', font=("Arial Bold", 6), command=u7)
    d7.place(x=140, y=104)
    p_all.append(d7)

    d8 = Button(p_window, width=1, height=1, bg='white', font=("Arial Bold", 6), command=u8)
    d8.place(x=155, y=104)
    p_all.append(d8)

    d9 = Button(p_window, width=1, height=1, bg='white', font=("Arial Bold", 6), command=u9)
    d9.place(x=170, y=104)
    p_all.append(d9)

    d10 = Button(p_window, width=1, height=1, bg='white', font=("Arial Bold", 6), command=u10)
    d10.place(x=185, y=104)
    p_all.append(d10)

    d11 = Button(p_window, width=1, height=1, bg='white', font=("Arial Bold", 6), command=u11)
    d11.place(x=200, y=104)
    p_all.append(d11)

    d12 = Button(p_window, width=1, height=1, bg='white', font=("Arial Bold", 6), command=u12)
    d12.place(x=215, y=104)
    p_all.append(d12)

    d13 = Button(p_window, width=1, height=1, bg='white', font=("Arial Bold", 6), command=u13)
    d13.place(x=230, y=104)
    p_all.append(d13)

    d14 = Button(p_window, width=1, height=1, bg='white', font=("Arial Bold", 6), command=u14)
    d14.place(x=245, y=104)
    p_all.append(d14)

    d15 = Button(p_window, width=1, height=1, bg='white', font=("Arial Bold", 6), command=u15)
    d15.place(x=260, y=104)
    p_all.append(d15)

    d16 = Button(p_window, width=1, height=1, bg='white', font=("Arial Bold", 6), command=u16)
    d16.place(x=275, y=104)
    p_all.append(d16)

    d17 = Button(p_window, width=1, height=1, bg='white', font=("Arial Bold", 6), command=u17)
    d17.place(x=290, y=104)
    p_all.append(d17)

    d18 = Button(p_window, width=1, height=1, bg='white', font=("Arial Bold", 6), command=u18)
    d18.place(x=305, y=104)
    p_all.append(d18)

    d19 = Button(p_window, width=1, height=1, bg='white', font=("Arial Bold", 6), command=u19)
    d19.place(x=320, y=104)
    p_all.append(d19)

    d20 = Button(p_window, width=1, height=1, bg='white', font=("Arial Bold", 6), command=u20)
    d20.place(x=335, y=104)
    p_all.append(d20)

    d21 = Button(p_window, width=1, height=1, bg='white', font=("Arial Bold", 6), command=u21)
    d21.place(x=350, y=104)
    p_all.append(d21)

    d22 = Button(p_window, width=1, height=1, bg='white', font=("Arial Bold", 6), command=u22)
    d22.place(x=365, y=104)
    p_all.append(d22)

    d23 = Button(p_window, width=1, height=1, bg='white', font=("Arial Bold", 6), command=u23)
    d23.place(x=380, y=104)
    p_all.append(d23)

    d24 = Button(p_window, width=1, height=1, bg='white', font=("Arial Bold", 6), command=u24)
    d24.place(x=395, y=104)
    p_all.append(d24)

    d25 = Button(p_window, width=1, height=1, bg='white', font=("Arial Bold", 6), command=u25)
    d25.place(x=410, y=104)
    p_all.append(d25)

    d26 = Button(p_window, width=1, height=1, bg='white', font=("Arial Bold", 6), command=u26)
    d26.place(x=425, y=104)
    p_all.append(d26)

    d27 = Button(p_window, width=1, height=1, bg='white', font=("Arial Bold", 6), command=u27)
    d27.place(x=440, y=104)
    p_all.append(d27)

    d28 = Button(p_window, width=1, height=1, bg='white', font=("Arial Bold", 6), command=u28)
    d28.place(x=455, y=104)
    p_all.append(d28)

    d29 = Button(p_window, width=1, height=1, bg='white', font=("Arial Bold", 6), command=u29)
    d29.place(x=470, y=104)
    p_all.append(d29)

    d30 = Button(p_window, width=1, height=1, bg='white', font=("Arial Bold", 6), command=u30)
    d30.place(x=485, y=104)
    p_all.append(d30)

    e1 = Button(p_window, width=1, height=1, bg='white', font=("Arial Bold", 6), command=v1)
    e1.place(x=50, y=122)
    p_all.append(e1)

    e2 = Button(p_window, width=1, height=1, bg='white', font=("Arial Bold", 6), command=v2)
    e2.place(x=65, y=122)
    p_all.append(e2)

    e3 = Button(p_window, width=1, height=1, bg='white', font=("Arial Bold", 6), command=v3)
    e3.place(x=80, y=122)
    p_all.append(e3)

    e4 = Button(p_window, width=1, height=1, bg='white', font=("Arial Bold", 6), command=v4)
    e4.place(x=95, y=122)
    p_all.append(e4)

    e5 = Button(p_window, width=1, height=1, bg='white', font=("Arial Bold", 6), command=v5)
    e5.place(x=110, y=122)
    p_all.append(e5)

    e6 = Button(p_window, width=1, height=1, bg='white', font=("Arial Bold", 6), command=v6)
    e6.place(x=125, y=122)
    p_all.append(e6)

    e7 = Button(p_window, width=1, height=1, bg='white', font=("Arial Bold", 6), command=v7)
    e7.place(x=140, y=122)
    p_all.append(e7)

    e8 = Button(p_window, width=1, height=1, bg='white', font=("Arial Bold", 6), command=v8)
    e8.place(x=155, y=122)
    p_all.append(e8)

    e9 = Button(p_window, width=1, height=1, bg='white', font=("Arial Bold", 6), command=v9)
    e9.place(x=170, y=122)
    p_all.append(e9)

    e10 = Button(p_window, width=1, height=1, bg='white', font=("Arial Bold", 6), command=v10)
    e10.place(x=185, y=122)
    p_all.append(e10)

    e11 = Button(p_window, width=1, height=1, bg='white', font=("Arial Bold", 6), command=v11)
    e11.place(x=200, y=122)
    p_all.append(e11)

    e12 = Button(p_window, width=1, height=1, bg='white', font=("Arial Bold", 6), command=v12)
    e12.place(x=215, y=122)
    p_all.append(e12)

    e13 = Button(p_window, width=1, height=1, bg='white', font=("Arial Bold", 6), command=v13)
    e13.place(x=230, y=122)
    p_all.append(e13)

    e14 = Button(p_window, width=1, height=1, bg='white', font=("Arial Bold", 6), command=v14)
    e14.place(x=245, y=122)
    p_all.append(e14)

    e15 = Button(p_window, width=1, height=1, bg='white', font=("Arial Bold", 6), command=v15)
    e15.place(x=260, y=122)
    p_all.append(e15)

    e16 = Button(p_window, width=1, height=1, bg='white', font=("Arial Bold", 6), command=v16)
    e16.place(x=275, y=122)
    p_all.append(e16)

    e17 = Button(p_window, width=1, height=1, bg='white', font=("Arial Bold", 6), command=v17)
    e17.place(x=290, y=122)
    p_all.append(e17)

    e18 = Button(p_window, width=1, height=1, bg='white', font=("Arial Bold", 6), command=v18)
    e18.place(x=305, y=122)
    p_all.append(e18)

    e19 = Button(p_window, width=1, height=1, bg='white', font=("Arial Bold", 6), command=v19)
    e19.place(x=320, y=122)
    p_all.append(e19)

    e20 = Button(p_window, width=1, height=1, bg='white', font=("Arial Bold", 6), command=v20)
    e20.place(x=335, y=122)
    p_all.append(e20)

    e21 = Button(p_window, width=1, height=1, bg='white', font=("Arial Bold", 6), command=v21)
    e21.place(x=350, y=122)
    p_all.append(e21)

    e22 = Button(p_window, width=1, height=1, bg='white', font=("Arial Bold", 6), command=v22)
    e22.place(x=365, y=122)
    p_all.append(e22)

    e23 = Button(p_window, width=1, height=1, bg='white', font=("Arial Bold", 6), command=v23)
    e23.place(x=380, y=122)
    p_all.append(e23)

    e24 = Button(p_window, width=1, height=1, bg='white', font=("Arial Bold", 6), command=v24)
    e24.place(x=395, y=122)
    p_all.append(e24)

    e25 = Button(p_window, width=1, height=1, bg='white', font=("Arial Bold", 6), command=v25)
    e25.place(x=410, y=122)
    p_all.append(e25)

    e26 = Button(p_window, width=1, height=1, bg='white', font=("Arial Bold", 6), command=v26)
    e26.place(x=425, y=122)
    p_all.append(e26)

    e27 = Button(p_window, width=1, height=1, bg='white', font=("Arial Bold", 6), command=v27)
    e27.place(x=440, y=122)
    p_all.append(e27)

    e28 = Button(p_window, width=1, height=1, bg='white', font=("Arial Bold", 6), command=v28)
    e28.place(x=455, y=122)
    p_all.append(e28)

    e29 = Button(p_window, width=1, height=1, bg='white', font=("Arial Bold", 6), command=v29)
    e29.place(x=470, y=122)
    p_all.append(e29)

    e30 = Button(p_window, width=1, height=1, bg='white', font=("Arial Bold", 6), command=v30)
    e30.place(x=485, y=122)
    p_all.append(e30)

    f1 = Button(p_window, width=1, height=1, bg='white', font=("Arial Bold", 6), command=w1)
    f1.place(x=50, y=140)
    p_all.append(f1)

    f2 = Button(p_window, width=1, height=1, bg='white', font=("Arial Bold", 6), command=w2)
    f2.place(x=65, y=140)
    p_all.append(f2)

    f3 = Button(p_window, width=1, height=1, bg='white', font=("Arial Bold", 6), command=w3)
    f3.place(x=80, y=140)
    p_all.append(f3)

    f4 = Button(p_window, width=1, height=1, bg='white', font=("Arial Bold", 6), command=w4)
    f4.place(x=95, y=140)
    p_all.append(f4)

    f5 = Button(p_window, width=1, height=1, bg='white', font=("Arial Bold", 6), command=w5)
    f5.place(x=110, y=140)
    p_all.append(f5)

    f6 = Button(p_window, width=1, height=1, bg='white', font=("Arial Bold", 6), command=w6)
    f6.place(x=125, y=140)
    p_all.append(f6)

    f7 = Button(p_window, width=1, height=1, bg='white', font=("Arial Bold", 6), command=w7)
    f7.place(x=140, y=140)
    p_all.append(f7)

    f8 = Button(p_window, width=1, height=1, bg='white', font=("Arial Bold", 6), command=w8)
    f8.place(x=155, y=140)
    p_all.append(f8)

    f9 = Button(p_window, width=1, height=1, bg='white', font=("Arial Bold", 6), command=w9)
    f9.place(x=170, y=140)
    p_all.append(f9)

    f10 = Button(p_window, width=1, height=1, bg='white', font=("Arial Bold", 6), command=w10)
    f10.place(x=185, y=140)
    p_all.append(f10)

    f11 = Button(p_window, width=1, height=1, bg='white', font=("Arial Bold", 6), command=w11)
    f11.place(x=200, y=140)
    p_all.append(f11)

    f12 = Button(p_window, width=1, height=1, bg='white', font=("Arial Bold", 6), command=w12)
    f12.place(x=215, y=140)
    p_all.append(f12)

    f13 = Button(p_window, width=1, height=1, bg='white', font=("Arial Bold", 6), command=w13)
    f13.place(x=230, y=140)
    p_all.append(f13)

    f14 = Button(p_window, width=1, height=1, bg='white', font=("Arial Bold", 6), command=w14)
    f14.place(x=245, y=140)
    p_all.append(f14)

    f15 = Button(p_window, width=1, height=1, bg='white', font=("Arial Bold", 6), command=w15)
    f15.place(x=260, y=140)
    p_all.append(f15)

    f16 = Button(p_window, width=1, height=1, bg='white', font=("Arial Bold", 6), command=w16)
    f16.place(x=275, y=140)
    p_all.append(f16)

    f17 = Button(p_window, width=1, height=1, bg='white', font=("Arial Bold", 6), command=w17)
    f17.place(x=290, y=140)
    p_all.append(f17)

    f18 = Button(p_window, width=1, height=1, bg='white', font=("Arial Bold", 6), command=w18)
    f18.place(x=305, y=140)
    p_all.append(f18)

    f19 = Button(p_window, width=1, height=1, bg='white', font=("Arial Bold", 6), command=w19)
    f19.place(x=320, y=140)
    p_all.append(f19)

    f20 = Button(p_window, width=1, height=1, bg='white', font=("Arial Bold", 6), command=w20)
    f20.place(x=335, y=140)
    p_all.append(f20)

    f21 = Button(p_window, width=1, height=1, bg='white', font=("Arial Bold", 6), command=w21)
    f21.place(x=350, y=140)
    p_all.append(f21)

    f22 = Button(p_window, width=1, height=1, bg='white', font=("Arial Bold", 6), command=w22)
    f22.place(x=365, y=140)
    p_all.append(f22)

    f23 = Button(p_window, width=1, height=1, bg='white', font=("Arial Bold", 6), command=w23)
    f23.place(x=380, y=140)
    p_all.append(f23)

    f24 = Button(p_window, width=1, height=1, bg='white', font=("Arial Bold", 6), command=w24)
    f24.place(x=395, y=140)
    p_all.append(f24)

    f25 = Button(p_window, width=1, height=1, bg='white', font=("Arial Bold", 6), command=w25)
    f25.place(x=410, y=140)
    p_all.append(f25)

    f26 = Button(p_window, width=1, height=1, bg='white', font=("Arial Bold", 6), command=w26)
    f26.place(x=425, y=140)
    p_all.append(f26)

    f27 = Button(p_window, width=1, height=1, bg='white', font=("Arial Bold", 6), command=w27)
    f27.place(x=440, y=140)
    p_all.append(f27)

    f28 = Button(p_window, width=1, height=1, bg='white', font=("Arial Bold", 6), command=w28)
    f28.place(x=455, y=140)
    p_all.append(f28)

    f29 = Button(p_window, width=1, height=1, bg='white', font=("Arial Bold", 6), command=w29)
    f29.place(x=470, y=140)
    p_all.append(f29)

    f30 = Button(p_window, width=1, height=1, bg='white', font=("Arial Bold", 6), command=w30)
    f30.place(x=485, y=140)
    p_all.append(f30)

    g1 = Button(p_window, width=1, height=1, bg='white', font=("Arial Bold", 6), command=x1)
    g1.place(x=50, y=158)
    p_all.append(g1)

    g2 = Button(p_window, width=1, height=1, bg='white', font=("Arial Bold", 6), command=x2)
    g2.place(x=65, y=158)
    p_all.append(g2)

    g3 = Button(p_window, width=1, height=1, bg='white', font=("Arial Bold", 6), command=x3)
    g3.place(x=80, y=158)
    p_all.append(g3)

    g4 = Button(p_window, width=1, height=1, bg='white', font=("Arial Bold", 6), command=x4)
    g4.place(x=95, y=158)
    p_all.append(g4)

    g5 = Button(p_window, width=1, height=1, bg='white', font=("Arial Bold", 6), command=x5)
    g5.place(x=110, y=158)
    p_all.append(g5)

    g6 = Button(p_window, width=1, height=1, bg='white', font=("Arial Bold", 6), command=x6)
    g6.place(x=125, y=158)
    p_all.append(g6)

    g7 = Button(p_window, width=1, height=1, bg='white', font=("Arial Bold", 6), command=x7)
    g7.place(x=140, y=158)
    p_all.append(g7)

    g8 = Button(p_window, width=1, height=1, bg='white', font=("Arial Bold", 6), command=x8)
    g8.place(x=155, y=158)
    p_all.append(g8)

    g9 = Button(p_window, width=1, height=1, bg='white', font=("Arial Bold", 6), command=x9)
    g9.place(x=170, y=158)
    p_all.append(g9)

    g10 = Button(p_window, width=1, height=1, bg='white', font=("Arial Bold", 6), command=x10)
    g10.place(x=185, y=158)
    p_all.append(g10)

    g11 = Button(p_window, width=1, height=1, bg='white', font=("Arial Bold", 6), command=x11)
    g11.place(x=200, y=158)
    p_all.append(g11)

    g12 = Button(p_window, width=1, height=1, bg='white', font=("Arial Bold", 6), command=x12)
    g12.place(x=215, y=158)
    p_all.append(g12)

    g13 = Button(p_window, width=1, height=1, bg='white', font=("Arial Bold", 6), command=x13)
    g13.place(x=230, y=158)
    p_all.append(g13)

    g14 = Button(p_window, width=1, height=1, bg='white', font=("Arial Bold", 6), command=x14)
    g14.place(x=245, y=158)
    p_all.append(g14)

    g15 = Button(p_window, width=1, height=1, bg='white', font=("Arial Bold", 6), command=x15)
    g15.place(x=260, y=158)
    p_all.append(g15)

    g16 = Button(p_window, width=1, height=1, bg='white', font=("Arial Bold", 6), command=x16)
    g16.place(x=275, y=158)
    p_all.append(g16)

    g17 = Button(p_window, width=1, height=1, bg='white', font=("Arial Bold", 6), command=x17)
    g17.place(x=290, y=158)
    p_all.append(g17)

    g18 = Button(p_window, width=1, height=1, bg='white', font=("Arial Bold", 6), command=x18)
    g18.place(x=305, y=158)
    p_all.append(g18)

    g19 = Button(p_window, width=1, height=1, bg='white', font=("Arial Bold", 6), command=x19)
    g19.place(x=320, y=158)
    p_all.append(g19)

    g20 = Button(p_window, width=1, height=1, bg='white', font=("Arial Bold", 6), command=x20)
    g20.place(x=335, y=158)
    p_all.append(g20)

    g21 = Button(p_window, width=1, height=1, bg='white', font=("Arial Bold", 6), command=x21)
    g21.place(x=350, y=158)
    p_all.append(g21)

    g22 = Button(p_window, width=1, height=1, bg='white', font=("Arial Bold", 6), command=x22)
    g22.place(x=365, y=158)
    p_all.append(g22)

    g23 = Button(p_window, width=1, height=1, bg='white', font=("Arial Bold", 6), command=x23)
    g23.place(x=380, y=158)
    p_all.append(g23)

    g24 = Button(p_window, width=1, height=1, bg='white', font=("Arial Bold", 6), command=x24)
    g24.place(x=395, y=158)
    p_all.append(g24)

    g25 = Button(p_window, width=1, height=1, bg='white', font=("Arial Bold", 6), command=x25)
    g25.place(x=410, y=158)
    p_all.append(g25)

    g26 = Button(p_window, width=1, height=1, bg='white', font=("Arial Bold", 6), command=x26)
    g26.place(x=425, y=158)
    p_all.append(g26)

    g27 = Button(p_window, width=1, height=1, bg='white', font=("Arial Bold", 6), command=x27)
    g27.place(x=440, y=158)
    p_all.append(g27)

    g28 = Button(p_window, width=1, height=1, bg='white', font=("Arial Bold", 6), command=x28)
    g28.place(x=455, y=158)
    p_all.append(g28)

    g29 = Button(p_window, width=1, height=1, bg='white', font=("Arial Bold", 6), command=x29)
    g29.place(x=470, y=158)
    p_all.append(g29)

    g30 = Button(p_window, width=1, height=1, bg='white', font=("Arial Bold", 6), command=x30)
    g30.place(x=485, y=158)
    p_all.append(g30)

    h1 = Button(p_window, width=1, height=1, bg='white', font=("Arial Bold", 6), command=y1)
    h1.place(x=50, y=176)
    p_all.append(h1)

    h2 = Button(p_window, width=1, height=1, bg='white', font=("Arial Bold", 6), command=y2)
    h2.place(x=65, y=176)
    p_all.append(h2)

    h3 = Button(p_window, width=1, height=1, bg='white', font=("Arial Bold", 6), command=y3)
    h3.place(x=80, y=176)
    p_all.append(h3)

    h4 = Button(p_window, width=1, height=1, bg='white', font=("Arial Bold", 6), command=y4)
    h4.place(x=95, y=176)
    p_all.append(h4)

    h5 = Button(p_window, width=1, height=1, bg='white', font=("Arial Bold", 6), command=y5)
    h5.place(x=110, y=176)
    p_all.append(h5)

    h6 = Button(p_window, width=1, height=1, bg='white', font=("Arial Bold", 6), command=y6)
    h6.place(x=125, y=176)
    p_all.append(h6)

    h7 = Button(p_window, width=1, height=1, bg='white', font=("Arial Bold", 6), command=y7)
    h7.place(x=140, y=176)
    p_all.append(h7)

    h8 = Button(p_window, width=1, height=1, bg='white', font=("Arial Bold", 6), command=y8)
    h8.place(x=155, y=176)
    p_all.append(h8)

    h9 = Button(p_window, width=1, height=1, bg='white', font=("Arial Bold", 6), command=y9)
    h9.place(x=170, y=176)
    p_all.append(h9)

    h10 = Button(p_window, width=1, height=1, bg='white', font=("Arial Bold", 6), command=y10)
    h10.place(x=185, y=176)
    p_all.append(h10)

    h11 = Button(p_window, width=1, height=1, bg='white', font=("Arial Bold", 6), command=y11)
    h11.place(x=200, y=176)
    p_all.append(h11)

    h12 = Button(p_window, width=1, height=1, bg='white', font=("Arial Bold", 6), command=y12)
    h12.place(x=215, y=176)
    p_all.append(h12)

    h13 = Button(p_window, width=1, height=1, bg='white', font=("Arial Bold", 6), command=y13)
    h13.place(x=230, y=176)
    p_all.append(h13)

    h14 = Button(p_window, width=1, height=1, bg='white', font=("Arial Bold", 6), command=y14)
    h14.place(x=245, y=176)
    p_all.append(h14)

    h15 = Button(p_window, width=1, height=1, bg='white', font=("Arial Bold", 6), command=y15)
    h15.place(x=260, y=176)
    p_all.append(h15)

    h16 = Button(p_window, width=1, height=1, bg='white', font=("Arial Bold", 6), command=y16)
    h16.place(x=275, y=176)
    p_all.append(h16)

    h17 = Button(p_window, width=1, height=1, bg='white', font=("Arial Bold", 6), command=y17)
    h17.place(x=290, y=176)
    p_all.append(h17)

    h18 = Button(p_window, width=1, height=1, bg='white', font=("Arial Bold", 6), command=y18)
    h18.place(x=305, y=176)
    p_all.append(h18)

    h19 = Button(p_window, width=1, height=1, bg='white', font=("Arial Bold", 6), command=y19)
    h19.place(x=320, y=176)
    p_all.append(h19)

    h20 = Button(p_window, width=1, height=1, bg='white', font=("Arial Bold", 6), command=y20)
    h20.place(x=335, y=176)
    p_all.append(h20)

    h21 = Button(p_window, width=1, height=1, bg='white', font=("Arial Bold", 6), command=y21)
    h21.place(x=350, y=176)
    p_all.append(h21)

    h22 = Button(p_window, width=1, height=1, bg='white', font=("Arial Bold", 6), command=y22)
    h22.place(x=365, y=176)
    p_all.append(h22)

    h23 = Button(p_window, width=1, height=1, bg='white', font=("Arial Bold", 6), command=y23)
    h23.place(x=380, y=176)
    p_all.append(h23)

    h24 = Button(p_window, width=1, height=1, bg='white', font=("Arial Bold", 6), command=y24)
    h24.place(x=395, y=176)
    p_all.append(h24)

    h25 = Button(p_window, width=1, height=1, bg='white', font=("Arial Bold", 6), command=y25)
    h25.place(x=410, y=176)
    p_all.append(h25)

    h26 = Button(p_window, width=1, height=1, bg='white', font=("Arial Bold", 6), command=y26)
    h26.place(x=425, y=176)
    p_all.append(h26)

    h27 = Button(p_window, width=1, height=1, bg='white', font=("Arial Bold", 6), command=y27)
    h27.place(x=440, y=176)
    p_all.append(h27)

    h28 = Button(p_window, width=1, height=1, bg='white', font=("Arial Bold", 6), command=y28)
    h28.place(x=455, y=176)
    p_all.append(h28)

    h29 = Button(p_window, width=1, height=1, bg='white', font=("Arial Bold", 6), command=y29)
    h29.place(x=470, y=176)
    p_all.append(h29)

    h30 = Button(p_window, width=1, height=1, bg='white', font=("Arial Bold", 6), command=y30)
    h30.place(x=485, y=176)
    p_all.append(h30)

    p_save_button = Button(p_window, text='Сохранить', bg='#9be0b4', width=10, font=('Times New Roman', 16),
                           command=p_save)
    p_save_button.place(x=50, y=220)

    p_delete_button = Button(p_window, text='Удалить', bg='#e69b93', width=10, font=('Times New Roman', 16),
                             command=p_delete)
    p_delete_button.place(x=210, y=220)

    p_open_button = Button(p_window, text='Открыть', bg='#e0dc9b', width=10, font=('Times New Roman', 16),
                           command=p_open)
    p_open_button.place(x=370, y=220)

    p_off = Button(p_window, text='⌂', font=('Arial Bold', 15), width=2, height=1, bg='black', fg='white',
                   command=p_to_home)
    p_off.place(x=0, y=5)
    ToolTip(p_off, 'На главную...')

    p_window.pack()
