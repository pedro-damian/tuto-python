
from tkinter import *

def añadir():
    lista_elementos.insert(END, entrada.get())

ventana= Tk()
ventana.geometry("700x600")
ventana.title("Lista")

lista_elementos= Listbox(ventana,width=50)

lista_elementos.insert(0,"Elemento 1")
lista_elementos.insert(1,"Elemento 2")
lista_elementos.insert(2,"Elemento 3")
lista_elementos.insert(3,"Elemento 4")

lista_elementos.place(x=100, y=120)
lista_etiq= Label(ventana, text="Lista de elementos").place(x=100, y=100)

entrada= StringVar()
entrada_elementos= Entry(ventana, textvariable=entrada, width=40).place(x=150, y=20)

boton_añadir = Button(ventana, text="añadir", height=2, width=18, command=añadir).place(x=400, y=20)


def recuperar(): 
        if len(lista_elementos.curselection())!=0: 
            Entry.configure(text=lista_elementos.get(lista_elementos.curselection()[0])) 

boton1=Button(ventana, text="Mostrar", command=recuperar).place(x=300, y=350)
#boton1.grid(column=1, row=3)

caja_precio = Entry(ventana, width=15)
caja_precio.place(x=300, y=400)

ventana.mainloop()