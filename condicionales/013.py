import os
os.system("cls")

numero = int(input("cifra de 3 numeros: "))

centena = numero / 100
decena = numero % 100/ 10
unidades = numero % 10

if numero > 100 and numero < 999:
    print("los numeros son de 3 cifras")
if centena > decena  and centena > unidades and decena > unidades:
    print("los numeros son desendentes")
elif unidades > decena and unidades > centena and decena > centena:
    print("los numeros son ascendentes")
else:
    print("los numeros no son ascendentes ni descendentes")
