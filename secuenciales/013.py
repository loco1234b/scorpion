import os,math
os.system("cls")

cateto1 = int(input("ingresa el cateto 1: "))
cateto2 = int(input("ingresa el cateto 2: "))

hipotenusa = math.sqrt((cateto1 ** 2)+ (cateto2 ** 2))

print("la hipotenusa: ",hipotenusa)