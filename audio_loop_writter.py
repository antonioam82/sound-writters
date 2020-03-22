from VALID import OKI, ns, OK
from pydub import AudioSegment
from pydub.playback import play
from pydub.generators import Sine
import glob

def guardar(sound):
    grabs = glob.glob('*.mp3')
    count = 0
    for i in grabs:
        if "audd" in i:
            count+=1
    if count>0:
        sound.export("audd"+str(count)+".mp3",format="mp3")
    else:
        sound.export("audd.mp3",format="mp3")

while True:
    print("-----------------LOOP SOUND WRITTER-----------------\n")
    result = AudioSegment.silent(duration=0)
    t = OKI(input("Times: "))
    f = OK(input("Frequency adding: "))
    fi = OK(input("Fade in: "))#50
    fo = OK(input("Fade out: "))#100

    for n in range(t):
        gen = Sine(f * n)
        sine = gen.to_audio_segment(duration=t)
        sine = sine.fade_in(fi).fade_out(fo)
        result += sine
    print("REPRODUCIENDO RESULTADO...")
    play(result)
    
    guard = ns(input("¿Guardar sonido?(n/s): "))
    if guard == "s":
        guardar(result)
        
    conti = ns(input("¿Continuar?(n/s): "))
    if conti == "n":
        break
    
    
