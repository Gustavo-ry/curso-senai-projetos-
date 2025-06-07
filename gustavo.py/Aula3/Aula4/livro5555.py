import tkinter as tk
from tkinter import messagebox, ttk
import json
import os

# Constants
ARQUIVO_JSON = 'livros.json'
FONT = ('Calibri', 16)
BG_COLOR = "#ffffff"
FG_COLOR = "#323130"
ACCENT_COLOR = "#2563eb"
ACCENT_HOVER = "#1e40af"
CARD_BG = "#f9fafb"
PADDING = 10

# Global Variables
livraria = []
indice_selecionado = None

# Functions for data persistence
def carregar_livros():
    global livraria
    if os.path.exists(ARQUIVO_JSON):
        with open(ARQUIVO_JSON, 'r', encoding='utf-8') as f:
            livraria = json.load(f)

def salvar_livros():
    with open(ARQUIVO_JSON, 'w', encoding='utf-8') as f:
        json.dump(livraria, f, ensure_ascii=False, indent=4)

# Clear input fields
def limpar_tela():
    entryISBN.delete(0, tk.END)
    entryTítulo.delete(0, tk.END)
    entryAutor.delete(0, tk.END)
    entryEditora.delete(0, tk.END)
    entryPáginas.delete(0, tk.END)
    entryAno.delete(0, tk.END)
    entryGênero.delete(0, tk.END)

# Save book
def gravar():
    livro = {
        'ISBN': entryISBN.get(),
        'Titulo': entryTítulo.get(),
        'Autor': entryAutor.get(),
        'Editora': entryEditora.get(),
        'Páginas': entryPáginas.get(),
        'Ano': entryAno.get(),
        'Gênero': entryGênero.get()
    }
    livraria.append(livro)
    salvar_livros()
    messagebox.showinfo('Sucesso', 'Livro cadastrado com sucesso!')
    limpar_tela()
    atualizar_tabela()

# Update table
def atualizar_tabela():
    for row in tabela.get_children():
        tabela.delete(row)

    for livro in livraria:
        tabela.insert('', 'end', values=(
            livro['ISBN'],
            livro['Titulo'],
            livro['Autor'],
            livro['Editora'],
            livro['Páginas'],
            livro['Ano'],
            livro['Gênero']
        ))

# Fill fields with selected book data
def preencher_campos(event):
    global indice_selecionado

    item_selecionado = tabela.selection()
    if item_selecionado:
        item_index = tabela.index(item_selecionado[0])
        indice_selecionado = item_index
        valores = tabela.item(item_selecionado)['values']

        entryISBN.delete(0, tk.END)
        entryISBN.insert(0, valores[0])
        entryTítulo.delete(0, tk.END)
        entryTítulo.insert(0, valores[1])
        entryAutor.delete(0, tk.END)
        entryAutor.insert(0, valores[2])
        entryEditora.delete(0, tk.END)
        entryEditora.insert(0, valores[3])
        entryPáginas.delete(0, tk.END)
        entryPáginas.insert(0, valores[4])
        entryAno.delete(0, tk.END)
        entryAno.insert(0, valores[5])
        entryGênero.delete(0, tk.END)
        entryGênero.insert(0, valores[6])

# Delete selected book
def excluir_livro():
    global indice_selecionado

    if indice_selecionado is not None:
        resposta = messagebox.askyesno('Confirmar Exclusão', 'Tem certeza que deseja excluir este livro?')
        if resposta:
            del livraria[indice_selecionado]
            salvar_livros()
            indice_selecionado = None
            limpar_tela()
            atualizar_tabela()
            messagebox.showinfo('Sucesso', 'Livro excluído com sucesso!')
    else:
        messagebox.showwarning('Aviso', 'Nenhum livro selecionado para excluir!')

# Search for a book by title
def localizar_livro():
    termo_busca = entryTítulo.get().lower()

    if not termo_busca:
        messagebox.showwarning('Aviso', 'Digite um título para buscar!')
        return

    for item in tabela.selection():
        tabela.selection_remove(item)

    for item in tabela.get_children():
        valores = tabela.item(item)['values']
        titulo_livro = valores[1].lower()

        if termo_busca in titulo_livro:
            tabela.selection_add(item)
            tabela.see(item)
            preencher_campos(None)  # Fill fields with found book data
            return

    messagebox.showinfo('Busca', 'Nenhum livro encontrado com esse termo!')

