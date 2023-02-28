import os
os.system("cls")

# categoria a = 1, categoria b = 2, categoria c= 3, categoria d= 4
categoria = int(input("ingrese la categoria: "))
promedio = float(input("ingrese el promedio: "))

if categoria == 1:
    pensionactual = 550
elif categoria == 2:
    pensionactual = 500
elif categoria == 3:
    pensionactual = 450
elif categoria == 4:
    pensionactual = 400

if promedio <= 13.99:
    descuento = "no hay descuento"
elif promedio >= 14 and promedio <= 15.99:
    descuento = pensionactual * 0.10
elif promedio >= 16 and promedio <= 17.99:
    descuento = pensionactual * 0.12
elif promedio >= 18 and promedio <= 20:
    descuento = pensionactual * 0.15

nuevapension = pensionactual - descuento

print("la pension actual es: ",pensionactual)
print("el descuento es: ",descuento)
print("la nueva pension es: ",nuevapension)