import os,math
os.system("cls")

valora =int(input("ingrese el valor a: "))
valorb = int(input("ingresa el valor b: "))
valorc = int(input("ingrese el valor c: "))

multi = valorb * valorb - 4 * valora * valorc
sum = math.sqrt(multi)
if multi<0:
    print("no existen soluciones reales")
else:
    ecuacion1 = (- valorb + sum) / (2 * valora)
    ecuacion2 = (- valorb - sum) / (2 * valora)




print("la ecuacion1 es: ",ecuacion1)
print("la ecuacion2: ",ecuacion2)
print()
