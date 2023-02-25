import os
os.system("cls")

donacion = int(input("la donacion de la institucion es: ""$"))

if donacion >= 10000:
    centrosalud = donacion * 0.30
    comedorniños = donacion * 0.50
    bolsa = donacion * 0.20
elif donacion <= 9999:
    centrosalud = donacion * 0.25
    comedorniños = donacion * 0.60
    bolsa = donacion * 0.15

print("donacion al centro de salud es: ",centrosalud)
print("donacion al comedor de niños es: ",comedorniños)
print("se invierte en la bolsa : ",bolsa)
