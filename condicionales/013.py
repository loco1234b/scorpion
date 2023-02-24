import os
os.system("cls")

numero = int(input("cifra de 3 numeros: "))

centena = numero / 100
decena = numero % 100/ 10
unidades = numero % 10

if numero > 100 and numero < 999:
    print("los numeros son de 3 cifras")
if decena == centena + 1 and unidades == decena + 1:
    print("los numeros son ascendente")
elif decena == centena -1 and unidades == decena -1:
    print("los numeros son desendentes")
