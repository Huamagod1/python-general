#Aqui van las actividades generales de la 1 a la 6
import os
os.system("cls")


# while True:
#              numero = int(input("Ingrese un valor numerico\n"))
#              if numero % 2 ==0:
#                  print("Favor ingrese un numero par")
#                  continue
#              else:
#                numero = numero*4
#                print(f"El numero inpar multiplicado por 4 es {numero}")
#                break    

#Ejercicio 6
resultado =1       
base= int(input("Favor ingresar valor de la base\n"))
exponente = int(input("Favor ingresar valor del exponente\n"))

for i in range(0,exponente):
   resultado  = resultado * base  

print(f"el resultado {base} con exponente {exponente} es de: {resultado}")

