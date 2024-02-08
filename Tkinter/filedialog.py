
from tkinter import *
from tkinter import filedialog    # importamos el modulo de filedialog

raiz = Tk() # inicio
raiz.title("Menu")
raiz.geometry("700x500")


barra_menu= Menu(raiz) 
raiz.config(menu=barra_menu) 


def abrir():
  fichero = filedialog.askopenfile(title="Abrir", filetypes=(("Ficheros de Python","*.py"),("Ficheros de imagenes","*.png")))
  print(fichero) # muestra la direccion donde se ubica el fichero
  
def guardar():
  fichero = filedialog.asksaveasfile(title="Guardar")


# elementos que tendra la barra de menu
elemento_archivo = Menu(barra_menu, tearoff=0)
# crea el texto de cada elemento para que se visualice en la barra menu 
barra_menu.add_cascade(label="Archivo", menu=elemento_archivo)


# SUBMENUS DE ARCHIVO
elemento_archivo.add_command(label="Nuevo")
elemento_archivo.add_command(label="Guardar", command=guardar)
elemento_archivo.add_command(label="Abrir", command=abrir)
elemento_archivo.add_separator() # separador es una linea que separa los submenus
elemento_archivo.add_command(label="salir")




raiz.mainloop()