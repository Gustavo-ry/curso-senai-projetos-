import tkinter as tk #importando a biblioteca tkinter
from tkinter import messagebox

def mensagem():
    messagebox.showinfo("ANTENÇÃO", F"voce foi hackeado {entryNome.get()}")

# crinado variaveis para o espaçamento
valorpady = 15
valorpadx = 15

# criando uma janela
janelaPrincipal = tk.Tk()
janelaPrincipal.title("minha primeira janela")
janelaPrincipal.geometry("800x600") # largura x altura
janelaPrincipal.configure(bg='white') # cor de fundo da janela


labelFrase = tk.Label(janelaPrincipal, text='seja bem vindo!',bg='gray',fg = 'orange', font=['Arial', 30],)
labelFrase.pack(padx=valorpadx, pady=valorpady) # adicionando um label a janela

labelNome = tk.Label(janelaPrincipal, text='digite seu nome:', font=['arial', 20])
labelNome.pack(padx=valorpadx, pady=valorpady)
entryNome = tk.Entry(janelaPrincipal,width=30,font=['Arial', 20],bg='white',fg='black',border= 5)
entryNome.pack(padx=valorpadx, pady=valorpady)

buttonEnviar = tk.Button(janelaPrincipal, text='enviar',width= 10, font=['Arial', 15],command=mensagem)
command=lambda:messagebox.showinfo("ANTENÇÃO", F"voce foi hackeado {entryNome.get()}")
buttonEnviar.pack(padx=valorpadx, pady=valorpady)


janelaPrincipal.mainloop()
