import os
os.system("cls")


suma = 0
for i in range(1,100):
    if i % 3 ==0 and i % 5 !=0:
        suma+= i
        print(i)
print("la suma de los multiplos de 3 pero no de 5 es: ",suma)