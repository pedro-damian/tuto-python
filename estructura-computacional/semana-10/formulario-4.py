
import tkinter as tk

ventana = tk.Tk()

def verificar_condicion():
    try:
        nombre_valor = nombre.get()
        edad_valor = int(edad.get())
        talla_valor = float(talla.get())

        if talla_valor >= 1.80:
            condicion.set("Apto")
        else:
            condicion.set("No Apto")

        # muestra en consola los datos
        print("Nombre:", nombre_valor)
        print("Edad:", edad_valor)
        print("Talla:", talla_valor)
        print("Condición:", condicion.get())

    except ValueError:
        print("Por favor, ingrese valores válidos.")

tk.Label(ventana, text="Nombre:").grid(row=0, column=0)
nombre = tk.Entry(ventana)
nombre.grid(row=0, column=1)

tk.Label(ventana, text="Edad:").grid(row=1, column=0)
edad = tk.Entry(ventana)
edad.grid(row=1, column=1)

tk.Label(ventana, text="Talla:").grid(row=2, column=0)
talla = tk.Entry(ventana)
talla.grid(row=2, column=1)

tk.Label(ventana, text="Condición:").grid(row=3, column=0)
condicion = tk.StringVar()
tk.Entry(ventana, textvariable=condicion, state='readonly').grid(row=3, column=1)

boton_verificar = tk.Button(ventana, text="Verificar Condicion", command=verificar_condicion)
boton_verificar.grid(row=4, column=1, columnspan=2)

ventana.mainloop()
