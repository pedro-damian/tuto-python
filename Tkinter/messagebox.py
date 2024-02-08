
from tkinter import *
from tkinter import messagebox


raiz = Tk() # inicio
raiz.title("Menu")
raiz.geometry("700x500")


def info():
  # Mostrara una ventana emergente
  messagebox.showinfo("Acerca de", "Version 1.1") # el primer parametro mostrara el titulo, el segundo parametro el contenido

def licencia():
  messagebox.showwarning("Licencia", "Producto bajo licencia de GNU Linux")
  
  
def salir():
  # ventana emergente askquestion ofrece 2 botones de Yes o No, que el resultado tambien sera Yes o No
  valor = messagebox.askquestion("Salir", "Deseas Salir de la Aplicacion")
  
  if valor == "yes":
    raiz.destroy()


def guardar():
  # ventana emergente askquestion ofrece 2 botones de OK o Cancel, que el resultado tambien sera True o False
  valor = messagebox.askokcancel("Guardar", "Deseas Guardar los cambios")
  
  if valor == False:
    raiz.destroy()
    

def cerrar():
  # ventana emergente askquestion ofrece 2 botones de Retry o Cancel, que el resultado tambien sera True o False
  valor = messagebox.askretrycancel("Cerrar", "Esta seguro que quiere cerrar sin Guardar cambios")
  
  if valor == False:
    raiz.destroy()



# Crea una variable donde almacenara el menu
barra_menu= Menu(raiz)  # menu pertenecera a raiz 
raiz.config(menu=barra_menu) # configura para que construya la barra de menu

# elementos que tendra la barra de menu
elemento_archivo = Menu(barra_menu, tearoff=0)  # tearoff elimina las lineas que vienen por defecto
elemento_ayuda = Menu(barra_menu, tearoff=0)

# crea el texto de cada elemento para que se visualice en la barra menu 
barra_menu.add_cascade(label="Archivo", menu=elemento_archivo)
barra_menu.add_cascade(label="Ayuda", menu=elemento_ayuda)

# SUBMENUS DE ARCHIVO
elemento_archivo.add_command(label="Nuevo")
elemento_archivo.add_command(label="Abrir")
elemento_archivo.add_command(label="Guardar", command=guardar)
elemento_archivo.add_separator() # separador es una linea que separa los submenus
elemento_archivo.add_command(label="Cerrar", command=cerrar)
elemento_archivo.add_command(label="salir", command=salir)


# SUBMENUS DE AYUDA
elemento_ayuda.add_command(label="Licencia", command=licencia)
elemento_ayuda.add_command(label="Acerca de", command=info)



  



raiz.mainloop()