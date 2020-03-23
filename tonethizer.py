from VALID import OKI, ns, OK
from pydub import AudioSegment
from pydub.playback import play
from pydub.generators import Sine
import os

if os.name == "posix":
   var = "clear"        
elif os.name == "ce" or os.name == "nt" or os.name == "dos":
   var = "cls"

while True:
    print("        /\                                         /\        ")
    print("       /  \                                       /  \       ")
    print("______/    \  /\____T O N E - T H I Z E R____/\  /    \______")
    print("            \/                                 \/            \n")
    
    result = AudioSegment.silent(duration=0)
    t = abs(OKI(input("Times: ")))
    f = OK(input("Frequency adding: "))
    fi = OK(input("Fade in: "))#50
    fo = OK(input("Fade out: "))#100
    try:
        for n in range(t):
            gen = Sine(f * n)
            sine = gen.to_audio_segment(duration=t)
            sine = sine.fade_in(fi).fade_out(fo)
            result += sine
        print("REPRODUCIENDO RESULTADO...")
        play(result)
    
        guard = ns(input("¿Guardar sonido?(n/s): "))
        if guard == "s":
            name = "audd"+"("+str(t)+","+str(f)+","+str(fi)+","+str(fo)+")"+".mp3"
            result.export(name,format="mp3")
    except:
        print("SE HA PRODUCIDO UN ERROR")
        
    conti = ns(input("¿Continuar?(n/s): "))
    if conti == "n":
        break
    else:
        os.system(var)
    
    
    
