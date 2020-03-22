from VALID import OKI, ns
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
    f = OKI(input("Frequency adding: "))

    for n in range(t):
        gen = Sine(f * n)
        sine = gen.to_audio_segment(duration=t)
        sine = sine.fade_in(50).fade_out(100)
        result += sine
    print("REPRODUCIENDO RESULTADO...")
    play(result)
    guard = ns(input("¿Guardar archivo?(n/s): "))
    if guard == "s":
        guardar(result)
    conti = ns(input("¿Continuar?(n/s): "))
    if conti == "n":
        break
