from pydub import AudioSegment
from pydub.playback import play
from pydub.generators import Sine
import tkinter
from tkinter import *
from tkinter import messagebox, filedialog

def play_sound():
    print("HELLO")


root = tkinter.Tk()
root.title("ToneThizer")
root.configure(background="gray45")
root.geometry("300x300")
times = IntVar()
#frequency = IntVar()
#fadein = IntVar()

Entry(root,textvariable=times,bg="khaki",width=20).place(x=120,y=40)
Entry(root,textvariable=times,bg="khaki",width=20).place(x=120,y=80)
Entry(root,textvariable=times,bg="khaki",width=20).place(x=120,y=120)
Entry(root,textvariable=times,bg="khaki",width=20).place(x=120,y=160)

Button(root,text="PLAY",command=play_sound).place(x=60,y=190)

root.mainloop()
