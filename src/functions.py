import datetime
import requests
from numpy import load
from winsound import Beep
from webbrowser import open_new

from src.center import center_window
from src.classes import *
from src.constants import VERSION
from src.init import m, root


def LoadingLine():
    lola = LoadingLineGlobals()

    lola.line_height = 1
    lola.logo_size = 1

    def LoadingLineCycle():
        line_1.configure(height=lola.line_height)
        line_2.configure(height=lola.line_height)
        lola.line_height += 1
        r1.configure(font=('Arial Bold', lola.logo_size))
        lola.logo_size += 9

    def destroying():
        line_1.destroy()
        line_2.destroy()

    line_1 = Label(m.window, height=1, width=8, bg='red')
    line_1.place(x=20, y=20)
    line_2 = Label(m.window, height=1, width=8, bg='red')
    line_2.place(x=595, y=20)

    root.title('MihaSoft ' + VERSION)
    center_window(root, 678, 730)
    root.minsize(678, 730)

    r1 = Label(m.window, text='Ⓜ', font=('Arial Bold', 1), fg='red')
    r1.place(x=160, y=0)

    for i in range(1, 30):
        m.window.after(20, LoadingLineCycle())
        m.window.update()

    line_1.configure(bg='green')
    line_2.configure(bg='green')
    m.window.update()
    m.window.after(800, destroying())
    r1.destroy()
    root.attributes('-topmost', 'false')


def YourWarningsDo():
    if not os.path.exists('C:/MihaSoft Files/YW Files'):
        os.mkdir('C:/MihaSoft Files/YW Files')
    now = datetime.datetime.now()

    for i in range(len(os.listdir('C:/MihaSoft Files/YW Files'))):
        if os.listdir('C:/MihaSoft Files/YW Files')[i] == (str(now.day) + '.' + str(now.month) + '.npy'):
            yw_data = load('C:/MihaSoft Files/YW Files/' + os.listdir('C:/MihaSoft Files/YW Files')[i])

            yw_window = Toplevel()
            yw_window.attributes('-topmost', 'true')
            center_window(yw_window, 435, 360)
            yw_window.title(os.listdir('C:/MihaSoft Files/YW Files')[i] + ': Уведомление!')

            yw_message = Text(yw_window, font=('Arial Bold', 20), fg='red', width=28, height=3)
            yw_message.place(x=5, y=255)

            yw_message.insert(1.0, yw_data[2], 'center')
            yw_message.configure(state=DISABLED)

            yw_logo = Label(yw_window, text='Ⓜ', font=('Arial Bold', 150), fg='green')
            yw_logo.place(x=120, y=5)


