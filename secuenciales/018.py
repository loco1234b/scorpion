import os
os.system("cls")

unidades = int(input("ingrese las unidades a comprar: "))
precio = int(input("ingrese el precio unitario: "))

importe = unidades * precio
descuento = (importe) - importe * 0.15 
descuentot = descuento * 0.15
descuentofi = (importe * 0.15) + descuentot
importeto = descuento - descuentot


print("ingrese el importe de la compra: ",importe)
print("ingrese el descuento: ",descuentofi)
print("ingrese el importe a pagar: ",importeto)
print()