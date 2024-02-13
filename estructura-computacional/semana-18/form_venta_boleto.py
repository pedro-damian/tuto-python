
import tkinter as tk
from tkinter import ttk

# ventana principal
ventana = tk.Tk()
ventana.title("VENTA DE BOLETOS VIAJE")
ventana.geometry("950x400")

def insertar_datos():
    # Obtener los datos de las entradas y el Combobox
    nombre = entry_nombre.get()
    origen = entry_origen.get()
    destino = combo_destinos.get()
    num_asientos = entry_asientos.get()

    # Insertar datos en el Treeview
    registros.insert("", "end", values=(nombre, origen, destino, num_asientos))


def eliminar_fila():
    # Obtener fila seleccionada
    seleccion = registros.selection()
    if seleccion:  # Verificar si se ha seleccionado una fila
        registros.delete(seleccion)  # Eliminar fila seleccionada


# datos personales
etiqueta_nombre = ttk.Label(ventana, text="Nombre:", anchor="e", width=10)
etiqueta_nombre.grid(column=0, row=0, pady=5)
entry_nombre = ttk.Entry(ventana)
entry_nombre.grid(column=1, row=0)

etiqueta_origen = ttk.Label(ventana, text="Origen:", anchor="e", width=10)
etiqueta_origen.grid(column=0, row=1, pady=5)
entry_origen = ttk.Entry(ventana)
entry_origen.grid(column=1, row=1)

etiqueta_destino = ttk.Label(ventana, text="Destino:", anchor="e")
etiqueta_destino.grid(column=0, row=2)
destinos = ("Cuzco", "Puno", "Arequipa", "Iquitos", "Tacna", "Piura", "Trujillo")
combo_destinos = ttk.Combobox(ventana, values=destinos, width=19)
combo_destinos.grid(column=1, row=2)

etiqueta_asientos = ttk.Label(ventana, text="N asientos:", anchor="e")
etiqueta_asientos.grid(column=0, row=3)
entry_asientos = ttk.Entry(ventana)
entry_asientos.grid(column=1, row=3)

# BOton registrar
boton_registrar = ttk.Button(ventana, text="Registrar", command=insertar_datos)
boton_registrar.grid(column=0, row=4, columnspan=2)

# Boton eliminar
boton_registrar = ttk.Button(ventana, text="Eliminar", command=eliminar_fila)
boton_registrar.grid(column=2, row=4, padx=(0,150))

# Boton reporte
boton_registrar = ttk.Button(ventana, text="Reporte")
boton_registrar.grid(column=2, row=4, padx=(150,0))



# SEGUNDA COLUMNA
registros = ttk.Treeview(ventana, columns=("col1", "col2", "col3", "col4"), show="headings")
registros.grid(row=0, column=2, rowspan=4, pady=20)

# Definir encabezados de columna
registros.heading("col1", text="Nombre")
registros.heading("col2", text="Origen")
registros.heading("col3", text="Destino")
registros.heading("col4", text="Asientos")

# Crear un Scrollbar
#scrollvertical = ttk.Scrollbar(ventana, command=registros.yview)
#scrollvertical.grid(row=1, column=3, sticky="ns")
#registros.config(yscrollcommand=scrollvertical.set)

# Barras de desplazamiento vertical y horizontal
scroll_y = tk.Scrollbar(ventana, orient="vertical", command=registros.yview)
scroll_y.grid(row=1, column=3, sticky="ns")
#scroll_x = tk.Scrollbar(ventana, orient="horizontal", command=registros.xview)
#scroll_x.grid(row=0, column=3, sticky="ew")

# Configurar barras de desplazamiento para el Treeview
registros.configure(yscrollcommand=scroll_y.set)



registros.column("col1", width=150)  # Ancho de la columna 1
registros.column("col2", width=150)  # Ancho de la columna 2
registros.column("col3", width=150)  # Ancho de la columna 3
registros.column("col4", width=100)  # Ancho de la columna 4


ventana.mainloop()



