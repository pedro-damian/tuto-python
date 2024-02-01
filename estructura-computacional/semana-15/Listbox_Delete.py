
from tkinter import *

class Aplicacion:
  def __init__(self):
          
    self.ventana =Tk()
    self.ventana.geometry("600x500")
    self.ventana.title("Lista de Productos")
    
    
    self.Productos = []
    
    #self.scrollbar = Scrollbar(self.ventana)
          
    self.lista_elementos= Listbox(self.ventana,width=50, selectmode=MULTIPLE)  # bd=2, relief="solid"
    self.lista_elementos.place(x=70, y=100)
    
    
    #self.scrollbar.config(command=self.lista_elementos.yview)
    #self.scrollbar.grid(column=2, row=0, sticky=NS)
    
    
    # Label Producto y Texto de entrada Producto
    self.label1= Label(self.ventana,text="Producto:")
    self.label1.place(x= 70, y=30)
    self.entrada_producto = StringVar()
    self.entrada_elementos1 = Entry(self.ventana, textvariable=self.entrada_producto, width=20)
    self.entrada_elementos1.place(x=70, y=50)
    
    # Label Precio y Texto de entrada Precio
    self.label1= Label(self.ventana,text="Precio:")
    self.label1.place(x= 300, y=30)
    self.entrada_precio = StringVar()
    self.entrada_elementos2 = Entry(self.ventana, textvariable=self.entrada_precio, width=10)
    self.entrada_elementos2.place(x=300, y=50)
    
    # BOTON AÑADIR ELEMENTO
    self.boton_añadir = Button(self.ventana, text="añadir", width=5, command=self.añadir)
    self.boton_añadir.place(x=450, y=40)
    
    # BOTON MOSTRAR PRECIO
    self.boton_añadir = Button(self.ventana, text="Mostrar Precio", width=15, command=self.mostrar_precio)
    self.boton_añadir.place(x=70, y=300)

    # CAJA SALIDA DE PRECIO
    self.caja_precio = Entry(self.ventana, width=10)
    self.caja_precio.place(x=70, y=350)
  
    # BOTON ELIMINAR 
    self.boton_añadir = Button(self.ventana, text="Eliminar", width=15, command=self.eliminar)
    self.boton_añadir.place(x=350, y=300)
          
    self.ventana.mainloop()
        

  def añadir(self):
    producto = self.entrada_producto.get()
    precio = self.entrada_precio.get()
    
    self.Productos.append({'nombre': producto, 'precio': precio})
    
    self.lista_elementos.insert(END, producto)
    #self.entrada_producto.set("")  # Limpiar la entrada productos después de añadir el elemento
    #self.entrada_precio.set("")    # Limpiar la entrada precios después de añadir el elemento
    #self.entrada_elementos1.focus_set() # Establecer el foco en la entrada de productos
    

  def mostrar_precio (self):
    # Obtener producto seleccionado
    seleccion = self.lista_elementos.get(self.lista_elementos.curselection())
    for producto in self.Productos:
      if producto['nombre'] == seleccion:
        precio = producto['precio']
        break
    self.caja_precio.delete(0,END)
    self.caja_precio.insert(0, precio)


  def eliminar(self):
    # Obtener los índices de los elementos seleccionados
    indices = self.lista_elementos.curselection()

    # Iterar sobre los índices seleccionados y eliminar los elementos
    for indice in reversed(indices):
      self.lista_elementos.delete(indice)



aplicacion1 = Aplicacion()
