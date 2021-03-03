from tkinter import *
from tkinter import ttk
from pydub import AudioSegment
from pydub.generators import Sine, Square, Triangle, Sawtooth
from pydub.playback import play

class app():
    def __init__(self):
        self.window = Tk()
        self.window.geometry("274x285")
        self.window.title("SBT")
        backgr = "light blue"
        self.window.configure(background=backgr)
        self.WaveForms = ["Sine","Square","Triangle","Sawtooth"]

        self.drlabel = Label(self.window,text="DURATION:",bg=backgr)
        self.drlabel.place(x=40,y=20)
        self.drentry = Entry(self.window,width=20)
        self.drentry.place(x=110,y=20)
        self.frlabel = Label(self.window,text="FREQUENCY:",bg=backgr)
        self.frlabel.place(x=33,y=70)
        self.frentry = Entry(self.window,width=20)
        self.frentry.place(x=110,y=70)
        self.wfentry = ttk.Combobox(self.window,width=17)
        self.wfentry.place(x=110,y=120)
        self.wflabel = Label(self.window,text="WAVEFORM:",bg=backgr)
        self.wflabel.place(x=33,y=120)
        self.wfentry["values"] = self.WaveForms
        self.btnplay = Button(self.window,text="PLAY",bg="light green",width=28)
        self.btnplay.place(x=33,y=190)
        self.btnsave = Button(self.window,text="SAVE",bg="gold3",width=28)
        self.btnsave.place(x=33,y=230)

        self.window.mainloop()

if __name__=="__main__":
    app()

