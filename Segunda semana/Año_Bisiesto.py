# año bisiesto
while True:
    año = int(input("Ingrese un año(0 para salir)"))
    if año ==0:
        break

    if (año % 4 == 0 and año % 100 != 0) or (año % 400 == 0):
        print(f"{año} es bisiesto")
    else:
        print(f"{año} NO es bisiesto")