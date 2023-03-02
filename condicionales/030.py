import os
os.system("cls")

cuota = int(input("ingrese la cuota mensual: "))
dias = int(input("ingrese el dia del pago: "))
descuento= 0
recargo= 0

if dias <= 10:
    descuento = cuota * 0.02
if dias <= 10 and descuento <5:
    descuento = 5
if dias >= 11 and dias <21:
    descuento = 0
if dias >21 and dias <=31:
    recargo = cuota * 0.03
if dias >21 and recargo <10:
    recargo = 10
    
debepagar = cuota - descuento + recargo

print("el cliente debe pagar: ",debepagar)