import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

# ventana principal
raiz = tk.Tk()
raiz.title("Numero Par o Impar")

def par_impar(event):
  numero_seleccionado = int(combobox1.get())
  if numero_seleccionado % 2 == 0:
    label4.config(text=f"{numero_seleccionado} es un numero Par")
  else:
    label4.config(text=f"{numero_seleccionado} es un numero Impar")


label1= tk.Label(raiz,text="Numeros:", anchor="e", width=10)
label1.grid(row=0,column=0,pady=(10,10),padx=10)

# Crear un Combobox con los números del 1 al 12
numeros = (1,2,3,4,5,6,7,8,9,10)
combobox1 = ttk.Combobox(raiz, values=numeros)
combobox1.grid(row=0,column=1, pady=(10,10),padx=10)
combobox1.set("Elija un numero")

# Asociar el evento <<ComboboxSelected>> a la función par_impar
combobox1.bind("<<ComboboxSelected>>", par_impar)

label4= tk.Label(raiz,text="", font=("comic sans MS", 20), fg="red")
label4.grid(row=1,columnspan=2, pady=(10,10),padx=10)





raiz.mainloop()