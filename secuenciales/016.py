import os
os.system("cls")

horast = int(input("ingrese el numero de horas trabajadas: "))
tarifah = int(input("ingrese la tarifa horaria: "))

sueldoba = horast * tarifah
sueldobru = sueldoba + (sueldoba * 0.20)
sueldone = sueldobru - ( sueldobru * 0.10)

print("el sueldo basico es: ",sueldoba)
print("el sueldo bruto es: ",sueldobru)
print("el sueldo neto es: ",sueldone)
print()