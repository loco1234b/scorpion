import os
os.system("cls")

texto_str = "hola mundo"
reversed =""
for i in range(len(texto_str)-1,-1,-1):
    reversed += texto_str[i]
    

print("texto invertido: ",reversed)