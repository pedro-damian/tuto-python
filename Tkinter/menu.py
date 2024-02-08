
from tkinter import *

raiz = Tk() # inicio
raiz.title("Menu")
raiz.geometry("700x500")

# Crea una variable donde almacenara el menu
barra_menu= Menu(raiz)  # menu pertenecera a raiz 
raiz.config(menu=barra_menu) # configura para que construya la barra de menu

# elementos que tendra la barra de menu
elemento_archivo = Menu(barra_menu, tearoff=0)  # tearoff elimina las lineas que vienen por defecto
elemento_edicion = Menu(barra_menu, tearoff=0)
elemento_herramientas = Menu(barra_menu, tearoff=0)
elemento_ayuda = Menu(barra_menu, tearoff=0)

# crea el texto de cada elemento para que se visualice en la barra menu 
barra_menu.add_cascade(label="Archivo", menu=elemento_archivo)
barra_menu.add_cascade(label="Edicion", menu=elemento_edicion)
barra_menu.add_cascade(label="Herramientas", menu=elemento_herramientas)
barra_menu.add_cascade(label="Ayuda", menu=elemento_ayuda)

# SUBMENUS DE ARCHIVO
elemento_archivo.add_command(label="Nuevo")
elemento_archivo.add_command(label="Abrir")
elemento_archivo.add_command(label="Guardar")
elemento_archivo.add_command(label="Guardar como")
elemento_archivo.add_separator() # separador es una linea que separa los submenus
elemento_archivo.add_command(label="salir")

# SUBMENUS DE EDICION
elemento_edicion.add_command(label="Copiar")
elemento_edicion.add_command(label="cortar")
elemento_edicion.add_command(label="pegar")
elemento_edicion.add_command(label="buscar")
elemento_edicion.add_command(label="reemplazar")

# SUBMENUS DE HERRAMIENTAS
elemento_herramientas.add_command(label="Copiar")
elemento_herramientas.add_command(label="cortar")
elemento_herramientas.add_command(label="pegar")
elemento_herramientas.add_command(label="buscar")
elemento_herramientas.add_command(label="reemplazar")

# SUBMENUS DE AYUDA
elemento_ayuda.add_command(label="Licencia")
elemento_ayuda.add_command(label="Acerca de")



raiz.mainloop()