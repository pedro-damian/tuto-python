import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Ejemplo de Treeview con inserción manual")

# Crear Treeview con cuatro columnas
tree = ttk.Treeview(root, columns=("Columna1", "Columna2", "Columna3", "Columna4"), show="headings")
tree.heading("Columna1", text="Columna 1")
tree.heading("Columna2", text="Columna 2")
tree.heading("Columna3", text="Columna 3")
tree.heading("Columna4", text="Columna 4")
tree.pack()

# Insertar datos manualmente
tree.insert("", "end", values=("Dato1", "Dato2", "Dato3", "Dato4"))
tree.insert("", "end", values=("Dato5", "Dato6", "Dato7", "Dato8"))
tree.insert("", "end", values=("Dato9", "Dato10", "Dato11", "Dato12"))

root.mainloop()