def HolidayWarningsDo():
    now = datetime.datetime.now()

    def okno(text):
        hw_window = Toplevel()
        hw_window.attributes('-topmost', 'true')
        center_window(hw_window, 440, 330)
        hw_window.title(str(now))

        hw_do_message = Label(hw_window, text=('ПОЗДРАВЛЯЕМ!!!\n' + text), font=('Times New Roman', 20), fg='red')
        hw_do_message.pack(side=BOTTOM)

        hw_do_logo = Label(hw_window, text='Ⓜ', font=("Arial Bold", 150), fg='red')
        hw_do_logo.pack()

    if os.path.exists('C:/MihaSoft Files/FlagHW.miha'):

        if now.day == 1 and now.month == 1:
            okno('Сегодня наступил новый\n    ' + str(now.year) + ' год!')

        if now.day == 7 and now.month == 1:
            okno('Сегодня отмечается\n      Рождество Христово! ')

        if now.day == 12 and now.month == 1:
            okno('Сегодня отмечается День\n Работника прокуратуры РФ!')

        if now.day == 13 and now.month == 1:
            okno('Сегодня День Российской\n печати!')

        if now.day == 14 and now.month == 1:
            okno('Сегодня День\n Трубопроводных войск!')

        if now.day == 21 and now.month == 1:
            okno('Сегодня День\n Инженерных войск!')

        if now.day == 25 and now.month == 1:
            okno('Сегодня День\n Российского студенчества!')

        if now.day == 27 and now.month == 1:
            okno('Сегодня День Снятия\n блокады Ленинграда!')

        if now.day == 2 and now.month == 2:
            okno('Сегодня День победы\n в Сталинградской битве!')

        if now.day == 8 and now.month == 2:
            okno('Сегодня День\n Российской науки!')

        if now.day == 9 and now.month == 2:
            okno('Сегодня День Работника\n гражданской авиации!')

        if now.day == 10 and now.month == 2:
            okno('Сегодня День\n Дипломатического работника!')

        if now.day == 15 and now.month == 2:
            okno('Сегодня День Памяти\n воинов-интернационалистов!')

        if now.day == 17 and now.month == 2:
            okno('Сегодня День Российских\n студенческих отрядов!')

        if now.day == 23 and now.month == 2:
            okno('Сегодня День\n Защитника Отечества!')

        if now.day == 24 and now.month == 2:
            okno('Сегодня день, когда\n Земля остановилась...')

        if now.day == 27 and now.month == 2:
            okno('Сегодня День Сил\n специальных операций!')

        if now.day == 1 and now.month == 3:
            okno('Сегодня Всемирный\n день Гражданской обороны!')

        if now.day == 8 and now.month == 3:
            okno('Сегодня Международный\n Женский день!')

        if now.day == 11 and now.month == 3:
            okno('Сегодня День\n Работников наркоконтроля!')

        if now.day == 12 and now.month == 3:
            okno('Сегодня День работников\n уголовно-исполнительной системы!')

        if now.day == 18 and now.month == 3:
            okno('Сегодня День\n Воссоединения Крыма и России!')

        if now.day == 19 and now.month == 3:
            okno('Сегодня День \nМоряка-подводника!')

        if now.day == 23 and now.month == 3:
            okno('Сегодня День Гидрометеоролога!')

        if now.day == 25 and now.month == 3:
            okno('Сегодня День\n Работника культуры России!')

        if now.day == 27 and now.month == 3:
            okno('Сегодня День Войск\n национальной гвардии РФ!')

        if now.day == 29 and now.month == 3:
            okno('Сегодня День Специалиста\n юридической службы!')

        if now.day == 1 and now.month == 4:
            okno('Сегодня День Смеха!')

        if now.day == 2 and now.month == 4:
            okno('Сегодня День Единения народов!')

        if now.day == 8 and now.month == 4:
            okno('Сегодня День\n Сотрудников военкоматов!')

        if now.day == 12 and now.month == 4:
            okno('Сегодня День Космонавтики!')

        if now.day == 15 and now.month == 4:
            okno('Сегодня День специалиста по\n радиоэлектронной борьбе!')

        if now.day == 18 and now.month == 4:
            okno('Сегодня День Победы\n на Чудском озере!')

        if now.day == 19 and now.month == 4:
            okno('Сегодня День\n Российской полиграфии!')

        if now.day == 21 and now.month == 4:
            okno('Сегодня День\n Местного самоуправления!')

        if now.day == 26 and now.month == 4:
            okno('Сегодня День Нотариата!')

        if now.day == 27 and now.month == 4:
            okno('Сегодня День\n Российского парламентаризма!')

        if now.day == 28 and now.month == 4:
            okno('Сегодня Международный\n день Охраны Труда!')

        if now.day == 30 and now.month == 4:
            okno('Сегодня День Пожарной охраны!')

        if now.day == 1 and now.month == 5:
            okno('Сегодня Праздник\n Весны и Труда!')

        if now.day == 7 and now.month == 5:
            okno('Сегодня День Радио!')

        if now.day == 9 and now.month == 5:
            okno('Сегодня День Победы!')

        if now.day == 21 and now.month == 5:
            okno('Сегодня День Полярника!')

        if now.day == 24 and now.month == 5:
            okno('Сегодня День Славянской\n письменности и культуры!')

        if now.day == 25 and now.month == 5:
            okno('Сегодня День Филолога!')

        if now.day == 26 and now.month == 5:
            okno('Сегодня День\n Российского предпринимательства!')

        if now.day == 27 and now.month == 5:
            okno('Сегодня Общероссийский\n день библиотек!')

        if now.day == 28 and now.month == 5:
            okno('Сегодня День Пограничника!')

        if now.day == 29 and now.month == 5:
            okno('Сегодня День\n Военного автомобилиста!')

        if now.day == 31 and now.month == 5:
            okno('Сегодня День\n Российской адвокатуры!')

        if now.day == 1 and now.month == 6:
            okno('Сегодня Международный День\n защиты детей!')

        if now.day == 2 and now.month == 6:
            okno('Сегодня День Спутникового\n мониторинга и навигации!')

        if now.day == 5 and now.month == 6:
            okno('Сегодня День Эколога!')

        if now.day == 6 and now.month == 6:
            okno('Сегодня День Русского языка!')

        if now.day == 8 and now.month == 6:
            okno('Сегодня День\n Социального работника!')

        if now.day == 12 and now.month == 6:
            okno('Сегодня День России!')

        if now.day == 14 and now.month == 6:
            okno('Сегодня День Работников\n миграционной службы!')

        if now.day == 18 and now.month == 6:
            okno('Сегодня День Службы\n военных сообщений!')

        if now.day == 25 and now.month == 6:
            okno('Сегодня День Работника\n статистики!')

        if now.day == 27 and now.month == 6:
            okno('Сегодня День Молодёжи!')

        if now.day == 29 and now.month == 6:
            okno('Сегодня День Партизан\n и подпольщиков!')

        if now.day == 30 and now.month == 6:
            okno('Сегодня День Экономиста!')

        if now.day == 3 and now.month == 7:
            okno('Сегодня День ГИБДД!')

        if now.day == 7 and now.month == 7:
            okno('Сегодня День Победы\n в Чесменском сражении!')

        if now.day == 8 and now.month == 7:
            okno('Сегодня День Семьи, любви и\n верности!')

        if now.day == 10 and now.month == 7:
            okno('Сегодня День Победы\n в Полтавской битве!')

        if now.day == 17 and now.month == 7:
            okno('Сегодня День Этнографа')

        if now.day == 25 and now.month == 7:
            okno('Сегодня День Следователя!')

        if now.day == 28 and now.month == 7:
            okno('Сегодня День Крещения Руси!')

        if now.day == 31 and now.month == 7:
            okno('Сегодня День ВМФ России!')

        if now.day == 1 and now.month == 8:
            okno('Сегодня День Тыла ВС РФ!')

        if now.day == 2 and now.month == 8:
            okno('Сегодня День ВДВ!')

        if now.day == 6 and now.month == 8:
            okno('Сегодня День\n Железнодорожных войск!')

        if now.day == 9 and now.month == 8:
            okno('Сегодня День Победы\n в Гангутском сражении!')

        if now.day == 12 and now.month == 8:
            okno('Сегодня День\n Военно-воздушных сил!')

        if now.day == 15 and now.month == 8:
            okno('Сегодня День Археолога!')

        if now.day == 18 and now.month == 8:
            okno('Сегодня День Географа!')

        if now.day == 22 and now.month == 8:
            okno('Сегодня День\n Государственного флага РФ!')

        if now.day == 23 and now.month == 8:
            okno('Сегодня День \nПобеды в Курской битве!')

        if now.day == 27 and now.month == 8:
            okno('Сегодня День Кино!')

        if now.day == 31 and now.month == 8:
            okno('Сегодня День\n Ветеринарного Работника!')

        if now.day == 1 and now.month == 9:
            okno('Сегодня День Знаний!')

        if now.day == 2 and now.month == 9:
            okno('Сегодня День \nРоссийской гвардии!')

        if now.day == 3 and now.month == 9:
            okno('Сегодня День\n Окончания Второй Мировой войны!')

        if now.day == 4 and now.month == 9:
            okno('Сегодня День Специалиста\n по ядерному обеспечению!')

        if now.day == 8 and now.month == 9:
            okno('Сегодня День\n Бородинского сражения!')

        if now.day == 9 and now.month == 9:
            okno('Сегодня День Тестировщика!')

        if now.day == 11 and now.month == 9:
            okno('Сегодня День\n Победы у мыса Тендра!')

        if now.day == 13 and now.month == 9:
            okno('Сегодня День Программиста!')

        if now.day == 19 and now.month == 9:
            okno('Сегодня День Оружейника!')

        if now.day == 21 and now.month == 9:
            okno('Сегодня День\n Победы в Куликовской битве!')

        if now.day == 24 and now.month == 9:
            okno('Сегодня День\n Системного аналитика!')

        if now.day == 27 and now.month == 9:
            okno('Сегодня Всемирный\n день Туризма!')

        if now.day == 28 and now.month == 9:
            okno('Сегодня День Работника\n атомной промышленности!')

        if now.day == 30 and now.month == 9:
            okno('Сегодня День Переводчика!')

        if now.day == 1 and now.month == 10:
            okno('Сегодня День Сухопутных войск!')

        if now.day == 4 and now.month == 10:
            okno('Сегодня День Космических войск!')

        if now.day == 5 and now.month == 10:
            okno('Сегодня День Учителя!')

        if now.day == 9 and now.month == 10:
            okno('День Победы в Битве за Кавказ!')

        if now.day == 19 and now.month == 10:
            okno('Сегодня Всероссийский\n день Лицеиста!')

        if now.day == 20 and now.month == 10:
            okno('Сегодня День\n Военного связиста!')

        if now.day == 22 and now.month == 10:
            okno('Сегодня День \nФинансово-экономической службы!')

        if now.day == 23 and now.month == 10:
            okno('Сегодня День Работников рекламы!')

        if now.day == 25 and now.month == 10:
            okno('Сегодня День Таможенника РФ!')

        if now.day == 29 and now.month == 10:
            okno('Сегодня День\n Вневедомственной охраны!')

        if now.day == 30 and now.month == 10:
            okno('Сегодня День Инженера-механика!')

        if now.day == 31 and now.month == 10:
            okno('Сегодня День\n Работника СИЗО и тюрем!')

        if now.day == 1 and now.month == 11:
            okno('Сегодня День\n Судебного пристава РФ!')

        if now.day == 4 and now.month == 11:
            okno('Сегодня День Народного Единства!')

        if now.day == 5 and now.month == 11:
            okno('Сегодня День Военного разведчика!')

        if now.day == 7 and now.month == 11:
            okno('Сегодня Годовщина\n Великой Октябрьской революции!')

        if now.day == 9 and now.month == 11:
            okno('Сегодня День Специального\n отряда быстрого реагирования!')

        if now.day == 10 and now.month == 11:
            okno('Сегодня День Сотрудника ОВД РФ!')

        if now.day == 11 and now.month == 11:
            okno('Сегодня День Экономиста!')

        if now.day == 13 and now.month == 11:
            okno('Сегодня День войск РХБЗ!')

        if now.day == 14 and now.month == 11:
            okno('Сегодня День Социолога!')

        if now.day == 19 and now.month == 11:
            okno('Сегодня Международный Мужской день')

        if now.day == 20 and now.month == 11:
            okno('Сегодня День Работника транспорта!')

        if now.day == 21 and now.month == 11:
            okno('Сегодня День Работника\n налоговых органов РФ!')

        if now.day == 27 and now.month == 11:
            okno('Сегодня День Морской пехоты!')

        if now.day == 30 and now.month == 11:
            okno('Сегодня Международный\n день Защиты информации!')

        if now.day == 1 and now.month == 12:
            okno('Сегодня День Победы \nв Синопском сражении!')

        if now.day == 3 and now.month == 12:
            okno('Сегодня День Неизвестного солдата!')

        if now.day == 5 and now.month == 12:
            okno('Сегодня День Волонтёра!')

        if now.day == 9 and now.month == 12:
            okno('Сегодня День Героев Отечества!')

        if now.day == 12 and now.month == 12:
            okno('Сегодня День Конституции РФ!')

        if now.day == 17 and now.month == 12:
            okno('Сегодня День Ракетных\n войск стратегического назначения!')

        if now.day == 18 and now.month == 12:
            okno('Сегодня День Работников ЗАГС!')

        if now.day == 19 and now.month == 12:
            okno('Сегодня День Работников\n военной контрразведки РФ!')

        if now.day == 20 and now.month == 12:
            okno('Сегодня День Работников\n органов безопасности РФ!')

        if now.day == 22 and now.month == 12:
            okno('Сегодня День Энергетика!')

        if now.day == 24 and now.month == 12:
            okno('Сегодня День Взятия\n турецкой крепости Измаил!')

        if now.day == 27 and now.month == 12:
            okno('Сегодня День Спасателя РФ!')

        if now.day == 31 and now.month == 12:
            okno('Сегодня Последний день ' + str(now.year) + ' года!')


