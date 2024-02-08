
from tkinter import *

raiz = Tk()
raiz.title("CheckButtons")
raiz.geometry("400x300")

foto=PhotoImage(file="guardar-grande.png")
label1= Label(raiz,image=foto)
label1.grid(row=0,column=0)

miframe = Frame(raiz, borderwidth=2, relief="groove")
miframe.grid(row=1, column=0,padx=(50,10))

label2= Label(miframe,text="Elige Tu destino:")
label2.grid(row=2,column=0)

playa=IntVar()
montaña=IntVar()
rural=IntVar()

def opciones_viaje():
  opcion=""
  if (playa.get()==1):
    opcion+=" playa" + "\n"
  if (montaña.get()==1):
    opcion+=" montaña"  + "\n"
  if (rural.get()==1):
    opcion+=" rural"
  
  resultado.config(text=opcion)
  

check1 = Checkbutton(miframe, text="Playa", padx=10, variable=playa, onvalue=1, offvalue=0, command=opciones_viaje)
check1.grid(row=3,column=0)
check1 = Checkbutton(miframe, text="Montaña", variable=montaña, onvalue=1, offvalue=0, command=opciones_viaje)
check1.grid(row=4,column=0)
check1 = Checkbutton(miframe, text="Rural", variable=rural, onvalue=1, offvalue=0, command=opciones_viaje)
check1.grid(row=5,column=0)

resultado= Label(miframe, text="Elige Tu destino:")
resultado.grid(row=6,column=0)



raiz.mainloop()