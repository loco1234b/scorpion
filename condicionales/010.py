import os,math
os.system("cls")

nota1 = int(input("la nota 1 es: "))
nota2 = int(input("la nota 2 es: "))
nota3 = int(input("la nota 3 es: "))
nota4 = int(input("la nota 4 es: "))
nota5 = int(input("la nota 5 es: "))

notamayor = max(nota1,nota2,nota3,nota4,nota5)
notamenor = min(nota1,nota2,nota3,nota4,nota5)

promedio = (nota1 + nota2 + nota3 + nota4 + nota5)/ 5

print("la nota eliminada mayor es: ",notamayor )
print("la nota eliminada menor es: ",notamenor )
print("el promedio es: ",promedio)