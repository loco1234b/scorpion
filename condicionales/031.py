import os
os.system("cls")

horas = int(input("ingrese las horas trabajadas: "))
# # categoria a = 1, categoria b = 2, categoria c= 3, categoria d= 4
categoria = int(input("ingrese la categoria del 1 al 4: "))

if categoria == 1:
    pagoporhora = 21
elif categoria == 2:
    pagoporhora = 19.50
elif categoria == 3:
    pagoporhora = 17
elif categoria == 4:
    pagoporhora = 15.50

sueldobruto = horas * pagoporhora

if sueldobruto >= 2500:
    descuento = sueldobruto * 0.20
elif sueldobruto <= 2499:
    descuento = sueldobruto * 0.15

sueldoneto = sueldobruto - descuento

print("el sueldo bruto es: ",sueldobruto)
print("el descuento es: ",descuento)
print("el sueldo neto es: ",sueldoneto)