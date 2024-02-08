
import tkinter as tk 
from tkinter import ttk
from tkinter import messagebox

raiz = tk.Tk()
raiz.title("Riesgos de Huaycos en Departamentos")
raiz.geometry("400x200")


def reportes(): 
  seleccion = opcion.get()
  if seleccion == "Lima":
    messagebox.showinfo("Lima", "Habitantes: 100,00.\nCasa alrededor del rio: SI\nIntensidad: 40%\n")
  if seleccion == "Ica":
    messagebox.showinfo("Ica", "Habitantes: 80,00.\nCasa alrededor del rio: SI\nIntensidad: 60%\n")
  if seleccion == "Arequipa":
    messagebox.showinfo("Arequipa", "Habitantes: 120,00.\nCasa alrededor del rio: SI\nIntensidad: 50%\n")
  if seleccion == "Ilo":
    messagebox.showinfo("Ilo", "Habitantes: 20,00.\nCasa alrededor del rio: SI\nIntensidad: 70%\n")
  if seleccion == "Chimbote":
    messagebox.showinfo("Chimbote", "Habitantes: 30,00.\nCasa alrededor del rio: SI\nIntensidad: 30%\n")
  if seleccion == "Trujillo":
    messagebox.showinfo("Trujillo", "Habitantes: 150,00.\nCasa alrededor del rio: SI\nIntensidad: 80%\n")
  if seleccion == "Tacna":
    messagebox.showinfo("Tacna", "Habitantes: 60,00.\nCasa alrededor del rio: SI\nIntensidad: 30%\n")
    

def abrir_combobox(event=None):
  combobox1.event_generate('<Down>')
  

label1=ttk.Label(raiz, text="Seleccione un Departamento") 
label1.grid(column=0, row=0, padx=100, pady=(50,10)) 
opcion=tk.StringVar() 
diassemana=("Lima","Ica","Arequipa","Ilo","Chimbote","Trujillo","Tacna") 
combobox1=ttk.Combobox(raiz, width=10, textvariable=opcion, values=diassemana) 
combobox1.current(0) 
combobox1.grid(column=0, row=1)
combobox1.bind("<Button-1>", abrir_combobox)
boton1=tk.Button(raiz, text="Reportes", command=reportes) 
boton1.grid(column=0, row=2, pady=10) 


raiz.mainloop()