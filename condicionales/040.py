import os
os.system("cls")

print("***********************************************************************")
print("curso : matematica")
prctica1 = int(input("ingrese la practica 1 de matematica: "))
prctica2 = int(input("ingrese la practica 2 de matematica: "))
prctica3 = int(input("ingrese la practica 3 de matematica: "))
examenparcial = int(input("ingrese el examen parcial de matematica: "))
examenfinal = int(input("ingrese el examen final de matematica: "))

promedio = (prctica1 + prctica2 + prctica3 + examenparcial + examenfinal) /5

if promedio >=13 and promedio <=20:
    print("usted aprobo el curso")
else:
    print("usted desaprobo el curso")
print("su promedio es: ",promedio)

print("****************************************************************")
print("curso : fisica")
practica1 = int(input("ingrese la practica 1 de fisica: "))
practica2 = int(input("ingrese la practica 2 de fisica: "))
practica3 = int(input("ingrese la practica 3 de fisica: "))
examenparcial1 = int(input("ingrese el examen parcial de fisica: "))
examenfinal1 = int(input("ingrese el examen final de fisica: "))

promedio1 = (practica1 + practica2 + practica3 + examenparcial1 + examenfinal1) /5

if promedio1 >=13 and promedio1 <=20:
    print("usted aprobo el curso")
else:
    print("usted desaprobo el curso")
print("su promedio es: ",promedio1)

print("************************************************************")
print("curso : quimica")
prctica1q = int(input("ingrese la practica 1 de quimica: "))
prctica2q = int(input("ingrese la practica 2 de quimica: "))
prctica3q = int(input("ingrese la practica 3 de quimica: "))
examenparcialq = int(input("ingrese el examen parcial de quimica: "))
examenfinalq = int(input("ingrese el examen final de quimica: "))

promedioq = (prctica1q + prctica2q + prctica3q + examenparcialq + examenfinalq) /5

if promedioq >=13 and promedioq <=20:
    print("usted aprobo el curso")
else:
    print("usted desaprobo el curso")
print("su promedio es: ",promedioq)