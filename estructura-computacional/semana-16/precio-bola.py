
import tkinter as tk 
class Aplicacion: 
    def __init__(self): 
        self.ventana1=tk.Tk()
        self.label1=tk.Label(self.ventana1,text="cantidad:") 
        self.label1.grid(column=0, row=0)
        self.dato1= tk.StringVar()
        self.entry1 = tk.Entry(self.ventana1, width=20, textvariable=self.dato1)
        self.entry1.grid(column=1, row=0)
        self.entry1.config(fg="blue", justify="center")

        self.label2=tk.Label(self.ventana1,text="precio:") 
        self.label2.grid(column=0, row=1)
        self.dato2= tk.StringVar()
        self.entry2 = tk.Entry(self.ventana1, width=20, textvariable=self.dato2)
        self.entry2.grid(column=1, row=1)
        self.entry2.config(fg="blue", justify="center")


        self.seleccion=tk.IntVar()
        self.radio1=tk.Radiobutton(self.ventana1, text="bola roja",fg="red", variable=self.seleccion,value=1)
        self.radio1.grid(column=2,row=1, sticky="w")

        self.radio2=tk.Radiobutton(self.ventana1, text="bola morada",fg="purple", variable=self.seleccion,value=2)
        self.radio2.grid(column=2,row=2, sticky="w")

        self.radio3=tk.Radiobutton(self.ventana1, text="bola verde",fg="green", variable=self.seleccion,value=3)
        self.radio3.grid(column=2,row=3, sticky="w")

        

        self.label3=tk.Label(self.ventana1,text="Subtotal:") 
        self.label3.grid(column=0, row=2)
        self.dato3= tk.StringVar()
        self.entry3 = tk.Entry(self.ventana1, width=20, textvariable=self.dato3, state='readonly')
        self.entry3.grid(column=1, row=2)
        self.entry3.config(fg="red", justify="center")

        self.label4=tk.Label(self.ventana1,text="Descuento:") 
        self.label4.grid(column=0, row=3)
        self.dato4= tk.StringVar()
        self.entry4 = tk.Entry(self.ventana1, width=20, textvariable=self.dato4, state='readonly')
        self.entry4.grid(column=1, row=3)
        self.entry4.config(fg="red", justify="center")

        self.label5=tk.Label(self.ventana1,text="total:") 
        self.label5.grid(column=0, row=4)
        self.dato5= tk.StringVar()
        self.entry5 = tk.Entry(self.ventana1, width=20, textvariable=self.dato5, state='readonly')
        self.entry5.grid(column=1, row=4)
        self.entry5.config(fg="red", justify="center")

        self.boton1=tk.Button(self.ventana1, text="Total",width=5, command=self.operar)
        self.boton1.grid(column=0, row=5, columnspan=2)

        self.boton2=tk.Button(self.ventana1, text="Limpiar",width=5, command=self.limpiar)
        self.boton2.grid(column=1, row=5, columnspan=2)

        self.ventana1.mainloop()

    def operar(self):
        if self.seleccion.get()==1:
            subtotal=float(self.dato1.get()) * float(self.dato2.get())
            self.dato3.set(subtotal)
            Descuento = 1
            self.dato4.set(Descuento)
            total = subtotal - Descuento
            self.dato5.set(total)
            
        if self.seleccion.get()==2:
            subtotal=float(self.dato1.get()) * float(self.dato2.get())
            self.dato3.set(subtotal)
            Descuento = 2
            self.dato4.set(Descuento)
            total = subtotal - Descuento
            self.dato5.set(total)
            
        if self.seleccion.get()==3:
            subtotal=float(self.dato1.get()) * float(self.dato2.get())
            self.dato3.set(subtotal)
            Descuento = 3
            self.dato4.set(Descuento)
            total = subtotal - Descuento
            self.dato5.set(total)


    def limpiar(self):
            self.dato1.set("")
            self.dato2.set("")
            self.entry1.focus_set()

aplicacion1=Aplicacion()