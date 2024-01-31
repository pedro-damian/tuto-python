
from tkinter import *

raiz = Tk() # inicio

raiz.title("Ventana de Pruebas")

# raiz.resizable(0,0) # ventana no modificable
# raiz.geometry("500x300") # tamaño de la ventana

raiz.iconbitmap("") # icono de la ventana
raiz.config(bg="green")

# CREANDO UN FRAME
miframe = Frame()

 # empaquetamos el frame (metemos dentro de la ventana raiz)
miframe.pack() 
#miframe.pack(side="right", anchor="n") # miframe se ubicara al lado derecho y arriba
# miframe.pack(side="right", anchor="s") # miframe se ubicara al lado derecho y abajo
# miframe.pack(side="left", anchor="n") # miframe se ubicara al lado izquierdo y arriba
# miframe.pack(side="left", anchor="s") # miframe se ubicara al lado izquierdo y abajo
# miframe.pack(fill="x") # miframe se expande horizontal
# miframe.pack(fill="y", expand="True") # miframe se expande vertical
# miframe.pack(fill="both", expand="True") # miframe se expande vertical y horizontal


miframe.config(bg="blue")
miframe.config(width="650", height="250")

miframe.config(bd=10) # tamaño del borde miframe
miframe.config(relief="groove") # borde de miframe
miframe.config(cursor="hand2") # cursor del mouse tipo mano


raiz.mainloop() # cierre