import tkinter as tk 
from tkinter import messagebox


Numero1 = 1
Numero2 = 1
soma = 1



valorpady = 15
valorpadx = 15



janelaPrincipal = tk.Tk()
janelaPrincipal.title('calculadora')
janelaPrincipal.geometry('800x600')
janelaPrincipal.configure(bg='white')

labelFrase = tk.Label(janelaPrincipal, text='seja bem vindo a calculadora!',bg='gray',fg = 'orange', font=['Arial', 30],)
labelFrase.pack(padx=15, pady=15)

labelNumero1 = tk.Label(janelaPrincipal, text='digite o primeiro numero:', font=['arial', 20])
labelNumero1.pack(padx=15, pady=15)
entryNumero1 = tk.Entry(janelaPrincipal,width=30,font=['Arial', 20],bg='white',fg='black',border= 5, justify='right')
entryNumero1.pack(padx=15, pady=15)


labelNumero2 = tk.Label(janelaPrincipal, text='digite o segundo numero:', font=['arial', 20])
labelNumero2.pack(padx=15, pady=15)
entryNumero2 = tk.Entry(janelaPrincipal,width=30,font=['Arial', 20],bg='white',fg='black',border= 5, justify='right')
entryNumero2.pack(padx=15, pady=15)

def somar():
    soma = (float(entryNumero1.get())) + (float(entryNumero2.get()))
    Numero1 + Numero2
    messagebox.showinfo("resultado", F"A soma é {soma}")
def subtrair():
    subtracao = (float(entryNumero1.get())) - (float(entryNumero2.get()))
    messagebox.showinfo("resultado", F"A subtração é {subtracao}")
def multiplicar():
    multiplicacao = (float(entryNumero1.get())) * (float(entryNumero2.get()))
    messagebox.showinfo("resultado", F"A multiplicação é {multiplicacao}")
def dividir():
    divisao = (float(entryNumero1.get())) / (float(entryNumero2.get()))
    messagebox.showinfo("resultado", F"A divisão é {divisao}")

    

  
buttonSomar = tk.Button(janelaPrincipal, text='+',width= 10, font=['Arial', 15], bg='pink',border=5, command=somar)
buttonSomar.pack(padx=15, pady=15)

buttonsubtrair = tk.Button(janelaPrincipal, text='-',width= 10, font=['Arial', 15], bg='blue',border=5, command=subtrair)
buttonsubtrair.pack(padx=15, pady=15)

buttonmultiplicar = tk.Button(janelaPrincipal, text='*',width= 10, font=['Arial', 15], bg='green',border=5, command=multiplicar)
buttonmultiplicar.pack(padx=15, pady=15)

buttondivisao = tk.Button(janelaPrincipal, text='/',width= 10, font=['Arial', 15], bg='red',border=5, command= dividir)
buttondivisao.pack(padx=15, pady=15)



comand = lambda : messagebox.showinfo("resultado", F"A soma é {soma:.2f}")


janelaPrincipal.mainloop()