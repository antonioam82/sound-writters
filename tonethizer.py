from VALID import OKI, OK, enum
from pydub import AudioSegment
from pydub.playback import play
from pydub.generators import Sine
import os

op = ["GUARDAR Y CONTINUAR","GUARDAR Y CERRAR","CERRAR SIN GUARDAR","CONTINUAR SIN GUARDAR"]
op2 = ["CONTINUAR","CERRAR"]

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
       
       print("\n----ESCOJA OPCIÓN----\n")
       opcion = enum(op)
       print("")
       
       if not "SIN GUARDAR" in opcion:
          name = "audd"+"("+str(t)+","+str(f)+","+str(fi)+","+str(fo)+")"+".mp3"
          result.export(name,format="mp3")

    except:
       print("SE PRODUJO UN ERROR AL REALIZAR LA OPERACIÓN")
       print("----\nESCOJA OPCIÓN----\n")
       opcion = enum(op2)
       
    if not "CERRAR" in opcion:
       os.system(var)
    else:
       break
    
    
    
