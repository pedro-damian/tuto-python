import tkinter as tk
#from tkinter import ttk

ventana = tk.Tk()
#ventana = ttk.Frame(ventana,padding=0)

def enviar_datos():
    print("Nombre1:", nombre1.get())
    print("Nombre2:", nombre2.get())
    print("Nombre3:", nombre3.get())
    print("Nombre4:", nombre4.get())
    print("Nombre5:", nombre5.get())
    print("Nombre6:", nombre6.get())
    print("Nombre7:", nombre7.get())
    print("Nombre8:", nombre8.get())
    print("Nombre9:", nombre9.get())
    print("Nombre10:", nombre10.get())

tk.Label(ventana,text="Nombre1:").grid(row=0, column=0)
nombre1 =tk.Entry(ventana)
nombre1.grid(row=0, column=1)

tk.Label(ventana,text="Nombre2:").grid(row=1, column=0)
nombre2 =tk.Entry(ventana)
nombre2.grid(row=1, column=1)

tk.Label(ventana,text="Nombre3:").grid(row=2, column=0)
nombre3 =tk.Entry(ventana)
nombre3.grid(row=2, column=1)

tk.Label(ventana,text="Nombre4:").grid(row=3, column=0)
nombre4 =tk.Entry(ventana)
nombre4.grid(row=3, column=1)

tk.Label(ventana,text="Nombre5:").grid(row=4, column=0)
nombre5 =tk.Entry(ventana)
nombre5.grid(row=4, column=1)

tk.Label(ventana,text="Nombre6:").grid(row=5, column=0)
nombre6 =tk.Entry(ventana)
nombre6.grid(row=5, column=1)

tk.Label(ventana,text="Nombre7:").grid(row=6, column=0)
nombre7 =tk.Entry(ventana)
nombre7.grid(row=6, column=1)

tk.Label(ventana,text="Nombre8:").grid(row=7, column=0)
nombre8 =tk.Entry(ventana)
nombre8.grid(row=7, column=1)

tk.Label(ventana,text="Nombre9:").grid(row=8, column=0)
nombre9 =tk.Entry(ventana)
nombre9.grid(row=8, column=1)

tk.Label(ventana,text="Nombre10:").grid(row=9, column=0)
nombre10 =tk.Entry(ventana)
nombre10.grid(row=9, column=1)

boton_enviar = tk.Button(ventana,text="Enviar", command=enviar_datos)
boton_enviar.grid(row=10, column=0, columnspan=2)

ventana.mainloop()