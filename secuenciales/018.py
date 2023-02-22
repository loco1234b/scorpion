import os
os.system("cls")

unidades = int(input("ingrese las unidades a comprar: "))
precio = int(input("ingrese el precio unitario: "))

importe = unidades * precio
descuento = (importe) - importe * 0.15 
descuentotal = descuento * 0.15
descuentofinal = (importe * 0.15) + descuentotal
importetotal = descuento - descuentotal


print("ingrese el importe de la compra: ",importe)
print("ingrese el descuento: ",descuentofinal)
print("ingrese el importe a pagar: ",importetotal)
print()