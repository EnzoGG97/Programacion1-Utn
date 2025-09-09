'''
Conversor de monedas
Escribir un programa que pida al usuario un monto en dólares y lo convierta a pesos argentinos y a euros. Usar funciones para cada conversión y mostrar el resultado con dos decimales.
'''
def dolares_pesos (dolares):
    tasa_cambio = 1361.0
    pesos = dolares * tasa_cambio
    return pesos

def dolares_euro (dolares):
    tasa_cambio = 1585.0
    euros = dolares * tasa_cambio
    return euros

monto_dolares = float(input("Ingrese el monto a convertir: "))

monto_pesos = dolares_pesos (monto_dolares)
monto_euros = dolares_euro (monto_dolares)

print(f"Su monto en pesos argentinos es: ${monto_pesos:.2f}")
print(f"Su monto en euros es: €{monto_euros:.2f}")