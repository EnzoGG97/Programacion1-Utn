# 1--- A partir del ingreso de la altura en centímetros de un jugador de baloncesto, el programa deberá determinar la posición del jugador en la cancha, considerando los siguientes parámetros:
# Menos de 160 cm: Base
# Entre 160 cm y 179 cm: Escolta
# Entre 180 cm y 199 cm: Alero
# 200 cm o más: Ala-Pívot o Pívot

#ingreso de datos
Altura = int(input("Ingrese la altura del jugador en cm: "))
print(f"Altura ingresada: {Altura}cm")

#Asignacion de posicion
if Altura < 160 : 
    print("Posicion asignada: Base")
elif Altura < 179 :
    print("Posicion asignada: Escolta")
elif Altura < 199 : 
    print("Posicion asignada : Alero")
else : 
    print("Posicion asignada: Ala-pívot o Pívot")

#============================================

# 2--- Calcular una nota aleatoria entre el 1 y el 10 inclusive, para luego mostrar un mensaje según el valor:
# 6, 7, 8, 9 y 10  ---> Promoción directa, la nota es ...
# 4 y 5                ---> Aprobado, la nota es ...
# 1, 2 y 3            ---> Desaprobado, la nota es ...

#Nota aleatoria
import random
Nota = random.randint (1,10)

#Resultado segun la nota
if Nota >= 6 :
    print(f"Promocion directa, la nota es: {Nota}")
elif Nota >=4 :
    print(f"Aprobado, la nota es: {Nota}")
else :
    print(f"Desaprobado, la nota es: {Nota}")