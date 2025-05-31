import tkinter as tk
from tkinter import messagebox

# Configurações visuais
valorpady = 10
valorpadx = 10

# Janela principal
janelaPrincipal = tk.Tk()
janelaPrincipal.title('Calculadora')
janelaPrincipal.geometry('600x400')
janelaPrincipal.configure(bg='white')

# Label e entrada do primeiro número
labelNumero1 = tk.Label(janelaPrincipal, text='Digite o primeiro número:', font=('Arial', 20), bg='white')
labelNumero1.grid(row=0, column=0, padx=valorpadx, pady=valorpady)

entryNumero1 = tk.Entry(janelaPrincipal, width=10, font=('Arial', 20), bg='white', fg='black', bd=5, justify='right')
entryNumero1.grid(row=0, column=1, padx=valorpadx, pady=valorpady)

# Label e entrada do segundo número
labelNumero2 = tk.Label(janelaPrincipal, text='Digite o segundo número:', font=('Arial', 20), bg='white')
labelNumero2.grid(row=1, column=0, padx=valorpadx, pady=valorpady)

entryNumero2 = tk.Entry(janelaPrincipal, width=10, font=('Arial', 20), bg='white', fg='black', bd=5, justify='right')
entryNumero2.grid(row=1, column=1, padx=valorpadx, pady=valorpady)

# Funções de operação
def pegar_valores():
    try:
        num1 = float(entryNumero1.get())
        num2 = float(entryNumero2.get())
        return num1, num2
    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira números válidos.")
        return None, None

def somar():
    num1, num2 = pegar_valores()
    if num1 is not None:
        resultado = num1 + num2
        messagebox.showinfo("Resultado", f"A soma é {resultado:.2f}")

def subtrair():
    num1, num2 = pegar_valores()
    if num1 is not None:
        resultado = num1 - num2
        messagebox.showinfo("Resultado", f"A subtração é {resultado:.2f}")

def multiplicar():
    num1, num2 = pegar_valores()
    if num1 is not None:
        resultado = num1 * num2
        messagebox.showinfo("Resultado", f"A multiplicação é {resultado:.2f}")

def dividir():
    num1, num2 = pegar_valores()
    if num1 is not None:
        if num2 == 0:
            messagebox.showerror("Erro", "Divisão por zero não é permitida.")
        else:
            resultado = num1 / num2
            messagebox.showinfo("Resultado", f"A divisão é {resultado:.2f}")

def limpar():
    entryNumero1.delete(0, tk.END)
    entryNumero2.delete(0, tk.END)

# Botões
buttonSomar = tk.Button(janelaPrincipal, text='+', width=15, font=('Arial', 15), bg='pink', bd=5, command=somar)
buttonSomar.grid(row=2, column=0, padx=15, pady=15)

buttonSubtrair = tk.Button(janelaPrincipal, text='-', width=15, font=('Arial', 15), bg='lightblue', bd=5, command=subtrair)
buttonSubtrair.grid(row=2, column=1, padx=15, pady=15)

buttonMultiplicar = tk.Button(janelaPrincipal, text='*', width=15, font=('Arial', 15), bg='lightgreen', bd=5, command=multiplicar)
buttonMultiplicar.grid(row=3, column=0, padx=15, pady=15)

buttonDividir = tk.Button(janelaPrincipal, text='/', width=15, font=('Arial', 15), bg='tomato', bd=5, command=dividir)
buttonDividir.grid(row=3, column=1, padx=15, pady=15)

buttonLimpar = tk.Button(janelaPrincipal, text='Limpar', width=15, font=('Arial', 15), bg='lightgray', bd=5, command=limpar)
buttonLimpar.grid(row=4, column=0, columnspan=1, padx=15, pady=15)

# Inicia a interface
janelaPrincipal.mainloop()
