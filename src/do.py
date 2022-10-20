from src.homex import *
from src.functions import *
from src.init import m, root


def start():
    text_1 = '''
    Вас приветствуют разработчики MihaSoft! Для корректного продолжения работы
    программы необходимо разрешение на создание системных папок на диске C:
    '''

    text_2 = '''
    На диске C: будет создана папка MihaSoft Files, в которой будут 
    размещаться новые папки и файлы, создаваемые в процессе работы программы
    '''

    def sss_exit():
        root.quit()

    def sss_welcome():
        os.mkdir('C:/MihaSoft Files')
        well_label.destroy()
        well_button.destroy()
        bye_button.destroy()
        m.window.configure(width=788, height=m.abs_height)
        homes()
        center_window(root, 678, m.abs_height)

    if not os.path.exists('C:/MihaSoft Files'):
        center_window(root, 500, 100)
        m.window.configure(width=500, height=100)
        root.title('Добро пожаловать!')
        root.minsize(500, 100)

        well_label = Label(m.window, text=text_1)
        well_label.place(x=5, y=5)

        well_button = Button(m.window, text='РАЗРЕШИТЬ', font=('Times New Roman', 10), width=13, command=sss_welcome)
        well_button.place(x=230, y=60)
        ToolTip(well_button, text_2)

        bye_button = Button(m.window, text='ОТМЕНА', font=('Times New Roman', 10), width=13, command=sss_exit)
        bye_button.place(x=350, y=60)

    else:
        def do_it():
            if os.path.exists('C:/MihaSoft Files/AnimationFlagFile.miha') and root.winfo_screenheight() >= 730:
                LoadingLine()
            if os.path.exists('C:/MihaSoft Files/SoundFlagFile.miha'):
                Music()

            homes()
            HolidayWarningsDo()
            YourWarningsDo()
            check_update()

        if os.path.exists('C:/MihaSoft Files/AnimationFlagFile.miha') and root.winfo_screenheight() >= 770:
            root.after(4000, do_it)
        else:
            do_it()


def main():
    if root.winfo_screenheight() < 820:
        m.abs_height = 350
    else:
        m.abs_height = 690

    if os.path.exists('C:/MihaSoft Files') and os.path.exists('C:/MihaSoft Files/AnimationFlagFile.miha'):
        root.attributes('-topmost', 'true')

        def hello_end():
            root.overrideredirect(False)
            root.configure(bg=root_c)
            m_img_label.destroy()

        root.overrideredirect(True)
        root_c = root['background']
        root.configure(bg='red')
        center_window(root, 583, 404)
        m_img_label = Label(root)
        m_img_obj = Image.open('images/image-m.png')
        m_img_label.image = ImageTk.PhotoImage(m_img_obj)
        m_img_label['image'] = m_img_label.image
        m_img_label.pack()
        root.after(4000, hello_end)

    m.window = Frame(root, width=788, height=m.abs_height)
    m.window.pack(expand=1)
    start()
    root.mainloop()
