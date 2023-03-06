f = open ('boleta.text','a')
f.write("|*********************************boleta electronica**************************\n")
f.write("|                                  **FALABELLA\n")
f.write("|                                                             RUC:254367890\n")
f.write("|                                                       NUMERO DE BOLETA:0000510\n")
f.write("|TIENDA = FALABELLA\n"+"\n|NOMBRE = AARON ALEJANDRO")
f.write("-------------------------------APELLIDOS = LURITA LLICAN\n")
f.write("|DNI = 1234567\n") 
f.write("|DIRECCION = AV.28 DE JULIO CENTRO DE LIMA\n")
f.write("|TELEFONO = 987654321\n")
f.write("|FECHA = 7/03/2023\n")
f.write("|************************************************************************************\n")
f.write("|DESCRIPCION:| ----------------|CANTIDAD:|-------------|PRECIO:|---------|SUBTOTAL:|\n")
f.write("Bicicleta BMX----------------------1-------------------|S/700|-----------|S/700|\n")
f.write("SOFA NEGRO ------------------------1-------------------|S/300|-----------|S/300|\n")
f.write("TELEVISOR--------------------------1-------------------|S/8001-----------|S/800|\n")
f.write("-----------------------------------------------------------------TOTAL = |S/1800|\n")






f.close()

