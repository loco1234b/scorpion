import tkinter as tk
from tkinter import *


def main() :
    window = tk.Tk()
    window.title('ferreteria el tornillo feliz')
    window.resizable(0,0)
    window.geometry('950x500')
    #window.iconbitmap('/logo.ico')

    frame = tk.Frame(window)
    frame.pack()
    frame.config(width=600, height=400)
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

    Label(frame, text='cod_pro : ').grid(row=9, column=0)
    codigo1 = Entry(frame)
    codigo1.grid(row = 10, column= 0)
    codigo2 = Entry(frame)
    codigo2.grid(row = 11, column= 0)
    codigo3 = Entry(frame)
    codigo3.grid(row = 12, column= 0)
    
    Label(frame, text='descripcion: ').grid(row=9, column=1)
    descripcion1 = Entry(frame)
    descripcion1.grid(row = 10, column= 1)
    descripcion2 = Entry(frame)
    descripcion2.grid(row = 11, column= 1)
    descripcion3 = Entry(frame)
    descripcion3.grid(row = 12, column= 1)
    
    Label(frame, text='cantidad : ').grid(row=9, column=3)
    cantidad1 = Entry(frame)
    cantidad1.grid(row = 10, column= 3)
    cantidad2 = Entry(frame)
    cantidad2.grid(row = 11, column= 3)
    cantidad3 = Entry(frame)
    cantidad3.grid(row = 12, column= 3)
   
    Label(frame, text='precio : ').grid(row=9, column=4)
    precio1 = Entry(frame)
    precio1.grid(row = 10, column= 4)
    precio2 = Entry(frame)
    precio2.grid(row = 11, column= 4)
    precio3 = Entry(frame)
    precio3.grid(row = 12, column= 4)

    Label(frame, text='subtotal : ').grid(row=9, column=5)
    subtotal1 = Entry(frame)
    subtotal1.grid(row = 10, column= 5)
    subtotal2 = Entry(frame)
    subtotal2.grid(row = 11, column= 5)
    subtotal3 = Entry(frame)
    subtotal3.grid(row = 12, column= 5)

    Label(frame, text='total : ').grid(row=12, column=6)
    txtotal = Entry(frame)
    txtotal.grid(row=12, column=7)

    Label(frame,text='nuevo')
    window.mainloop()
    
if __name__ == '__main__' : main()
