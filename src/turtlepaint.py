from turtle import *
from time import sleep
from autopy.bitmap import capture_screen
from tkinter.filedialog import asksaveasfile
from tkinter import colorchooser

from src.functions import *
from src.init import m, root
from src.homex import *


def TurtlePaint():
    def tp_help():
        def tp_help_ok():
            tp.help_window.destroy()

        def tp_create_help_window():
            tp.help_window = Toplevel()
            center_window(tp.help_window, 470, 190)
            tp.help_window.resizable(False, False)
            tp.help_window.title('TurtlePaint - справка')

            paint_help_text = '''
При опущенном пере:
Левая кнопка мыши - провести линию;
Правая кнопка мыши - закрасить последнюю начертанную фигуру,
поднять перо.

При поднятом пере:
Левая кнопка мыши - переместить перо;
Правая кнопка мыши - опустить перо.
                        '''
            paint_help_label = Label(tp.help_window, text=paint_help_text)
            paint_help_label.pack()

            tp_help_button = Button(tp.help_window, text='ОK', bg='#b8b8b8', command=tp_help_ok, width=10)
            tp_help_button.place(x=335, y=150)

        try:
            tp.help_window.resizable(False, False)

        except AttributeError:
            tp_create_help_window()

        except TclError:
            tp_create_help_window()

    def paint_save():
        paint_window.setup(width=1.0, height=1.0)
        root.state('iconic')
        sleep(0.3)
        paint_image = capture_screen()
        sleep(0.3)
        root.state('normal')
        paint_window.setup(800, 600)
        paint_file = asksaveasfile(title='Сохранить файл', defaultextension='.png',
                                   filetypes=(('PNG file', '*.png'), ('All Files', '*.*')))
        if paint_file:
            paint_image.save(paint_file.name)

    def paint_destroy():
        try:
            paint_window.bye()
        finally:
            try:
                tp.help_window.destroy()
            except AttributeError:
                pass

            paint_off.destroy()
            paint_save_button.destroy()
            paint_help_button.destroy()
            paint_color_button.destroy()
            paint_label.destroy()
            homes()
            m.window.configure(width=788, height=m.abs_height)
            center_window(root, 678, m.abs_height)

    def tp_choose_color():
        tp_colorchoose_window = colorchooser.askcolor()
        tp.now_color = tp_colorchoose_window[1]
        paint_main()
        up()
        paint_label.configure(text='Перо поднято...')
        paint_color_button.configure(bg=str(tp.now_color))

    root.geometry('530x80+0+0')
    m.window.configure(width=520, height=100)
    root.title('TurtlePaint')
    root.minsize(520, 100)

    paint_help_button = Button(m.window, text='СПРАВКА', bg='#b8b8b8', font=('Arial Bold', 12),
                               command=tp_help)
    paint_help_button.place(x=60, y=10)

    paint_save_button = Button(m.window, text='СОХРАНИТЬ РИСУНОК', bg='#93e6a8', font=('Arial Bold', 12),
                               command=paint_save)
    paint_save_button.place(x=160, y=10)

    paint_color_button = Button(m.window, text='ВЫБРАТЬ ЦВЕТ', bg='white', font=('Arial Bold', 12),
                                command=tp_choose_color)
    paint_color_button.place(x=360, y=10)

    paint_label = Label(m.window, text='Перо поднято...')
    paint_label.place(x=60, y=50)

    paint_off = Button(m.window, text='⌂', font=('Arial Bold', 15), width=2, height=1, bg='black', fg='white',
                       command=paint_destroy)
    paint_off.place(x=0, y=5)
    ToolTip(paint_off, 'На главную...')

    TurtleScreen._RUNNING = True
    tp = TurtlePaintGlobal()

    def paint_switchupdown(xx=0.0, yy=0.0):
        if pen()['pendown']:
            end_fill()
            up()
            paint_label.configure(text='Перо поднято...')
        else:
            down()
            begin_fill()
            paint_label.configure(text='Перо опущено...')
        return xx, yy

    def paint_main():
        shape('circle')
        resizemode('user')
        shapesize(.5)
        width(3)
        tp.colors = ['red', 'green', 'blue', 'yellow', 'grey', 'black']
        color(tp.now_color)
        paint_switchupdown()
        onscreenclick(goto, 1)
        onscreenclick(paint_switchupdown, 3)

    paint_window = Screen()
    paint_window.title('TurtlePaint')
    paint_window.setup(800, 600)

    paint_main()
