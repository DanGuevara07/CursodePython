import tkinter
from tkinter import ttk

window = tkinter.Tk()
window.columnconfigure(0, weight=1)
window.columnconfigure(1, weight=3)

label = ttk.Label(window, text='Seleccione un item de la lista:')
label.grid(column=0, row=0, sticky=tkinter.W, padx=50,pady=50)

# lista muestra una lista de items seleccionables
lista = ['Pan', 'Tomate', 'Lechuga', 'Queso', 'Huevos', 'Azucar', 'Sal']
lista_items = tkinter.StringVar(value= lista)
listbox = tkinter.Listbox(window, height=10, listvariable=lista_items)
listbox.grid(column=0,row=1, sticky=tkinter.W)

window.mainloop()