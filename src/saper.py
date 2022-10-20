from random import choice
from numpy import save
from tkinter import ttk

from src.functions import *
from src.init import m, root
from src.homex import *


def Saper():
    s = SaperGlobals()

    def Return():
        try:
            s.stat_window.destroy()
        except AttributeError:
            pass

        try:
            s.params_window.destroy()
        except AttributeError:
            pass

        s_title.destroy()
        restart_button.destroy()
        info_label.destroy()
        off.destroy()
        s_box_a1.destroy()
        s_box_a2.destroy()
        s_box_a3.destroy()
        s_box_a4.destroy()
        s_box_a5.destroy()
        s_box_b1.destroy()
        s_box_b2.destroy()
        s_box_b3.destroy()
        s_box_b4.destroy()
        s_box_b5.destroy()
        s_box_c1.destroy()
        s_box_c2.destroy()
        s_box_c3.destroy()
        s_box_c4.destroy()
        s_box_c5.destroy()
        s_box_d1.destroy()
        s_box_d2.destroy()
        s_box_d3.destroy()
        s_box_d4.destroy()
        s_box_d5.destroy()
        s_box_e1.destroy()
        s_box_e2.destroy()
        s_box_e3.destroy()
        s_box_e4.destroy()
        s_box_e5.destroy()
        stat_button.destroy()
        param_button.destroy()
        homes()
        m.window.configure(width=788, height=m.abs_height)
        center_window(root, 678, m.abs_height)

    def NewGame():
        s.start_flag = True
        s.to_flags_list = [False, False, False, False, False, False, False, False, False, False, False, False, False,
                           False, False, False, False, False, False, False, False, False, False, False, False]
        s.box_list = [s_box_a1, s_box_a2, s_box_a3, s_box_a4, s_box_a5, s_box_b1, s_box_b2, s_box_b3, s_box_b4,
                      s_box_b5, s_box_c1, s_box_c2, s_box_c3, s_box_c4, s_box_c5, s_box_d1, s_box_d2, s_box_d3,
                      s_box_d4, s_box_d5, s_box_e1, s_box_e2, s_box_e3, s_box_e4, s_box_e5]
        s_flags_list = [False, False, False, False, False, False, False, False, False, False, False, False, False,
                        False, False, False, False, False, False, False, False, False, False, False, False]
        s_numbers_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24]
        s.bomb_list = []
        for i in range(1, s.number_of_mines + 1):
            s_bomb_loc = choice(s_numbers_list)
            s_numbers_list.remove(s_bomb_loc)
            s_flags_list[s_bomb_loc] = True
            s.bomb_list.append(s.box_list[s_bomb_loc])
        for i in range(len(s.bomb_list)):
            s.box_list.remove(s.bomb_list[i])
        s.global_flag = True
        s.flag_a1, s.flag_a2, s.flag_a3, s.flag_a4, s.flag_a5, s.flag_b1, s.flag_b2, s.flag_b3, s.flag_b4, s.flag_b5, \
            s.flag_c1, s.flag_c2, s.flag_c3, s.flag_c4, s.flag_c5, s.flag_d1, s.flag_d2, s.flag_d3, s.flag_d4, \
            s.flag_d5, s.flag_e1, s.flag_e2, s.flag_e3, s.flag_e4, s.flag_e5 = \
            s_flags_list[0], s_flags_list[1], s_flags_list[2], s_flags_list[3], s_flags_list[4], s_flags_list[5], \
            s_flags_list[6], s_flags_list[7], s_flags_list[8], s_flags_list[9], s_flags_list[10], s_flags_list[11], \
            s_flags_list[12], s_flags_list[13], s_flags_list[14], s_flags_list[15], s_flags_list[16], s_flags_list[17],\
            s_flags_list[18], s_flags_list[19], s_flags_list[20], s_flags_list[21], s_flags_list[22], s_flags_list[23],\
            s_flags_list[24]

        s.flags_array = [s.flag_a1, s.flag_a2, s.flag_a3, s.flag_a4, s.flag_a5, s.flag_b1, s.flag_b2, s.flag_b3,
                         s.flag_b4, s.flag_b5,
                         s.flag_c1, s.flag_c2, s.flag_c3, s.flag_c4, s.flag_c5, s.flag_d1, s.flag_d2, s.flag_d3,
                         s.flag_d4,
                         s.flag_d5, s.flag_e1, s.flag_e2, s.flag_e3, s.flag_e4, s.flag_e5]

    def GameOver():
        if s.global_flag:
            for i in range(len(s.bomb_list)):
                s.bomb_list[i].configure(bg='red')
            for i in range(len(s.box_list)):
                s.box_list[i].configure(bg='white')
            info_label.configure(text='Вы проиграли!', fg='red')
            s.global_flag = False
            stat_list = load('C:/MihaSoft Files/SaperStat.npy')
            numb_of_games = stat_list[0] + 1
            new_stat_list = [numb_of_games, stat_list[1]]
            save('C:/MihaSoft Files/SaperStat', new_stat_list)
            if os.path.exists('C:/MihaSoft Files/SoundFlagFile.miha'):
                Beep(1000, 500)

    def CheckWin():
        k = 0
        for i in range(len(s.box_list)):
            if s.box_list[i]['background'] != 'white':
                k += 1
        if k == 0:
            for i in range(len(s.box_list)):
                s.box_list[i].configure(bg='white')
            for i in range(len(s.bomb_list)):
                s.bomb_list[i].configure(bg='green')
            s.global_flag = False
            info_label.configure(text='Вы выиграли!', fg='green')
            stat_list = load('C:/MihaSoft Files/SaperStat.npy')
            numb_of_games = stat_list[0] + 1
            numb_of_wins = stat_list[1] + 1
            new_stat_list = [numb_of_games, numb_of_wins]
            save('C:/MihaSoft Files/SaperStat', new_stat_list)
            if os.path.exists('C:/MihaSoft Files/SoundFlagFile.miha'):
                Beep(500, 400)
                m.window.after(30, Beep(500, 400))
                m.window.after(30, Beep(500, 400))

    def RestartGame():
        NewGame()
        info_label.configure(text='')
        s_box_list_2 = [s_box_a1, s_box_a2, s_box_a3, s_box_a4, s_box_a5, s_box_b1, s_box_b2, s_box_b3, s_box_b4,
                        s_box_b5,
                        s_box_c1, s_box_c2, s_box_c3, s_box_c4, s_box_c5, s_box_d1, s_box_d2, s_box_d3, s_box_d4,
                        s_box_d5,
                        s_box_e1, s_box_e2, s_box_e3, s_box_e4, s_box_e5]
        for i in range(len(s_box_list_2)):
            s_box_list_2[i].configure(bg='#7a9cd6', text='')

    def to_flag_1(full=None):
        if s_box_a1['background'] != 'white':
            if not s.to_flags_list[0]:
                s.to_flags_list[0] = True
                s_box_a1.configure(bg='yellow')
            else:
                s.to_flags_list[0] = False
                s_box_a1.configure(bg='#7a9cd6')
        return full

    def to_flag_2(full=None):
        if s_box_a2['background'] != 'white':
            if not s.to_flags_list[1]:
                s.to_flags_list[1] = True
                s_box_a2.configure(bg='yellow')
            else:
                s.to_flags_list[1] = False
                s_box_a2.configure(bg='#7a9cd6')
        return full

    def to_flag_3(full=None):
        if s_box_a3['background'] != 'white':
            if not s.to_flags_list[2]:
                s.to_flags_list[2] = True
                s_box_a3.configure(bg='yellow')
            else:
                s.to_flags_list[2] = False
                s_box_a3.configure(bg='#7a9cd6')
        return full

    def to_flag_4(full=None):
        if s_box_a4['background'] != 'white':
            if not s.to_flags_list[3]:
                s.to_flags_list[3] = True
                s_box_a4.configure(bg='yellow')
            else:
                s.to_flags_list[3] = False
                s_box_a4.configure(bg='#7a9cd6')
        return full

    def to_flag_5(full=None):
        if s_box_a5['background'] != 'white':
            if not s.to_flags_list[4]:
                s.to_flags_list[4] = True
                s_box_a5.configure(bg='yellow')
            else:
                s.to_flags_list[4] = False
                s_box_a5.configure(bg='#7a9cd6')
        return full

    def to_flag_6(full=None):
        if s_box_b1['background'] != 'white':
            if not s.to_flags_list[5]:
                s.to_flags_list[5] = True
                s_box_b1.configure(bg='yellow')
            else:
                s.to_flags_list[5] = False
                s_box_b1.configure(bg='#7a9cd6')
        return full

    def to_flag_7(full=None):
        if s_box_b2['background'] != 'white':
            if not s.to_flags_list[6]:
                s.to_flags_list[6] = True
                s_box_b2.configure(bg='yellow')
            else:
                s.to_flags_list[6] = False
                s_box_b2.configure(bg='#7a9cd6')
        return full

    def to_flag_8(full=None):
        if s_box_b3['background'] != 'white':
            if not s.to_flags_list[7]:
                s.to_flags_list[7] = True
                s_box_b3.configure(bg='yellow')
            else:
                s.to_flags_list[7] = False
                s_box_b3.configure(bg='#7a9cd6')
        return full

    def to_flag_9(full=None):
        if s_box_b4['background'] != 'white':
            if not s.to_flags_list[8]:
                s.to_flags_list[8] = True
                s_box_b4.configure(bg='yellow')
            else:
                s.to_flags_list[8] = False
                s_box_b4.configure(bg='#7a9cd6')
        return full

    def to_flag_10(full=None):
        if s_box_b5['background'] != 'white':
            if not s.to_flags_list[9]:
                s.to_flags_list[9] = True
                s_box_b5.configure(bg='yellow')
            else:
                s.to_flags_list[9] = False
                s_box_b5.configure(bg='#7a9cd6')
        return full

    def to_flag_11(full=None):
        if s_box_c1['background'] != 'white':
            if not s.to_flags_list[10]:
                s.to_flags_list[10] = True
                s_box_c1.configure(bg='yellow')
            else:
                s.to_flags_list[10] = False
                s_box_c1.configure(bg='#7a9cd6')
        return full

    def to_flag_12(full=None):
        if s_box_c2['background'] != 'white':
            if not s.to_flags_list[11]:
                s.to_flags_list[11] = True
                s_box_c2.configure(bg='yellow')
            else:
                s.to_flags_list[11] = False
                s_box_c2.configure(bg='#7a9cd6')
        return full

    def to_flag_13(full=None):
        if s_box_c3['background'] != 'white':
            if not s.to_flags_list[12]:
                s.to_flags_list[12] = True
                s_box_c3.configure(bg='yellow')
            else:
                s.to_flags_list[12] = False
                s_box_c3.configure(bg='#7a9cd6')
        return full

    def to_flag_14(full=None):
        if s_box_c4['background'] != 'white':
            if not s.to_flags_list[13]:
                s.to_flags_list[13] = True
                s_box_c4.configure(bg='yellow')
            else:
                s.to_flags_list[13] = False
                s_box_c4.configure(bg='#7a9cd6')
        return full

    def to_flag_15(full=None):
        if s_box_c5['background'] != 'white':
            if not s.to_flags_list[14]:
                s.to_flags_list[14] = True
                s_box_c5.configure(bg='yellow')
            else:
                s.to_flags_list[14] = False
                s_box_c5.configure(bg='#7a9cd6')
        return full

    def to_flag_16(full=None):
        if s_box_d1['background'] != 'white':
            if not s.to_flags_list[15]:
                s.to_flags_list[15] = True
                s_box_d1.configure(bg='yellow')
            else:
                s.to_flags_list[15] = False
                s_box_d1.configure(bg='#7a9cd6')
        return full

    def to_flag_17(full=None):
        if s_box_d2['background'] != 'white':
            if not s.to_flags_list[16]:
                s.to_flags_list[16] = True
                s_box_d2.configure(bg='yellow')
            else:
                s.to_flags_list[16] = False
                s_box_d2.configure(bg='#7a9cd6')
        return full

    def to_flag_18(full=None):
        if s_box_d3['background'] != 'white':
            if not s.to_flags_list[17]:
                s.to_flags_list[17] = True
                s_box_d3.configure(bg='yellow')
            else:
                s.to_flags_list[17] = False
                s_box_d3.configure(bg='#7a9cd6')
        return full

    def to_flag_19(full=None):
        if s_box_d4['background'] != 'white':
            if not s.to_flags_list[18]:
                s.to_flags_list[18] = True
                s_box_d4.configure(bg='yellow')
            else:
                s.to_flags_list[18] = False
                s_box_d4.configure(bg='#7a9cd6')
        return full

    def to_flag_20(full=None):
        if s_box_d5['background'] != 'white':
            if not s.to_flags_list[19]:
                s.to_flags_list[19] = True
                s_box_d5.configure(bg='yellow')
            else:
                s.to_flags_list[19] = False
                s_box_d5.configure(bg='#7a9cd6')
        return full

    def to_flag_21(full=None):
        if s_box_e1['background'] != 'white':
            if not s.to_flags_list[20]:
                s.to_flags_list[20] = True
                s_box_e1.configure(bg='yellow')
            else:
                s.to_flags_list[20] = False
                s_box_e1.configure(bg='#7a9cd6')
        return full

    def to_flag_22(full=None):
        if s_box_e2['background'] != 'white':
            if not s.to_flags_list[21]:
                s.to_flags_list[21] = True
                s_box_e2.configure(bg='yellow')
            else:
                s.to_flags_list[21] = False
                s_box_e2.configure(bg='#7a9cd6')
        return full

    def to_flag_23(full=None):
        if s_box_e3['background'] != 'white':
            if not s.to_flags_list[22]:
                s.to_flags_list[22] = True
                s_box_e3.configure(bg='yellow')
            else:
                s.to_flags_list[22] = False
                s_box_e3.configure(bg='#7a9cd6')
        return full

    def to_flag_24(full=None):
        if s_box_e4['background'] != 'white':
            if not s.to_flags_list[23]:
                s.to_flags_list[23] = True
                s_box_e4.configure(bg='yellow')
            else:
                s.to_flags_list[23] = False
                s_box_e4.configure(bg='#7a9cd6')
        return full

    def to_flag_25(full=None):
        if s_box_e5['background'] != 'white':
            if not s.to_flags_list[24]:
                s.to_flags_list[24] = True
                s_box_e5.configure(bg='yellow')
            else:
                s.to_flags_list[24] = False
                s_box_e5.configure(bg='#7a9cd6')
        return full

    def s_open_box_1(box, flag_1, flag_2, flag_3):
        k = 0
        listok = [flag_1, flag_2, flag_3]
        for j in range(len(listok)):
            if listok[j]:
                k += 1
        box.configure(text=k, bg='white')
        CheckWin()

    def on_a1():
        if os.path.exists('C:/MihaSoft Files/SoundFlagFile.miha'):
            Beep(300, 50)
        if s.global_flag and not s.to_flags_list[0]:
            if not s.flag_a1:
                if s.start_flag:
                    s.start_flag = False
                s_open_box_1(s_box_a1, s.flag_a2, s.flag_b2, s.flag_b1)
            else:
                if s.start_flag:
                    while s.flag_a1:
                        RestartGame()
                    s_open_box_1(s_box_a1, s.flag_a2, s.flag_b2, s.flag_b1)
                    s.start_flag = False
                else:
                    GameOver()

    def on_a5():
        if os.path.exists('C:/MihaSoft Files/SoundFlagFile.miha'):
            Beep(300, 50)
        if s.global_flag and not s.to_flags_list[4]:
            if not s.flag_a5:
                if s.start_flag:
                    s.start_flag = False
                s_open_box_1(s_box_a5, s.flag_a4, s.flag_b4, s.flag_b5)
            else:
                if s.start_flag:
                    while s.flag_a5:
                        RestartGame()
                    s_open_box_1(s_box_a5, s.flag_a4, s.flag_b4, s.flag_b5)
                    s.start_flag = False
                else:
                    GameOver()

    def on_e1():
        if os.path.exists('C:/MihaSoft Files/SoundFlagFile.miha'):
            Beep(300, 50)
        if s.global_flag and not s.to_flags_list[20]:
            if not s.flag_e1:
                if s.start_flag:
                    s.start_flag = False

                s_open_box_1(s_box_e1, s.flag_d1, s.flag_d2, s.flag_e2)
            else:
                if s.start_flag:
                    while s.flag_e1:
                        RestartGame()
                    s_open_box_1(s_box_e1, s.flag_d1, s.flag_d2, s.flag_e2)
                    s.start_flag = False
                else:
                    GameOver()

    def on_e5():
        if os.path.exists('C:/MihaSoft Files/SoundFlagFile.miha'):
            Beep(300, 50)
        if s.global_flag and not s.to_flags_list[24]:
            if not s.flag_e5:
                if s.start_flag:
                    s.start_flag = False
                s_open_box_1(s_box_e5, s.flag_e4, s.flag_d4, s.flag_d5)

            else:
                if s.start_flag:
                    while s.flag_e5:
                        RestartGame()
                    s_open_box_1(s_box_e5, s.flag_e4, s.flag_d4, s.flag_d5)
                    s.start_flag = False
                else:
                    GameOver()

    def s_open_box_2(box, flag_1, flag_2, flag_3, flag_4, flag_5):
        k = 0
        listok = [flag_1, flag_2, flag_3, flag_4, flag_5]
        for j in range(len(listok)):
            if listok[j]:
                k += 1
        box.configure(text=k, bg='white')
        CheckWin()

    def on_a2():
        if os.path.exists('C:/MihaSoft Files/SoundFlagFile.miha'):
            Beep(300, 50)
        if s.global_flag and not s.to_flags_list[1]:
            if not s.flag_a2:
                if s.start_flag:
                    s.start_flag = False
                s_open_box_2(s_box_a2, s.flag_a1, s.flag_b1, s.flag_b2, s.flag_b3, s.flag_a3)

            else:
                if s.start_flag:
                    while s.flag_a2:
                        RestartGame()
                    s_open_box_2(s_box_a2, s.flag_a1, s.flag_b1, s.flag_b2, s.flag_b3, s.flag_a3)
                    s.start_flag = False
                else:
                    GameOver()

    def on_a3():
        if os.path.exists('C:/MihaSoft Files/SoundFlagFile.miha'):
            Beep(300, 50)
        if s.global_flag and not s.to_flags_list[2]:
            if not s.flag_a3:
                if s.start_flag:
                    s.start_flag = False
                s_open_box_2(s_box_a3, s.flag_a2, s.flag_b2, s.flag_b3, s.flag_b4, s.flag_a4)

            else:
                if s.start_flag:
                    while s.flag_a3:
                        RestartGame()
                    s_open_box_2(s_box_a3, s.flag_a2, s.flag_b2, s.flag_b3, s.flag_b4, s.flag_a4)
                    s.start_flag = False
                else:
                    GameOver()

    def on_a4():
        if os.path.exists('C:/MihaSoft Files/SoundFlagFile.miha'):
            Beep(300, 50)
        if s.global_flag and not s.to_flags_list[3]:
            if not s.flag_a4:
                if s.start_flag:
                    s.start_flag = False
                s_open_box_2(s_box_a4, s.flag_a3, s.flag_b3, s.flag_b4, s.flag_b5, s.flag_a5)

            else:
                if s.start_flag:
                    while s.flag_a4:
                        RestartGame()
                    s_open_box_2(s_box_a4, s.flag_a3, s.flag_b3, s.flag_b4, s.flag_b5, s.flag_a5)
                    s.start_flag = False
                else:
                    GameOver()

    def on_b1():
        if os.path.exists('C:/MihaSoft Files/SoundFlagFile.miha'):
            Beep(300, 50)
        if s.global_flag and not s.to_flags_list[5]:
            if not s.flag_b1:
                if s.start_flag:
                    s.start_flag = False
                s_open_box_2(s_box_b1, s.flag_a1, s.flag_a2, s.flag_b2, s.flag_c2, s.flag_c1)

            else:
                if s.start_flag:
                    while s.flag_b1:
                        RestartGame()
                    s_open_box_2(s_box_b1, s.flag_a1, s.flag_a2, s.flag_b2, s.flag_c2, s.flag_c1)
                    s.start_flag = False
                else:
                    GameOver()

    def on_c1():
        if os.path.exists('C:/MihaSoft Files/SoundFlagFile.miha'):
            Beep(300, 50)
        if s.global_flag and not s.to_flags_list[10]:
            if not s.flag_c1:
                if s.start_flag:
                    s.start_flag = False
                s_open_box_2(s_box_c1, s.flag_b1, s.flag_b2, s.flag_c2, s.flag_d2, s.flag_d1)

            else:
                if s.start_flag:
                    while s.flag_c1:
                        RestartGame()
                    s_open_box_2(s_box_c1, s.flag_b1, s.flag_b2, s.flag_c2, s.flag_d2, s.flag_d1)
                    s.start_flag = False
                else:
                    GameOver()

    def on_d1():
        if os.path.exists('C:/MihaSoft Files/SoundFlagFile.miha'):
            Beep(300, 50)
        if s.global_flag and not s.to_flags_list[15]:
            if not s.flag_d1:
                if s.start_flag:
                    s.start_flag = False
                s_open_box_2(s_box_d1, s.flag_c1, s.flag_c2, s.flag_d2, s.flag_e2, s.flag_e1)

            else:
                if s.start_flag:
                    while s.flag_d1:
                        RestartGame()
                    s_open_box_2(s_box_d1, s.flag_c1, s.flag_c2, s.flag_d2, s.flag_e2, s.flag_e1)
                    s.start_flag = False
                else:
                    GameOver()

    def on_e2():
        if os.path.exists('C:/MihaSoft Files/SoundFlagFile.miha'):
            Beep(300, 50)
        if s.global_flag and not s.to_flags_list[21]:
            if not s.flag_e2:
                if s.start_flag:
                    s.start_flag = False
                s_open_box_2(s_box_e2, s.flag_e1, s.flag_d1, s.flag_d2, s.flag_d3, s.flag_e3)

            else:
                if s.start_flag:
                    while s.flag_e2:
                        RestartGame()
                    s_open_box_2(s_box_e2, s.flag_e1, s.flag_d1, s.flag_d2, s.flag_d3, s.flag_e3)
                    s.start_flag = False
                else:
                    GameOver()

    def on_e3():
        if os.path.exists('C:/MihaSoft Files/SoundFlagFile.miha'):
            Beep(300, 50)
        if s.global_flag and not s.to_flags_list[22]:
            if not s.flag_e3:
                if s.start_flag:
                    s.start_flag = False
                s_open_box_2(s_box_e3, s.flag_e2, s.flag_d2, s.flag_d3, s.flag_d4, s.flag_e4)

            else:
                if s.start_flag:
                    while s.flag_e3:
                        RestartGame()
                    s_open_box_2(s_box_e3, s.flag_e2, s.flag_d2, s.flag_d3, s.flag_d4, s.flag_e4)
                    s.start_flag = False
                else:
                    GameOver()

    def on_e4():
        if os.path.exists('C:/MihaSoft Files/SoundFlagFile.miha'):
            Beep(300, 50)
        if s.global_flag and not s.to_flags_list[23]:
            if not s.flag_e4:
                if s.start_flag:
                    s.start_flag = False
                s_open_box_2(s_box_e4, s.flag_e3, s.flag_d3, s.flag_d4, s.flag_d5, s.flag_e5)

            else:
                if s.start_flag:
                    while s.flag_e4:
                        RestartGame()
                    s_open_box_2(s_box_e4, s.flag_e3, s.flag_d3, s.flag_d4, s.flag_d5, s.flag_e5)
                    s.start_flag = False
                else:
                    GameOver()

    def on_b5():
        if os.path.exists('C:/MihaSoft Files/SoundFlagFile.miha'):
            Beep(300, 50)
        if s.global_flag and not s.to_flags_list[9]:
            if not s.flag_b5:
                if s.start_flag:
                    s.start_flag = False
                s_open_box_2(s_box_b5, s.flag_a5, s.flag_a4, s.flag_b4, s.flag_c4, s.flag_c5)

            else:
                if s.start_flag:
                    while s.flag_b5:
                        RestartGame()
                    s_open_box_2(s_box_b5, s.flag_a5, s.flag_a4, s.flag_b4, s.flag_c4, s.flag_c5)
                    s.start_flag = False
                else:
                    GameOver()

    def on_c5():
        if os.path.exists('C:/MihaSoft Files/SoundFlagFile.miha'):
            Beep(300, 50)
        if s.global_flag and not s.to_flags_list[14]:
            if not s.flag_c5:
                if s.start_flag:
                    s.start_flag = False
                s_open_box_2(s_box_c5, s.flag_b5, s.flag_b4, s.flag_c4, s.flag_d4, s.flag_d5)

            else:
                if s.start_flag:
                    while s.flag_c5:
                        RestartGame()
                    s_open_box_2(s_box_c5, s.flag_b5, s.flag_b4, s.flag_c4, s.flag_d4, s.flag_d5)
                    s.start_flag = False
                else:
                    GameOver()

    def on_d5():
        if os.path.exists('C:/MihaSoft Files/SoundFlagFile.miha'):
            Beep(300, 50)
        if s.global_flag and not s.to_flags_list[19]:
            if not s.flag_d5:
                if s.start_flag:
                    s.start_flag = False
                s_open_box_2(s_box_d5, s.flag_c5, s.flag_c4, s.flag_d4, s.flag_e4, s.flag_e5)

            else:
                if s.start_flag:
                    while s.flag_d5:
                        RestartGame()
                    s_open_box_2(s_box_d5, s.flag_c5, s.flag_c4, s.flag_d4, s.flag_e4, s.flag_e5)
                    s.start_flag = False
                else:
                    GameOver()

    def s_open_box_3(box, flag_1, flag_2, flag_3, flag_4, flag_5, flag_6, flag_7, flag_8):
        k = 0
        listok = [flag_1, flag_2, flag_3, flag_4, flag_5, flag_6, flag_7, flag_8]
        for j in range(len(listok)):
            if listok[j]:
                k += 1
        box.configure(text=k, bg='white')
        CheckWin()

    def on_b2():
        if os.path.exists('C:/MihaSoft Files/SoundFlagFile.miha'):
            Beep(300, 50)
        if s.global_flag and not s.to_flags_list[6]:
            if not s.flag_b2:
                if s.start_flag:
                    s.start_flag = False
                s_open_box_3(s_box_b2, s.flag_a1, s.flag_a2, s.flag_a3, s.flag_b3, s.flag_c3, s.flag_c2,
                             s.flag_c1, s.flag_b1)

            else:
                if s.start_flag:
                    while s.flag_b2:
                        RestartGame()
                    s_open_box_3(s_box_b2, s.flag_a1, s.flag_a2, s.flag_a3, s.flag_b3, s.flag_c3, s.flag_c2,
                                 s.flag_c1, s.flag_b1)
                    s.start_flag = False
                else:
                    GameOver()

    def on_b3():
        if os.path.exists('C:/MihaSoft Files/SoundFlagFile.miha'):
            Beep(300, 50)
        if s.global_flag and not s.to_flags_list[7]:
            if not s.flag_b3:
                if s.start_flag:
                    s.start_flag = False
                s_open_box_3(s_box_b3, s.flag_a2, s.flag_a3, s.flag_a4, s.flag_b4, s.flag_c4, s.flag_c3, s.flag_c2,
                             s.flag_b2)

            else:
                if s.start_flag:
                    while s.flag_b3:
                        RestartGame()
                    s_open_box_3(s_box_b3, s.flag_a2, s.flag_a3, s.flag_a4, s.flag_b4, s.flag_c4, s.flag_c3, s.flag_c2,
                                 s.flag_b2)
                    s.start_flag = False
                else:
                    GameOver()

    def on_b4():
        if os.path.exists('C:/MihaSoft Files/SoundFlagFile.miha'):
            Beep(300, 50)
        if s.global_flag and not s.to_flags_list[8]:
            if not s.flag_b4:
                if s.start_flag:
                    s.start_flag = False
                s_open_box_3(s_box_b4, s.flag_a3, s.flag_a4, s.flag_a5, s.flag_b5, s.flag_c5, s.flag_c4, s.flag_c3,
                             s.flag_b3)

            else:
                if s.start_flag:
                    while s.flag_b4:
                        RestartGame()
                    s_open_box_3(s_box_b4, s.flag_a3, s.flag_a4, s.flag_a5, s.flag_b5, s.flag_c5, s.flag_c4, s.flag_c3,
                                 s.flag_b3)
                    s.start_flag = False
                else:
                    GameOver()

    def on_c2():
        if os.path.exists('C:/MihaSoft Files/SoundFlagFile.miha'):
            Beep(300, 50)
        if s.global_flag and not s.to_flags_list[11]:
            if not s.flag_c2:
                if s.start_flag:
                    s.start_flag = False
                s_open_box_3(s_box_c2, s.flag_b1, s.flag_b2, s.flag_b3, s.flag_c3, s.flag_d3, s.flag_d2, s.flag_d1,
                             s.flag_c1)

            else:
                if s.start_flag:
                    while s.flag_c2:
                        RestartGame()
                    s_open_box_3(s_box_c2, s.flag_b1, s.flag_b2, s.flag_b3, s.flag_c3, s.flag_d3, s.flag_d2, s.flag_d1,
                                 s.flag_c1)
                    s.start_flag = False
                else:
                    GameOver()

    def on_c3():
        if os.path.exists('C:/MihaSoft Files/SoundFlagFile.miha'):
            Beep(300, 50)
        if s.global_flag and not s.to_flags_list[12]:
            if not s.flag_c3:
                if s.start_flag:
                    s.start_flag = False
                s_open_box_3(s_box_c3, s.flag_b2, s.flag_b3, s.flag_b4, s.flag_c4, s.flag_d4, s.flag_d3, s.flag_d2,
                             s.flag_c2)

            else:
                if s.start_flag:
                    while s.flag_c3:
                        RestartGame()
                    s_open_box_3(s_box_c3, s.flag_b2, s.flag_b3, s.flag_b4, s.flag_c4, s.flag_d4, s.flag_d3, s.flag_d2,
                                 s.flag_c2)
                    s.start_flag = False
                else:
                    GameOver()

    def on_c4():
        if os.path.exists('C:/MihaSoft Files/SoundFlagFile.miha'):
            Beep(300, 50)
        if s.global_flag and not s.to_flags_list[13]:
            if not s.flag_c4:
                if s.start_flag:
                    s.start_flag = False
                s_open_box_3(s_box_c4, s.flag_b3, s.flag_b4, s.flag_b5, s.flag_c5, s.flag_d5, s.flag_d4, s.flag_d3,
                             s.flag_c3)

            else:
                if s.start_flag:
                    while s.flag_c4:
                        RestartGame()
                    s_open_box_3(s_box_c4, s.flag_b3, s.flag_b4, s.flag_b5, s.flag_c5, s.flag_d5, s.flag_d4, s.flag_d3,
                                 s.flag_c3)
                    s.start_flag = False
                else:
                    GameOver()

    def on_d2():
        if os.path.exists('C:/MihaSoft Files/SoundFlagFile.miha'):
            Beep(300, 50)
        if s.global_flag and not s.to_flags_list[16]:
            if not s.flag_d2:
                if s.start_flag:
                    s.start_flag = False
                s_open_box_3(s_box_d2, s.flag_c1, s.flag_c2, s.flag_c3, s.flag_d3, s.flag_e3, s.flag_e2, s.flag_e1,
                             s.flag_d1)

            else:
                if s.start_flag:
                    while s.flag_d2:
                        RestartGame()
                    s_open_box_3(s_box_d2, s.flag_c1, s.flag_c2, s.flag_c3, s.flag_d3, s.flag_e3, s.flag_e2, s.flag_e1,
                                 s.flag_d1)
                    s.start_flag = False
                else:
                    GameOver()

    def on_d3():
        if os.path.exists('C:/MihaSoft Files/SoundFlagFile.miha'):
            Beep(300, 50)
        if s.global_flag and not s.to_flags_list[17]:
            if not s.flag_d3:
                if s.start_flag:
                    s.start_flag = False
                s_open_box_3(s_box_d3, s.flag_c2, s.flag_c3, s.flag_c4, s.flag_d4, s.flag_e4, s.flag_e3, s.flag_e2,
                             s.flag_d2)

            else:
                if s.start_flag:
                    while s.flag_d3:
                        RestartGame()
                    s_open_box_3(s_box_d3, s.flag_c2, s.flag_c3, s.flag_c4, s.flag_d4, s.flag_e4, s.flag_e3, s.flag_e2,
                                 s.flag_d2)
                    s.start_flag = False
                else:
                    GameOver()

    def on_d4():
        if os.path.exists('C:/MihaSoft Files/SoundFlagFile.miha'):
            Beep(300, 50)
        if s.global_flag and not s.to_flags_list[18]:
            if not s.flag_d4:
                if s.start_flag:
                    s.start_flag = False
                s_open_box_3(s_box_d4, s.flag_c3, s.flag_c4, s.flag_c5, s.flag_d5, s.flag_e5, s.flag_e4, s.flag_e3,
                             s.flag_d3)

            else:
                if s.start_flag:
                    while s.flag_d4:
                        RestartGame()
                    s_open_box_3(s_box_d4, s.flag_c3, s.flag_c4, s.flag_c5, s.flag_d5, s.flag_e5, s.flag_e4, s.flag_e3,
                                 s.flag_d3)
                    s.start_flag = False
                else:
                    GameOver()

    def Statistics():
        def CleanStat():
            s_stats_start_list = [0, 0]
            save('C:/MihaSoft Files/SaperStat', s_stats_start_list)
            s.stat_window.destroy()

        def Close():
            s.stat_window.destroy()

        def s_create_stat_window():
            s.stat_window = Toplevel()
            center_window(s.stat_window, 200, 220)
            s.stat_window.resizable(False, False)
            s.stat_window.title('Статистика')

            first_label = Label(s.stat_window, text='Побед:')
            first_label.place(x=5, y=5)

            second_label = Label(s.stat_window, text='Всего игр:')
            second_label.place(x=5, y=50)

            third_label = Label(s.stat_window, text='Процент выигрышей:')
            third_label.place(x=5, y=95)

            s_stat_list = load('C:/MihaSoft Files/SaperStat.npy')

            if s_stat_list[0] == 0:
                percent = '0%'

            else:
                percent = str(int((s_stat_list[1] / s_stat_list[0]) * 100)) + '%'

            wins = Label(s.stat_window, text=s_stat_list[1])
            wins.place(x=150, y=5)

            games = Label(s.stat_window, text=s_stat_list[0])
            games.place(x=150, y=50)

            percents = Label(s.stat_window, text=percent)
            percents.place(x=150, y=95)

            clean_button = Button(s.stat_window, text='Очистить статистику', bg='#db9c9c', command=CleanStat)
            clean_button.place(x=30, y=135)

            close_button = Button(s.stat_window, text='ОК', bg='#b6e0e0', width=16, command=Close)
            close_button.place(x=32, y=170)

        try:
            s.stat_window.resizable(False, False)

        except AttributeError:
            s_create_stat_window()

        except TclError:
            s_create_stat_window()

    def s_params():
        def s_params_abort():
            s.params_window.destroy()

        def s_create_par_window():
            def s_params_ok():
                s.number_of_mines = int(s_params_combobox.get())
                RestartGame()
                s.params_window.destroy()

            s.params_window = Toplevel()
            center_window(s.params_window, 180, 100)
            s.params_window.resizable(False, False)
            s.params_window.title('Параметры')

            s_p_m = []
            for i in range(1, 24):
                s_p_m.append(str(i))

            s_params_label = Label(s.params_window, text='Выберите число мин:')
            s_params_label.place(x=5, y=5)

            s_params_combobox = ttk.Combobox(s.params_window, values=s_p_m, state='readonly')
            s_params_combobox.place(x=10, y=30)

            s_params_ok_button = Button(s.params_window, text='OK', width=6, command=s_params_ok)
            s_params_ok_button.place(x=10, y=60)

            s_params_abort_button = Button(s.params_window, text='Отмена', width=6, command=s_params_abort)
            s_params_abort_button.place(x=95, y=60)

        try:
            s.params_window.resizable(False, False)

        except AttributeError:
            s_create_par_window()

        except TclError:
            s_create_par_window()

    if not os.path.exists('C:/MihaSoft Files/SaperStat.npy'):
        s_stat_start_list = [0, 0]
        save('C:/MihaSoft Files/SaperStat', s_stat_start_list)

    center_window(root, 430, 450)
    m.window.configure(width=430, height=450)
    root.title('Saper 2.0')
    root.minsize(430, 450)

    s_title = Label(m.window, text='Saper 2.0', font=('Arial Bold', 16), fg='red')
    s_title.place(x=50, y=10)

    s_box_a1 = Button(m.window, width=6, height=3, bg='#7a9cd6', command=on_a1)
    s_box_a1.place(x=80, y=100)

    s_box_a2 = Button(m.window, width=6, height=3, bg='#7a9cd6', command=on_a2)
    s_box_a2.place(x=132, y=100)

    s_box_a3 = Button(m.window, width=6, height=3, bg='#7a9cd6', command=on_a3)
    s_box_a3.place(x=184, y=100)

    s_box_a4 = Button(m.window, width=6, height=3, bg='#7a9cd6', command=on_a4)
    s_box_a4.place(x=236, y=100)

    s_box_a5 = Button(m.window, width=6, height=3, bg='#7a9cd6', command=on_a5)
    s_box_a5.place(x=288, y=100)

    s_box_b1 = Button(m.window, width=6, height=3, bg='#7a9cd6', command=on_b1)
    s_box_b1.place(x=80, y=156)

    s_box_b2 = Button(m.window, width=6, height=3, bg='#7a9cd6', command=on_b2)
    s_box_b2.place(x=132, y=156)

    s_box_b3 = Button(m.window, width=6, height=3, bg='#7a9cd6', command=on_b3)
    s_box_b3.place(x=184, y=156)

    s_box_b4 = Button(m.window, width=6, height=3, bg='#7a9cd6', command=on_b4)
    s_box_b4.place(x=236, y=156)

    s_box_b5 = Button(m.window, width=6, height=3, bg='#7a9cd6', command=on_b5)
    s_box_b5.place(x=288, y=156)

    s_box_c1 = Button(m.window, width=6, height=3, bg='#7a9cd6', command=on_c1)
    s_box_c1.place(x=80, y=212)

    s_box_c2 = Button(m.window, width=6, height=3, bg='#7a9cd6', command=on_c2)
    s_box_c2.place(x=132, y=212)

    s_box_c3 = Button(m.window, width=6, height=3, bg='#7a9cd6', command=on_c3)
    s_box_c3.place(x=184, y=212)

    s_box_c4 = Button(m.window, width=6, height=3, bg='#7a9cd6', command=on_c4)
    s_box_c4.place(x=236, y=212)

    s_box_c5 = Button(m.window, width=6, height=3, bg='#7a9cd6', command=on_c5)
    s_box_c5.place(x=288, y=212)

    s_box_d1 = Button(m.window, width=6, height=3, bg='#7a9cd6', command=on_d1)
    s_box_d1.place(x=80, y=268)

    s_box_d2 = Button(m.window, width=6, height=3, bg='#7a9cd6', command=on_d2)
    s_box_d2.place(x=132, y=268)

    s_box_d3 = Button(m.window, width=6, height=3, bg='#7a9cd6', command=on_d3)
    s_box_d3.place(x=184, y=268)

    s_box_d4 = Button(m.window, width=6, height=3, bg='#7a9cd6', command=on_d4)
    s_box_d4.place(x=236, y=268)

    s_box_d5 = Button(m.window, width=6, height=3, bg='#7a9cd6', command=on_d5)
    s_box_d5.place(x=288, y=268)

    s_box_e1 = Button(m.window, width=6, height=3, bg='#7a9cd6', command=on_e1)
    s_box_e1.place(x=80, y=324)

    s_box_e2 = Button(m.window, width=6, height=3, bg='#7a9cd6', command=on_e2)
    s_box_e2.place(x=132, y=324)

    s_box_e3 = Button(m.window, width=6, height=3, bg='#7a9cd6', command=on_e3)
    s_box_e3.place(x=184, y=324)

    s_box_e4 = Button(m.window, width=6, height=3, bg='#7a9cd6', command=on_e4)
    s_box_e4.place(x=236, y=324)

    s_box_e5 = Button(m.window, width=6, height=3, bg='#7a9cd6', command=on_e5)
    s_box_e5.place(x=288, y=324)

    restart_button = Button(m.window, text='Новая игра', width=10, bg='#93e6a8', font=('Arial Bold', 12),
                            command=RestartGame)
    restart_button.place(x=300, y=10)

    info_label = Label(m.window, font=('Arial Bold', 16))
    info_label.place(x=138, y=400)

    stat_button = Button(m.window, text='Статистика', width=10, bg='#d9c786', font=('Arial Bold', 12),
                         command=Statistics)
    stat_button.place(x=180, y=10)

    param_button = Button(m.window, text='Параметры', width=10, bg='#a8a8a8', font=('Arial Bold', 12), command=s_params)
    param_button.place(x=300, y=50)

    NewGame()

    s_box_a1.bind('<Button-3>', to_flag_1)
    s_box_a2.bind('<Button-3>', to_flag_2)
    s_box_a3.bind('<Button-3>', to_flag_3)
    s_box_a4.bind('<Button-3>', to_flag_4)
    s_box_a5.bind('<Button-3>', to_flag_5)
    s_box_b1.bind('<Button-3>', to_flag_6)
    s_box_b2.bind('<Button-3>', to_flag_7)
    s_box_b3.bind('<Button-3>', to_flag_8)
    s_box_b4.bind('<Button-3>', to_flag_9)
    s_box_b5.bind('<Button-3>', to_flag_10)
    s_box_c1.bind('<Button-3>', to_flag_11)
    s_box_c2.bind('<Button-3>', to_flag_12)
    s_box_c3.bind('<Button-3>', to_flag_13)
    s_box_c4.bind('<Button-3>', to_flag_14)
    s_box_c5.bind('<Button-3>', to_flag_15)
    s_box_d1.bind('<Button-3>', to_flag_16)
    s_box_d2.bind('<Button-3>', to_flag_17)
    s_box_d3.bind('<Button-3>', to_flag_18)
    s_box_d4.bind('<Button-3>', to_flag_19)
    s_box_d5.bind('<Button-3>', to_flag_20)
    s_box_e1.bind('<Button-3>', to_flag_21)
    s_box_e2.bind('<Button-3>', to_flag_22)
    s_box_e3.bind('<Button-3>', to_flag_23)
    s_box_e4.bind('<Button-3>', to_flag_24)
    s_box_e5.bind('<Button-3>', to_flag_25)
    off = Button(m.window, text='⌂', font=('Arial Bold', 15), width=2, height=1, bg='black', fg='white',
                 command=Return)
    off.place(x=0, y=5)
    ToolTip(off, 'На главную...')
