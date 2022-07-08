import tkinter as tk

root = tk.Tk()

clicked_array = [False, False, False, False, False, False, False, False, False]

btnscore = tk.Button(root, width=30, height=2, text="0", font=("Arial", "14"))
btnscore.grid(row=1, column=1, columnspan=3)

btn1 = tk.Button(root, width=16, height=8)
btn2 = tk.Button(root, width=16, height=8)
btn3 = tk.Button(root, width=16, height=8)
btn4 = tk.Button(root, width=16, height=8)
btn5 = tk.Button(root, width=16, height=8)
btn6 = tk.Button(root, width=16, height=8)
btn7 = tk.Button(root, width=16, height=8)
btn8 = tk.Button(root, width=16, height=8)
btn9 = tk.Button(root, width=16, height=8)

button_array = [btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8, btn9]

#Размещение кнопок в таблице 3х3
c = 0
for i in range(2, 5):
    for j in range(1, 4):
        button_array[c].grid(row=i, column=j)
        button_array[c].configure(bg="white")
        c += 1
