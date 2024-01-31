
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
        self.scroll1.grid(column=1, row=0, sticky=tk.NS) # le da ubicacion al scroll1 y configura el desplazamiento del scroll

        self.listbox1.grid(column=0,row=0)
        self.listbox1.insert(0,"amazonas")
        self.listbox1.insert(1,"ancash")
        self.listbox1.insert(2,"apurimac")
        self.listbox1.insert(3,"arequipa")
        self.listbox1.insert(4,"ayacucho")
        self.listbox1.insert(5,"cajamarca")
        self.listbox1.insert(6,"callao")
        self.listbox1.insert(7,"cuzco")
        self.listbox1.insert(8,"huancavelica")
        self.listbox1.insert(9,"huanuco")
        self.listbox1.insert(10,"ica")
        self.listbox1.insert(11,"junin")
        self.listbox1.insert(12,"la libertad")
        self.listbox1.insert(13,"lambayeque")
        self.listbox1.insert(14,"lima")
        self.listbox1.insert(15,"loreto")
        self.listbox1.insert(16,"madre de dios")
        self.listbox1.insert(17,"moquegua")
        self.listbox1.insert(18,"pasco")
        self.listbox1.insert(19,"piura")
        self.listbox1.insert(20,"puno")
        self.listbox1.insert(21,"san martin")
        self.listbox1.insert(22,"tacna")
        self.listbox1.insert(23,"tumbes")
        self.listbox1.insert(24,"ucayali")

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