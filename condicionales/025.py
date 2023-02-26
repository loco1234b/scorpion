import os
os.system("cls")

hijos = int(input("ingrese el numero de hijos: "))
sueldo = int(input("ingrese el sueldo bruto: "))

if hijos >= 1:
    bonificacion = 0.125 * sueldo + (40 * hijos)
    sueldoneto = bonificacion + sueldo

else:
    bonificacion = 0.10 * sueldo
    sueldoneto = bonificacion + sueldo

print("la bonificacion es: ",bonificacion)
print("el sueldo neto es: ",sueldoneto)