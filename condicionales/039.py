import os
os.system("cls")

horas =float(input("ausencia al trabajo: "))
tornillosd =int(input("tornillos defectuosos: "))
tornillosn = int(input("tornillos no defectuosos: "))

if horas > 1.5 and tornillosd > 300 and tornillosn < 10000:
    grado = 5
if horas < 1.5 and tornillosd > 300 and tornillosn <  10000:
    grado = 7
if horas > 1.5 and tornillosd < 300 and tornillosn <  10000:
    grado = 8
if horas > 1.5 and tornillosd > 300 and tornillosn >  10000:
    grado = 9
if horas < 1.5 and tornillosd < 300 and tornillosn <  10000:
    grado = 12
if horas < 1.5 and tornillosd > 300 and tornillosn >  10000:
    grado = 13
if horas > 1.5 and tornillosd < 300 and tornillosn >  10000:
    grado = 15
if horas < 1.5 and tornillosd < 300 and tornillosn >  10000:
    grado = 20
  
print("el grado de eficiencia es: ",grado)