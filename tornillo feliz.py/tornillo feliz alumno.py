import tkinter as tk
from tkinter import *

window = tk.Tk()
window.title('ferreteria el tornillo feliz')
window.resizable(0,0)
window.geometry('950x500')
 #window.iconbitmap('/logo.ico')


frame = tk.Frame(window)
frame.pack()
frame.config(width=600, height=600)
Label(frame,text='BIENVENIDOS',fg='blue').grid(row =0, column=2)
Label(frame, text='').grid(row=1, column=0)
Label(frame, text='Dni : ').grid(row=5, column=0)
txtDni = Entry(frame)
txtDni.grid(row=5, column=1 , pady= 5,padx=5)
txtDni.focus()

Label(frame,text ='apellidos : ').grid(row =6, column =0)
txtapellidos = Entry(frame)
txtapellidos.grid(row =6, column =1)

Label(frame, text='Nombres : ').grid(row=6, column=2)
txtNombres = Entry(frame)
txtNombres.grid(row=6, column=3)

Label(frame, text='direccion : ').grid(row=7, column=0)
txtdireccion = Entry(frame)
txtdireccion.grid(row=7, column=1)

Label(frame, text='telefono : ').grid(row=8, column=0)
txttelefono = Entry(frame)
txttelefono.grid(row=8, column=1)

def calculo():
    cant=int(obtenercantidad1.get())
    cant1=int(obtenercantidad2.get())
    cant2=int(obtenercantidad3.get())
    prec=float(obtenerPrecio1.get())
    prec1=float(obtenerPrecio2.get())
    prec2=float(obtenerPrecio3.get())
    #calculo del subtotal de ventas
    subt=(cant*prec)
    subt1=(cant1*prec1)
    subt2=(cant2*prec2)
    #calculo del total de ventas
    totl = (subt+subt1+subt2);    
    obtenerSubtotal1.set(str(subt))
    obtenerSubtotal2.set(str(subt1))
    obtenerSubtotal3.set(str(subt2))
    obtenerTotal.set(str(totl))
    
    
def Codigos():
          
    codg=int(obtenerCodigo1.get())
    codg1=int(obtenerCodigo2.get())
    codg2=int(obtenerCodigo3.get())
    desc=obtenerDescripcion1.get()
    desc1=obtenerDescripcion2.get()
    desc2=obtenerDescripcion3.get()

    prec=obtenerPrecio1.get()
    prec1=obtenerPrecio2.get()
    prec2=obtenerPrecio3.get()

    if codg== 1:
        desc="lija"
        prec=15 
    elif codg == 0:
         desc="nada" 
         prec=0      
    if codg1== 2:
            desc1="tornillos"
            prec1=1.50
    elif codg1==0:
         desc1="nada"
         prec1=0
    if codg2== 3:
            desc2="clavos"
            prec2=2
    elif codg2==0:
         desc2="nada"
         prec2=0

    obtenerPrecio1.set(str(prec))
    obtenerPrecio2.set(str(prec1))
    obtenerPrecio3.set(str(prec2))
        
    obtenerDescripcion1.set(str(desc))
    obtenerDescripcion2.set(str(desc1))
    obtenerDescripcion3.set(str(desc2))

    obtenerCodigo1.set(str(codg))
    obtenerCodigo2.set(str(codg1))
    obtenerCodigo3.set(str(codg2))
def Limpiar():
    obtenerCodigo1.set("")
    obtenerCodigo2.set("")
    obtenerCodigo3.set("")
    obtenerDescripcion1.set("")
    obtenerDescripcion2.set("")
    obtenerDescripcion3.set("")
    obtenercantidad1.set("")
    obtenercantidad2.set("")
    obtenercantidad3.set("")
    obtenerPrecio1.set("")
    obtenerPrecio2.set("")
    obtenerPrecio3.set("")
    obtenerSubtotal1.set("")
    obtenerSubtotal2.set("")
    obtenerSubtotal3.set("")
    obtenerTotal.set("")
    

