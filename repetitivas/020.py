import os,math
os.system("cls")

n1 =int(input("numero 1: "))
n2 =int(input("numero 2: "))
n3 =int(input("numero 3: "))
n4 =int(input("numero 4: "))
n5 =int(input("numero 5: "))
n6 =int(input("numero 6: "))
n7 =int(input("numero 7: "))
n8 =int(input("numero 8: "))
n9 =int(input("numero 9: "))
n10 =int(input("numero 10: "))

lista=(n1,n2,n3,n4,n5,n6,n7,n8,n9,n10)
mayor = max(lista)
menor = min(lista)
promedio =(n1 + n2 + n3 + n4 + n5 + n6 + n7 + n8 + n9 + n10) / 10

print("el numero mayor es : ",mayor)
print("el numero menor es : ",menor)
print("el promedio es: ",promedio)