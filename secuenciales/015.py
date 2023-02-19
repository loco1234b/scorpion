import os
os.system("cls")

juan = int(input("ingrese cuantos dolares aporto juan: $"))
rosa = int(input("ingrese cuantos dolares aporto rosa: $"))
daniel = int(input("ingrese cuantos soles aporto daniel:  s/"))

daniels = daniel / 3
capitalto = juan + rosa + daniels

juan1 = (juan * 100) / capitalto
rosa1 = (rosa * 100) / capitalto
daniel1 = (daniels * 100) / capitalto

print("el importe de daniel a euros es: ",daniels,"$")
print("capital total en dolares es: ",capitalto,"$")

print("juan aporto el : " ,juan1,"%")
print("rosa aporto el : " ,rosa1,"%")
print("daniel aporto el : " ,daniel1,"%")
print()

