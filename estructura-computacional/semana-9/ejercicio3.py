import tkinter as tk
#from tkinter import ttk

ventana = tk.Tk()
#ventana = ttk.Frame(ventana,padding=0)

def enviar_datos():
    print("Nombre:", nombre.get())
    print("Edad:", edad.get())
    print("Email:", email.get())

tk.Label(ventana,text="Nombre:").grid(row=0, column=0)
nombre =tk.Entry(ventana)
nombre.grid(row=0, column=1)

tk.Label(ventana,text="Edad:").grid(row=1, column=0)
edad =tk.Entry(ventana)
edad.grid(row=1, column=1)

tk.Label(ventana,text="Email:").grid(row=2, column=0)
email =tk.Entry(ventana)
email.grid(row=2, column=1)

tk.Label(ventana,text="Carrera:").grid(row=3, column=0)
carrera =tk.Entry(ventana)
carrera.grid(row=3, column=1)

boton_enviar = tk.Button(ventana,text="Enviar", command=enviar_datos)
boton_enviar.grid(row=4, column=0, columnspan=2)

boton_enviar = tk.Button(ventana,text="Enviar", command=enviar_datos)
boton_enviar.grid(row=4, column=2, columnspan=1)

ventana.mainloop()