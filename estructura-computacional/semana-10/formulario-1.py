
import tkinter as tk

ventana = tk.Tk()

def enviar_datos():
    print("Nombre:", nombre.get())
    print("Apellido Paterno:", apellido_paterno.get())
    print("Apellido Materno:", apellido_materno.get())
    print("Correo:", email.get())
    print("Celular:", mobile.get())
    print("Direccion:", direccion.get())

tk.Label(ventana,text="Nombre:").grid(row=0, column=0)
nombre =tk.Entry(ventana)
nombre.grid(row=0, column=1)

tk.Label(ventana,text="Apellido Paterno:").grid(row=1, column=0)
apellido_paterno =tk.Entry(ventana)
apellido_paterno.grid(row=1, column=1)

tk.Label(ventana,text="Apellido Materno:").grid(row=2, column=0)
apellido_materno =tk.Entry(ventana)
apellido_materno.grid(row=2, column=1)

tk.Label(ventana,text="Correo:").grid(row=3, column=0)
email =tk.Entry(ventana)
email.grid(row=3, column=1)

tk.Label(ventana,text="Celular:").grid(row=4, column=0)
mobile =tk.Entry(ventana)
mobile.grid(row=4, column=1)

tk.Label(ventana,text="Direccion:").grid(row=5, column=0)
direccion =tk.Entry(ventana)
direccion.grid(row=5, column=1)

boton_enviar = tk.Button(ventana,text="Enviar", command=enviar_datos)
boton_enviar.grid(row=6, column=1, columnspan=2)

ventana.mainloop()