# Main Application
class BookManagerApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Cadastro de Livros')
        self.geometry('1000x600')
        self.configure(bg=BG_COLOR)

        # Create main frame
        self.main_frame = tk.Frame(self, bg=BG_COLOR)
        self.main_frame.pack(padx=PADDING, pady=PADDING, fill='both', expand=True)

        # Create input fields
        self.create_input_fields()

        # Create buttons
        self.create_buttons()

        # Create table
        self.create_table()

        # Load existing books
        carregar_livros()
        atualizar_tabela()

    def create_input_fields(self):
        labels = ['ISBN', 'Título', 'Autor', 'Editora', 'Páginas', 'Ano', 'Gênero']
        global entryISBN, entryTítulo, entryAutor, entryEditora, entryPáginas, entryAno, entryGênero

        for i, label in enumerate(labels):
            tk.Label(self.main_frame, text=label, font=FONT, bg=BG_COLOR, fg=FG_COLOR).grid(row=i, column=0, padx=PADDING, pady=PADDING, sticky='w')
            entry = ttk.Entry(self.main_frame, font=FONT, width=40)
            entry.grid(row=i, column=1, padx=PADDING, pady=PADDING)
            if label == 'ISBN':
                entryISBN = entry
            elif label == 'Título':
                entryTítulo = entry
            elif label == 'Autor':
                entryAutor = entry
            elif label == 'Editora':
                entryEditora = entry
            elif label == 'Páginas':
                entryPáginas = entry
            elif label == 'Ano':
                entryAno = entry
            elif label == 'Gênero':
                entryGênero = entry

    def create_buttons(self):
        button_frame = tk.Frame(self.main_frame, bg=BG_COLOR)
        button_frame.grid(row=len(entryGênero.grid_info()) + 1, columnspan=2, pady=PADDING)

        btn_gravar = tk.Button(button_frame, text='Gravar', font=FONT, bg=ACCENT_COLOR, fg='white', command=gravar)
        btn_gravar.grid(row=0, column=0, padx=PADDING)

        btn_deletar = tk.Button(button_frame, text='Excluir', font=FONT, bg=ACCENT_COLOR, fg='white', command=excluir_livro)
        btn_deletar.grid(row=0, column=1, padx=PADDING)

        btn_localizar = tk.Button(button_frame, text='Localizar', font=FONT, bg=ACCENT_COLOR, fg='white', command=localizar_livro)
        btn_localizar.grid(row=0, column=2, padx=PADDING)

    def create_table(self):
        frame_tabela = tk.Frame(self.main_frame, bg=BG_COLOR)
        frame_tabela.grid(row=len(entryGênero.grid_info()) + 2, columnspan=2, pady=PADDING, sticky='nsew')

        global tabela
        tabela = ttk.Treeview(frame_tabela, columns=('ISBN', 'Título', 'Autor', 'Editora', 'Páginas', 'Ano', 'Gênero'), show='headings')
        tabela.heading('ISBN', text='ISBN')
        tabela.heading('Título', text='Título')
        tabela.heading('Autor', text='Autor')
        tabela.heading('Editora', text='Editora')
        tabela.heading('Páginas', text='Páginas')
        tabela.heading('Ano', text='Ano')
        tabela.heading('Gênero', text='Gênero')

        tabela.column('ISBN', width=100)
        tabela.column('Título', width=200)
        tabela.column('Autor', width=150)
        tabela.column('Editora', width=100)
        tabela.column('Páginas', width=70)
        tabela.column('Ano', width=70)
        tabela.column('Gênero', width=100)

        tabela.pack(fill='both', expand=True)
        tabela.bind('<ButtonRelease-1>', preencher_campos)

        scrollbar = ttk.Scrollbar(frame_tabela, orient='vertical', command=tabela.yview)
        tabela.configure(yscroll=scrollbar.set)
        scrollbar.pack(side='right', fill='y')

# Run the application
if __name__ == "__main__":
    app = BookManagerApp()
    app.mainloop()
