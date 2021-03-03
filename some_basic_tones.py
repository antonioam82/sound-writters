from tkinter import *
from tkinter import ttk
from pydub import AudioSegment
from pydub.generators import Sine, Square, Triangle, Sawtooth
from pydub.playback import play

class app():
    def __init__(self):
        self.window = Tk()
        self.window.geometry("400x400")
        self.window.title("SBT")
        self.WaveForms = ["Sine","Square","Triangle","Sawtooth"]

        self.drlabel = Label(self.window,text="DURATION:")
        self.drlabel.place(x=40,y=20)
        self.drentry = Entry(self.window,width=20)
        self.drentry.place(x=110,y=20)
        self.frlabel = Label(self.window,text="FREQUENCY:")
        self.frlabel.place(x=33,y=70)
        self.frentry = Entry(self.window,width=20)
        self.frentry.place(x=110,y=70)
        self.wfentry = ttk.Combobox(self.window,width=17)
        self.wfentry.place(x=110,y=120)
        self.wflabel = Label(self.window,text="WAVEFORM:")
        self.wflabel.place(x=33,y=120)
        self.wfentry["values"] = self.WaveForms

        self.window.mainloop()

if __name__=="__main__":
    app()


