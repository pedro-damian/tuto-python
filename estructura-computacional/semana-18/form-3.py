
import tkinter as tk
from tkinter import ttk


# ventana principal
raiz = tk.Tk()
raiz.title("Tienda Abarrotes")

def stock():
    seleccion = opciones.get()
    if seleccion == "Fideos":
        dato1.set("100")


label2= tk.Label(raiz,text="Productos:", anchor="w")
label2.grid(row=0,column=0,pady=(10,10),padx=10)

# Crear un Combobox con los números del 1 al 12
opciones = ("Fideos","Aceite","Arroz","Leche","Azucar","Vinagre","Condimentos","ketchup","Menestras","Conservas")
combobox1 = ttk.Combobox(raiz, values=opciones)
combobox1.grid(row=0,column=1, pady=(10,10),padx=10)
combobox1.set("Elija un producto")

# CAJA DE STOCK
label3= tk.Label(raiz,text="Stock:", anchor="w")
label3.grid(row=1,column=0, pady=(10,10),padx=10)
dato1= tk.StringVar()
entry1 = tk.Entry(raiz, width=20, textvariable=dato1, state='readonly')
entry1.grid(row=1, column=1, pady=(10,10),padx=10)
entry1.config(fg="blue", justify="center")

# CAJA DE CANTIDAD
label4= tk.Label(raiz,text="Cantidad:", anchor="w")
label4.grid(row=2,column=0, pady=(10,10),padx=10)
dato2= tk.StringVar()
entry2 = tk.Entry(raiz, width=20, textvariable=dato2)
entry2.grid(row=2, column=1, pady=(10,10),padx=10)
entry2.config(fg="blue", justify="center")


boton1=tk.Button(raiz, text="Agregar",width=15)
boton1.grid(column=0, row=3,columnspan=2, pady=20)
boton1.config(cursor="hand2")


raiz.mainloop()