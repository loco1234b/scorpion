import os
os.system("cls")

angulo = int(input("ingrese el angulo: "))

if angulo == 0:
    print("angulo nulo")
elif angulo > 0 and angulo < 90:
    print("angulo agudo")
elif angulo == 90:
    print("angulo recto")
elif angulo > 90 and angulo < 180:
    print("angulo obtuso")
elif angulo == 180:
    print("angulo llano")
elif angulo > 180 and angulo < 360:
    print("angulo concavo")
elif angulo == 360:
    print("angulo completo")
