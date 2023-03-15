import os
os.system("cls")

comienzo = 100
final = 999
capicuas=[]
for i in range(comienzo,final + 1):
    derecha = str(i)
    izquierda = derecha[::-1]
    if derecha== izquierda:
        capicuas.append(i)
print(capicuas)

#lista =[i for i in range(comienzo,final + 1)if str(i)== str(i)[::-1]]
#print(lista)