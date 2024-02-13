import tkinter as tk
from tkinter import ttk

def insertar_datos():
    # Obtener los datos de las entradas y el Combobox
    nombre = entry_nombre.get()
    origen = entry_origen.get()
    destino = combobox_destino.get()
    num_asientos = entry_num_asientos.get()

    # Insertar datos en el Treeview
    registros.insert("", "end", values=(nombre, origen, destino, num_asientos))

ventana = tk.Tk()
ventana.title("Ejemplo de Treeview con inserción de datos desde un botón")

# Crear Treeview con cuatro columnas
registros = ttk.Treeview(ventana, columns=("col1", "col2", "col3", "col4"), show="headings")
registros.grid(row=0, column=0, padx=20, pady=20)

# Definir encabezados de columna
registros.heading("col1", text="Nombre")
registros.heading("col2", text="Origen")
registros.heading("col3", text="Destino")
registros.heading("col4", text="N° Asientos")

# Entradas para ingresar datos
tk.Label(ventana, text="Nombre:").grid(row=1, column=0, padx=10, pady=5)
entry_nombre = tk.Entry(ventana)
entry_nombre.grid(row=1, column=1, padx=10, pady=5)
tk.Label(ventana, text="Origen:").grid(row=2, column=0, padx=10, pady=5)
entry_origen = tk.Entry(ventana)
entry_origen.grid(row=2, column=1, padx=10, pady=5)
tk.Label(ventana, text="Destino:").grid(row=3, column=0, padx=10, pady=5)
destinos = ["Destino " + str(i) for i in range(1, 11)]  # Ejemplo de 10 destinos predefinidos
combobox_destino = ttk.Combobox(ventana, values=destinos)
combobox_destino.grid(row=3, column=1, padx=10, pady=5)
combobox_destino.current(0)  # Seleccionar el primer destino por defecto
tk.Label(ventana, text="N° Asientos:").grid(row=4, column=0, padx=10, pady=5)
entry_num_asientos = tk.Entry(ventana)
entry_num_asientos.grid(row=4, column=1, padx=10, pady=5)

# Botón para insertar datos
boton_insertar = tk.Button(ventana, text="Insertar datos", command=insertar_datos)
boton_insertar.grid(row=5, column=0, columnspan=2, pady=10)

ventana.mainloop()

