
from tkinter import *

root = Tk()

# creamos un frame donde se ubicara dentro de root con una medida de 500x400
miframe = Frame(root, width=500, height=400)

# empaquetamos el frame metemos dentro de root
miframe.pack()

# milabel = Label(miframe, text="Hola mundo")
# milabel.place(x=10, y=20)

# Insertar una imagen
miImagen = PhotoImage(file="guardar.png")
Label(miframe, image=miImagen).place(x=100, y=200)

# Estilos al label
Label(miframe, text="Titulo", fg="red", font=("comic sans MS", 40)).place(x=200,y=20)



root.mainloop()
