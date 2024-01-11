import tkinter as tk  # importa la libreria tkinter y lo renombre como tk para facilitar sus uso

class Aplicacion: # define una clase llamada aplicacion
  
  def __init__(self):
    self.ventana=tk.Tk()
    
    # Controles: Label, Entry, Button
    
    self.label1=tk.Label(self.ventana,text="Ingrese un Numero:") # label = etiquetas
    self.label1.grid(column=0, row=0) # ubicar el la etiqueta en la ventana
    self.dato=tk.StringVar() # Almacena el valor
    
    self.entry1=tk.Entry(self.ventana, width=10, textvariable=self.dato) # Entry = cajas de texto
    self.entry1.grid(column=0, row=1) # ubicar la caja de texto en la ventana
    
    
    self.boton= tk.Button(self.ventana, text="Calcular Cuadrado", command=self.calcularcuadrado) # Button = botones
    self.boton.grid(column=0, row=2) # ubicar el boton en la ventana
    
    self.label2= tk.Label(self.ventana, text="Resultado") # label = etiquetas
    self.label2.grid(column=0, row=3) # ubicar el la etiqueta en la ventana
    
    self.ventana.mainloop() # evento mainloop(), muestra la interfaz grafica
    
  def calcularcuadrado(self):
    valor= int(self.dato.get()) # convierte el valor ingresado en entero
    Cuadrado=valor*valor
    self.label2.configure(text=Cuadrado) # mostrara el resultado
    
aplicacion1=Aplicacion()