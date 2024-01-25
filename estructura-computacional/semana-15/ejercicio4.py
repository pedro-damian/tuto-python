
from tkinter import ttk
from tkinter import *

# Función para añadir elementos a la tabla
def añadir():
    nombre = entrada_nombre.get()
    precio = entrada_precio.get()
    tree.insert("", END, values=(nombre, precio))

# Crear la ventana principal
ventana = Tk()
ventana.geometry("700x600")
ventana.title("Tabla de elementos")

# Crear el Treeview con dos columnas
tree = ttk.Treeview(ventana, columns=("Nombre", "Precio"), show="headings", height=10)
tree.heading("Nombre", text="Nombre")
tree.heading("Precio", text="Precio")

tree.pack(pady=20)

# Crear las variables de entrada para el nombre y precio
entrada_nombre = StringVar()
entrada_precio = StringVar()

# Crear la entrada de texto para el nombre
entrada_elementos = Entry(ventana, textvariable=entrada_nombre, width=40)
entrada_elementos.pack(pady=5)

# Crear la entrada de texto para el precio
entrada_precio = Entry(ventana, textvariable=entrada_precio, width=15)
entrada_precio.pack(pady=5)

# Crear el botón para añadir elementos
boton_añadir = Button(ventana, text="Añadir", height=2, width=18, command=añadir)
boton_añadir.pack(pady=10)

# Iniciar el bucle principal
ventana.mainloop()
