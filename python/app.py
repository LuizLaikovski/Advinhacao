from tkinter import *
from tkinter import ttk
from random import randint

numeroParaAdivinhar = randint(1, 50)


janela = Tk()
janela.title("Jogo de Advinhação")
janela.geometry("400x400")

def exibirvar():
    valor = float(num.get())
    print(valor)

texto1 = Label(janela, text="Seja bem vindo ao Jogo de Adivinhação!!")
texto1.grid(column=0, row=0, padx=100, pady=10)

txt2 = Label(janela, text="Digite um númeor entre 1 e 50, Você possui apenas 5 tentativas")

num = StringVar()
numero = ttk.Entry(janela, textvariable=num)
numero.grid(column=0, row=2, padx=100, pady= 10)

botao = ttk.Button(janela, command=exibirvar, text="Enviar")
botao.grid(column=0, row=5, padx=100, pady=10)

resposta = Label(janela, text="")
resposta.grid(column=0, row=6, padx=10, pady=10)




janela.mainloop()