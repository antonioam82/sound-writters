from pydub import AudioSegment
from pydub.playback import play
from pydub.generators import Sine, Square
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
    try:
        t=int(tmes.get())
        f=float(freq.get())
        fi=float(fadein.get())
        fo=float(fadeo.get())
        g =float(gaine.get())
    except:
        pass
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
        try:
            arch=filedialog.asksaveasfilename(initialdir="/",
                    title="Guardar en",defaultextension="."+formato)
            if arch != "":
                result.export(arch,format=formato)
                messagebox.showinfo("GUARDADO","Audio guardado correctamente.")
        except:
            messagebox.showwarning("ERROR","ALGO SALIÓ MAL")

def inicia(i,*args):
    global formato
    for arg in args:
        formato = arg
    t = threading.Thread(target=l_f[i])
    t.start()
    
root = tkinter.Tk()
root.title("ToneThizer")
root.configure(background="Slate Gray3")
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
tmes.place(x=120,y=20)
freq=Entry(root,textvariable=frequency,bg="khaki",width=20,validate="key",validatecommand=(validatecommand, "%S"))
freq.place(x=120,y=60)
fadei=Entry(root,textvariable=fadein,bg="khaki",width=20,validate="key",validatecommand=(validatecommand, "%S"))
fadei.place(x=120,y=100)
fadeo=Entry(root,textvariable=fadeon,bg="khaki",width=20,validate="key",validatecommand=(validatecommand, "%S"))
fadeo.place(x=120,y=140)
gaine=Entry(root,textvariable=ga,bg="khaki",width=20,validate="key",validatecommand=(validatecommandII, "%S"))
gaine.place(x=120,y=180)
Label(root,text="DURATION:",bg="Slate Gray3").place(x=50,y=20)
Label(root,text="FREQUENCY:",bg="Slate Gray3").place(x=42,y=60)
Label(root,text="FADE IN:",bg="Slate Gray3").place(x=64,y=100)
Label(root,text="FADE OUT:",bg="Slate Gray3").place(x=54,y=140)
Label(root,text="GAIN:",bg="Slate Gray3").place(x=80,y=180)

Button(root,text="PLAY",width=8,command=lambda:inicia(0)).place(x=60,y=230)
Button(root,text=".WAV",width=8,command=lambda:inicia(1,"wav")).place(x=200,y=230)
Button(root,text=".MP3",width=8,command=lambda:inicia(1,"mp3")).place(x=200,y=260)
Label(root,text="SAVE AS:",bg="Slate Gray3",fg="black").place(x=200,y=208)
btnMode=Button(root,text="MODE A",width=8,command=change_mode)
btnMode.place(x=60,y=260)

root.mainloop()



