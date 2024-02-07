
from tkinter import *

raiz = Tk() # inicio

raiz.title("Frames")
#raiz.geometry("500x500") # tamaño de la ventana

miframe = Frame(raiz, bg="blue", width=250, height=250, highlightthickness=0,borderwidth=2, relief="solid")
miframe.grid(row=0, column=0, sticky="nsew")

def genero():
  #print(variable_opcion.get())
  if var.get()== 1:
    label2.config(text="Eres de Genero Masculino")
  else:
    label2.config(text="Eres de Genero Femenino")

label1=Label(miframe,text="Genero:",bg="blue", fg="white") 
label1.grid(column=0, row=0, pady=(50,10))
var=IntVar()
radio1=Radiobutton(miframe,text="Varon", value=1, variable=var, bg="blue",fg="red", command=genero) 
radio1.grid(column=0, row=1, padx=80)
radio2=Radiobutton(miframe,text="Mujer", value=2, variable=var, bg="blue",fg="red", command=genero) 
radio2.grid(column=0, row=2, padx=80)
label2=Label(miframe,text="",bg="blue", fg="white") 
label2.grid(column=0, row=3)



miframe3 = Frame(raiz, bg="red", width=250, height=250)
miframe3.grid(row=1, column=0, sticky="s")


miframe2 = Frame(raiz, bg="green", width=250, height=250)
miframe2.grid(row=0, column=1, sticky="n")

miframe4 = Frame(raiz, bg="purple", width=250, height=250)
miframe4.grid(row=1, column=1, sticky="s")

raiz.mainloop()