def Music():
    Beep(300, 900)
    for i in range(1, 4):
        m.window.after(50, Beep(300, 100))


def check_update():
    def cu_abort():
        fl = open('C:/MihaSoft Files/UpdateFlag.miha', 'w')
        fl.close()
        cu_window.destroy()

    def cu_open():
        cu_window.destroy()
        open_new('https://mihasoft.glitch.me/#zov')

    if not os.path.exists('C:/MihaSoft Files/UpdateFlag.miha'):
        try:
            cu_response = requests.get('https://mihasoft.glitch.me/vers.txt')
            if cu_response.text != VERSION:
                cu_window = Toplevel()
                center_window(cu_window, 410, 150)
                cu_window.resizable(False, False)
                cu_window.title('Обновление')

                cu_label = Label(cu_window,
                                 text='''Внимание! Ваша версия MihaSoft устарела. 
Вы можете скачать последнюю версию {}
на официальном сайте.'''.format(cu_response.text), font=('Times New Roman', 13), fg='red')
                cu_label.pack()

                site_button = Button(cu_window, text='Перейти на сайт', bg='green', fg='white', width=18,
                                     font=('Times New Roman', 12), command=cu_open)
                site_button.place(x=25, y=70)

                ab_button = Button(cu_window, text='Больше не показывать', bg='#b8b8b8', width=18,
                                   font=('Times New Roman', 12), command=cu_abort)
                ab_button.place(x=215, y=70)
        except requests.exceptions.ConnectionError:
            pass


