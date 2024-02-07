
from tkinter import *

raiz=Tk()

miframe = Frame(raiz)
miframe.pack()

#------------------------Pantalla --------------------------------

numero_pantalla=StringVar()  # creamos una variable con el nombre numero_pantalla donde recibira los numeros 
pantalla=Entry(miframe, textvariable=numero_pantalla) # agregamos un argumento de configuracion textvariable mostrara los numeros 
pantalla.grid(row=1, column=1,pady=5,columnspan=4)
pantalla.config(background="black", fg="#03f943", justify="right")

#------------------------Pulsaciones de los Botones --------------------------------
def numero_pulsado(num):
  numero_pantalla.set(numero_pantalla.get() + num)
  



#--------------- Fila 1 --------------------
boton7= Button(miframe, text="7", width=3, command=lambda:numero_pulsado("7"))
boton7.grid(row=2,column=1)
boton8= Button(miframe, text="8", width=3, command=lambda:numero_pulsado("8"))
boton8.grid(row=2,column=2)
boton9= Button(miframe, text="9", width=3, command=lambda:numero_pulsado("9"))
boton9.grid(row=2,column=3)
boton_division= Button(miframe, text="/", width=3)
boton_division.grid(row=2,column=4)

#--------------- Fila 2 --------------------
boton4= Button(miframe, text="4", width=3, command=lambda:numero_pulsado("4"))
boton4.grid(row=3,column=1)
boton5= Button(miframe, text="5", width=3, command=lambda:numero_pulsado("5"))
boton5.grid(row=3,column=2)
boton6= Button(miframe, text="6", width=3, command=lambda:numero_pulsado("6"))
boton6.grid(row=3,column=3)
boton_multiplicacion= Button(miframe, text="x", width=3)
boton_multiplicacion.grid(row=3,column=4)

#--------------- Fila 3 --------------------
boton1= Button(miframe, text="1", width=3, command=lambda:numero_pulsado("1"))
boton1.grid(row=4,column=1)
boton2= Button(miframe, text="2", width=3, command=lambda:numero_pulsado("2"))
boton2.grid(row=4,column=2)
boton3= Button(miframe, text="3", width=3, command=lambda:numero_pulsado("3"))
boton3.grid(row=4,column=3)
boton_restar= Button(miframe, text="-", width=3)
boton_restar.grid(row=4,column=4)

#--------------- Fila 4 --------------------
boton_punto= Button(miframe, text=".", width=3)
boton_punto.grid(row=5,column=1)
boton0= Button(miframe, text="0", width=3, command=lambda:numero_pulsado("0"))
boton0.grid(row=5,column=2)
boton_resultado= Button(miframe, text="=", width=3)
boton_resultado.grid(row=5,column=3)
boton_suma= Button(miframe, text="+", width=3)
boton_suma.grid(row=5,column=4)

def enviardatos():
  minombre.set("Pedro") 


raiz.mainloop()