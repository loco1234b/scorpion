import os
os.system("cls")

costo = int(input("ingrese el costo de la casa: "))
ingresos = int(input("ingrese los ingresos del comprador: "))

if ingresos < 1250:
    cuotainicial = costo - (costo * 0.15)
    cuotamensual = cuotainicial / 120
if ingresos >= 1250:
    cuotainicial = costo - (costo * 0.30) 
    cuotamensual = cuotainicial / 75

print("la cuota inicial es: ",cuotainicial)
print("la cuota mensual es: ",cuotamensual)