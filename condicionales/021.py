import os
os.system("cls")

numero = int (input ("Ingresa el numero de 4 cifras: "))

estadocivil=(numero % 10000-numero % 1000)//1000
if estadocivil==1:
    print("es Soltero")
if estadocivil==2:
    print("es Casado")
if estadocivil==3:
    print("es Viudo")
if estadocivil==4:
    print("es Divorciado")

edad=(numero % 1000-numero % 10)//10

sexo= numero % 10
if sexo==1:
    print("es Femenino")
if sexo==2:
    print("es Masculino")


print("la edad es: ",edad)