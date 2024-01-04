
import tkinter as tk

class Aplicacion:

    def __init__(self):
        self.ventana1=tk.Tk()
        self.label1=tk.Label(self.ventana1, text="Ingrese N1:")
        self.label1.grid(column=0, row=0)
        self.dato1=tk.StringVar()
        self.entry1=tk.Entry(self.ventana1, width=20, textvariable=self.dato1)
        self.entry1.grid(column=1, row=0)
        self.label2=tk.Label(self.ventana1, text="Ingrese N2:")
        self.label2.grid(column=0, row=1)
        self.dato2=tk.StringVar()
        self.entry2=tk.Entry(self.ventana1, width=20, textvariable=self.dato2)
        self.entry2.grid(column=1, row=1)

        # botones
        self.boton1=tk.Button(self.ventana1,width=10, text="Suma", command=self.suma)
        self.boton1.grid(column=1, row=2)
        self.boton1=tk.Button(self.ventana1,width=10, text="Resta", command=self.resta)
        self.boton1.grid(column=1, row=3)
        self.boton1=tk.Button(self.ventana1,width=10, text="Producto", command=self.Multiplicacion)
        self.boton1.grid(column=1, row=4)
        self.boton1=tk.Button(self.ventana1, width=10,text="Division", command=self.division)
        self.boton1.grid(column=1, row=5)
        # resultado
        self.label3=tk.Label(self.ventana1,width=20,height=3, text="")
        self.label3.grid(column=1, row=6)
        self.label4=tk.Label(self.ventana1,height=3, text="Resultado:")
        self.label4.grid(column=0, row=6)

        self.ventana1.mainloop()

    def suma(self):
        valor1 = int(self.dato1.get())
        valor2 = int(self.dato2.get())
        sum = valor1+valor2
        self.label3.configure(text=sum)
        self.dato1.set("")
        self.dato2.set("")
        self.entry1.focus_set()


    def resta(self):
        valor1 = int(self.dato1.get())
        valor2 = int(self.dato2.get())
        rest = valor1-valor2
        self.label3.configure(text=rest)
        self.dato1.set("")
        self.dato2.set("")
        self.entry1.focus_set()

    def Multiplicacion(self):
        valor1 = int(self.dato1.get())
        valor2 = int(self.dato2.get())
        prod = valor1*valor2
        self.label3.configure(text=prod)
        self.dato1.set("")
        self.dato2.set("")
        self.entry1.focus_set()

    def division(self):
        valor1 = int(self.dato1.get())
        valor2 = int(self.dato2.get())
        div = valor1/valor2
        self.label3.configure(text=div)
        self.dato1.set("")
        self.dato2.set("")
        self.entry1.focus_set()

aplicacion1=Aplicacion()