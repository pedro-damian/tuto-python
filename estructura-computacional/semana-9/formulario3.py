import tkinter as tk
ventana = tk.Tk()


tk.Label(ventana,text="Codigo:").grid(row=0, column=0)
nombre =tk.Entry(ventana)
nombre.grid(row=0, column=1)

tk.Label(ventana,text="Producto:").grid(row=1, column=1)
edad =tk.Entry(ventana)
edad.grid(row=1, column=2)

tk.Label(ventana,text="Precio:").grid(row=2, column=0)
email =tk.Entry(ventana)
email.grid(row=2, column=1)

tk.Label(ventana,text="Cantidad:").grid(row=3, column=1)
cantidad =tk.Entry(ventana)
cantidad.grid(row=3, column=2)


ventana.mainloop()