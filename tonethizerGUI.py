from pydub import AudioSegment
from pydub.playback import play
from pydub.generators import Sine
import threading
import tkinter
from tkinter import *
from tkinter import messagebox, filedialog

def play_sound():
    global result
    result = AudioSegment.silent(duration=0)
    t=int(tmes.get())
    f=float(freq.get())
    fi=float(fadein.get())
    fo=float(fadeo.get())
    if t>0:
        try:
            for n in range(t):
                gen = Sine(f*n)
                sine = gen.to_audio_segment(duration=t)
                sine = sine.fade_in(fi).fade_out(fo)
                result+=sine
            play(result)
        except:
            messagebox.showwarning("ERROR","ALGO SALIÓ MAL")
            result = ""

def guardar():
    if result != "":
        arch=filedialog.asksaveasfilename(initialdir="/",
                    title="Guardar en",defaultextension=".mp3")
        result.export(arch,format="mp3")

def inicia(i):
    t = threading.Thread(target=l_f[i])
    t.start()
    
root = tkinter.Tk()
root.title("ToneThizer")
root.configure(background="gray45")
root.geometry("300x300")
times = IntVar()
frequency = DoubleVar()
fadein = DoubleVar()
fadeon = DoubleVar()
result = ""
l_f = [lambda:play_sound(),lambda:guardar()]

tmes=Entry(root,textvariable=times,bg="khaki",width=20)
tmes.place(x=120,y=40)
freq=Entry(root,textvariable=frequency,bg="khaki",width=20)
freq.place(x=120,y=80)
fadei=Entry(root,textvariable=fadein,bg="khaki",width=20)
fadei.place(x=120,y=120)
fadeo=Entry(root,textvariable=fadeon,bg="khaki",width=20)
fadeo.place(x=120,y=160)

Button(root,text="PLAY",command=lambda:inicia(0)).place(x=60,y=190)
Button(root,text="SAVE",command=lambda:inicia(1)).place(x=60,y=220)

root.mainloop()



