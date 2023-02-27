import os
os.system("cls")

cuadernos = int(input("el numero de cuadernos adquiridos es: "))

if cuadernos <= 12:
    lapicero = 0
    print("no hay obsequio")
elif cuadernos >= 12 and cuadernos <= 24:
    lapicerolucas = 1 * (cuadernos / 4)
    print(" se obsequia lapicero lucas: ",lapicerolucas)
elif cuadernos >= 24 and cuadernos <= 36:
    lapicerosfaber = 2 * (cuadernos / 4)
    print(" se obsequia lapicero faber: ",lapicerosfaber)
elif cuadernos >= 36:
    lapicerospilot = 2 * (cuadernos / 4) 
    lapicerofab = 1 * (cuadernos / 6)
    lapiceroluca = 1 * (cuadernos / 12)
    print(" se obsequia lapiceros pilot : ",lapicerospilot,"+","lapiceros faber",lapicerofab,"+",
    "lapiceros lucas",lapiceroluca)

