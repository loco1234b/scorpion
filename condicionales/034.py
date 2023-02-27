import os
os.system("cls")

peso = float(input("ingrese el peso: "))
estatura = float(input("ingrese la estatura: "))

imc = peso / (estatura * estatura)

if imc < 20:
    grado = "delgado"
elif imc > 20 and imc < 25:
    grado = "normal"
elif imc > 25 and imc < 27:
    grado = "sobrepeso"
elif imc > 27:
    grado = "obesidad"

print("el grado es: ",grado)