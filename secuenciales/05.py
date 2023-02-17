import os
os.system("cls")

gigabytes = int(input("ingresa la cantidad de gigabytes: "))

mb = gigabytes * 1024
kb = mb * 1024
by = kb * 1024 

print("megabytes es: ",mb,"mb")
print("kilobytes es: ",kb,"kb")
print("bytes es: ",by,"by")
print()
