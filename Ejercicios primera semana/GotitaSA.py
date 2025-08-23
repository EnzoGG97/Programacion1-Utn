#Ingreso de datos
Metrosconsum = int(input("Ingrese la cantidad de metros consumidos: "))
Tp = input("Ingrese que tipo de cliente es: Residencial, Comercial o Industrial: ")

if Tp not in ["Residencial", "Comercial", "Industrial"]:
    print("Tipo de cliente invalido. Debe ser Residencial, Comercial o Industrial.")
    exit()

print(f"Cantidad de metros consumidos: {Metrosconsum}m³")
print(f"Tipo de cliente: {Tp}")

#Calculos 
#Subtotal
cargo_fijo = 7000
costo_mt = 200 

subtotal = cargo_fijo + (Metrosconsum * costo_mt)

print(f"Subtotal: ${subtotal}")

#Bonificaciones
bonificacion = 0
recargo = 0 

if Tp == "Residencial":
    if Metrosconsum < 30 :
        bonificacion = 0.10 
    elif Metrosconsum > 80:
        recargo = 0.15
elif Tp == "Comercial":
    if Metrosconsum > 300 :
        bonificacion = 0.12 
    elif Metrosconsum > 150 :
        bonificacion = 0.08
    elif Metrosconsum < 50 :
        recargo = 0.05 
elif Tp == "Industrial" : 
    if Metrosconsum > 1000 :
        bonificacion = 0.30
    elif Metrosconsum > 500 :
        bonificacion = 0.20
    elif Metrosconsum < 200 :
        recargo = 0.10

#Aplicación de bonifiaciones y recargos 
if bonificacion > 0 :
    subtotal = subtotal - (subtotal * bonificacion)

if recargo > 0 :
    subtotal = subtotal + (subtotal * recargo)

print(f"Bonificacion aplicada: {bonificacion * 100}%")
print(f"Recargo aplicado: {recargo * 100}%")
print(f"Subtotal con bonificaciones o  recargos aplicados: ${subtotal}")

#Iva y bonificacion especial
bonificacion_extra = 0

if Tp == "Residencial" and bonificacion <= 0 and recargo <=0 and subtotal < 35000 : 
    bonificacion_extra = 0.05 
    subtotal = subtotal - (subtotal * bonificacion_extra)

Iva = subtotal * 0.21

Total_final = subtotal + Iva

print(f"Bonificacion especial aplicada: {bonificacion_extra * 100}%")
print(f"Iva aplicado(21%): ${Iva}")
print(f"Total final a pagar: ${Total_final}")