
import tkinter as tk
from tkinter import ttk

def on_select(event):
    item = tree.selection()[0]
    value = tree.item(item, "values")
    print("Elemento seleccionado:", value)

root = tk.Tk()
root.title("Ejemplo de Treeview con eventos")

# Crear Treeview
tree = ttk.Treeview(root, columns=("col1", "col2"), show="headings")
tree.pack()

# Definir encabezados de columna
tree.heading("col1", text="Nombre")
tree.heading("col2", text="Edad")

# Agregar datos
tree.insert("", "0", values=("Juan", 30))
tree.insert("", "1", values=("María", 25))

# Configurar evento de selección
tree.bind("<<TreeviewSelect>>", on_select)

root.mainloop()


