import os
os.system("cls")

gigabytes = int(input("ingresa la cantidad de gigabytes: "))

megabytes = gigabytes * 1024
kilobytes = megabytes * 1024
bytes = kilobytes * 1024 

print("megabytes es: ",megabytes,"mb")
print("kilobytes es: ",kilobytes,"kb")
print("bytes es: ",bytes,"by")
print()