obtenerCodigo1 = StringVar()
obtenerCodigo2 = StringVar()
obtenerCodigo3 = StringVar()   
Label(frame, text='cod_pro : ').grid(row=9, column=0)
codigo1 = Entry(frame,textvariable= obtenerCodigo1)
codigo1.grid(row = 10, column= 0)
codigo2 = Entry(frame,textvariable= obtenerCodigo2)
codigo2.grid(row = 11, column= 0)
codigo3 = Entry(frame,textvariable= obtenerCodigo3)
codigo3.grid(row = 12, column= 0)

Label(frame,text='codigo 1= lija',fg='blue').grid(row =13, column=0)
Label(frame,text='codigo 2= tornillos',fg='blue').grid(row =14, column=0)
Label(frame,text='codigo 3= clavos',fg='blue').grid(row =15, column=0)
Label(frame,text='codigo 0= nada',fg='blue').grid(row =16, column=0)


obtenerDescripcion1 = StringVar() 
obtenerDescripcion2 =StringVar()
obtenerDescripcion3 =StringVar()    
Label(frame, text='descripcion: ').grid(row=9, column=1)
descripcion1 = Entry(frame,textvariable= obtenerDescripcion1)
descripcion1.grid(row = 10, column= 1)
descripcion2 = Entry(frame,textvariable= obtenerDescripcion2)
descripcion2.grid(row = 11, column= 1)
descripcion3 = Entry(frame,textvariable= obtenerDescripcion3)
descripcion3.grid(row = 12, column= 1)

obtenercantidad1 = StringVar() 
obtenercantidad2 = StringVar()
obtenercantidad3 = StringVar()
Label(frame, text='cantidad : ').grid(row=9, column=3)
cantidad1 = Entry(frame,textvariable= obtenercantidad1)
cantidad1.grid(row = 10, column= 3)
cantidad2 = Entry(frame,textvariable= obtenercantidad2)
cantidad2.grid(row = 11, column= 3)
cantidad3 = Entry(frame,textvariable= obtenercantidad3)
cantidad3.grid(row = 12, column= 3)

Label(frame,text='poner 0 si no desea un producto',fg='blue').grid(row =13, column=3)


obtenerPrecio1 = StringVar()
obtenerPrecio2 = StringVar()
obtenerPrecio3 = StringVar()
Label(frame, text='precio : ').grid(row=9, column=4)
precio1 = Entry(frame,text='2',textvariable= obtenerPrecio1)
precio1.grid(row = 10, column= 4)
precio2 = Entry(frame,textvariable= obtenerPrecio2)
precio2.grid(row = 11, column= 4)
precio3 = Entry(frame,textvariable= obtenerPrecio3)
precio3.grid(row = 12, column= 4)

obtenerSubtotal1 = StringVar()
obtenerSubtotal2 = StringVar()
obtenerSubtotal3 = StringVar()
Label(frame, text='subtotal : ').grid(row=9, column=5)
subtotal1 = Entry(frame,textvariable= obtenerSubtotal1)
subtotal1.grid(row = 10, column= 5)
subtotal2 = Entry(frame,textvariable= obtenerSubtotal2)
subtotal2.grid(row = 11, column= 5)
subtotal3 = Entry(frame,textvariable= obtenerSubtotal3)
subtotal3.grid(row = 12, column= 5)

obtenerTotal = StringVar()
Label(frame, text='total : ').grid(row=12, column=6)
txtotal = Entry(frame,textvariable= obtenerTotal)
txtotal.grid(row=12, column=7)

btnNuevo = Button(frame, text='calcular',bg="sky blue", command=calculo, cursor='hand2').place(x =500,y=100)
btnu= Button(frame, text='Informacion',bg="sky blue",cursor='hand2', command=Codigos).place(x=570,y=100)
btn=Button(frame, text='Limpiar',bg= "sky blue", command= Limpiar).place(x=660,y=100)


Label(frame,text='nuevo')
window.mainloop()

