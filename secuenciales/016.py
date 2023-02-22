import os
os.system("cls")

horasTrabajadas = int(input("ingrese el numero de horas trabajadas: "))
tarifahoraria = int(input("ingrese la tarifa horaria: "))

sueldobasico = horasTrabajadas * tarifahoraria
sueldobruto = sueldobasico + (sueldobasico * 0.20)
sueldoneto = sueldobruto - ( sueldobruto * 0.10)

print("el sueldo basico es: ",sueldobasico)
print("el sueldo bruto es: ",sueldobruto)
print("el sueldo neto es: ",sueldoneto)
print()