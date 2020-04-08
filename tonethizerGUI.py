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
        btnMode.configure(text="MODE B")
        mode = "B"
    else:
        mode = "A"
        btnMode.configure(text="MODE A")

def valid_entry(char):
    return char in "0123456789."

def valid_entryI(char):
    return char in "0123456789"

def valid_entryII(char):
    return char in "-0123456789."
    
def play_sound():
    global result
    result = AudioSegment.silent(duration=0)
    t=int(tmes.get())
    f=float(freq.get())
    fi=float(fadein.get())
    fo=float(fadeo.get())
    g = float(gaine.get())
    if t>0:
        try:
            for n in range(t):
                if mode == "A":
                    gen = Sine(f*n)#f*n)
                else:
                    gen = Sine(f)
                sine = gen.to_audio_segment(duration=t).apply_gain(g)
                sine = sine.fade_in(fi).fade_out(fo)
                result+=sine
            play(result)
        except:
            messagebox.showwarning("ERROR","ALGO SALIÓ MAL")
            result = ""

def guardar():
    if result != "":
        arch=filedialog.asksaveasfilename(initialdir="/",
                    title="Guardar en",defaultextension="."+formato)
        if arch != "":
            result.export(arch,format=formato)

def inicia(i,*args):
    global formato
    for arg in args:
        formato = arg
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
ga = DoubleVar()
result = ""
mode = "A"
l_f = [lambda:play_sound(),lambda:guardar()]
validatecommand = root.register(valid_entry)
validatecommandI = root.register(valid_entryI)
validatecommandII = root.register(valid_entryII)

tmes=Entry(root,textvariable=times,bg="khaki",width=20,validate="key",validatecommand=(validatecommandI, "%S"))
tmes.place(x=120,y=10)
freq=Entry(root,textvariable=frequency,bg="khaki",width=20,validate="key",validatecommand=(validatecommand, "%S"))
freq.place(x=120,y=50)
fadei=Entry(root,textvariable=fadein,bg="khaki",width=20,validate="key",validatecommand=(validatecommand, "%S"))
fadei.place(x=120,y=90)
fadeo=Entry(root,textvariable=fadeon,bg="khaki",width=20,validate="key",validatecommand=(validatecommand, "%S"))
fadeo.place(x=120,y=130)
gaine=Entry(root,textvariable=ga,bg="khaki",width=20,validate="key",validatecommand=(validatecommandII, "%S"))
gaine.place(x=120,y=170)

Button(root,text="PLAY",width=8,command=lambda:inicia(0)).place(x=60,y=220)
#Button(root,text="SAVE",command=lambda:inicia(1)).place(x=60,y=220)
Button(root,text=".WAV",width=8,command=lambda:inicia(1,"wav")).place(x=200,y=220)
Button(root,text=".MP3",width=8,command=lambda:inicia(1,"mp3")).place(x=200,y=250)
Label(root,text="SAVE AS:",bg="gray45",fg="white").place(x=200,y=198)
btnMode=Button(root,text="MODE A",width=8,command=change_mode)
btnMode.place(x=60,y=250)

root.mainloop()






