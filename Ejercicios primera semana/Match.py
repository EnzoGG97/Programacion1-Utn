# Una agencia de viajes nos pide informar si hacemos viajes a lugares según la estación del año. 
# En caso de hacerlo mostrar por print  el mensaje “Se viaja”, caso contrario mostrar “No se viaja”. 
# a- Si es invierno: solo se viaja a Bariloche.
# b- Si es verano: se viaja a Mar del plata y Cataratas.
# c- Si es otoño: se viaja a todos los lugares.
# d- Si es primavera: se viaja a todos los lugares menos Bariloche.

Estacion = input("Ingrese la estación del año en la que desea viajar: Verano, Otoño, Invierno o Primavera ")

print(f"La estación en la que usted desea viajar es:{Estacion}")

match Estacion :
    case "Invierno" :
        print("Solo se viaja a Bariloche.")
    case "Verano" :
        print("Se viaja a mar del plata y Cataratas.")
    case "Otoño" :
        print("Se viaja a todos los lugares.")
    case "Primavera" : 
        print("Se viaja a todos los lugares, menos bariloche.")
    case _ :
        print("Ingreso invalido, por favor ingrese una estación correta: Verano, Otoño, Invierno o Primavera. Respetando que la primera letra sea mayuscula")