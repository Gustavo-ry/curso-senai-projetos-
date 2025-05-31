import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

itens = []

def Adicionar():
    item = entryitem.get()
    if item.strip() != '':
       itens.append(item)  
       comboItens = ttk.Combobox(janela, values=itens)
       comboItens.set('selecione um item')
       comboItens.grid(row=1, column=0, padx=5, pady=5)
       entryitem.delete(0, tk.END)
         


janela = tk.Tk()
janela.title('Testando Lista')
janela.geometry('800x600')

labelitem = tk.Label(janela, text='digite um item')
labelitem.grid(row=0, column=0, padx=5, pady=5)
entryitem = tk.Entry(janela)
entryitem.grid(row=0, column=1, padx=5, pady=5)


buttonItem = tk.Button(janela, text='Adicionar', command=Adicionar)
buttonItem.grid(row=0, column=2, padx=5, pady=5)

comboItens = ttk.Combobox(janela, values=itens)
comboItens.set('selecione um item')
comboItens.grid(row=1, column=0, padx=5, pady=5)

janela.mainloop() 