import os
os.system("cls")

monto = int(input("el monto total de la compra es : "))

if monto >= 5000:
    prestamo = monto * 0.30
else:
    prestamo = monto * 0.20

propiodinero = monto - prestamo
intereses = propiodinero * 0.10
total = propiodinero + intereses

print("el prestamo del banco es: ",prestamo)
print("la empresa tendra que pagar con su propio dinero: ",total)