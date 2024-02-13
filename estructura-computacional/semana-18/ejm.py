
import tkinter as tk
from tkinter import ttk
from PIL import ImageTk, Image # pip install pillow en caso no lo tengas instalado


def mostrar_imagen():
    # Obtener la ruta de la imagen seleccionada en el Combobox
    imagen_seleccionada = combobox_imagen.get()

    # Cargar la imagen
    imagen = Image.open(imagen_seleccionada)
    imagen = imagen.resize((200, 200), Image.ANTIALIAS)  # Ajustar el tamaño de la imagen
    imagen = ImageTk.PhotoImage(imagen)

    # Mostrar la imagen en un Label
    label_imagen.config(image=imagen)
    label_imagen.image = imagen

ventana = tk.Tk()
ventana.title("Ejemplo de Treeview con imagen y Combobox")

# Crear Treeview con cuatro columnas
registros = ttk.Treeview(ventana, columns=("col1", "col2", "col3", "col4"), show="headings")
registros.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")

# Definir encabezados de columna
registros.heading("col1", text="Nombre")
registros.heading("col2", text="Origen")
registros.heading("col3", text="Destino")
registros.heading("col4", text="N° Asientos")

# Agregar datos de ejemplo
for i in range(50):
    registros.insert("", "end", values=("Nombre " + str(i), "Origen " + str(i), "Destino " + str(i), i))

# Barras de desplazamiento vertical y horizontal
scroll_y = tk.Scrollbar(ventana, orient="vertical", command=registros.yview)
scroll_y.grid(row=0, column=1, sticky="ns")
scroll_x = tk.Scrollbar(ventana, orient="horizontal", command=registros.xview)
scroll_x.grid(row=1, column=0, sticky="ew")

# Configurar barras de desplazamiento para el Treeview
registros.configure(yscrollcommand=scroll_y.set, xscrollcommand=scroll_x.set)

# Crear Combobox para seleccionar imagen
combobox_imagen = ttk.Combobox(ventana, values=["cuzco.jpg", "arequipa.jpg", "imagen3.jpg"])
combobox_imagen.grid(row=2, column=0, padx=20, pady=10)
combobox_imagen.current(0)  # Seleccionar la primera imagen por defecto

# Botón para mostrar imagen
boton_mostrar = tk.Button(ventana, text="Mostrar imagen", command=mostrar_imagen)
boton_mostrar.grid(row=2, column=1, padx=20, pady=10)

# Label para mostrar la imagen
label_imagen = tk.Label(ventana)
label_imagen.grid(row=3, column=0, columnspan=2, padx=20, pady=10)

ventana.mainloop()

