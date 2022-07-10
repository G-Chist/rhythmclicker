import tkinter as tk
import tkinter.filedialog as fd

filename = False
gameactive = True

def summon_menu():
    global filename
    global gameactive

    def exitgame():
        global gameactive
        gameactive = False
        menuwindow.destroy()

    def choosing():
        global filename
        types = [(".wav audio files", "*.wav"), ("All files", "*.*")]
        filename = fd.askopenfilename(title="Open file", initialdir="", filetypes=types)
        if filename:
            print("Chosen file: ", filename)
            menuwindow.destroy()

    menuwindow = tk.Tk()
    choosesong = tk.Button(menuwindow, width=15, height=5, text="Play", font=("Arial", "14"), command=choosing)
    choosesong.grid(row=1, column=1)

    transcrsong = tk.Button(menuwindow, width=15, height=5, text="Transcribe", font=("Arial", "14"))
    transcrsong.configure(state="disabled")
    transcrsong.grid(row=2, column=1)

    exitbutton = tk.Button(menuwindow, width=15, height=5, text="Exit", font=("Arial", "14"), command=exitgame)
    exitbutton.grid(row=3, column=1)

    def on_closing():
        if tk.messagebox.askokcancel("Quit", "Do you want to quit?"):
            global gameactive
            gameactive = False
            menuwindow.destroy()

    menuwindow.protocol("WM_DELETE_WINDOW", on_closing)

    menuwindow.mainloop()
