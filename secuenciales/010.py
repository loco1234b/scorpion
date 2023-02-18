import os
os.system("cls")

numero = int(input("ingresa el numero natural de 4 cifras: "))

c4 = numero % 10
c3 = ((numero % 1000)% 100) // 10
c2 = (numero % 1000) // 100
c1 = numero // 1000

print(f'suma-> {c4}{c3}{c2}{c1}') 
print()