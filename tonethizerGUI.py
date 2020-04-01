from pydub import AudioSegment
from pydub.playback import play
from pydub.generators import Sine
import tkinter
from tkinter import *
from tkinter import messagebox, filedialog

def play_sound():
    result = AudioSegment.silent(duration=0)
    t=int(tmes.get())
    f=float(freq.get())
    fi=float(fadein.get())
    fo=float(fadeo.get())
    try:
        for n in range(t):
            gen = Sine(f*n)
            sine = gen.to_audio_segment(duration=t)
            sine = sine.fade_in(fi).fade_out(fo)
            result+=sine
        play(result)
    except:
        print("Algo salio mal")


root = tkinter.Tk()
root.title("ToneThizer")
root.configure(background="gray45")
root.geometry("300x300")
times = IntVar()
frequency = DoubleVar()
fadein = DoubleVar()
fadeon = DoubleVar()

tmes=Entry(root,textvariable=times,bg="khaki",width=20)
tmes.place(x=120,y=40)
freq=Entry(root,textvariable=frequency,bg="khaki",width=20)
freq.place(x=120,y=80)
fadei=Entry(root,textvariable=fadein,bg="khaki",width=20)
fadei.place(x=120,y=120)
fadeo=Entry(root,textvariable=fadeon,bg="khaki",width=20)
fadeo.place(x=120,y=160)

Button(root,text="PLAY",command=play_sound).place(x=60,y=190)

root.mainloop()

