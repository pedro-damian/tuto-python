
import tkinter as tk
from tkinter import ttk

# Funcion para mostrar la tabla de multiplicar del numero seleccionado
def mostrar_tabla():
  seleccion = int(combobox1.get())
  resultado=""
  caja_texto.delete(1.0, tk.END)
  for elemento in range(1,13):
      resultado+= f"{seleccion} x {elemento} = {seleccion * elemento}\n"

  caja_texto.insert(tk.END,resultado)


# ventana principal
raiz = tk.Tk()
raiz.title("Tabla de Multiplicar")

# Crear un Combobox con los números del 1 al 12
opciones = (1,2,3,4,5,6,7,8,9,10,11,12)
combobox1 = ttk.Combobox(raiz, values=opciones, width=10)
combobox1.grid(row=0,column=0)

# Botón para mostrar la tabla de multiplicar
boton_mostrar = ttk.Button(raiz, text="Mostrar Tabla", command=mostrar_tabla)
boton_mostrar.grid(row=1,column=0)

# Widget Text para mostrar la tabla de multiplicar con barra de desplazamiento
caja_texto = tk.Text(raiz, height=10, width=20)
caja_texto.grid(row=2, column=0)

# Crear una barra de desplazamiento
scrollbar = ttk.Scrollbar(raiz, command=caja_texto.yview)
scrollbar.grid(row=2, column=1, sticky="ns")
caja_texto.config(yscrollcommand=scrollbar.set)


raiz.mainloop()
