
import tkinter as tk

ventana = tk.Tk()

def enviar_datos():
    print("Nombre:", nombre.get())
    print("Edad:", edad.get())
    print("Peso:", peso.get())
    print("Talla:", talla.get())
    print("Sexo:", sexo.get())

tk.Label(ventana,text="Nombre:").grid(row=0, column=0)
nombre =tk.Entry(ventana)
nombre.grid(row=0, column=1)

tk.Label(ventana,text="Edad:").grid(row=1, column=0)
edad =tk.Entry(ventana)
edad.grid(row=1, column=1)

tk.Label(ventana,text="Peso:").grid(row=2, column=0)
peso =tk.Entry(ventana)
peso.grid(row=2, column=1)

tk.Label(ventana,text="Talla:").grid(row=3, column=0)
talla =tk.Entry(ventana)
talla.grid(row=3, column=1)

tk.Label(ventana,text="Sexo:").grid(row=4, column=0)
sexo =tk.Entry(ventana)
sexo.grid(row=4, column=1)

boton_enviar = tk.Button(ventana,text="Enviar", command=enviar_datos)
boton_enviar.grid(row=6, column=1, columnspan=2)

ventana.mainloop()