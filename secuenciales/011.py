import os
os.system("cls")

cifra1 = int(input("primer numero de 3 cifras: "))
cifra2 = int(input("segundo numero de 3 cifras: "))

c1 = cifra1 // 100
c2 = (cifra1 % 100) // 10
c3 = ((cifra1 % 100)% 10) // 1

c4 = cifra2 // 100
c5 = (cifra2 % 100) // 10
c6 = ((cifra2 % 100)% 10) // 1

print(f'suma-> {c6}{c2}{c4} y {c3}{c5}{c1}') 
print()