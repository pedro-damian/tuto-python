
import tkinter as tk
from tkinter import messagebox

class VentasPasajesApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Formulario de Ventas de Pasajes")

        self.label_origen = tk.Label(master, text="Origen:")
        self.label_origen.grid(row=0, column=0, sticky="e")
        self.entry_origen = tk.Entry(master)
        self.entry_origen.grid(row=0, column=1)

        self.label_destino = tk.Label(master, text="Destino:")
        self.label_destino.grid(row=1, column=0, sticky="e")
        self.entry_destino = tk.Entry(master)
        self.entry_destino.grid(row=1, column=1)

        self.label_fecha = tk.Label(master, text="Fecha:")
        self.label_fecha.grid(row=2, column=0, sticky="e")
        self.entry_fecha = tk.Entry(master)
        self.entry_fecha.grid(row=2, column=1)

        self.label_pasajero = tk.Label(master, text="Nombre del Pasajero:")
        self.label_pasajero.grid(row=3, column=0, sticky="e")
        self.entry_pasajero = tk.Entry(master)
        self.entry_pasajero.grid(row=3, column=1)

        self.label_asientos = tk.Label(master, text="Número de Asientos:")
        self.label_asientos.grid(row=4, column=0, sticky="e")
        self.entry_asientos = tk.Entry(master)
        self.entry_asientos.grid(row=4, column=1)

        self.btn_vender = tk.Button(master, text="Vender Pasaje", command=self.vender_pasaje)
        self.btn_vender.grid(row=5, columnspan=2)

    def vender_pasaje(self):
        origen = self.entry_origen.get()
        destino = self.entry_destino.get()
        fecha = self.entry_fecha.get()
        pasajero = self.entry_pasajero.get()
        asientos = self.entry_asientos.get()

        # Aquí podrías implementar la lógica para guardar los datos de la venta, como enviarlos a una base de datos o archivo.

        mensaje = f"Pasaje vendido:\nOrigen: {origen}\nDestino: {destino}\nFecha: {fecha}\nPasajero: {pasajero}\nNúmero de Asientos: {asientos}"
        messagebox.showinfo("Venta Exitosa", mensaje)

def main():
    root = tk.Tk()
    app = VentasPasajesApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
