
import tkinter as tk

class Aplicacion:
    def __init__(self):
        self.ventana =tk.Tk()
        self.listbox1=tk.Listbox(self.ventana,selectmode=tk.MULTIPLE)
        self.listbox1.grid(column=0,row=0)
        self.listbox1.insert(0,"papa")
        self.listbox1.insert(1,"manzana")
        self.listbox1.insert(2,"pera")
        self.listbox1.insert(3,"sandia")
        self.listbox1.insert(4,"naranja")
        self.listbox1.insert(5,"melon")
        self.boton1=tk.Button(self.ventana, text="Mostrar", command=self.recuperar)
        self.boton1.grid(column=0, row=1)
        self.label1=tk.Label(self.ventana,text="seleccionado:")
        self.label1.grid(column=0,row=2)
        self.ventana.mainloop()

    def recuperar(self):
        if len(self.listbox1.curselection()) !=0:
            todas=''
            for posicion in self.listbox1.curselection():
                todas+=self.listbox1.get(posicion)+"\n"
            self.label1.configure(text=todas)

aplicacion1 = Aplicacion()