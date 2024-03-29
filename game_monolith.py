import tkinter as tk

import keyboard
import librosa
import time
import random
import pygame.mixer as mixer
import tkinter.filedialog as fd

gameactive = True
filename = False
menuactive = True
waiting = 3

while gameactive:

    def exitgame():
        global gameactive
        global menuactive
        gameactive = False
        menuactive = False
        menuwindow.destroy()

    def choosing():
        global filename
        types = [(".wav audio files", "*.wav"), ("All files", "*.*")]
        filename = fd.askopenfilename(title="Open file", initialdir="", filetypes=types)
        if filename:
            print("Chosen file: ", filename)
            menuwindow.destroy()

    filename = False
    menuwindow = tk.Tk()
    choosesong = tk.Button(menuwindow, width=15, height=5, text="Play", font=("Arial", "14"), command=choosing)
    choosesong.grid(row=1, column=1)

    transcrsong = tk.Button(menuwindow, width=15, height=5, text="Transcribe", font=("Arial", "14"))
    transcrsong.configure(state="disabled")
    transcrsong.grid(row=2, column=1)

    exitbutton = tk.Button(menuwindow, width=15, height=5, text="Exit", font=("Arial", "14"), command=exitgame)
    exitbutton.grid(row=3, column=1)


    def on_closing():
        global gameactive
        global menuactive
        if tk.messagebox.askokcancel("Quit", "Do you want to quit?"):
            gameactive = False
            menuactive = False
            menuwindow.destroy()


    menuwindow.protocol("WM_DELETE_WINDOW", on_closing)

    while not filename and menuactive:
        try:
            menuwindow.update()
        except tk.TclError:
            pass

    if gameactive:

        start_time = time.time()

        # Название файла с песней
        song_name = filename
        # Чем ниже коэффициент k, тем строже отбор нот
        k = 0.77
        # Минимальная частота смены нот (в миллисекундах)
        too_fast = 200

        print("Song analysis started!")
        x, sr = librosa.load(song_name)
        X = librosa.stft(x)
        Xdb = librosa.amplitude_to_db(abs(X))

        # Массив с моментами времени, каждый элемент равен 23*i миллисекунд
        times = librosa.times_like(Xdb)

        # В массиве Xdb меняются местами столбцы и строки, новый массив называется spectro
        spectro = []
        for i in range(len(Xdb[0])):
            spectro.append([])
        for i in range(len(spectro)):
            for j in Xdb:
                spectro[i].append(j[i])

        # Каждый элемент массива spectro - среднее арифметическое своих элементов со знаком +
        for i in range(len(spectro)):
            spectro[i] = abs(sum(spectro[i]) / len(spectro[i]))

        # Нота появляется, если значение спектра в данный момент ниже среднего * k
        timearr = []
        c = 0
        for i in range(len(spectro)):
            fragment = c // 100
            # Среднее значение вычисляется каждые 2,3 секунды
            mean = sum(spectro[fragment:fragment + 1:]) / len(spectro[fragment:fragment + 1:])
            # print(mean)
            if spectro[i] < mean * k:
                timearr.append(int(times[i] * 1000))
            c += 1

        #Самые резкие появления нот убираются с учётом минимальной частоты смены нот
        for i in range(len(timearr) - 1):
            if timearr[i + 1] - timearr[i] < too_fast:
                timearr[i + 1] = timearr[i]

        #print(timearr)

        print("Song analysis time: ", time.time() - start_time, " seconds")
        print("Song analysis time per 1 second: ", (time.time() - start_time) / (len(times) * 0.023), " seconds")

        clicked_array = [False, False, False, False, False, False, False, False, False]

        root = tk.Tk()

        clicked_array = [False, False, False, False, False, False, False, False, False]

        btnscore = tk.Button(root, width=30, height=2, text="0", font=("Arial", "14"))
        btnscore.grid(row=1, column=1, columnspan=3)

        btn1 = tk.Button(root, width=8, height=4, text="Q")
        btn2 = tk.Button(root, width=8, height=4, text="W")
        btn3 = tk.Button(root, width=8, height=4, text="E")
        btn4 = tk.Button(root, width=8, height=4, text="A")
        btn5 = tk.Button(root, width=8, height=4, text="S")
        btn6 = tk.Button(root, width=8, height=4, text="D")
        btn7 = tk.Button(root, width=8, height=4, text="Z")
        btn8 = tk.Button(root, width=8, height=4, text="X")
        btn9 = tk.Button(root, width=8, height=4, text="C")

        keys_array = ['q', 'w', 'e',
                      'a', 's', 'd',
                      'z', 'x', 'c']

        button_array = [btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8, btn9]

        # Размещение кнопок в таблице 3х3
        c = 0
        for i in range(2, 5):
            for j in range(1, 4):
                button_array[c].grid(row=i, column=j)
                button_array[c].configure(bg="white")
                button_array[c].configure(font=("Arial", "16"))
                c += 1


        def rgbtohex(r, g, b):
            r = int(r)
            g = int(g)
            b = int(b)

            if r < 0:
                r = 0
            if r > 255:
                r = 255

            if g < 0:
                g = 0
            if g > 255:
                g = 255

            if b < 0:
                b = 0
            if b > 255:
                b = 255

            return f'#{r:02x}{g:02x}{b:02x}'


        def waitNsecs(n):
            start_time = time.time() * 1000
            # Цикл ожидания (5 секунд)
            while time.time() * 1000 - start_time <= n * 1000:
                root.update()
                # Обратный отсчёт
                btnscore.configure(text=str(n - int((time.time() * 1000 - start_time) / 1000)))
            btnscore.configure(text="0")

        last_clicked = 0
        def clicked(a):
            global last_clicked
            if not clicked_array[rb]:
                print("Button ", a, " clicked")
                clicked_array[a - 1] = True
                try:
                    # Если нажата нужная кнопка, добавляются очки
                    if a - 1 == rb:
                        clicktime = int(time.time() * 1000 - btn_start_time)
                        currscore = int(btnscore["text"])
                        btnscore.configure(text=str(1000 - clicktime + currscore))
                except NameError:
                    pass
            last_clicked = time.time() * 1000


        btn1.configure(command=lambda: clicked(1))
        btn2.configure(command=lambda: clicked(2))
        btn3.configure(command=lambda: clicked(3))
        btn4.configure(command=lambda: clicked(4))
        btn5.configure(command=lambda: clicked(5))
        btn6.configure(command=lambda: clicked(6))
        btn7.configure(command=lambda: clicked(7))
        btn8.configure(command=lambda: clicked(8))
        btn9.configure(command=lambda: clicked(9))
        mixer.init()
        mixer.music.load(filename)
        print("Game initialized!")

        playing = True

        try:
            waitNsecs(waiting)
        except tk.TclError:
            playing = False

        start_time = time.time() * 1000
        prevrb = -1
        tcount = 0

        if playing:
            mixer.music.play()

        # Основной цикл
        while time.time() * 1000 - start_time <= times[-1] * 1000 and playing:

            try:
                root.update()

                cou = 0
                for j in button_array:
                    cou += 1
                    if keyboard.is_pressed(j['text']):
                        clicked(cou)

                currtime = time.time() * 1000

                if int(currtime - start_time) in timearr:

                    for i in button_array:
                        i.configure(bg="white")

                    rb = random.randint(0, 8)
                    while rb == prevrb:
                        rb = random.randint(0, 8)

                    btn_start_time = time.time() * 1000
                    prevrb = rb
                    clicked_array = [False, False, False, False, False, False, False, False, False]

                # Кнопка меняет цвет со временем
                if prevrb >= 0 and not clicked_array[rb]:
                    diff = int(time.time() * 1000 - btn_start_time)
                    button_array[prevrb].configure(bg=rgbtohex(0 + diff / 4, 255 - diff / 4, 0))

            except tk.TclError:
                playing = False
                mixer.music.stop()
                mixer.music.unload()
                break

    print("Game finished!")

print("Game exited")
