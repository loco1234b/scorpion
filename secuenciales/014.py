import os,math
os.system("cls")

uno = int(input("primer numero: "))
segun= int(input("segundo numero: "))
tercer = int(input("tercer numero: "))
cuar = int(input("cuarto numero: "))
quint = int(input("quinto numero: "))

valor = math.max (uno,segun,tercer,cuar,quint)
print("mayor: ",valor)