
from tkinter import *

raiz = Tk()
raiz.title("CheckButtons")
raiz.geometry("400x200")

playa=IntVar()
montaña=IntVar()
rural=IntVar()

foto=PhotoImage(file="guardar-grande.png")
label1= Label(raiz,image=foto)
label1.grid(row=0,column=0)

miframe = Frame(raiz, borderwidth=2, relief="groove")
miframe.grid(row=1, column=0,padx=(50,10))

label2= Label(miframe,text="Elige Tu destino:")
label2.grid(row=2,column=0)
check1 = Checkbutton(miframe, text="Playa",padx=10)
check1.grid(row=3,column=0)
check1 = Checkbutton(miframe, text="Montaña")
check1.grid(row=4,column=0)
check1 = Checkbutton(miframe, text="Rural")
check1.grid(row=5,column=0)


raiz.mainloop()