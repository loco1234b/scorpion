import os
os.system("cls")

matematica = int(input("la nota de matematica es: "))
fisica = int(input("la nota de fisica es: "))

if matematica >= 17:
    propina = 3
elif matematica <= 16:
    propina = 1

if fisica >= 15:
    propina1 = 2
elif fisica <= 14:
    propina1 = 0.50

promedio = (matematica + fisica) / 2

if promedio >= 16:
    reloj = 1
else:
    reloj = 0


print("la propina matematica es: ",propina)
print("la propina fisica es: ",propina1)
print("la propina total es:",propina + propina1)
print("el promedio es: ",promedio)
print(" obsequio reloj es: ",reloj)