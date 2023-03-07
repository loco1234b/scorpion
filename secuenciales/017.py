import os
os.system("cls")

monto = int(input("ingresa la donacion: "))

centro_salud = monto * 0.25
comedor_infantil = monto * 0.35
escuela_infantil = monto * 0.25
asilo_deancianos = monto * 0.15

print("centro de salud:  s/",centro_salud)
print("comedor infantil: s/",comedor_infantil)
print("escuela infantil: s/",escuela_infantil)
print("asilo de ancianos: s/",asilo_deancianos)
print()