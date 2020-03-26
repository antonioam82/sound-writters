from VALID import OKI, OK, enum
from pydub import AudioSegment
from pydub.playback import play
from pydub.generators import Sine
import matplotlib.pyplot as plt
import librosa.display
import os

op = ["GUARDAR Y CONTINUAR","GUARDAR Y CERRAR","CERRAR SIN GUARDAR","CONTINUAR SIN GUARDAR","CAMBIAR MODO"]
op2 = ["CONTINUAR","CERRAR","CAMBIAR MODO"]

if os.name == "posix":
   var = "clear"        
elif os.name == "ce" or os.name == "nt" or os.name == "dos":
   var = "cls"

def cambia_modo():
   global mode
   while True:
      mode = input("Mode: ")
      if mode == "A" or mode == "B":
         break

cambia_modo()

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
          if mode == "A":
             gen = Sine(f * n)#f
          else:
             gen = Sine(f)
          sine = gen.to_audio_segment(duration=t)
          sine = sine.fade_in(fi).fade_out(fo)
          result += sine
 
       print("REPRODUCIENDO RESULTADO EN MODO "+mode)
       play(result)
       
       print("\n----ESCOJA OPCIÓN----\n")
       opcion = enum(op)
       print("")

       if opcion == "CAMBIAR MODO":
          cambia_modo()
          continue
         
       if not "SIN GUARDAR" in opcion:
          print("Guardo")
          name = "audd"+"("+str(t)+","+str(f)+","+str(fi)+","+str(fo)+")"+".mp3"
          result.export(name,format="mp3")

    except:
       print("SE PRODUJO UN ERROR AL REALIZAR LA OPERACIÓN")
       print("\n----ESCOJA OPCIÓN----\n")
       opcion = enum(op2)

    if opcion == "CAMBIAR MODO":
       cambia_modo()
       
    if not "CERRAR" in opcion:
       os.system(var)
    else:
       break
    
    
    
