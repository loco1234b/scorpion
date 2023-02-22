import os
os.system("cls")

monto = int(input("ingresa la donacion: "))

centrosalud = monto * 0.25
comedorinfantil = monto * 0.35
escuelainfantil = monto * 0.25
asilodeancianos = monto * 0.15

print("centro de salud:  s/",centrosalud)
print("comedor infantil: s/",comedorinfantil)
print("escuela infantil: s/",escuelainfantil)
print("asilo de ancianos: s/",asilodeancianos)
print()