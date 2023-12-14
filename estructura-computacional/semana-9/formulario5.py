import tkinter as tk

ventana = tk.Tk()

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
    print("Nombre11:", nombre11.get())
    print("Nombre12:", nombre12.get())
    print("Nombre13:", nombre13.get())
    print("Nombre14:", nombre14.get())
    print("Nombre15:", nombre15.get())
    print("Nombre16:", nombre16.get())
    print("Nombre17:", nombre17.get())
    print("Nombre18:", nombre18.get())
    print("Nombre19:", nombre19.get())
    print("Nombre20:", nombre20.get())

#--------------------Lado Izquierdo---------------------------

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

tk.Label(ventana,text="             ").grid(row=0, column=2)

#nombre10 =tk.Entry(ventana)
#nombre10.grid(row=0, column=1)

#--------------------Lado Derecho---------------------------

tk.Label(ventana,text="Nombre11:").grid(row=0, column=3)
nombre11 =tk.Entry(ventana)
nombre11.grid(row=0, column=4)

tk.Label(ventana,text="Nombre12:").grid(row=1, column=3)
nombre12 =tk.Entry(ventana)
nombre12.grid(row=1, column=4)

tk.Label(ventana,text="Nombre13:").grid(row=2, column=3)
nombre13 =tk.Entry(ventana)
nombre13.grid(row=2, column=4)

tk.Label(ventana,text="Nombre14:").grid(row=3, column=3)
nombre14 =tk.Entry(ventana)
nombre14.grid(row=3, column=4)

tk.Label(ventana,text="Nombre15:").grid(row=4, column=3)
nombre15 =tk.Entry(ventana)
nombre15.grid(row=4, column=4)

tk.Label(ventana,text="Nombre16:").grid(row=5, column=3)
nombre16 =tk.Entry(ventana)
nombre16.grid(row=5, column=4)

tk.Label(ventana,text="Nombre17:").grid(row=6, column=3)
nombre17 =tk.Entry(ventana)
nombre17.grid(row=6, column=4)

tk.Label(ventana,text="Nombre18:").grid(row=7, column=3)
nombre18 =tk.Entry(ventana)
nombre18.grid(row=7, column=4)

tk.Label(ventana,text="Nombre19:").grid(row=8, column=3)
nombre19 =tk.Entry(ventana)
nombre19.grid(row=8, column=4)

tk.Label(ventana,text="Nombre20:").grid(row=9, column=3)
nombre20 =tk.Entry(ventana)
nombre20.grid(row=9, column=4)

boton_enviar = tk.Button(ventana,text="Enviar", command=enviar_datos)
boton_enviar.grid(row=10, column=2, columnspan=1)

ventana.mainloop()