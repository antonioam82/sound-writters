from pydub import AudioSegment
from pydub.playback import play
from pydub.generators import Sine
import threading
import tkinter
from tkinter import *
from tkinter import messagebox, filedialog

def change_mode():
    global mode
    if mode == "A":
        print("fdfdf")
        btnMode.configure(text="MODE B")
        mode = "B"
    else:
        mode = "A"
        btnMode.configure(text="MODE A")

def valid_entry(char):
    return char in "0123456789."

def valid_entryI(char):
    return char in "0123456789"
    
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
                if mode == "A":
                    gen = Sine(f*n)
                else:
                    gen = Sine(f)
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
        if arch != "":
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
mode = "A"
l_f = [lambda:play_sound(),lambda:guardar()]
validatecommand = root.register(valid_entry)
validatecommandI = root.register(valid_entryI)

tmes=Entry(root,textvariable=times,bg="khaki",width=20,validate="key",validatecommand=(validatecommandI, "%S"))
tmes.place(x=120,y=40)
freq=Entry(root,textvariable=frequency,bg="khaki",width=20,validate="key",validatecommand=(validatecommand, "%S"))
freq.place(x=120,y=80)
fadei=Entry(root,textvariable=fadein,bg="khaki",width=20,validate="key",validatecommand=(validatecommand, "%S"))
fadei.place(x=120,y=120)
fadeo=Entry(root,textvariable=fadeon,bg="khaki",width=20,validate="key",validatecommand=(validatecommand, "%S"))
fadeo.place(x=120,y=160)

Button(root,text="PLAY",command=lambda:inicia(0)).place(x=60,y=190)
Button(root,text="SAVE",command=lambda:inicia(1)).place(x=60,y=220)
btnMode=Button(root,text="MODE A",command=change_mode)
btnMode.place(x=60,y=250)

root.mainloop()




