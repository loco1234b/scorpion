import os
os.system("cls")

monto = int(input("ingresa la donacion: "))

centros = monto * 0.25
comedorin = monto * 0.35
escuelain = monto * 0.25
asilodean = monto * 0.15

print("centro de salud:  s/",centros)
print("comedor infantil: s/",comedorin)
print("escuela infantil: s/",escuelain)
print("asilo de ancianos: s/",asilodean)
print()