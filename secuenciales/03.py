import os
os.system("cls")


km = int(input("ingresa la cantidad de km: "))
pies = int(input("ingresa la cantidad de pies: "))
millas = int(input("ingresa la cantidad de millas: "))

metros = km * 1000
pies = pies / 3.2808
millas = millas * 1609

mmetro = metros + pies + millas
yardas = mmetro * 1.094

print("en metros son: ",mmetro)
print("en yardas son: ",yardas)
print()


