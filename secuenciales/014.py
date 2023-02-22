import os,math
os.system("cls")

n1 = int(input("primer numero: "))
n2 = int(input("segundo numero: "))
n3 = int(input("tercer numero: "))
n4 = int(input("cuarto numero: "))
n5 = int(input("quinto numero: "))

valor = max( n1,n2,n3,n4,n5)
valor1 = min(valor)
valor2 = max(valor1)

print("mayor: ",valor)
print("mayor: ",valor2)
