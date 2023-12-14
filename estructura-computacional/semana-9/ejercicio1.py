from tkinter import *
from tkinter import ttk
root = Tk()
frm= ttk.Frame(root,padding=10)
frm.grid()
ttk.Label(frm,text="Pedro Noriega ").grid(column=0,row=0)
ttk.Label(frm,text="Gestion de sistemas ").grid(column=0,row=1)
ttk.Label(frm,text="Zegel IPAE").grid(column=0,row=2)
ttk.Button(frm,text="salir",command=root.destroy).grid(column=1,row=0)

root.mainloop()