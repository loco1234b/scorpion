import os
os.system("cls")

monto = int(input("el monto total vendido es: "))

if monto >=5000:
    sueldo = 0.10 * monto + 25 * ( monto / 500)

print(" el sueldo del vendedor es: ",sueldo)