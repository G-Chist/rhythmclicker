import time
import random
import tkinter
from pygame import mixer
import keyboard

from clickerexterior import *
from songanalyzer import *
from menu import *

def rgbtohex(r,g,b):
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
    start_time = time.time()*1000
    # Цикл ожидания (5 секунд)
    while time.time()*1000 - start_time <= n*1000:
        root.update()
        # Обратный отсчёт
        btnscore.configure(text=str(n - int((time.time()*1000 - start_time) / 1000)))
    btnscore.configure(text="0")

last_clicked = 0

def playGame(gamearr, timeout, waiting):
    global last_clicked
    clicked_array = [False, False, False, False, False, False, False, False, False]

    def clicked(a):
        global last_clicked
        if time.time() * 1000 - last_clicked > too_fast:
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
    mixer.music.load(song_name)
    print("Game initialized!")

    waitNsecs(waiting)

    start_time = time.time()*1000
    prevrb = -1
    tcount = 0

    mixer.music.play()
    playing = True

    # Основной цикл
    while time.time()*1000 - start_time <= timeout*1000 and playing:

        try:
            root.update()

            cou = 0
            for j in button_array:
                cou += 1
                if keyboard.is_pressed(j['text']):
                    clicked(cou)

            currtime = time.time() * 1000

            if int(currtime - start_time) in gamearr:

                for i in button_array:
                    i.configure(bg="white")

                rb = random.randint(0, 8)
                while rb == prevrb:
                    rb = random.randint(0, 8)

                btn_start_time = time.time()*1000
                prevrb = rb
                clicked_array = [False, False, False, False, False, False, False, False, False]

            # Кнопка меняет цвет со временем
            if prevrb >= 0 and not clicked_array[rb]:
                diff = int(time.time()*1000 - btn_start_time)
                button_array[prevrb].configure(bg=rgbtohex(0 + diff / 4, 255 - diff / 4, 0))

        except tkinter.TclError:
            playing = False
