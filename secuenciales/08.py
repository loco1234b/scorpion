import os, math
os.system("cls")

radio = int(input("ingresa el radio: "))
altura= int(input("ingresa el altura: "))

areabase = math.pi * math.pow(radio,2)
arealateral = 2 * math.pi * radio * altura
areatotal = 2 * areabase * arealateral

print(f'area base = {areabase},u2')
print(f'area lateral = {arealateral},u2')
print(f'area total = {areatotal},u2')
print()