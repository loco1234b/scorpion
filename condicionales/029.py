import os
os.system("cls")

horas = int(input("ingrese las horas trabajadas: "))
tarifa = int(input("ingrese la tarifa horaria: "))

if horas <= 48:
    sueldobruto = horas * tarifa 
elif horas >=49:
    recarga = (horas * tarifa) * 0.20
    sueldobruto = (horas * tarifa) + recarga

if sueldobruto >= 1500:
    descuento = sueldobruto * 0.11
elif sueldobruto <= 1499:
    descuento = 0

totalapagar = sueldobruto - descuento

print("las horas trabajadas son: ",horas)
print("el pago por hora es: ",tarifa)
print("el sueldo bruto es: ",sueldobruto)
print("el descuento es: ",descuento)
print("el total a pagar por la empresa es: ",totalapagar)
