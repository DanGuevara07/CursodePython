import tkinter
from tkinter import ttk

window = tkinter.Tk()
window.columnconfigure(0, weight=1)
window.columnconfigure(1, weight=3)

def mifuncion():
    seleccionado.set(None)

seleccionado= tkinter.StringVar()
r1= ttk.Radiobutton(window, text='opcion1', value= '1', variable=seleccionado)
r2= ttk.Radiobutton(window, text='opcion2', value= '2', variable=seleccionado)
r3= ttk.Radiobutton(window, text='opcion3', value= '3', variable=seleccionado)

r1.grid(column=1, row=0,sticky=tkinter.W, pady=5, padx=5)
r2.grid(column=1, row=1,sticky=tkinter.W, pady=5, padx=5)
r3.grid(column=1, row=2,sticky=tkinter.W, pady=5, padx=5)

botonReinicio = ttk.Button(window, text="Reiniciar Selección", command=mifuncion)
botonReinicio.grid(column=1,row=3,sticky=tkinter.W, pady=5,padx=5)



window.mainloop()