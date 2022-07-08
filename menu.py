import tkinter as tk
import tkinter.filedialog as fd

filename = False

def summon_menu():
    global filename

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

    menuwindow.mainloop()
