import os
os.system("cls")

monto = int(input("ingresa la cantidad de dinero: "))

d200 = monto / 200
d100 =(monto / 100) /1
d50 = (monto / 50) /1
d20 = monto / 20
d10 = monto /10
d5 =  monto / 5
d2 = monto / 2 
d1 = monto / 1

print(f'existen ',int(d200),"billetes de 200")
print(f'existen ',int(d100),"billetes de 100")
print(f'existen ',int(d50),"billetes de 50")
print(f'existen ',int(d20),"billetes de 20")
print(f'existen ',int(d10),"billetes de 10")
print(f'existen ',int(d5),"monedas de 5 ")
print(f'existen ',int(d2),"monedas de 2")
print(f'existen ',int(d1),"monedas de 1")






