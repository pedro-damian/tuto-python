
import tkinter as tk

ventana = tk.Tk()
#ventana.title("BOLETA DE PAGO")
#ventana.geometry("650x340")
#ventana.config(bg="green")


def calcular_total():
    try:
        # se declara una variable donde se almacenara el valor introducido en el campo cantidad y lo convertira a float
        cantidad_valor = float(cantidad.get())
        # se declara una variable donde se almacenara el valor introducido en el campo precio y lo convertira a float
        precio_valor = float(precio.get())

        # calcula el subtotal
        subtotal_valor = cantidad_valor * precio_valor
        # calcula el IGV
        igv_valor = subtotal_valor * 0.18
        # calcula el total
        total_valor = subtotal_valor + igv_valor

        # enviamos el subtotal calculado al campo de entrada del formulario
        subtotal.set(subtotal_valor)
        # enviamos el IGV calculado al campo de entrada del formulario
        igv.set(igv_valor)
        # enviamos el total calculado al campo de entrada del formulario
        total.set(total_valor)

        # impprime los resultados en la consola
        print("Producto:", producto.get())
        print("Cantidad:", cantidad.get())
        print("Precio:", precio.get())
        print("Subtotal:", subtotal.get())
        print("IGV:", igv.get())
        print("Total:", total.get())

    # este error aparecera en el terminal cuando se ingrese un valor diferente a un numero en el campo de entrada de cantidad y precio
    except ValueError:
        print("Ingrese valores numéricos para Cantidad y Precio.")

tk.Label(ventana, text="Producto:").grid(row=0, column=0)
producto = tk.Entry(ventana)
producto.grid(row=0, column=1)

tk.Label(ventana, text="Cantidad:").grid(row=1, column=0)
cantidad = tk.Entry(ventana)
cantidad.grid(row=1, column=1)

tk.Label(ventana, text="Precio:").grid(row=2, column=0)
precio = tk.Entry(ventana)
precio.grid(row=2, column=1)

tk.Label(ventana, text="Subtotal:").grid(row=3, column=0)
subtotal = tk.StringVar()
# se crea una entrada de solo lectura
tk.Entry(ventana, textvariable=subtotal, state='readonly').grid(row=3, column=1)

tk.Label(ventana, text="IGV 18%:").grid(row=4, column=0)
igv = tk.StringVar()
tk.Entry(ventana, textvariable=igv, state='readonly').grid(row=4, column=1)

tk.Label(ventana, text="Total:").grid(row=5, column=0)
total = tk.StringVar()
tk.Entry(ventana, textvariable=total, state='readonly').grid(row=5, column=1)

boton_calcular = tk.Button(ventana, text="Calcular Total", command=calcular_total)
boton_calcular.grid(row=6, column=1, columnspan=2)

ventana.mainloop()
