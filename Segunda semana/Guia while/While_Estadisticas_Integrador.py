# 1 - Realizar un programa que permita que el usuario ingrese todos los números que desee. Una vez finalizada la carga determinar:
# La suma acumulada de los números negativos.
# La suma acumulada de los números positivos.
# La cantidad de números negativos ingresados.
# El promedio de los números positivos.
# El número positivo más grande.
# El porcentaje de números negativos ingresados, respecto del total de ingresos.

numero_max = 0
suma_pos = 0
suma_neg = 0 
cant_neg = 0
cant_pos = 0 
contador = 0

while True:
    entrada = input("Ingrese un numero (o 'e' para salir): ")
    
    if entrada == 'e' or entrada == 'E':   
        break
    
    numero = int(entrada)  
    
    if numero > 0: 
        if numero > numero_max:
            numero_max = numero 
        suma_pos += numero
        cant_pos += 1
        
    elif numero < 0: 
        suma_neg += numero
        cant_neg += 1
    
    contador += 1

promedio = suma_pos / cant_pos
if cant_neg > 0 : 
    porcentaje_neg = (cant_neg / contador) * 100
else: 
    porcentaje_neg = 0

print(f"Suma de positivos acumulados: {suma_pos}")
print(f"Suma de negativos acumulados: {suma_neg}")
print(f"Cantidad de numero negativos ingresados: {cant_neg}")
print(f"Promedio de los numeros positivos ingresados: {promedio:.2f}")
print(f"Numero positivo mas grande ingresado: {numero_max}")
print(f"El porcentaje de los numero negativos ingresados sobre el total es: {porcentaje_neg:.2f}")

