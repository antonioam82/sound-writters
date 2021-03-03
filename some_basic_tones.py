from tkinter import *
from pydub import AudioSegment
from pydub.generators import Sine, Square, Triangle
from pydub.playback import play

class app():
    def __init__(self):
        self.window = Tk()
        self.window.geometry("200x200")
        self.window.title("SBT")

        self.window.mainloop()

if __name__=="__main__":
    app()
