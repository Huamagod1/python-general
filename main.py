#Aqui van las actividades generales de la 1 a la 6
import os
os.system("cls")

while True:
    try:
       
      numero = int(input("Ingrese un valor numerico"))
      if numero % 2 ==0:
          
         inpar = 2*numero+1

    except:
        print("Ingrese una wea valida porfa ")
        