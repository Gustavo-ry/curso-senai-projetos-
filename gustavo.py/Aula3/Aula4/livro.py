import tkinter as tk
from tkinter import messagebox

# Configurações visuais
valorpady = 10
valorpadx = 10

livraria = []

def limparTela():
    entryTexto1.delete(0, tk.END)
    entryTexto2.delete(0, tk.END)
    entryTexto3.delete(0, tk.END)
    entryTexto4.delete(0, tk.END)
    entryTexto5.delete(0, tk.END)
    entryTexto6.delete(0, tk.END)
    entryTexto7.delete(0, tk.END)


def gravar():
    livro = {'ISBN': entryTexto1.get(),
         'titulo': entryTexto2.get(),
         'Autor': entryTexto3.get(),
         'Editora': entryTexto4.get(),
         'Paginas': entryTexto5.get(),
         'Ano': entryTexto6.get(),
         'Genero': entryTexto7.get()
         }
    livraria.append(livro)
    messagebox.showinfo("Gravar", "Livro cadastrado com sucesso!")
    limparTela()




# Janela principal
janelaPrincipal = tk.Tk()
janelaPrincipal.title('Biblioteca')
janelaPrincipal.geometry('800x600')
janelaPrincipal.configure(bg='white')


# Label e entrada do primeiro número
labelTexto1 = tk.Label(janelaPrincipal, text='Digite o título do livro:', font=('Arial', 18), bg='white', width=20,)
labelTexto1.grid(row=0, column=0, padx=valorpadx, pady=valorpady)

entryTexto1 = tk.Entry(janelaPrincipal, width=10, font=('Arial', 20), bg='white', fg='black', bd=5, justify='right')
entryTexto1.grid(row=0, column=1, padx=valorpadx, pady=valorpady)

# Label e entrada do segundo número
labelTexto2 = tk.Label(janelaPrincipal, text='Digite o Autor do livro:', font=('Arial', 18), bg='white', width=20)
labelTexto2.grid(row=1, column=0, padx=valorpadx, pady=valorpady)

entryTexto2 = tk.Entry(janelaPrincipal, width=10, font=('Arial', 20), bg='white', fg='black', bd=5, justify='right')
entryTexto2.grid(row=1, column=1, padx=valorpadx, pady=valorpady)

# Label e entrada do terceiro número
labelTexto3 = tk.Label(janelaPrincipal, text='Digite o ano do livro:', font=('Arial', 18), bg='white', width=20)
labelTexto3.grid(row=2, column=0, padx=valorpadx, pady=valorpady)

entryTexto3 = tk.Entry(janelaPrincipal, width=10, font=('Arial', 20), bg='white', fg='black', bd=5, justify='right')
entryTexto3.grid(row=2, column=1, padx=valorpadx, pady=valorpady)

# Label e entrada do quarto número
labelTexto4 = tk.Label(janelaPrincipal, text='Digite o genero do livro:', font=('Arial', 18), bg='white', width=20)
labelTexto4.grid(row=3, column=0, padx=valorpadx, pady=valorpady)

entryTexto4 = tk.Entry(janelaPrincipal, width=10, font=('Arial', 20), bg='white', fg='black', bd=5, justify='right')
entryTexto4.grid(row=3, column=1, padx=valorpadx, pady=valorpady)

# Label e entrada do quinto número
labelTexto5 = tk.Label(janelaPrincipal, text='Digite o numero de paginas do livro:', font=('Arial', 18), bg='white',)
labelTexto5.grid(row=4, column=0, padx=valorpadx, pady=valorpady)

entryTexto5 = tk.Entry(janelaPrincipal, width=10, font=('Arial', 20), bg='white', fg='black', bd=5, justify='right')
entryTexto5.grid(row=4, column=1, padx=valorpadx, pady=valorpady)

# Label e entrada do sexto número
labelTexto6 = tk.Label(janelaPrincipal, text='Digite a editora:', font=('Arial', 18), bg='white', width=20)
labelTexto6.grid(row=5, column=0, padx=valorpadx, pady=valorpady)

entryTexto6 = tk.Entry(janelaPrincipal, width=10, font=('Arial', 20), bg='white', fg='black', bd=5, justify='right')
entryTexto6.grid(row=5, column=1, padx=valorpadx, pady=valorpady)

# Label e entrada do setimo numero
labelTexto7 = tk.Label(janelaPrincipal, text='Digite o codigo ISBN:', font=('Arial', 18), bg='white', width=20)
labelTexto7.grid(row=6, column=0, padx=valorpadx, pady=valorpady)

entryTexto7 = tk.Entry(janelaPrincipal, width=10, font=('Arial', 20), bg='white', fg='black', bd=5, justify='right')
entryTexto7.grid(row=6, column=1, padx=valorpadx, pady=valorpady)



# Funções de operação


def localizar():
    titulo = entryTexto1.get()
    autor = entryTexto2.get()
    ano = entryTexto3.get()
    genero = entryTexto4.get()
    numeropaginas = entryTexto5.get()
    editora = entryTexto6.get()
    IBSN = entryTexto7.get()

def excluir():
    entryTexto1.delete(0, tk.END)
    entryTexto2.delete(0, tk.END)
    entryTexto3.delete(0, tk.END)
    entryTexto4.delete(0, tk.END)
    entryTexto5.delete(0, tk.END)
    entryTexto6.delete(0, tk.END)
    entryTexto7.delete(0, tk.END)

    messagebox.showinfo("Limpar", "Limpos com sucesso!")


# Botões
buttongravar = tk.Button(janelaPrincipal, text='gravar', width=15, font=('Arial', 15), bg='pink', bd=5, command=gravar)
buttongravar.grid(row=7, column=0, padx=valorpadx, pady=valorpady)

buttonExcluir = tk.Button(janelaPrincipal, text='Limpar', width=15, font=('Arial', 15), bg='lightblue', bd=5, command=excluir)
buttonExcluir.grid(row=7, column=1, padx=valorpadx, pady=valorpady, columnspan=1)

buttonLocalizar = tk.Button(janelaPrincipal, text='Localizar', width=15, font=('Arial', 15), bg='lightgreen', bd=5, command=localizar)
buttonLocalizar.grid(row=8, column=1, padx=valorpadx, pady=valorpady, columnspan=1)

listagem = tk.Text(janela)
listagem.grid(row=9, column=0, columnspan=2, padx=valorpadx, pady=valorpady, sticky='nsew')


# Inicia a interface
janelaPrincipal.mainloop()
