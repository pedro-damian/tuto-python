
from tkinter import *

raiz = Tk()

miframe = Frame(raiz, width=1200, height=600)
miframe.pack() # empaquetar dentro de raiz


# sticky
#               N
#         nw           ne
#   w                         e
#         sw           se
#               s

# Padding
# padx : tamaño horizontal
# pady : tamaño vertical

nombrelabel = Label(miframe, text="Nombre:")
nombrelabel.grid(row=0, column=0, sticky="w", padx=60)

minombre = StringVar()
cuadronombre = Entry(miframe, textvariable=minombre)
cuadronombre.grid(row=0, column=1)
cuadronombre.config(fg="red", justify="center")

apellidolabel = Label(miframe, text="Apellido:")
apellidolabel.grid(row=1, column=0, sticky="w", padx=60)
cuadroapellido = Entry(miframe)
cuadroapellido.grid(row=1, column=1)
cuadroapellido.config(fg="red", justify="center")

direccionlabel = Label(miframe, text="Direccion Actual:")
direccionlabel.grid(row=2, column=0, sticky="w", padx=60)
cuadrodireccion = Entry(miframe)
cuadrodireccion.grid(row=2, column=1)
cuadrodireccion.config(fg="red", justify="center")

passlabel = Label(miframe, text="Password:")
passlabel.grid(row=3, column=0, sticky="w", padx=60, pady=20)
cuadropass = Entry(miframe)
cuadropass.grid(row=3, column=1)
cuadropass.config(show="*", justify="center")

# Widgets Text y Button
comentariolabel = Label(miframe, text="Comentarios:")
comentariolabel.grid(row=4, column=0, sticky="w", padx=60, pady=10)
cuadrocomentario = Text(miframe, width=50, height=5)
cuadrocomentario.grid(row=5, column=0, columnspan=2)


def enviardatos():
  minombre.set("Pedro")

botonenviar = Button(raiz, text="Enviar", command=enviardatos)
botonenviar.pack()


# Crear un Scrollbar
scrollvertical = Scrollbar(miframe, command=cuadrocomentario.yview)
scrollvertical.grid(row=5, column=2, sticky="ns")
cuadrocomentario.config(yscrollcommand=scrollvertical.set)




raiz.mainloop()