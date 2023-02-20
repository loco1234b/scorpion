import os
os.system("cls")

monto = int(input("ingresa la cantidad de dinero: "))

if monto >= 200:
    diner = monto // 200
    print("existen " + str(diner) + " billetes de 200 soles")
    dinerr = monto % 200

if monto >= 100:
    diner = monto // 100
    print("existen " + str(diner) + " billetes de 100 soles")
    dinerr = monto % 100
if monto >= 50:
    diner = monto // 50
    print("existen " + str(diner) + " billetes de 50 soles")
    dinerr = monto % 50
if monto >= 20:
    diner = monto // 20
    print("existen " + str(diner) + " billetes de 20 soles")
    dinerr = monto % 20
if monto >= 10:
    diner = monto // 10
    print("existen " + str(diner) + " billetes de 10 soles")
    dinerr = monto % 10
if monto >= 5:
    diner = monto // 5
    print("existen " + str(diner) + " monedas de 5 soles")
    dinerr = monto % 5
if monto >= 2:
    diner = monto // 2
    print("existen " + str(diner) + " monedas de 2 soles")
    dinerr = monto % 2
if monto >= 1:
    diner = monto // 1
    print("existen " + str(diner) + " monedas de 1 sol")
    dinerr = monto % 1






