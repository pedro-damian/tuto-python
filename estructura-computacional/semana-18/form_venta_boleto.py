
import tkinter as tk
from tkinter import ttk

# ventana principal
ventana = tk.Tk()
ventana.title("VENTA DE BOLETOS VIAJE")
ventana.geometry("1000x400")

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
boton_registrar = ttk.Button(ventana, text="Registrar")
boton_registrar.grid(column=0, row=4, columnspan=2)


# SEGUNDA COLUMNA
registros = ttk.Treeview(ventana, columns=("col1", "col2", "col3", "col4"), show="headings")
registros.grid(row=0, column=2, rowspan=4, padx=20, pady=20)

# Definir encabezados de columna
registros.heading("col1", text="Nombre")
registros.heading("col2", text="Origen")
registros.heading("col3", text="Destino")
registros.heading("col4", text="N° Asientos")

# Agregar datos
registros.insert("", "end", values=("Juan", "lima", "cuzco", 2))


registros.column("col1", width=150)  # Ancho de la columna 1
registros.column("col2", width=100)  # Ancho de la columna 2
registros.column("col3", width=100)  # Ancho de la columna 3
registros.column("col4", width=100)  # Ancho de la columna 4


ventana.mainloop()



