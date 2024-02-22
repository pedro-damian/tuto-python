import tkinter as tk
from tkinter import ttk
from tkinter import PhotoImage
# from PIL import ImageTk, Image # pip install pillow en caso no lo tengas instalado

# ventana principal
ventana = tk.Tk()
ventana.title("VENTA DE BOLETOS VIAJE")
ventana.geometry("1100x700")

# --------------------------------------------- FUNCIONES --------------------------------------------
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
        
        
        
# Función para actualizar la imagen y el texto descriptivo
def info_imagen(event):
    seleccion = combo_destinos.get()
    if seleccion == "Cuzco":
        label_imagen.image = cuzco
        #label_imagen.config(image=cuzco)
        cuzco = PhotoImage(file="cuzco.png")
        cuzco_size = cuzco.subsample(2,2)
        label_imagen = tk.Label(imagenes, image=cuzco_size)
        label_imagen.grid(row=4, column=0,pady=10)
        
        #label_imagen.image = cuzco  # Actualizar referencia a la imagen
        #label1.config(text="Machu Picchu\ns/ 240\nBus")
        
    

#-------------------------------- CREAMOS UN FRAME PARA ENCAPSULAR LOS LABELS Y ENTRYS -------------------------------
datos_personales = tk.Frame(ventana, width=250, height=250, highlightthickness=0,borderwidth=1, relief="solid")
datos_personales.grid(row=0, column=0, sticky="nsew", pady=50, padx=20)

# LABELS Y ENTRYS
etiqueta_nombre = ttk.Label(datos_personales, text="Nombre:", anchor="e", width=10)
etiqueta_nombre.grid(column=0, row=0, pady=10)
entry_nombre = ttk.Entry(datos_personales)
entry_nombre.grid(column=1, row=0)

etiqueta_origen = ttk.Label(datos_personales, text="Origen:", anchor="e", width=10)
etiqueta_origen.grid(column=0, row=1, pady=10)
entry_origen = ttk.Entry(datos_personales)
entry_origen.grid(column=1, row=1)

etiqueta_destino = ttk.Label(datos_personales, text="Destino:", anchor="e", width=10)
etiqueta_destino.grid(column=0, row=2, pady=10)
destinos = ("Cuzco", "Puno", "Arequipa","Ica", "Loreto", "Ayacucho")
combo_destinos = ttk.Combobox(datos_personales, values=destinos, width=19)
combo_destinos.grid(column=1, row=2)
combo_destinos.bind("<<ComboboxSelected>>", info_imagen)

etiqueta_asientos = ttk.Label(datos_personales, text="N° Asientos:", anchor="e", width=10)
etiqueta_asientos.grid(column=0, row=3, pady=10)
entry_asientos = ttk.Entry(datos_personales)
entry_asientos.grid(column=1, row=3)


#----------------------------------- CREAMOS UN FRAME PARA ENCAPSULAR LOS BOTONES --------------------------------------
botones = tk.Frame(ventana, width=250, height=250)
botones.grid(row=0, column=4, sticky="nsew", pady=20)

# BOton registrar
boton_registrar = ttk.Button(botones, text="Registrar", command=insertar_datos)
boton_registrar.grid(column=4, row=0, padx=30, pady=10)

# Boton eliminar
boton_registrar = ttk.Button(botones, text="Eliminar", command=eliminar_fila)
boton_registrar.grid(column=4, row=1, padx=30, pady=10)

# Boton reporte
boton_registrar = ttk.Button(botones, text="Reporte")
boton_registrar.grid(column=4, row=2, padx=30, pady=10)



#---------------------- componente Treeview: muestra informacion en mas de 1 columna ------------------------------------------
registros = ttk.Treeview(ventana, columns=("col1", "col2", "col3", "col4"), show="headings")
registros.grid(row=0, column=2, rowspan=4, pady=20, padx=(20,0))

# Definir encabezados de columna
registros.heading("col1", text="Nombre")
registros.heading("col2", text="Origen")
registros.heading("col3", text="Destino")
registros.heading("col4", text="Asientos")

# Crear un Scrollbar
scrollvertical = ttk.Scrollbar(ventana, command=registros.yview)
scrollvertical.grid(row=0,rowspan=4, column=3,pady=20, sticky="ns")
registros.config(yscrollcommand=scrollvertical.set)

registros.column("col1", width=150)  # Ancho de la columna 1
registros.column("col2", width=150)  # Ancho de la columna 2
registros.column("col3", width=150)  # Ancho de la columna 3
registros.column("col4", width=150)  # Ancho de la columna 4


#--------------------------------------- IMAGENES --------------------------------
imagenes = tk.Frame(ventana, width=250, height=250, highlightthickness=0,borderwidth=1, relief="solid")
imagenes.grid(row=4, column=0, sticky="nsew", pady=10, padx=20)

#cuzco = PhotoImage(file="cuzco.png")
#cuzco_size = cuzco.subsample(2,2)
#label_imagen = tk.Label(imagenes, image=cuzco_size)
#label_imagen.grid(row=4, column=0,pady=10)

#label1 = tk.Label(imagenes, text="Machu Picchu\ns/ 240\nBus")
#label1.grid(row=5, column=0)

#arequipa = PhotoImage(file="arequipa.png")
#arequipa_size = arequipa.subsample(2,2)
#label_imagen = tk.Label(imagenes, image=arequipa_size)
#label_imagen.grid(row=4, column=0,pady=10)

#label1 = tk.Label(imagenes, text="Volcan del Misti\ns/ 240\nBus")
#label1.grid(row=5, column=0)




ventana.mainloop()



