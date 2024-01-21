
import tkinter as tk

class Aplicacion:
    def __init__(self):
        self.ventana =tk.Tk()

        # Crear un scrollbar
        self.scroll1 =tk.Scrollbar(self.ventana)
        # Crear el Listbox y asociarlo con el scrollbar
        self.listbox1=tk.Listbox(self.ventana,selectmode=tk.MULTIPLE, yscrollcommand=self.scroll1.set, selectbackground="lightblue")

        # Configurar el scrollbar para desplazar el Listbox
        self.scroll1.config(command=self.listbox1.yview)

        self.listbox1.grid(column=0,row=0)
        self.scroll1.grid(column=1, row=0, sticky=tk.NS) # le da ubicacion al scroll1 y configura el desplazamiento del scroll
        self.listbox1.insert(0,"memoria ram")
        self.listbox1.insert(1,"procesador")
        self.listbox1.insert(2,"HDD")
        self.listbox1.insert(3,"SDD")
        self.listbox1.insert(4,"teclado")
        self.listbox1.insert(5,"mouse")
        self.listbox1.insert(6,"parlantes")
        self.listbox1.insert(7,"motherboard")
        self.listbox1.insert(8,"cable hdmi")
        self.listbox1.insert(9,"monitor")
        
        

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