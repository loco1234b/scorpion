import os
os.system("cls")

dividiendo =int(input("dividiendo: "))
divisor = int(input("divisor: "))

cociente = 0
if dividiendo >= divisor:
    dividiendo -= divisor
    cociente += 1

print(f"cociente : {cociente}")
print(f"residuo : {dividiendo}")