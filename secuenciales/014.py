import os,math
os.system("cls")

n1 = int(input("primer numero: "))
n2 = int(input("segundo numero: "))
n3 = int(input("tercer numero: "))
n4 = int(input("cuarto numero: "))
n5 = int(input("quinto numero: "))

mayor = sorted({n1,n2,n3,n4,n5})
del mayor[0]
del mayor[0]
print("los numereos mayores son",mayor)
mayorr = sum(mayor)
print("la suma es: ",mayorr)
print("el promedio es:",mayorr / 3)