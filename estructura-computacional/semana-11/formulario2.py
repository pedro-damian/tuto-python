
import tkinter as tk

ventana = tk.Tk()

def verificar_condicion():
        nombre_valor = nombre.get()
        edad_valor = int(edad.get())
        sexo_valor = sexo.get().upper()

        if edad_valor >= 18 and sexo_valor == "M":
            condicion.set("NATACION")
        elif edad_valor < 18 and sexo_valor == "F":
            condicion.set("VOLEY")

        else:
            condicion.set("RECHAZADO")


        # muestra en consola los datos
        print("Nombre:", nombre_valor)
        print("Edad:", edad_valor)
        print("Sexo:", sexo_valor)
        print("Condición:", condicion.get())

tk.Label(ventana, text="Nombre:").grid(row=0, column=0)
nombre = tk.Entry(ventana)
nombre.grid(row=0, column=1)

tk.Label(ventana, text="Edad:").grid(row=1, column=0)
edad = tk.Entry(ventana)
edad.grid(row=1, column=1)

tk.Label(ventana, text="Sexo(M-F):").grid(row=2, column=0)
sexo = tk.Entry(ventana)
sexo.grid(row=2, column=1)

tk.Label(ventana, text="Grupo:").grid(row=3, column=0)
condicion = tk.StringVar()
tk.Entry(ventana, textvariable=condicion, state='readonly').grid(row=3, column=1)

boton_verificar = tk.Button(ventana, text="Verificar Condicion", command=verificar_condicion)
boton_verificar.grid(row=4, column=1, columnspan=2)

ventana.mainloop()
