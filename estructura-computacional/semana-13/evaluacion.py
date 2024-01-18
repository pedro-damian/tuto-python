

import tkinter as tk
from tkinter import ttk

def calcular_importe():
    tipo_membresia = combo_tipo_membresia.get()
    genero = combo_genero.get()

    descuento = 0.0
    if genero == "Femenino":
        descuento = 0.20

    if tipo_membresia == "Mensual":
        importe = 80.0
    elif tipo_membresia == "Trimestral":
        importe = 150.0
    elif tipo_membresia == "Anual":
        importe = 300.0

    importe_con_descuento = importe - (importe * descuento)
    label_importe.config(text=f"s/{importe_con_descuento:.2f}")

def mostrar_registro():
    mensaje = "----------- Registro exitoso -----------\n"
    mensaje += f"Nombre: {entry_nombre.get()}\n"
    mensaje += f"Género: {combo_genero.get()}\n"
    mensaje += f"Horario: {combo_horario.get()}\n"
    mensaje += f"Tipo de membresía: {combo_tipo_membresia.get()}\n"
    mensaje += f"Edad: {entry_edad.get()}\n"
    mensaje += f"Fecha de inscripción: {entry_fecha_inscripcion.get()}\n"
    mensaje += f"Fecha de finalización: {entry_fecha_finalizacion.get()}\n"
    
    total = label_importe.cget("text")
    mensaje += f"Total: {total}\n"

    # Limpiar los campos de entrada
    entry_nombre.delete(0, tk.END)
    combo_genero.set("")
    combo_horario.set("")
    combo_tipo_membresia.set("")
    entry_edad.delete(0, tk.END)
    entry_fecha_inscripcion.delete(0, tk.END)
    entry_fecha_finalizacion.delete(0, tk.END)
    label_importe.config(text="")

    ventana_registro = tk.Toplevel(ventana)
    ventana_registro.title("Registro Exitoso")
    etiqueta_registro = ttk.Label(ventana_registro, text=mensaje)
    etiqueta_registro.grid(column=0, row=0, padx=10, pady=10)


# ventana principal
ventana = tk.Tk()
ventana.title("GIMNASIO ATLAS")


etiqueta_nombre = ttk.Label(ventana, text="Nombre:")
etiqueta_nombre.grid(column=0, row=0, padx=10, pady=10)
entry_nombre = ttk.Entry(ventana)
entry_nombre.grid(column=1, row=0, padx=10, pady=10)

etiqueta_genero = ttk.Label(ventana, text="Género:")
etiqueta_genero.grid(column=0, row=1, padx=10, pady=10)
generos = ["Masculino", "Femenino"]
combo_genero = ttk.Combobox(ventana, values=generos)
combo_genero.grid(column=1, row=1, padx=10, pady=10)

etiqueta_horario = ttk.Label(ventana, text="Horario:")
etiqueta_horario.grid(column=0, row=2, padx=10, pady=10)
horarios = ["Mañana", "Tarde", "Noche"]
combo_horario = ttk.Combobox(ventana, values=horarios)
combo_horario.grid(column=1, row=2, padx=10, pady=10)

etiqueta_tipo_membresia = ttk.Label(ventana, text="Tipo de membresía:")
etiqueta_tipo_membresia.grid(column=0, row=3, padx=10, pady=10)
tipos_membresia = ["Mensual", "Trimestral", "Anual"]
combo_tipo_membresia = ttk.Combobox(ventana, values=tipos_membresia)
combo_tipo_membresia.grid(column=1, row=3, padx=10, pady=10)

etiqueta_tipo_membresia = ttk.Label(ventana, text="Tipo de membresía:")
etiqueta_tipo_membresia.grid(column=4, row=0, padx=60, pady=10)

etiqueta_tipo_membresia = ttk.Label(ventana, text="Mensual: s/ 80", foreground='blue')
etiqueta_tipo_membresia.grid(column=4, row=1, padx=60, pady=10)

etiqueta_tipo_membresia = ttk.Label(ventana, text="Trimestral: s/ 150", foreground='blue')
etiqueta_tipo_membresia.grid(column=4, row=2, padx=60, pady=10)

etiqueta_tipo_membresia = ttk.Label(ventana, text="Anual: s/ 300", foreground='blue')
etiqueta_tipo_membresia.grid(column=4, row=3, padx=60, pady=10)

etiqueta_tipo_membresia = ttk.Label(ventana, text="PROMOCION: 20% DESCUENTO MUJERES", foreground='red')
etiqueta_tipo_membresia.grid(column=4, row=5, padx=60, pady=10)

etiqueta_edad = ttk.Label(ventana, text="Edad:")
etiqueta_edad.grid(column=0, row=4, padx=10, pady=10)
entry_edad = ttk.Entry(ventana)
entry_edad.grid(column=1, row=4, padx=10, pady=10)

etiqueta_fecha_inscripcion = ttk.Label(ventana, text="Fecha de inscripción:")
etiqueta_fecha_inscripcion.grid(column=0, row=5, padx=10, pady=10)
entry_fecha_inscripcion = ttk.Entry(ventana)
entry_fecha_inscripcion.grid(column=1, row=5, padx=10, pady=10)

etiqueta_fecha_finalizacion = ttk.Label(ventana, text="Fecha de finalización:")
etiqueta_fecha_finalizacion.grid(column=0, row=6, padx=10, pady=10)
entry_fecha_finalizacion = ttk.Entry(ventana)
entry_fecha_finalizacion.grid(column=1, row=6, padx=10, pady=10)

label_importe = ttk.Label(ventana, text="")
label_importe.grid(column=1, row=7, pady=10)


boton_importe = ttk.Button(ventana, text="Calcular Importe", command=calcular_importe)
boton_importe.grid(column=0, row=7, pady=10)


boton_registrar = ttk.Button(ventana, text="Registrar", command=mostrar_registro)
boton_registrar.grid(column=0, row=9, columnspan=5, pady=20, padx=10)

boton_registrar.style = ttk.Style()
boton_registrar.style.configure('TButton', background='#A2FEEE')


ventana.mainloop()
