from tkinter import messagebox
from subprocess import Popen
from tkinter.filedialog import askopenfilename, asksaveasfilename
from pyperclip import copy, paste
from math import ceil
from time import sleep

from src.functions import *
from src.init import m, root
from src.homex import *


def Morse():
    def mr_destroy():
        mr_title.destroy()
        translate_label.destroy()
        translate_paste_1.destroy()
        translate_copy_1.destroy()
        translate_save_1.destroy()
        translate_open_1.destroy()
        translate_help.destroy()
        translate_input.destroy()
        translate_output.destroy()
        translate_paste_2.destroy()
        translate_copy_2.destroy()
        translate_save_2.destroy()
        translate_open_2.destroy()
        translate_label_2.destroy()
        rtm_listen.destroy()
        listen_speed.destroy()
        listen_speed_input.destroy()
        rtm_button.destroy()
        mtr_button.destroy()
        mte_button.destroy()
        mr_off.destroy()

        homes()
        m.window.configure(width=788, height=m.abs_height)
        center_window(root, 678, m.abs_height)

    def rtm_main():
        if translate_input.get(1.0, END) == '' or translate_input.get(1.0, END) == '\n':
            messagebox.showwarning('INFO', 'Введите текст для перевода!')
            print(translate_input.get(1.0, END))
        content = translate_input.get(1.0, END)
        if translate_output.get(1.0, END):
            translate_output.delete(1.0, END)

        result = ''
        k = 0
        ban_list = ['~', '`', '#', '№', '%', '^', '*', '/', '|', '<', '>', '{', '}', '[', ']']
        extra_ban = '\ '
        extra_ban = extra_ban.replace(' ', '')
        for zix in range(len(ban_list)):
            if (ban_list[zix] in content or extra_ban in content) and k == 0:
                messagebox.showinfo('INFO', 'Символы ~ ` # № % ^ * / \ | < > { } [ ]\nне \
переводятся в азбуку морзе! Посторонние символы будут автоматически удалены.')
                k += 1

        for i in content:
            if 1040 <= ord(i) <= 1103 or i == ' ' or ord(i) == 1105 or 43 <= ord(i) <= 46 \
                    or 63 <= ord(i) <= 90 or 97 <= ord(i) <= 122 or 48 <= ord(i) <= 59 \
                    or 32 <= ord(i) <= 34 or 38 <= ord(i) <= 41 or ord(i) == 61 \
                    or i == '\n':
                result += i
        result = result[::-1].replace('\n', '', 1)[::-1]
        translate_input.delete('1.0', 'end')
        translate_input.insert('end', result)
        content = str(result).lower()

        rus_to_morse = {'а': '.-',
                        'б': '-...',
                        'в': '.--',
                        'г': '--.',
                        'д': '-..',
                        'е': '.',
                        'ё': '.',
                        'ж': '...-',
                        'з': '--..',
                        'и': '..',
                        'й': '.---',
                        'к': '-.-',
                        'л': '.-..',
                        'м': '--',
                        'н': '-.',
                        'о': '---',
                        'п': '.--.',
                        'р': '.-.',
                        'с': '...',
                        'т': '-',
                        'у': '..-',
                        'ф': '..-.',
                        'х': '....',
                        'ц': '-.-.',
                        'ч': '---.',
                        'ш': '----',
                        'щ': '--.-',
                        'ъ': '.--.-.',
                        'ы': '-.--',
                        'ь': '-..-',
                        'э': '..-..',
                        'ю': '..--',
                        'я': '.-.-',
                        'a': '.-',
                        'b': '-...',
                        'c': '-.-.',
                        'd': '-..',
                        'e': '.',
                        'f': '..-.',
                        'g': '--.',
                        'h': '....',
                        'i': '..',
                        'j': '.---',
                        'k': '-.-',
                        'l': '.-..',
                        'm': '--',
                        'n': '-.',
                        'o': '---',
                        'p': '.--.',
                        'q': '--.-',
                        'r': '.-.',
                        's': '...',
                        't': '-',
                        'u': '..-',
                        'v': '...-',
                        'w': '.--',
                        'x': '-..-',
                        'y': '-.--',
                        'z': '--..',
                        '0': '-----',
                        '1': '.----',
                        '2': '..---',
                        '3': '...--',
                        '4': '....-',
                        '5': '.....',
                        '6': '-....',
                        '7': '--...',
                        '8': '---..',
                        '9': '----.',
                        '-': '-....-',
                        '.': '......',
                        ',': '.-.-.-',
                        ';': '-.-.-.',
                        ':': '---...',
                        '!': '--..--',
                        '?': '..--..',
                        '\n': '\n',
                        '$': '...-..-',
                        '@': '.--.-.',
                        ''': '.-..-.',
                        ''': '.----.',
                        '&': '.-...',
                        '+': '.-.-.',
                        '=': '-...-',
                        '(': '-.--.',
                        ')': '-.--.-',
                        ' ': ' ',
                        '"': '',
                        "'": ''}

        result = ''

        for x in content:
            if rus_to_morse[x] == '\n' or rus_to_morse[x] == ' ':
                result += (rus_to_morse[x])
            else:
                result += (rus_to_morse[x] + ' ')

        if '.' in result or '-' in result:
            translate_output.insert(1.0, result[::-1].replace(' ', '', 1)[::-1])
            copy(result[::-1].replace(' ', '', 1)[::-1])

    def open_any():
        file_types = [('Текстовые файлы', '*.txt'), ('PY файлы', '*.py'), ('PYW файлы', '*.pyw')]
        fl = askopenfilename(filetypes=file_types)
        if fl:
            text = open(fl).read()
            translate_input.insert(END, text)

    def open_any_1():
        file_types = [('MORSE файлы', '*.mrs'), ('Текстовые файлы', '*.txt')]
        fl = askopenfilename(filetypes=file_types)
        if fl:
            text = open(fl).read()
            translate_output.insert(END, text)

    def play():
        def speed_check(sp):
            k = 0
            alphabet = '1234567890.,'
            for ia in range(len(sp)):
                if sp[ia] not in alphabet:
                    k += 1
                    if k == 1:
                        return 0
            if k == 0:
                return 1

        def speed_change(x, speeds):
            if (100 * x / speeds) % 1 >= 0.5:
                return ceil(100 * x / speeds)
            else:
                return int(100 * x / speeds)

        frequency = 500
        content = translate_output.get(1.0, END)
        content_check = content
        content_check = content_check.replace('.', '')
        content_check = content_check.replace('-', '')
        content_check = content_check.replace(' ', '')
        content_check = content_check.replace('\n', '')
        if content_check != '':
            messagebox.showwarning('INFO',
                                   'Отсутствует код морзе для воспроизведения или он содержит посторонние символы.')
        else:
            if content == '' or ('.' not in content and '-' not in content):
                messagebox.showwarning('INFO', 'Отсутствует код морзе для воспроизведения!')
            else:
                a = 0
                b = 0
                speeder = listen_speed_input.get()
                speeder = speeder.replace('\n', '', 1)
                if not (speeder.count('0') != 0 and speeder.count('1') == 0 and speeder.count('2') == 0 and
                        speeder.count('3') == 0 and speeder.count('4') == 0 and speeder.count('5') == 0 and
                        speeder.count('6') == 0 and speeder.count('7') == 0 and speeder.count('8') == 0 and
                        speeder.count('9') == 0):
                    speed_check_2 = speeder.split(',')
                    speed_check_3 = speeder.split('.')
                    while a < len(speed_check_2):
                        if speed_check_2[a] == '' or speed_check_3[b] == '.':
                            speed_check_2.pop(a)
                        else:
                            a += 1
                    while b < len(speed_check_3):
                        if speed_check_3[b] == '' or speed_check_3[b] == ',':
                            speed_check_3.pop(b)
                        else:
                            b += 1
                    if speed_check(speeder) == 0 or len(speed_check_2) == 0 or len(speed_check_3) == 0 or \
                            speeder.count('.') > 1 or speeder.count(',') > 1 \
                            or speeder.count('.') + speeder.count(',') > 1:
                        messagebox.showwarning('INFO', 'Некорректное значение скорости!')
                    else:
                        if speeder.count('0') == 0 and speeder.count('1') == 0 and speeder.count('2') == 0 and \
                                speeder.count('3') == 0 and speeder.count('4') == 0 and speeder.count('5') == 0 and \
                                speeder.count('6') == 0 and speeder.count('7') == 0 and speeder.count('8') == 0 and \
                                speeder.count('9') == 0:
                            speeder = 1
                        else:
                            speeder = speeder.replace(',', '.')
                            if speeder.count('.') == 0:
                                speeder = int(speeder)
                            else:
                                speeder = float(speeder)
                        with open('flag', 'w'):
                            pass
                        os.startfile('res/morse.exe')
                        for i in content:
                            mr_flag = True
                            for symbol in i:
                                if symbol == '.':
                                    Beep(frequency, speed_change(1, speeder))
                                    sleep(0.1 / speeder)
                                elif symbol == '-':
                                    Beep(frequency, speed_change(3, speeder))
                                    sleep(0.1 / speeder)
                                elif symbol == ' ':
                                    sleep(0.3 / speeder)
                                if not os.path.exists('flag'):
                                    mr_flag = False
                                    break
                            if not mr_flag:
                                break
                        Popen('taskkill /im morse.exe /f')
                else:
                    messagebox.showwarning('INFO', 'Некорректное значение скорости!')

    def paste_0():
        translate_input.delete(1.0, END)
        translate_input.insert(1.0, str(paste()))

    def paste_1():
        translate_output.delete(1.0, END)
        translate_output.insert(1.0, str(paste()))

    def mtr_main():
        if translate_input.get(1.0, END):
            translate_input.delete(1.0, END)
        rez = ''
        content = translate_output.get(1.0, END)
        if content[-1] != ' ':
            content = content + ' '
        k = 0
        clean_content = ''
        content_check = content
        content_check = content_check.replace(' ', '')
        content_check = content_check.replace('\n', '')
        content_check = content_check.replace('-', '')
        content_check = content_check.replace('.', '')

        if content_check == '':
            content = content[::-1].replace('\n', '', 1)[::-1]
            clean_content = content
        else:
            if '.' not in content and '-' not in content:
                messagebox.showwarning('INFO', 'Введите код для перевода!')
            elif k == 0:
                messagebox.showinfo('INFO',
                                    'Недопустимые символы или их сочетания будут автоматически удалены!')
                k += 1
            for mih in range(len(content)):
                if content[mih] == '.' or content[mih] == '-' or content[mih] == ' ' or content[mih] == '\n':
                    clean_content += content[mih]
            clean_content = clean_content[::-1].replace('\n', '', 1)[::-1]
            translate_input.delete(1.0, END)
            translate_input.insert(1.0, clean_content)
        clean_content = clean_content.replace('\n', ' \n ')
        clean_content = clean_content.split(' ')
        clean_content[-1] = clean_content[-1].replace('\n', '', 1)

        def translator_mtr(content_piece):
            if content_piece == '':
                return ' '
            if content_piece == '\n':
                return '\n'
            if content_piece == '-.--.-':
                return ')'
            if content_piece == '-.--.':
                return '('
            if content_piece == '-...-':
                return '='
            if content_piece == '.-.-.':
                return '+'
            if content_piece == '.-...':
                return '&'
            if content_piece == '.----.':
                return "'"
            if content_piece == '.-..-.':
                return '"'
            if content_piece == '.--.-.':
                return '@'
            if content_piece == '...-..-':
                return '$'
            if content_piece == '..--..':
                return '?'
            if content_piece == '--..--':
                return '!'
            if content_piece == '---...':
                return ':'
            if content_piece == '-.-.-.':
                return ';'
            if content_piece == '.-.-.-':
                return ','
            if content_piece == '......':
                return '.'
            if content_piece == '-....-':
                return '-'
            if content_piece == '----.':
                return '9'
            if content_piece == '---..':
                return '8'
            if content_piece == '--...':
                return '7'
            if content_piece == '-....':
                return '6'
            if content_piece == '.....':
                return '5'
            if content_piece == '....-':
                return '4'
            if content_piece == '...--':
                return '3'
            if content_piece == '..---':
                return '2'
            if content_piece == '.----':
                return '1'
            if content_piece == '-----':
                return '0'
            if content_piece == '.-.-':
                return 'я'
            if content_piece == '..--':
                return 'ю'
            if content_piece == '..-..':
                return 'э'
            if content_piece == '-..-':
                return 'ь'
            if content_piece == '-.--':
                return 'ы'
            if content_piece == '.--.-.':
                return 'ъ'
            if content_piece == '--.-':
                return 'щ'
            if content_piece == '----':
                return 'ш'
            if content_piece == '---.':
                return 'ч'
            if content_piece == '-.-.':
                return 'ц'
            if content_piece == '....':
                return 'х'
            if content_piece == '..-.':
                return 'ф'
            if content_piece == '..-':
                return 'у'
            if content_piece == '-':
                return 'т'
            if content_piece == '...':
                return 'с'
            if content_piece == '.-.':
                return 'р'
            if content_piece == '.--.':
                return 'п'
            if content_piece == '---':
                return 'о'
            if content_piece == '-.':
                return 'н'
            if content_piece == '--':
                return 'м'
            if content_piece == '.-..':
                return 'л'
            if content_piece == '-.-':
                return 'к'
            if content_piece == '.---':
                return 'й'
            if content_piece == '..':
                return 'и'
            if content_piece == '--..':
                return 'з'
            if content_piece == '...-':
                return 'ж'
            if content_piece == '.':
                return 'е'
            if content_piece == '-..':
                return 'д'
            if content_piece == '--.':
                return 'г'
            if content_piece == '.--':
                return 'в'
            if content_piece == '-...':
                return 'б'
            if content_piece == '.-':
                return 'а'
            else:
                messagebox.showwarning('INFO',
                                       'Введённое сочетание символов имеет буквы из другого языка или не имеет смысла!')
                return '#'

        for zix in range(len(clean_content)):
            rez_temp = translator_mtr(clean_content[zix])
            rez += rez_temp
        if rez.count('#') == 0:
            translate_input.insert(1.0, rez[::-1].replace(' ', '', 1)[::-1])
            copy(rez[::-1].replace(' ', '', 1)[::-1])

    def mte_main():
        if translate_input.get(1.0, END):
            translate_input.delete(1.0, END)
        rez = ''
        content = translate_output.get(1.0, END)
        if content[-1] != ' ':
            content = content + ' '
        k = 0
        clean_content = ''
        content_check = content
        content_check = content_check.replace(' ', '')
        content_check = content_check.replace('\n', '')
        content_check = content_check.replace('-', '')
        content_check = content_check.replace('.', '')

        if content_check == '':
            content = content[::-1].replace('\n', '', 1)[::-1]
            clean_content = content
        else:
            if '.' not in content and '-' not in content:
                messagebox.showwarning('INFO', 'Введите код для перевода!')
            elif k == 0:
                messagebox.showinfo('INFO',
                                    'Недопустимые символы или их сочетания будут автоматически удалены!')
                k += 1
            for mih in range(len(content)):
                if content[mih] == '.' or content[mih] == '-' or content[mih] == ' ' or content[mih] == '\n':
                    clean_content += content[mih]
            clean_content = clean_content[::-1].replace('\n', '', 1)[::-1]
            translate_input.delete(1.0, END)
            translate_input.insert(1.0, clean_content)
        clean_content = clean_content.replace('\n', ' \n ')
        clean_content = clean_content.split(' ')
        clean_content[-1] = clean_content[-1].replace('\n', '', 1)

        def translator_mte(content_piece):
            if content_piece == '':
                return ' '
            if content_piece == '\n':
                return '\n'
            if content_piece == '-.--.-':
                return ')'
            if content_piece == '-.--.':
                return '('
            if content_piece == '-...-':
                return '='
            if content_piece == '.-.-.':
                return '+'
            if content_piece == '.-...':
                return '&'
            if content_piece == '.----.':
                return "'"
            if content_piece == '.-..-.':
                return '"'
            if content_piece == '.--.-.':
                return '@'
            if content_piece == '...-..-':
                return '$'
            if content_piece == '..--..':
                return '?'
            if content_piece == '--..--':
                return '!'
            if content_piece == '---...':
                return ':'
            if content_piece == '-.-.-.':
                return ';'
            if content_piece == '.-.-.-':
                return ','
            if content_piece == '......':
                return '.'
            if content_piece == '-....-':
                return '-'
            if content_piece == '----.':
                return '9'
            if content_piece == '---..':
                return '8'
            if content_piece == '--...':
                return '7'
            if content_piece == '-....':
                return '6'
            if content_piece == '.....':
                return '5'
            if content_piece == '....-':
                return '4'
            if content_piece == '...--':
                return '3'
            if content_piece == '..---':
                return '2'
            if content_piece == '.----':
                return '1'
            if content_piece == '-----':
                return '0'
            if content_piece == '--..':
                return 'z'
            if content_piece == '-.--':
                return 'y'
            if content_piece == '-..-':
                return 'x'
            if content_piece == '.--':
                return 'w'
            if content_piece == '...-':
                return 'v'
            if content_piece == '..-':
                return 'u'
            if content_piece == '-':
                return 't'
            if content_piece == '...':
                return 's'
            if content_piece == '.-.':
                return 'r'
            if content_piece == '--.-':
                return 'q'
            if content_piece == '.--.':
                return 'p'
            if content_piece == '---':
                return 'o'
            if content_piece == '-.':
                return 'n '
            if content_piece == '--':
                return 'm'
            if content_piece == '.-..':
                return 'l'
            if content_piece == '-.-':
                return 'k'
            if content_piece == '.---':
                return 'j'
            if content_piece == '..':
                return 'i'
            if content_piece == '....':
                return 'h'
            if content_piece == '--.':
                return 'g'
            if content_piece == '..-.':
                return 'f'
            if content_piece == '.':
                return 'e'
            if content_piece == '-..':
                return 'd'
            if content_piece == '-.-.':
                return 'c'
            if content_piece == '-...':
                return 'b'
            if content_piece == '.-':
                return 'a'
            else:
                messagebox.showwarning('INFO',
                                       'Введённое сочетание символов имеет буквы из другого языка или не имеет смысла!')
                return '#'

        for zix in range(len(clean_content)):
            rez_temp = translator_mte(clean_content[zix])
            rez += rez_temp
        if rez.count('#') == 0:
            translate_input.insert(1.0, rez[::-1].replace(' ', '', 1)[::-1])
            copy(rez[::-1].replace(' ', '', 1)[::-1])

    def mr_help():
        messagebox.showinfo('Справка', 'Некоторые сочетания символов в Азбуке Морзе можно перевести сразу на \
несколько языков\n\nПри переводе из Морзе все символы будут преобразованы только в один из языков.')

    def mr_copy():
        copy(translate_input.get(1.0, END))

    def mr_copy_1():
        copy(translate_output.get(1.0, END))

    def mr_save():
        mr_name = asksaveasfilename(title='Сохранить', filetypes=(('TXT File', '*.txt'),
                                                                  ('All files', '*.*')),
                                    defaultextension='.txt')
        if mr_name:
            d_file = open(mr_name, 'w')
            d_file.close()
            with open(mr_name, 'w') as f:
                f.write(translate_input.get(1.0, END))

    def mr_save_1():
        mr_name = asksaveasfilename(title='Сохранить', filetypes=(('MORSE File', '*.mrs'),
                                                                  ('TXT File', '*.txt'),
                                                                  ('All files', '*.*')),
                                    defaultextension='.mrs')
        if mr_name:
            d_file = open(mr_name, 'w')
            d_file.close()
            with open(mr_name, 'w') as f:
                f.write(translate_output.get(1.0, END))

    center_window(root, 550, 420)
    root.title('Morse 1.0')
    m.window.configure(width=550, height=420)
    root.minsize(550, 420)

    mr_title = Label(m.window, text='Morse 1.0', font=('Arial Bold', 16), fg='red')
    mr_title.place(x=50, y=10)

    translate_label = Label(m.window, text='Текст:', height=1)
    translate_label.place(x=50, y=129)

    translate_paste_1 = Button(m.window, text='Вставить', bg='#fab1b1', width=12,
                               command=paste_0, font=('Calibri', 10))
    translate_paste_1.place(x=100, y=125)

    translate_copy_1 = Button(m.window, text='Копировать', bg='#facab1', width=12,
                              command=mr_copy, font=('Calibri', 10))
    translate_copy_1.place(x=200, y=125)

    translate_save_1 = Button(m.window, text='Сохранить', bg='#b3fab1', width=12,
                              command=mr_save, font=('Calibri', 10))
    translate_save_1.place(x=300, y=125)

    translate_open_1 = Button(m.window, text='Открыть', bg='#b1e5fa', width=12,
                              command=open_any, font=('Calibri', 10))
    translate_open_1.place(x=400, y=125)

    translate_help = Button(m.window, text='Справка', bg='#dedede', width=21, command=mr_help,
                            font=('Calibri', 10))
    translate_help.place(x=340, y=10)

    translate_input = Text(m.window, width=55, height=5)
    translate_input.place(x=50, y=159)

    translate_output = Text(m.window, width=55, height=5)
    translate_output.place(x=50, y=297)

    translate_paste_2 = Button(m.window, text='Вставить', bg='#fab1b1', width=12,
                               command=paste_1, font=('Calibri', 10))
    translate_paste_2.place(x=100, y=263)

    translate_copy_2 = Button(m.window, text='Копировать', bg='#facab1', width=12,
                              command=mr_copy_1, font=('Calibri', 10))
    translate_copy_2.place(x=200, y=263)

    translate_save_2 = Button(m.window, text='Сохранить', bg='#b3fab1', width=12,
                              command=mr_save_1, font=('Calibri', 10))
    translate_save_2.place(x=300, y=263)

    translate_open_2 = Button(m.window, text='Открыть', bg='#b1e5fa', width=12,
                              command=open_any_1, font=('Calibri', 10))
    translate_open_2.place(x=400, y=263)

    translate_label_2 = Label(m.window, text='Код:', height=1)
    translate_label_2.place(x=50, y=267)

    rtm_listen = Button(m.window, text='Воспроизвести', bg='#ffdab3', fg='black', width=21,
                        command=play, font=('Calibri', 10))
    rtm_listen.place(x=340, y=50)

    listen_speed = Label(m.window, text='Скорость воспроизведения:', height=1)
    listen_speed.place(x=155, y=90)

    listen_speed_input = Entry(m.window, width=10)
    listen_speed_input.place(x=320, y=90)

    rtm_button = Button(m.window, text='Перевести в Морзе', bg='#80fff7', width=15,
                        command=rtm_main, font=('Calibri', 10))
    rtm_button.place(x=50, y=50)

    mtr_button = Button(m.window, text='Перевести на Русский', bg='#80fff7', width=21, command=mtr_main,
                        font=('Calibri', 10))
    mtr_button.place(x=175, y=10)

    mte_button = Button(m.window, text='Перевести на Английский', bg='#80fff7', width=21, command=mte_main,
                        font=('Calibri', 10))
    mte_button.place(x=175, y=50)

    listen_speed_input.insert(0, '1')

    mr_off = Button(m.window, text='⌂', font=('Arial Bold', 15), width=2, height=1, bg='black', fg='white',
                    command=mr_destroy)
    mr_off.place(x=0, y=5)
    ToolTip(mr_off, 'На главную...')
