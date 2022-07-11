import tkinter as tk

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
