
from tkinter import *

raiz = Tk() # inicio

variable_opcion = IntVar()

def genero():
  #print(variable_opcion.get())
  if variable_opcion.get()== 1:
    resultado.config(text="Eres de Genero Masculino")
  else:
    resultado.config(text="Eres de Genero Femenino")
    
    

Label(raiz, text="Genero:").pack()
Radiobutton(raiz,text="Masculino", variable=variable_opcion, value=1, command=genero).pack()
Radiobutton(raiz,text="Femenino", variable=variable_opcion, value=2, command=genero).pack()
resultado=Label(raiz)
resultado.pack()

raiz.mainloop()