def blackout(button):
    """
    Затемнение кнопок главной страницы
    при наведении на них курсора.
    """

    bg = button['background']
    fg = button['foreground']

    def on_enter(e):
        button['background'] = '#6e6e6e'
        button['foreground'] = 'white'
        return e

    def on_leave(e):
        button['background'] = bg
        button['foreground'] = fg
        return e

    button.bind('<Enter>', on_enter)
    button.bind('<Leave>', on_leave)


def help_show(h_title, message, url):
    def help_destroy():
        m.help_window.destroy()

    def help_more():
        open_new(url)
        m.help_window.destroy()

    def create_help_window():
        m.help_window = Toplevel()
        center_window(m.help_window, 500, 300)
        m.help_window.title(h_title)
        m.help_window.resizable(False, False)

        help_text = Text(m.help_window, width=60, height=12)
        help_text.insert(1.0, message)
        help_text.configure(state=DISABLED)
        help_text.place(x=5, y=5)

        h_exit_but = Button(m.help_window, text='OK', bg='#b8b8b8', width=12,
                            font=('Times New Roman', 12), command=help_destroy)
        h_exit_but.place(x=10, y=250)

        h_more_but = Button(m.help_window, text='ПОДРОБНЕЕ', bg='green', fg='white', width=12,
                            font=('Times New Roman', 12), command=help_more)
        h_more_but.place(x=370, y=250)

    try:
        m.help_window.resizable(False, False)

    except AttributeError:
        create_help_window()

    except TclError:
        create_help_window()


