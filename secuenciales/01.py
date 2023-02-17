import os
os.system("cls")


varones = int(input("ingresa la cantidad de varones: "))
mujeres = int(input("ingresa la cantidad de mujeres: "))

total = varones + mujeres
print(f'% varones ={format(varones / total * 100)},%')
print(f'% mujeres ={format(mujeres / total * 100 )},%')
print()