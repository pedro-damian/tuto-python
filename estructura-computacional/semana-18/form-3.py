
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

# ventana principal
raiz = tk.Tk()
raiz.title("Tienda Abarrotes")


def mostrar_stock(event):
    producto_seleccionado = combobox1.get()
    stock = productos.get(producto_seleccionado)
    dato1.set(stock)
    

def agregar_producto():
    producto_seleccionado = combobox1.get()
    stock = productos.get(producto_seleccionado)
    cantidad_solicitada = int(entry2.get())
    if cantidad_solicitada > stock:
        messagebox.showwarning("Productos", "¡Stock no disponible!")
    else:
        messagebox.showinfo("Productos", "¡Stock disponible!")

label2= tk.Label(raiz,text="Productos:", anchor="e", width=10)
label2.grid(row=0,column=0,pady=(10,10),padx=10)

# Crear un Combobox 
productos = {"Fideos":100,"Aceite":200,"Arroz":300,"Leche":400,"Azucar":500,"Vinagre":600,"Condimentos":700,"ketchup":800,"Menestras":900,"Conservas":1000}
combobox1 = ttk.Combobox(raiz, values=list(productos.keys()))
combobox1.grid(row=0,column=1, pady=(10,10),padx=10)
combobox1.set("Elija un producto")

# STOCK
label3= tk.Label(raiz,text="Stock:", anchor="e", width=10)
label3.grid(row=1,column=0, pady=(10,10),padx=10)
#label4= tk.Label(raiz,text="", width=10)
#label4.grid(row=1,column=1, pady=(10,10),padx=10)

dato1= tk.StringVar()
entry1 = tk.Entry(raiz, width=20, textvariable=dato1, state="readonly")
entry1.grid(row=1, column=1, pady=(10,10),padx=10)
entry1.config(fg="blue", justify="center")


# Asociar el evento <<ComboboxSelected>> a la función mostrar_stock
combobox1.bind("<<ComboboxSelected>>", mostrar_stock)

# CAJA DE CANTIDAD
label5= tk.Label(raiz,text="Cantidad:", anchor="e", width=10)
label5.grid(row=2,column=0, pady=(10,10),padx=10)

entry2 = tk.Entry(raiz, width=20)
entry2.grid(row=2, column=1, pady=(10,10),padx=10)
entry2.config(fg="blue", justify="center")


boton1=tk.Button(raiz, text="Comprar",width=15, command=agregar_producto)
boton1.grid(column=0, row=3,columnspan=2, pady=20)
boton1.config(cursor="hand2")


raiz.mainloop()