def about_yourwarnings(her):
    help_show('YourWarnings', 'Приложение для создания пользовательских уведомлений. Сохраняет текст и дату \
уведомления в файл и автоматически выводит уведомление при запуске MihaSoft в указанную дату.',
              'https://mihasoft.glitch.me/yw.html')
    return her


def about_accountmanager(her):
    help_show('AccountManager', 'Приложение для генерации паролей, сохранения данных о регистрации на конкретном '
                                'сервисе (логина и пароля), их демонстрации.',
              'https://mihasoft.glitch.me/')
    return her


def about_windowmanager(her):
    help_show('WindowManager', 'Приложение для создание кастомизированных окон с надписями. \
Поддерживает сохранение, редактирование, удаление и демонстрацию таких окон.',
              'https://mihasoft.glitch.me/wm.html')
    return her


def about_mihnote(her):
    help_show('MihNote', 'Приложение для работы с текстовыми заметками. \
Поддерживает создание, редактирование, удаление и просмотр заметок.',
              'https://mihasoft.glitch.me/mn.html')
    return her


def about_crosszero(her):
    help_show('CrossZero', 'Классическая игра «Крестики-нолики» 3х3 клетки. Поддерживает использование \
собственных имён игроков и автоматическую запись отчётов о проведённых играх.',
              'https://mihasoft.glitch.me/cz.html')
    return her


