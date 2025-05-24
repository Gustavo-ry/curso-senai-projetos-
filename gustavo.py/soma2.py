import tkinter as tk 
from tkinter import messagebox


Numero1 = 1
Numero2 = 1
soma = 1



valorpady = 10
valorpadx = 10



janelaPrincipal = tk.Tk()
janelaPrincipal.title('calculadora')
janelaPrincipal.geometry('550x300')
janelaPrincipal.configure(bg='white')


labelNumero1 = tk.Label(janelaPrincipal, text='digite o primeiro numero:', font=['arial', 20])
labelNumero1.grid(row=0, column=0,padx=10, pady=10)
entryNumero1 = tk.Entry(janelaPrincipal,width=10,font=['Arial', 20],bg='white',fg='black',border= 5, justify='right')
entryNumero1.grid(row=0, column=1,padx=10, pady=10)


labelNumero2 = tk.Label(janelaPrincipal, text='digite o segundo numero:', font=['arial', 20])
labelNumero2.grid(row=1, column=0,padx=10, pady=10)
entryNumero2 = tk.Entry(janelaPrincipal,width=10,font=['Arial', 20],bg='white',fg='black',border= 5, justify='right')
entryNumero2.grid(row=1, column=1,padx=10, pady=10)

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

    


buttonSomar = tk.Button(janelaPrincipal, text='+',width= 15, font=['Arial', 15], bg='pink',border=5, command=somar)
buttonSomar.grid(row=2, column=0,padx=15, pady=15)

buttonsubtrair = tk.Button(janelaPrincipal, text='-',width= 15 , font=['Arial', 15], bg='blue',border=5, command=subtrair)
buttonsubtrair.grid(row=2, column=1,padx=15, pady=15)

buttonmultiplicar = tk.Button(janelaPrincipal, text='*',width= 15, font=['Arial', 15], bg='green',border=5, command=multiplicar)
buttonmultiplicar.grid(row=3, column=0,padx=15, pady=15)

buttondivisao = tk.Button(janelaPrincipal, text='/',width= 15, font=['Arial', 15], bg='red',border=5, command= dividir)
buttondivisao.grid(row=3, column=1,padx=15, pady=15)



comand = lambda : messagebox.showinfo("resultado", F"A soma é {soma:.2f}")


janelaPrincipal.mainloop()