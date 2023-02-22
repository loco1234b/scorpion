import os,math
os.system("cls")

valora =int(input("ingrese el valor a: "))
valorb = int(input("ingresa el valor b: "))
valorc = int(input("ingrese el valor c: "))

raiz =math.sqrt(pow(valorb,2)- 4 * valora * valorc)

ecuacion1 = (- valorb + raiz) / (2 * valora)
ecuacion2 = (- valorb - raiz) / (2 * valora)




print("la ecuacion1 es: ",ecuacion1)
print("la ecuacion2: ",ecuacion2)
print()
