from tkinter import *
from tkinter import ttk
from random import randint

numeroParaAdivinhar = 3


janela = Tk()
janela.title("Jogo de Advinhação")
janela.geometry("400x400")




def ConferirNumero():
    valor = float(num.get())
    print(valor)
    for i in range(1, 6):
        if valor < numeroParaAdivinhar:
            resposta.config(text="Maior")
        elif valor > numeroParaAdivinhar:
            resposta.config(text="Menor")
        else:
            resposta.config(text="Ganhouu!!!!!!")
        txt3.config(text=f"Você possui apenas {i} tentativas")

texto1 = ttk.Label(janela, text="Seja bem vindo ao Jogo de Adivinhação!!")
texto1.grid(column=0, row=0, padx=50, pady=10)

txt2 = ttk.Label(janela, text="Digite um númeor entre 1 e 50.")
txt2.grid(column=0, row=1, padx=25, pady=10)

txt3 = ttk.Label(janela, text=f"Você possui apenas 5 tentativas.")
txt3.grid(column=0, row=2, padx=25, pady=10)

num = StringVar()
numero = ttk.Entry(janela, textvariable=num)
numero.grid(column=0, row=3, padx=100, pady= 10)

botao = ttk.Button(janela, command=ConferirNumero, text="Enviar")
botao.grid(column=0, row=6, padx=100, pady=10)

resposta = ttk.Label(janela, text="")
resposta.grid(column=0, row=7, padx=10, pady=10)




janela.mainloop()