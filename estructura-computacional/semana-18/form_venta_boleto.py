
import tkinter as tk
from tkinter import ttk

# ventana principal
ventana = tk.Tk()
ventana.title("VENTA DE BOLETOS VIAJE")


# datos personales
etiqueta_nombre = ttk.Label(ventana, text="Nombre:", anchor="e", width=10)
etiqueta_nombre.grid(column=0, row=0, pady=5)
entry_nombre = ttk.Entry(ventana)
entry_nombre.grid(column=1, row=0)

etiqueta_origen = ttk.Label(ventana, text="Origen:", anchor="e", width=10)
etiqueta_origen.grid(column=0, row=1, pady=5)
entry_origen = ttk.Entry(ventana)
entry_origen.grid(column=1, row=1)

etiqueta_destino = ttk.Label(ventana, text="Destino:", anchor="e", width=10)
etiqueta_destino.grid(column=0, row=2, pady=5)
destinos = ("Cuzco", "Puno", "Arequipa", "Iquitos", "Tacna", "Piura", "Trujillo")
combo_destinos = ttk.Combobox(ventana, values=destinos, width=19)
combo_destinos.grid(column=1, row=2)

etiqueta_asientos = ttk.Label(ventana, text="N asientos:", anchor="e", width=10)
etiqueta_asientos.grid(column=0, row=3, pady=5)
entry_asientos = ttk.Entry(ventana)
entry_asientos.grid(column=1, row=3)

# BOton registrar
boton_registrar = ttk.Button(ventana, text="Registrar")
boton_registrar.grid(column=0, row=4, columnspan=2, pady=10)


# SEGUNDA COLUMNA




ventana.mainloop()



