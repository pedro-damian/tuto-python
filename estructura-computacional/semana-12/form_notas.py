
import tkinter as tk
class Aplicacion:

    def __init__(self):
        self.ventana1 = tk.Tk()

        # MATEMATICAS
        self.matematica = tk.Label(self.ventana1, text="MATEMATICA")
        self.matematica.grid(column=0, row=0)

        self.label1 = tk.Label(self.ventana1, text="NOTA1:")
        self.label1.grid(column=0, row=1)
        self.notamate1 = tk.StringVar()
        self.entry1 = tk.Entry(self.ventana1, width=10,
                               textvariable=self.notamate1)
        self.entry1.grid(column=1, row=1)

        self.label2 = tk.Label(self.ventana1, text="NOTA2:")
        self.label2.grid(column=0, row=2)
        self.notamate2 = tk.StringVar()
        self.entry2 = tk.Entry(self.ventana1, width=10,
                               textvariable=self.notamate2)
        self.entry2.grid(column=1, row=2)

        self.label3 = tk.Label(self.ventana1, text="NOTA3:")
        self.label3.grid(column=0, row=3)
        self.notamate3 = tk.StringVar()
        self.entry3 = tk.Entry(self.ventana1, width=10,
                               textvariable=self.notamate3)
        self.entry3.grid(column=1, row=3)

        # botones
        self.boton1 = tk.Button(
            self.ventana1, text="Promedio:", command=self.promediomatematica)
        self.boton1.grid(column=0, row=4)

        self.label4 = tk.Label(self.ventana1, width=10, text="")
        self.label4.grid(column=1, row=4)

        # LENGUAJE
        self.lenguaje = tk.Label(self.ventana1, text="LENGUAJE")
        self.lenguaje.grid(column=3, row=0)

        self.label5 = tk.Label(self.ventana1, text="NOTA1:")
        self.label5.grid(column=3, row=1)
        self.notalengua1 = tk.StringVar()
        self.entry4 = tk.Entry(self.ventana1, width=10,
                               textvariable=self.notalengua1)
        self.entry4.grid(column=4, row=1)

        self.label6 = tk.Label(self.ventana1, text="NOTA2:")
        self.label6.grid(column=3, row=2)
        self.notalengua2 = tk.StringVar()
        self.entry5 = tk.Entry(self.ventana1, width=10,
                               textvariable=self.notalengua2)
        self.entry5.grid(column=4, row=2)

        self.label7 = tk.Label(self.ventana1, text="NOTA3:")
        self.label7.grid(column=3, row=3)
        self.notalengua3 = tk.StringVar()
        self.entry6 = tk.Entry(self.ventana1, width=10,
                               textvariable=self.notalengua3)
        self.entry6.grid(column=4, row=3)

        # botones
        self.boton2 = tk.Button(
            self.ventana1, text="Promedio:", command=self.promediolenguaje)
        self.boton2.grid(column=3, row=4)

        self.label8 = tk.Label(self.ventana1, width=10, height=3, text="")
        self.label8.grid(column=4, row=4)

        # HISTORIA
        self.historia = tk.Label(self.ventana1, text="HISTORIA")
        self.historia.grid(column=5, row=0)

        self.label9 = tk.Label(self.ventana1, text="NOTA1:")
        self.label9.grid(column=5, row=1)
        self.notahistoria1 = tk.StringVar()
        self.entry7 = tk.Entry(self.ventana1, width=10,
                               textvariable=self.notahistoria1)
        self.entry7.grid(column=6, row=1)

        self.label10 = tk.Label(self.ventana1, text="NOTA2:")
        self.label10.grid(column=5, row=2)
        self.notahistoria2 = tk.StringVar()
        self.entry8 = tk.Entry(self.ventana1, width=10,
                               textvariable=self.notahistoria2)
        self.entry8.grid(column=6, row=2)

        self.label11 = tk.Label(self.ventana1, text="NOTA3:")
        self.label11.grid(column=5, row=3)
        self.notahistoria3 = tk.StringVar()
        self.entry9 = tk.Entry(self.ventana1, width=10,
                               textvariable=self.notahistoria3)
        self.entry9.grid(column=6, row=3)

        # botones
        self.boton3 = tk.Button(
            self.ventana1, text="Promedio:", command=self.promediohistoria)
        self.boton3.grid(column=5, row=4)

        self.label12 = tk.Label(self.ventana1, width=10, height=3, text="")
        self.label12.grid(column=6, row=4)

        # RESULTADOS ESTADISTICOS
        # MATEMATICAS
        self.label40 = tk.Label(
            self.ventana1, text="RESULTADOS  ESTADISTICOS:")
        self.label40.grid(column=2, row=6, columnspan=3)

        self.label40 = tk.Label(self.ventana1, text="NOTA MAYOR:")
        self.label40.grid(column=0, row=7)
        self.label41 = tk.Label(self.ventana1, width=10, text="")
        self.label41.grid(column=1, row=7)

        self.label40 = tk.Label(self.ventana1, text="NOTA MENOR:")
        self.label40.grid(column=0, row=8)
        self.label42 = tk.Label(self.ventana1, width=10, text="")
        self.label42.grid(column=1, row=8)

        # LENGUAJE
        self.label40 = tk.Label(self.ventana1, text="NOTA MAYOR:")
        self.label40.grid(column=3, row=7)
        self.label43 = tk.Label(self.ventana1, width=10, text="")
        self.label43.grid(column=4, row=7)

        self.label40 = tk.Label(self.ventana1, text="NOTA MENOR:")
        self.label40.grid(column=3, row=8)
        self.label44 = tk.Label(self.ventana1, width=10, text="")
        self.label44.grid(column=4, row=8)

        # HISTORIA
        self.label40 = tk.Label(self.ventana1, text="NOTA MAYOR:")
        self.label40.grid(column=5, row=7)
        self.label45 = tk.Label(self.ventana1, width=10, text="")
        self.label45.grid(column=6, row=7)

        self.label40 = tk.Label(self.ventana1, text="NOTA MENOR:")
        self.label40.grid(column=5, row=8)
        self.label46 = tk.Label(self.ventana1, width=10, text="")
        self.label46.grid(column=6, row=8)

        # MATERIAS CON PROMEDIO MAYOR Y MENOR
        self.label60 = tk.Label(self.ventana1, text="")
        self.label60.grid(column=0, row=9, columnspan=4)
        self.boton4 = tk.Button(self.ventana1, text="EL MAYOR PROMEDIO GENERAL:", command=self.promedio_mayor)
        self.boton4.grid(column=0, row=10, columnspan=4)
        self.label62 = tk.Label(self.ventana1, width=10, text="")
        self.label62.grid(column=5, row=10)

        self.boton5 = tk.Button(self.ventana1, text="EL MENOR PROMEDIO GENERAL:", command=self.promedio_menor)
        self.boton5.grid(column=0, row=11, columnspan=4)
        self.label64 = tk.Label(self.ventana1, width=10, text="")
        self.label64.grid(column=5, row=11)

        self.ventana1.mainloop()

    def promediomatematica(self):

        valor1 = int(self.notamate1.get())
        valor2 = int(self.notamate2.get())
        valor3 = int(self.notamate3.get())

        self.promedio1 = (valor1 * 0.4) + (valor2 * 0.4) + (valor3 * 0.2)

        notas = [valor1, valor2, valor3]
        nota_mayor = max(notas)
        nota_menor = min(notas)

        self.label4.configure(text=round(self.promedio1, 1))
        self.label41.configure(text=nota_mayor)
        self.label42.configure(text=nota_menor)
        self.notamate1.set("")
        self.notamate2.set("")
        self.notamate3.set("")
        self.entry1.focus_set()

    def promediolenguaje(self):

        valor1 = int(self.notalengua1.get())
        valor2 = int(self.notalengua2.get())
        valor3 = int(self.notalengua3.get())

        self.promedio2 = (valor1 * 0.4) + (valor2 * 0.4) + (valor3 * 0.2)

        notas = [valor1, valor2, valor3]
        nota_mayor = max(notas)
        nota_menor = min(notas)

        self.label43.configure(text=nota_mayor)
        self.label44.configure(text=nota_menor)
        self.label8.configure(text=round(self.promedio2, 1))
        self.notalengua1.set("")
        self.notalengua2.set("")
        self.notalengua3.set("")
        self.entry4.focus_set()

    def promediohistoria(self):

        valor1 = int(self.notahistoria1.get())
        valor2 = int(self.notahistoria2.get())
        valor3 = int(self.notahistoria3.get())

        self.promedio3 = (valor1 * 0.4) + (valor2 * 0.4) + (valor3 * 0.2)

        notas = [valor1, valor2, valor3]
        nota_mayor = max(notas)
        nota_menor = min(notas)

        self.label45.configure(text=nota_mayor)
        self.label46.configure(text=nota_menor)
        self.label12.configure(text=round(self.promedio3, 1))
        self.notahistoria1.set("")
        self.notahistoria2.set("")
        self.notahistoria3.set("")
        self.entry7.focus_set()

    def promedio_mayor(self):

        promedios = [self.promedio1,self.promedio2,self.promedio3]
        promedio_mayor = max(promedios)
        self.label62.configure(text=round(promedio_mayor,1))

    def promedio_menor(self):
        promedios = [self.promedio1, self.promedio2,self.promedio3]
        promedio_menor = min(promedios)
        self.label64.configure(text=round(promedio_menor,1))


aplicacion1 = Aplicacion()
