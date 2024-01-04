
import tkinter as tk

class Aplicacion:

    def __init__(self):
        self.ventana1=tk.Tk()
        self.label1=tk.Label(self.ventana1, text="Ingrese usuario:")
        self.label1.grid(column=0, row=0)
        self.dato1=tk.StringVar()
        self.entry1=tk.Entry(self.ventana1, width=30, textvariable=self.dato1)
        self.entry1.grid(column=1, row=0)
        self.label2=tk.Label(self.ventana1, text="Ingrese Clave:")
        self.label2.grid(column=0, row=1)
        self.dato2=tk.StringVar()
        self.entry2=tk.Entry(self.ventana1, width=30, textvariable=self.dato2,show="*")
        self.entry2.grid(column=1, row=1)
        self.boton1=tk.Button(self.ventana1, text="Ingresar", command=self.ingresar)
        self.boton1.grid(column=1, row=2)
        self.ventana1.mainloop()

    def ingresar(self):
        print("Botón 'Ingresar' clicado.")
        print(f"Usuario ingresado: {self.dato1.get()}")
        print(f"Clave ingresada: {self.dato2.get()}")
        if self.dato1.get()=="pedro" and self.dato2.get()=="123":
            self.ventana1.title("correcto")
        else:
            self.ventana1.title("incorrecto")

aplicacion1=Aplicacion()