import os
os.system("cls")

codigo = int(input("el codigo es: "))

if codigo % 2 ==0 and codigo % 3 ==0 and codigo % 5 ==0:
    print("tipo de empleado administrativo")
if codigo % 3 ==0 and codigo % 5 ==0 and codigo % 2 !=0:
    print("tipo de empleado directivo")
if codigo % 2 ==0 and codigo % 3 !=0 and codigo % 5 !=0:
    print("tipo de empleado vendedor")
if codigo % 2!=0 and codigo % 3 !=0 and codigo % 5 !=0:
    print("tipo de empleado seguridad")
else:
    print("error")