import os
os.system("cls")

puntualidad = int(input("ingrese los minutos de tardanza: "))
rendimiento = int(input("ingrese la cantidad de observaciones: "))

if puntualidad == 0:
    puntaje = 10
elif puntualidad >=1 and puntualidad <=2:
    puntaje = 8
elif puntualidad >=3 and puntualidad <=5:
    puntaje = 6
elif puntualidad >=6 and puntualidad <=9:
    puntaje = 4
elif puntualidad > 9:
    puntaje = 0

if rendimiento == 0:
    puntaje1 = 10
elif rendimiento == 1:
    puntaje1 = 8
elif rendimiento == 2:
    puntaje1 = 5
elif rendimiento == 3:
    puntaje1 = 1
elif rendimiento > 3:
    puntaje1 = 0

puntajetotal = puntaje + puntaje1

if puntajetotal <= 10:
    bonificacion = 2.5 * puntajetotal
    print("la bonificacion es: ",bonificacion)
elif puntajetotal >= 11 and puntajetotal <= 13:
    bonificacion = 5 * puntajetotal
    print("la bonificacion es: ",bonificacion)
elif puntajetotal >= 14 and puntajetotal <= 16:
    bonificacion = 7.5 * puntajetotal
    print("la bonificacion es: ",bonificacion)
elif puntajetotal >= 17 and puntajetotal <= 19:
    bonificacion = 10 * puntajetotal
    print("la bonificacion es: ",bonificacion)
elif puntajetotal > 20:
    bonificacion = 12.5 * puntajetotal
    print("la bonificacion es: ",bonificacion)

print("el puntaje de la puntualidad es: ",puntaje)
print("el puntaje del rendimiento es: ",puntaje1)
print("el puntaje total es: ",puntajetotal)