def about_paint(her):
    help_show('Paint', 'Графический пиксельный редактор с полем редактирование 30х10 клеток. \
Использует оригинальный формат изображения. Поддерживает сохранение, редактирование и удаление файлов.',
              'https://mihasoft.glitch.me/p.html')
    return her


def about_turtlepaint(her):
    help_show('TurtlePaint', 'Графический векторный редактор. Поддерживает сохранение файлов методом скриншотирования, \
а также изменение цвета редактирования.',
              'https://mihasoft.glitch.me/tp.html')
    return her


def about_yourage(her):
    help_show('YourAge', 'Приложение для определения промежутка времени между двумя датами. \
Поддерживает подстановку системной даты, сохранение и подстановку исходных дат, вывод времени в двух форматах.',
              'https://mihasoft.glitch.me/yao.html')
    return her


def about_middlescore(her):
    help_show('MiddleScore', 'Приложение для расчёта среднего балла оценок. \
Поддерживает оценки с двойным индексом и игнорирование чисел, не являющихся оценками..',
              'https://mihasoft.glitch.me/mso.html')
    return her


def about_saper(her):
    help_show('Saper', 'Классическая игра «Сапёр» с полем 5х5 клеток. Поддерживает сохранение статистики, \
изменение количества мин в пределах от 1 до 23 и установку флажков.',
              'https://mihasoft.glitch.me/s.html')
    return her


def about_watermarks(her):
    help_show('WaterMarks', 'Приложение для нанесения текстовых водяных знаков на изображение. \
Поддерживает выбор шрифта, размера, местоположения и цвета текста, предварительный просмотр результата..',
              'https://mihasoft.glitch.me/')
    return her


def about_hypertext(her):
    help_show('HyperText', 'Приложение для создания, сохранения и публикации в Интернете html-страниц. \
Поддерживает добавление блоков, кнопок, ссылок и изображений, изменение цвета текста и фона, предварительный \
просмотр страниц и публикацию на сервере MihaSoft.',
              'https://mihasoft.glitch.me/')
    return her


def about_sml(her):
    help_show('The SML - IDE & Interpreter', 'Редактор и интерпретатор кода на простейшем языке программирования. \
Поддерживает сохранение файлов с кодом и вывод сообщений об ошибках при запуске программ.',
              'https://mihasoft.glitch.me/sml.html')
    return her


def about_numbersystems(her):
    help_show('NumberSystems', 'Перевод чисел из систем счисления вплоть до миллионеричной. \
Поддерживает копирование результата перевода в буфер обмена.',
              'https://mihasoft.glitch.me/tns.html')
    return her


def about_shmalyalka(her):
    help_show('Shmalyalka', 'Динамическая игра-шутер. Поддерживает запись статистики.',
              'https://mihasoft.glitch.me/sml.html')
    return her


def on_M(par=None):
    m.monk_window.append(Toplevel())
    m.monk_window[-1].title('monkey...')
    center_window(m.monk_window[-1], 240, 178)
    m.monk_window[-1].resizable(False, False)
    monk_gif = Gif(m.monk_window[-1], path='images/monkey.gif')
    monk_gif.pack()
    root.bind('<KeyPress-BackSpace>', M_out)
    return par


def M_out(param=None):
    try:
        m.monk_window[-1].destroy()
        m.monk_window.pop(-1)
    except IndexError:
        pass
    return param
