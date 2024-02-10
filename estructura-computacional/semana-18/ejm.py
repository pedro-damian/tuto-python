
import tkinter as tk

def mostrar_stock(event=None):
    producto_seleccionado = combo_productos.get()
    stock = stock_productos.get(producto_seleccionado, "Producto no encontrado")
    stock_text.delete(0, tk.END)
    stock_text.insert(tk.END, stock)

def verificar_stock(event=None):
    producto_seleccionado = combo_productos.get()
    stock_disponible = stock_productos.get(producto_seleccionado, 0)
    cantidad_solicitada = int(cantidad_entry.get())
    if cantidad_solicitada > stock_disponible:
        mensaje_label.config(text="¡Stock no disponible!")
    else:
        mensaje_label.config(text="Stock disponible")

root = tk.Tk()
root.title("Stock de productos")

stock_productos = {
    "Arroz": 100,
    "Frijoles": 200,
    "Azúcar": 300,
    "Aceite": 400,
    "Sal": 500,
    "Café": 600,
    "Harina": 700,
    "Sopa": 800,
    "Leche": 900,
    "Pasta": 1000
}

combo_productos = tk.StringVar()
combo_productos.set("Arroz")

label_producto = tk.Label(root, text="Selecciona un producto:")
label_producto.grid(row=0, column=0)

productos_disponibles = list(stock_productos.keys())
combo_box = tk.OptionMenu(root, combo_productos, *productos_disponibles, command=mostrar_stock)
combo_box.grid(row=0, column=1)

label_stock = tk.Label(root, text="Stock:")
label_stock.grid(row=1, column=0)

stock_text = tk.Entry(root)
stock_text.grid(row=1, column=1)

cantidad_label = tk.Label(root, text="Cantidad:")
cantidad_label.grid(row=2, column=0)

cantidad_entry = tk.Entry(root)
cantidad_entry.grid(row=2, column=1)

verificar_btn = tk.Button(root, text="Verificar stock", command=verificar_stock)
verificar_btn.grid(row=3, columnspan=2)

mensaje_label = tk.Label(root, text="")
mensaje_label.grid(row=4, columnspan=2)

combo_productos.trace("w", mostrar_stock)

root.mainloop()



