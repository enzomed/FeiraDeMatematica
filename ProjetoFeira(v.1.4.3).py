import tkinter as tk
from tkinter import *
import tkinter.ttk
import PIL
import os
from PIL import Image, ImageTk
import urllib
import urllib.request
from tkinter.ttk import Label
import random
from random import shuffle
import json
import pynput

## Função do gameover, somente chamada quando o jogador perde todas as vidas.
## Neste caso, o jogador é obrigado a fechar o programa.

def gameover():
    gameoverwindow = tk.Tk()
    gameoverwindow.title('GAME OVER')
    gameoverwindow.geometry('400x300')
    gameoverwindow.configure(background="#111111")

    textgameover = Label(gameoverwindow,text='GAME OVER, o jogo acabou!',background="#111111",
                         foreground='white',
                         font=('Bebas Neue',15)
                         )
    exitbutton = tk.Button(gameoverwindow,text='Encerrar',background='#111111',
                           foreground='white',
                           font=('Bebas Neue',15),
                           command=exit)

    textgameover.pack()
    exitbutton.pack()
    gameoverwindow.mainloop()




## Devidos créditos a equipe de propaganda:

def creditospropaganda():
    creditos_propaganda = tk.Tk()
    creditos_propaganda.title('Créditos')
    creditos_propaganda.geometry('1366x768')
    creditos_propaganda.configure(background='#111111')
    textocreditos = Label(creditos_propaganda, text='Equipe responsável pela propaganda da feira:')
    botaoencerrar = tk.Button(creditos_propaganda, text='Sair', command=creditos_propaganda.destroy)
    textocreditos.pack()
    botaoencerrar.pack()

## Devidos créditos a equipe que criou as perguntas:

def creditosperguntas():
    creditos_perguntas = tk.Tk()
    creditos_perguntas.title('Créditos das perguntas')
    creditos_perguntas.geometry('1366x768')
    creditos_perguntas.configure(background='#111111')
    textocreditos = Label(creditos_perguntas,
                          text='Equipe responsável pela criação das perguntas: Vitórias, Patrine, Rafael, Maisa, Pedro, Arthur, Sarah ',
                          background='#111111',
                          foreground='white',
                          font=('Bebas Neue', 16)
                          )
    botaoproxcred = tk.Button(creditos_perguntas, text='Próxima equipe', command=creditospropaganda,
                              background='#111111',
                              foreground='white',
                              font=('Bebas Neue', 16)
                              )
    creditos_perguntas.after(30000, creditos_perguntas.destroy)
    textocreditos.pack()
    botaoproxcred.pack()


## Devidos créditos a equipe das imagens:

def creditosimagens():
    creditos_imagens = tk.Tk()
    creditos_imagens.title('Créditos das imagens')
    creditos_imagens.geometry('1366x768')
    creditos_imagens.configure(background='#111111')
    textocreditos = Label(creditos_imagens, text='Equipe das imagens: Juliana, Yasmin, Matheus, Nicolas, Miguel',
                          background='#111111',
                          foreground='white',
                          font=('Bebas Neue', 16)
                          )
    botaoproxcred = tk.Button(creditos_imagens, text='Próxima equipe', command=creditosperguntas,
                              background='#111111',
                              foreground='white',
                              font=('Bebas Neue', 16)
                              )
    creditos_imagens.after(30000, creditos_imagens.destroy)
    textocreditos.pack()
    botaoproxcred.pack()


## Devidos créditos a equipe de programação:

def creditosprogramadores():
    creditos_programadores = tk.Tk()
    creditos_programadores.title('Equipe responsável pela modelagem e criação do código para o programa.')
    creditos_programadores.geometry('1366x768')
    creditos_programadores.configure(background='#111111')
    textocreditos = Label(creditos_programadores,
                          text='Equipe de programação: Enzo Fernandes, Kleber Rogério, Gabryel Pereira, Leandro Kenji, Paulo Roberto,',
                          background='#111111',
                          foreground='white',
                          font=('Bebas Neue', 16)
                          )
    botaoproxcred = tk.Button(creditos_programadores, text='Próxima equipe', command=creditosimagens,
                              background='#111111',
                              foreground='white',
                              font=('Bebas Neue', 16),
                              )
    creditos_programadores.after(30000, creditos_programadores.destroy)
    textocreditos.pack()
    botaoproxcred.pack()


## Definiçao da classe Jogador:

class Jogador:
    def __init__(self,nome,pontos,vidas):
        self.nome = nome
        self.pontos = pontos
        self.vidas = vidas



## Janela principal:

janela_principal = tk.Tk()
janela_principal.title('Menu principal')
janela_principal.geometry('1366x768')
urlimagem = urllib.request.urlopen('https://i.postimg.cc/3RD94Fc1/logo.png')
img = ImageTk.PhotoImage(file=urlimagem, master=janela_principal)
imagemtitulo = Label(janela_principal, image=img)

botaocreditos = tk.Button(janela_principal,
                          text='Ver créditos',
                          background='#111111',
                          foreground='white',
                          font=('Bebas Neue', 16),
                          command=creditosprogramadores)
botaoinicio = tk.Button(janela_principal,
                        text='Clique para iniciar!',
                        background="#111111",
                        foreground="white",
                        font=("Bebas Neue", 16),
                        command=janela_principal.destroy)
botaoencerrar = tk.Button(janela_principal, text='Clique para encerrar o programa!',
                          background="#111111",
                          foreground="white",
                          font=("Bebas Neue", 16),
                          command=exit)
textointro = Label(janela_principal, text='Bem vindo ao Projeto da Feira de Matemática!',
                   background="#111111",
                   foreground="white",
                   font=("Bebas Neue", 16))
textosubintro = Label(janela_principal, text='Um projeto realizado pela turma do 3°B!',
                      background="#111111",
                      foreground="white",
                      font=("Bebas Neue", 16))
imagemtitulo.pack()
textointro.pack()
textosubintro.pack()
botaoinicio.pack()
botaocreditos.pack()
botaoencerrar.pack()
janela_principal.configure(bg='#111111')
janela_principal.mainloop()

## Função para coletar o nome do jogador e definir o objeto jogador da classe Jogador:
def nameentry():
    global nomejogador #Definição de uma varíavel global para evitar problemas de referência
    nomejogador = nomeentry.get() #Recolhe o nome que o usuário digitou na caixa de entrada
    janelanome.destroy()

janelanome = tk.Tk()
janelanome.geometry('400x300')
janelanome.title('Coloque o seu nome!')
janelanome.configure(background='#111111')

textonome = Label(janelanome,text='Insira seu nome:',background='#111111',
                  foreground='white',
                  font=('Bebas Neue',15)
                  )
nomeentry = Entry(janelanome,font=('Bebas Neue',12))
entername = tk.Button(janelanome,text='ENTER',background="#111111",
                      foreground="white",
                      font=('Bebas Neue',15),
                      command=nameentry)
textonome.pack()
nomeentry.pack()
entername.pack()
janelanome.mainloop()

#Definição do objeto jogador da classe Jogador
# Além de informações iniciais do jogador, como: nome,pontos e vidas.

jogador = Jogador(nomejogador,0,3)
infojogador = {}

## Definição das questões:
lista = [1,2,3]
shuffle(lista)
ultimoitem = lista[-1]
print(lista)


for questao in lista:
    if questao == 1:

        # Parte reservada aos comentários


        def perguntaacerto1():

            jogador.pontos = jogador.pontos + 100

            if questao == ultimoitem:
                janelaultima.destroy()
            elif questao == 1:
                janela1.destroy()


        def correcao():

            janelaerro1.destroy()
            janelacorrecao = tk.Tk()
            janelacorrecao.title('Correção')
            janelacorrecao.geometry('430x600')
            janelacorrecao.configure(background='#111111')
            urlimagemcorrecao = urllib.request.urlopen(
                'https://i.postimg.cc/MKC1wdJm/corre-reflex-o-redimensionada.png')
            imgcorrecao = ImageTk.PhotoImage(file=urlimagemcorrecao, master=janelacorrecao)
            imagemcorrecao = Label(janelacorrecao, image=imgcorrecao)
            imagemcorrecao.pack()
            janelacorrecao.mainloop()


        def perguntaerrada1():

            jogador.vidas = jogador.vidas - 1

            if jogador.vidas == 0:
                gameover()
            else:
                pass

            if jogador.pontos == 0:
                pass
            else:
                jogador.pontos = jogador.pontos - 100

            if questao == ultimoitem:
                janelaultima.destroy()
            elif questao == 1:
                janela1.destroy()

            global janelaerro1
            janelaerro1 = tk.Tk()
            janelaerro1.title('Você errou!')
            janelaerro1.geometry('200x200')
            janelaerro1.configure(background='#111111')
            textoerro = Label(janelaerro1, text='Sinto muito, você errou!',
                              background='#111111',
                              foreground='white',
                              font=('Bebas Neue', 12))
            button = tk.Button(janelaerro1, text='Saiba o porquê.', command=correcao,
                               background='#111111',
                               foreground='white',
                               font=('Bebas Neue', 12))
            textoerro.pack()
            button.pack()
            janelaerro1.mainloop()


        if questao == ultimoitem:
            janelaultima = tk.Tk()
            janelaultima.geometry('1366x768')
            janelaultima.title('Última questao')
            janelaultima.configure(background='#111111')
            textoquestaoultima = Label(janelaultima, text='A figura que corresponde a uma reflexão axial:',
                                       background='#111111',
                                       foreground='white',
                                       font=('Bebas Neue', 20)
                                       )
            urlimagem = urllib.request.urlopen('https://i.postimg.cc/wjXDFLRx/imagem-questao1.png')
            img = ImageTk.PhotoImage(file=urlimagem, master=janelaultima)
            imagem = Button(janelaultima, image=img)
            imagem.configure(background='purple', border='7')
            imagem.pack()
            textoquestaoultima.pack()

            button_1_1 = tk.Button(janelaultima, text='A) É a figura 3.', command=perguntaerrada1,
                                   background='purple',
                                   foreground='white',
                                   font=('Bebas Neue', 16),
                                   border='7'
                                   )
            button_1 = tk.Button(janelaultima, text='A) É a figura 3.', command=perguntaerrada1,
                                 background='#111111',
                                 foreground='white',
                                 font=('Bebas Neue', 16)
                                 )
            button_2_1 = tk.Button(janelaultima, text='B) É a figura 1.', command=perguntaerrada1,
                                   background='purple',
                                   foreground='white',
                                   font=('Bebas Neue', 16),
                                   border='7'
                                   )
            button_2 = tk.Button(janelaultima, text='B) É a figura 1.', command=perguntaerrada1,
                                 background='#111111',
                                 foreground='white',
                                 font=('Bebas Neue', 16)
                                 )
            button_3_1 = tk.Button(janelaultima, text='C) É a figura 4.', command=perguntaerrada1,
                                   background='purple',
                                   foreground='white',
                                   font=('Bebas Neue', 16),
                                   border='7'
                                   )
            button_3 = tk.Button(janelaultima, text='C) É a figura 4.', command=perguntaerrada1,
                                 background='#111111',
                                 foreground='white',
                                 font=('Bebas Neue', 16)
                                 )
            button_4_1 = tk.Button(janelaultima, text='D) É a figura 2.', command=perguntaacerto1,
                                   background='purple',
                                   foreground='white',
                                   font=('Bebas Neue', 16),
                                   border='7'
                                   )
            button_4 = tk.Button(janelaultima, text='D) É a figura 2.', command=perguntaacerto1,
                                 background='#111111',
                                 foreground='white',
                                 font=('Bebas Neue', 16)
                                 )
            button_1_1.pack()
            button_1_1.place(x=50, y=600)
            button_1.pack()
            button_1.place(x=54, y=604)
            button_2_1.pack()
            button_2_1.place(x=220, y=600)
            button_2.pack()
            button_2.place(x=224, y=604)
            button_3_1.pack()
            button_3_1.place(x=1020, y=600)
            button_3.pack()
            button_3.place(x=1024, y=604)
            button_4_1.pack()
            button_4_1.place(x=1190, y=600)
            button_4.pack()
            button_4.place(x=1194, y=604)
            janelaultima.mainloop()

        else:
            janela1 = tk.Tk()
            janela1.title('Pergunta 1')
            janela1.geometry('1366x768')
            janela1.configure(background='#111111')
            urlimagem_1 = urllib.request.urlopen('https://i.postimg.cc/wjXDFLRx/imagem-questao1.png')
            img_1 = ImageTk.PhotoImage(file=urlimagem_1, master=janela1)
            imagem_1 = Button(janela1, image=img_1)
            imagem_1.configure(background='purple', border='7')
            textoquestao = Label(janela1, text='A figura que corresponde a uma reflexão axial:',
                                 background='#111111',
                                 foreground='white',
                                 font=('Bebas Neue', 20)
                                 )
            imagem_1.pack()
            textoquestao.pack()

            button_1_1 = tk.Button(janela1, text='A) É a figura 3.', command=perguntaerrada1,
                                   background='purple',
                                   foreground='white',
                                   font=('Bebas Neue', 16),
                                   border='7'
                                   )
            button_1 = tk.Button(janela1, text='A) É a figura 3.', command=perguntaerrada1,
                                 background='#111111',
                                 foreground='white',
                                 font=('Bebas Neue', 16)
                                 )
            button_2_1 = tk.Button(janela1, text='B) É a figura 1.', command=perguntaerrada1,
                                   background='purple',
                                   foreground='white',
                                   font=('Bebas Neue', 16),
                                   border='7'
                                   )
            button_2 = tk.Button(janela1, text='B) É a figura 1.', command=perguntaerrada1,
                                 background='#111111',
                                 foreground='white',
                                 font=('Bebas Neue', 16)
                                 )
            button_3_1 = tk.Button(janela1, text='C) É a figura 4.', command=perguntaerrada1,
                                   background='purple',
                                   foreground='white',
                                   font=('Bebas Neue', 16),
                                   border='7'
                                   )
            button_3 = tk.Button(janela1, text='C) É a figura 4.', command=perguntaerrada1,
                                 background='#111111',
                                 foreground='white',
                                 font=('Bebas Neue', 16)
                                 )
            button_4_1 = tk.Button(janela1, text='D) É a figura 2.', command=perguntaacerto1,
                                   background='purple',
                                   foreground='white',
                                   font=('Bebas Neue', 16),
                                   border='7'
                                   )
            button_4 = tk.Button(janela1, text='D) É a figura 2.', command=perguntaacerto1,
                                 background='#111111',
                                 foreground='white',
                                 font=('Bebas Neue', 16)
                                 )
            button_1_1.pack()
            button_1_1.place(x=50, y=600)
            button_1.pack()
            button_1.place(x=54, y=604)
            button_2_1.pack()
            button_2_1.place(x=220, y=600)
            button_2.pack()
            button_2.place(x=224, y=604)
            button_3_1.pack()
            button_3_1.place(x=1020, y=600)
            button_3.pack()
            button_3.place(x=1024, y=604)
            button_4_1.pack()
            button_4_1.place(x=1190, y=600)
            button_4.pack()
            button_4.place(x=1194, y=604)
            janela1.mainloop()

    if questao == 2:

        def perguntaacerto2():

            jogador.pontos = jogador.pontos + 100

            if questao == ultimoitem:
                janelaultima.destroy()
            elif questao == 2:
                janela2.destroy()

        def correcao():

            janelaerro2.destroy()
            janelacorrecao = tk.Tk()
            janelacorrecao2 = tk.Tk()
            janelacorrecao.title('Correção 1')
            janelacorrecao2.title('Correção 2')
            janelacorrecao.geometry('430x600')
            janelacorrecao2.geometry('430x600')
            janelacorrecao.configure(background='#111111')
            janelacorrecao2.configure(background='#111111')
            urlimagemcorrecao1 = urllib.request.urlopen('https://i.postimg.cc/52Gt796y/corre-rota-o-redimensionada.png')
            urlimagemcorrecao2 = urllib.request.urlopen(
                'https://i.postimg.cc/MKC1wdJm/corre-reflex-o-redimensionada.png')
            imgcorrecao1 = ImageTk.PhotoImage(file=urlimagemcorrecao1, master=janelacorrecao)
            imgcorrecao2 = ImageTk.PhotoImage(file=urlimagemcorrecao2, master=janelacorrecao2)
            imagemcorrecao1 = Label(janelacorrecao, image=imgcorrecao1)
            imagemcorrecao2 = Label(janelacorrecao2, image=imgcorrecao2)
            imagemcorrecao1.pack()
            imagemcorrecao2.pack()
            janelacorrecao.mainloop()
            janelacorrecao2.mainloop()


        def perguntaerrada2():

            jogador.vidas = jogador.vidas - 1

            if jogador.vidas == 0:
                gameover()
            else:
                pass


            if jogador.pontos == 0:
                pass
            else:
                jogador.pontos = jogador.pontos - 100

            if questao == ultimoitem:
                janelaultima.destroy()
            elif questao == 2:
                janela2.destroy()

            global janelaerro2
            janelaerro2 = tk.Tk()
            janelaerro2.title('Você errou!')
            janelaerro2.geometry('200x200')
            janelaerro2.configure(background='#111111')
            textoerro = Label(janelaerro2, text='Sinto muito, você errou!',
                              background='#111111',
                              foreground='white',
                              font=('Bebas Neue', 12)
                              )
            button = tk.Button(janelaerro2, text='Saiba o porquê.', command=correcao,
                               background='#111111',
                               foreground='white',
                               font=('Bebas Neue', 12)
                               )
            textoerro.pack()
            button.pack()
            janelaerro2.mainloop()


        if questao == ultimoitem:
            janelaultima = tk.Tk()
            janelaultima.title('Última questão')
            janelaultima.geometry('1366x768')
            janelaultima.configure(background='#111111')

            frame_quest = tk.Frame(master=janelaultima, highlightbackground='red', highlightthickness=8, height=458
                                   , width=610)
            frame_quest.pack(padx=10, pady=10)
            frame_quest.place(x=378, y=0)
            frame1 = tk.Frame(master=janelaultima, highlightbackground="red", highlightthickness=8, height=162
                              , width=262)
            frame1.pack(padx=10, pady=10)
            frame1.place(x=7, y=496)

            frame2 = tk.Frame(master=janelaultima, highlightbackground="red", highlightthickness=8, height=162
                              , width=262)
            frame2.pack(padx=10, pady=10)
            frame2.place(x=297, y=496)

            frame3 = tk.Frame(master=janelaultima, highlightbackground="red", highlightthickness=8, height=162
                              , width=262)
            frame3.pack(padx=10, pady=10)
            frame3.place(x=797, y=496)

            frame4 = tk.Frame(master=janelaultima, highlightbackground="red", highlightthickness=8, height=162
                              , width=262)
            frame4.pack(padx=10, pady=10)
            frame4.place(x=1097, y=496)

            urlimagem_1 = urllib.request.urlopen('https://i.postimg.cc/wvGwyqDY/quest-exer2.png')
            urlalternativa1 = urllib.request.urlopen('https://i.postimg.cc/zDwqCGJ8/ex2-1-red.png')
            urlalternativa2 = urllib.request.urlopen('https://i.postimg.cc/dVGxZLRK/ex2-2-red.png')
            urlalternativa3 = urllib.request.urlopen('https://i.postimg.cc/Vk9KL21f/ex2-3-red.png')
            urlalternativa4 = urllib.request.urlopen('https://i.postimg.cc/W3ynHvmn/ex2-4-red.png')
            img_1 = ImageTk.PhotoImage(file=urlimagem_1, master=janelaultima)
            imgal1 = ImageTk.PhotoImage(file=urlalternativa1, master=janelaultima)
            imgal2 = ImageTk.PhotoImage(file=urlalternativa2, master=janelaultima)
            imgal3 = ImageTk.PhotoImage(file=urlalternativa3, master=janelaultima)
            imgal4 = ImageTk.PhotoImage(file=urlalternativa4, master=janelaultima)
            imagem_1 = Label(janelaultima, image=img_1)
            imagem_1.pack()
            button_1 = tk.Button(janelaultima, image=imgal1, command=perguntaerrada2)
            button_2 = tk.Button(janelaultima, image=imgal2, command=perguntaerrada2)
            button_3 = tk.Button(janelaultima, image=imgal3, command=perguntaerrada2)
            button_4 = tk.Button(janelaultima, image=imgal4, command=perguntaacerto2)
            button_1.pack()
            button_1.place(x=10, y=500)
            button_2.pack()
            button_2.place(x=300, y=500)
            button_3.pack()
            button_3.place(x=800, y=500)
            button_4.pack()
            button_4.place(x=1100, y=500)
            janelaultima.mainloop()

        else:
            janela2 = tk.Tk()
            janela2.title('Pergunta 2')
            janela2.geometry('1366x768')
            janela2.configure(background='#111111')

            frame_quest = tk.Frame(master=janela2, highlightbackground='red', highlightthickness=8, height=458
                                   , width=610)
            frame_quest.pack(padx=10, pady=10)
            frame_quest.place(x=378, y=0)
            frame1 = tk.Frame(master=janela2, highlightbackground="red", highlightthickness=8, height=162
                              , width=262)
            frame1.pack(padx=10, pady=10)
            frame1.place(x=7, y=496)

            frame2 = tk.Frame(master=janela2, highlightbackground="red", highlightthickness=8, height=162
                              , width=262)
            frame2.pack(padx=10, pady=10)
            frame2.place(x=297, y=496)

            frame3 = tk.Frame(master=janela2, highlightbackground="red", highlightthickness=8, height=162
                              , width=262)
            frame3.pack(padx=10, pady=10)
            frame3.place(x=797, y=496)

            frame4 = tk.Frame(master=janela2, highlightbackground="red", highlightthickness=8, height=162
                              , width=262)
            frame4.pack(padx=10, pady=10)
            frame4.place(x=1097, y=496)

            urlimagem_1 = urllib.request.urlopen('https://i.postimg.cc/wvGwyqDY/quest-exer2.png')
            urlalternativa1 = urllib.request.urlopen('https://i.postimg.cc/zDwqCGJ8/ex2-1-red.png')
            urlalternativa2 = urllib.request.urlopen('https://i.postimg.cc/dVGxZLRK/ex2-2-red.png')
            urlalternativa3 = urllib.request.urlopen('https://i.postimg.cc/Vk9KL21f/ex2-3-red.png')
            urlalternativa4 = urllib.request.urlopen('https://i.postimg.cc/W3ynHvmn/ex2-4-red.png')
            img_1 = ImageTk.PhotoImage(file=urlimagem_1, master=janela2)
            imgal1 = ImageTk.PhotoImage(file=urlalternativa1, master=janela2)
            imgal2 = ImageTk.PhotoImage(file=urlalternativa2, master=janela2)
            imgal3 = ImageTk.PhotoImage(file=urlalternativa3, master=janela2)
            imgal4 = ImageTk.PhotoImage(file=urlalternativa4, master=janela2)
            imagem_1 = Label(janela2, image=img_1)
            imagem_1.pack()
            button_1 = tk.Button(janela2, image=imgal1, command=perguntaerrada2)
            button_2 = tk.Button(janela2, image=imgal2, command=perguntaerrada2)
            button_3 = tk.Button(janela2, image=imgal3, command=perguntaerrada2)
            button_4 = tk.Button(janela2, image=imgal4, command=perguntaacerto2)
            button_1.pack()
            button_1.place(x=10, y=500)
            button_2.pack()
            button_2.place(x=300, y=500)
            button_3.pack()
            button_3.place(x=800, y=500)
            button_4.pack()
            button_4.place(x=1100, y=500)
            janela2.mainloop()

    if questao == 3:

        def perguntaacerto3():

            jogador.pontos = jogador.pontos + 100

            if questao == ultimoitem:
                janelaultima.destroy()
            elif questao == 3:
                janela3.destroy()


        def correcao():

            janelaerro3.destroy()
            janelacorrecao = tk.Tk()
            janelacorrecao.title('Correção')
            janelacorrecao.geometry('600x600')
            janelacorrecao.configure(background='#111111')
            textocorrecao = Label(janelacorrecao, text='Insira o texto aqui!',
                                  background='#111111',
                                  foreground='white',
                                  font=('Bebas Neue', 12))
            textocorrecao.pack()
            janelacorrecao.mainloop()


        def perguntaerrada3():

            jogador.vidas = jogador.vidas - 1

            if jogador.vidas == 0:
                gameover()
            else:
                pass

            if jogador.pontos == 0:
                pass
            else:
                jogador.pontos = jogador.pontos - 100

            if questao == ultimoitem:
                janelaultima.destroy()
            elif questao == 3:
                janela3.destroy()

            global janelaerro3
            janelaerro3 = tk.Tk()
            janelaerro3.title('Você errou!')
            janelaerro3.geometry('200x200')
            janelaerro3.configure(background='#111111')
            textoerro = Label(janelaerro3, text='Sinto muito, você errou!',
                              background='#111111',
                              foreground='white',
                              font=('Bebas Neue', 12)
                              )
            button = tk.Button(janelaerro3, text='Saiba o porquê.', command=correcao,
                               background='#111111',
                               foreground='white',
                               font=('Bebas Neue', 12)
                               )
            textoerro.pack()
            button.pack()
            janelaerro3.mainloop()


        if questao == ultimoitem:
            janelaultima = tk.Tk()
            janelaultima.title('Última questão')
            janelaultima.geometry('1366x768')
            janelaultima.configure(background='#111111')

            frame_3 = tk.Frame(master=janelaultima, highlightbackground='orange', highlightthickness=8, height=383,
                               width=510)
            frame_3.pack()
            frame_3.place(x=428, y=0)
            frame_3_1 = tk.Frame(master=janelaultima, highlightbackground="orange", highlightthickness=8, height=160,
                                 width=260)
            frame_3_1.pack(padx=10, pady=10)
            frame_3_1.place(x=48, y=448)
            frame_3_2 = tk.Frame(master=janelaultima, highlightbackground="orange", highlightthickness=8, height=160,
                                 width=260)
            frame_3_2.pack(padx=10, pady=10)
            frame_3_2.place(x=348, y=448)
            frame_3_3 = tk.Frame(master=janelaultima, highlightbackground="orange", highlightthickness=8, height=160,
                                 width=260)
            frame_3_3.pack(padx=10, pady=10)
            frame_3_3.place(x=764, y=448)
            frame_3_4 = tk.Frame(master=janelaultima, highlightbackground="orange", highlightthickness=8, height=160,
                                 width=260)
            frame_3_4.pack(padx=10, pady=10)
            frame_3_4.place(x=1064, y=448)

            urlimagem_1 = urllib.request.urlopen('https://i.postimg.cc/cCGbmzq6/quest-exer4.png')
            urlalternativa1 = urllib.request.urlopen('https://i.postimg.cc/0jyYGGth/ex4-1-red.png')
            urlalternativa2 = urllib.request.urlopen('https://i.postimg.cc/kGcDMkqb/ex4-2-red.png')
            urlalternativa3 = urllib.request.urlopen('https://i.postimg.cc/TwsC7HZn/ex4-3-red.png')
            urlalternativa4 = urllib.request.urlopen('https://i.postimg.cc/hP2bpYTv/ex4-4-red.png')
            img_1 = ImageTk.PhotoImage(file=urlimagem_1, master=janelaultima)
            imgal1 = ImageTk.PhotoImage(file=urlalternativa1, master=janelaultima)
            imgal2 = ImageTk.PhotoImage(file=urlalternativa2, master=janelaultima)
            imgal3 = ImageTk.PhotoImage(file=urlalternativa3, master=janelaultima)
            imgal4 = ImageTk.PhotoImage(file=urlalternativa4, master=janelaultima)
            imagem_1 = Label(janelaultima, image=img_1)
            imagem_1.pack()
            button_1 = tk.Button(janelaultima, image=imgal1, command=perguntaacerto3)
            button_2 = tk.Button(janelaultima, image=imgal2, command=perguntaerrada3)
            button_3 = tk.Button(janelaultima, image=imgal3, command=perguntaerrada3)
            button_4 = tk.Button(janelaultima, image=imgal4, command=perguntaerrada3)
            button_1.pack()
            button_1.place(x=50, y=450)
            button_2.pack()
            button_2.place(x=350, y=450)
            button_3.pack()
            button_3.place(x=766, y=450)
            button_4.pack()
            button_4.place(x=1066, y=450)
            janelaultima.mainloop()

        else:
            janela3 = tk.Tk()
            janela3.title('Pergunta 3')
            janela3.geometry('1366x768')
            janela3.configure(background='#111111')

            frame_3 = tk.Frame(master=janela3, highlightbackground='orange', highlightthickness=8, height=383,
                               width=510)
            frame_3.pack()
            frame_3.place(x=428, y=0)
            frame_3_1 = tk.Frame(master=janela3, highlightbackground="orange", highlightthickness=8, height=160,
                                 width=260)
            frame_3_1.pack(padx=10, pady=10)
            frame_3_1.place(x=48, y=448)
            frame_3_2 = tk.Frame(master=janela3, highlightbackground="orange", highlightthickness=8, height=160,
                                 width=260)
            frame_3_2.pack(padx=10, pady=10)
            frame_3_2.place(x=348, y=448)
            frame_3_3 = tk.Frame(master=janela3, highlightbackground="orange", highlightthickness=8, height=160,
                                 width=260)
            frame_3_3.pack(padx=10, pady=10)
            frame_3_3.place(x=764, y=448)
            frame_3_4 = tk.Frame(master=janela3, highlightbackground="orange", highlightthickness=8, height=160,
                                 width=260)
            frame_3_4.pack(padx=10, pady=10)
            frame_3_4.place(x=1064, y=448)

            urlimagem_1 = urllib.request.urlopen('https://i.postimg.cc/cCGbmzq6/quest-exer4.png')
            urlalternativa1 = urllib.request.urlopen('https://i.postimg.cc/0jyYGGth/ex4-1-red.png')
            urlalternativa2 = urllib.request.urlopen('https://i.postimg.cc/kGcDMkqb/ex4-2-red.png')
            urlalternativa3 = urllib.request.urlopen('https://i.postimg.cc/TwsC7HZn/ex4-3-red.png')
            urlalternativa4 = urllib.request.urlopen('https://i.postimg.cc/hP2bpYTv/ex4-4-red.png')
            img_1 = ImageTk.PhotoImage(file=urlimagem_1, master=janela3)
            imgal1 = ImageTk.PhotoImage(file=urlalternativa1, master=janela3)
            imgal2 = ImageTk.PhotoImage(file=urlalternativa2, master=janela3)
            imgal3 = ImageTk.PhotoImage(file=urlalternativa3, master=janela3)
            imgal4 = ImageTk.PhotoImage(file=urlalternativa4, master=janela3)
            imagem_1 = Label(janela3, image=img_1)
            imagem_1.pack()
            button_1 = tk.Button(janela3, image=imgal1, command=perguntaacerto3)
            button_2 = tk.Button(janela3, image=imgal2, command=perguntaerrada3)
            button_3 = tk.Button(janela3, image=imgal3, command=perguntaerrada3)
            button_4 = tk.Button(janela3, image=imgal4, command=perguntaerrada3)
            button_1.pack()
            button_1.place(x=50, y=450)
            button_2.pack()
            button_2.place(x=350, y=450)
            button_3.pack()
            button_3.place(x=766, y=450)
            button_4.pack()
            button_4.place(x=1066, y=450)
            janela3.mainloop()

    if questao == 4:

        def perguntaacerto4():

            jogador.pontos = jogador.pontos + 100
            if questao == ultimoitem:
                janelaultima.destroy()
            elif questao == 4:
                janela4.destroy()


        def correcao():

            janelaerro4.destroy()
            if questao == ultimoitem:
                janelaultima.destroy()
            elif questao == 4:
                janela4.destroy()

            janelacorrecao = tk.Tk()
            janelacorrecao.title('Correção')
            janelacorrecao.geometry('430x600')
            janelacorrecao.configure(background='#111111')
            urlimagemcorrecao = urllib.request.urlopen(
                'https://i.postimg.cc/MKC1wdJm/corre-reflex-o-redimensionada.png')
            imgcorrecao = ImageTk.PhotoImage(file=urlimagemcorrecao, master=janelacorrecao)
            imagemcorrecao = Label(janelacorrecao, image=imgcorrecao)
            imagemcorrecao.pack()
            janelacorrecao.mainloop()


        def perguntaerrada4():

            jogador.vidas = jogador.vidas - 1

            if jogador.vidas == 0:
                gameover()
            else:
                pass

            if jogador.pontos == 0:
                pass
            else:
                jogador.pontos = jogador.pontos - 100

            if questao == ultimoitem:
                janelaultima.destroy()
            elif questao == 4:
                janela4.destroy()

            global janelaerro4
            janelaerro4 = tk.Tk()
            janelaerro4.title('Você errou!')
            janelaerro4.geometry('200x200')
            janelaerro4.configure(background='#111111')
            textoerro = Label(janelaerro4, text='Sinto muito, você errou!',
                              background='#111111',
                              foreground='white',
                              font=('Bebas Neue', 12)
                              )
            button = tk.Button(janelaerro4, text='Saiba o porquê.', command=correcao,
                               background='#111111',
                               foreground='white',
                               font=('Bebas Neue', 12)
                               )
            textoerro.pack()
            button.pack()
            janelaerro4.mainloop()


        def answer():
            getresposta1 = resposta1.get()
            if getresposta1 == 'Reflexão' or getresposta1 == 'reflexão':
                perguntaacerto4()
            else:
                perguntaerrada4()


        if questao == ultimoitem:
            janelaultima = tk.Tk()
            janelaultima.title('Última questão')
            janelaultima.geometry('1366x768')
            janelaultima.configure(background='#111111')
            urlalternativa_4 = urllib.request.urlopen('https://i.postimg.cc/fbt1gMnf/ex3-un.png')
            imgal1 = ImageTk.PhotoImage(file=urlalternativa_4, master=janelaultima)
            imagemalternativa4 = Button(janelaultima, image=imgal1)
            imagemalternativa4.configure(background='blue', border=3)
            textoquestao4 = Label(janelaultima,
                                  text='Descreva qual transformação geométrica foi realizada para essa figura.',
                                  background='#111111',
                                  foreground='white',
                                  font=('Bebas Neue', 20)
                                  )
            resposta1 = tk.Entry(janelaultima, bd=3)
            buttonenter_1 = tk.Button(janelaultima, text='Verificar',
                                      background='#111111',
                                      foreground='white',
                                      font=('Bebas Neue', 16),
                                      command=answer, bg='blue', bd=5
                                      )
            buttonenter = tk.Button(janelaultima, text='Verificar',
                                    background='#111111',
                                    foreground='white',
                                    font=('Bebas Neue', 16),
                                    command=answer
                                    )
            textoquestao4.pack()
            imagemalternativa4.pack()
            resposta1.pack()
            resposta1.place(x=618, y=500)
            buttonenter_1.pack()
            buttonenter_1.place(x=632, y=533)
            buttonenter.pack()
            buttonenter.place(x=634, y=535)
            janelaultima.mainloop()

        else:
            janela4 = tk.Tk()
            janela4.title('Pergunta 4')
            janela4.geometry('1366x768')
            janela4.configure(background='#111111')
            urlalternativa_4 = urllib.request.urlopen('https://i.postimg.cc/fbt1gMnf/ex3-un.png')
            imgal1 = ImageTk.PhotoImage(file=urlalternativa_4, master=janela4)
            imagemalternativa4 = Button(janela4, image=imgal1)
            imagemalternativa4.configure(background='blue', border=3)
            textoquestao4 = Label(janela4,
                                  text='Descreva qual transformação geométrica foi realizada para essa figura.',
                                  background='#111111',
                                  foreground='white',
                                  font=('Bebas Neue', 20)
                                  )
            resposta1 = tk.Entry(janela4, bd=3)
            buttonenter_1 = tk.Button(janela4, text='Verificar',
                                      background='#111111',
                                      foreground='white',
                                      font=('Bebas Neue', 16),
                                      command=answer, bg='blue', bd=5
                                      )
            buttonenter = tk.Button(janela4, text='Verificar',
                                    background='#111111',
                                    foreground='white',
                                    font=('Bebas Neue', 16),
                                    command=answer
                                    )
            textoquestao4.pack()
            imagemalternativa4.pack()
            resposta1.pack()
            resposta1.place(x=618, y=500)
            buttonenter_1.pack()
            buttonenter_1.place(x=632, y=533)
            buttonenter.pack()
            buttonenter.place(x=634, y=535)
            janela4.mainloop()

    if questao == 5:

        def perguntaacerto5():

            jogador.pontos = jogador.pontos + 100

            if questao == ultimoitem:
                janelaultima.destroy()
            elif questao == 5:
                janela5.destroy()


        def correcao():

            janelaerro5.destroy()
            if questao == ultimoitem:
                janelaultima.destroy()
            elif questao == 5:
                janela5.destroy()

            janelacorrecao = tk.Tk()
            janelacorrecao.title('Correção')
            janelacorrecao.geometry('430x600')
            janelacorrecao.configure(background='#111111')
            urlimagemcorrecao = urllib.request.urlopen(
                'https://i.postimg.cc/fR6w7Hr0/corre-transla-o-redimensionada.png')
            imgcorrecao = ImageTk.PhotoImage(file=urlimagemcorrecao, master=janelacorrecao)
            imagemcorrecao = Label(janelacorrecao, image=imgcorrecao)
            imagemcorrecao.pack()
            janelacorrecao.mainloop()


        def perguntaerrada5():

            jogador.vidas = jogador.vidas - 1

            if jogador.vidas == 0:
                gameover()
            else:
                pass

            if jogador.pontos == 0:
                pass
            else:
                jogador.pontos = jogador.pontos - 100

            if questao == ultimoitem:
                janelaultima.destroy()
            elif questao == 5:
                janela5.destroy()


            global janelaerro5
            janelaerro5 = tk.Tk()
            janelaerro5.title('Você errou!')
            janelaerro5.geometry('200x200')
            janelaerro5.configure(background='#111111')
            textoerro = Label(janelaerro5, text='Sinto muito, você errou!',
                              background='#111111',
                              foreground='white',
                              font=('Bebas Neue', 12)
                              )
            button = tk.Button(janelaerro5, text='Saiba o porquê.', command=correcao,
                               background='#111111',
                               foreground='white',
                               font=('Bebas Neue', 12)
                               )
            textoerro.pack()
            button.pack()
            janelaerro5.mainloop()


        def answer():
            getresposta = resposta1.get()
            if getresposta == 'Translação' or getresposta == 'translação':
                perguntaacerto5()
            else:
                perguntaerrada5()


        if questao == ultimoitem:
            janelaultima = tk.Tk()
            janelaultima.title('Última questão')
            janelaultima.geometry('1366x768')
            janelaultima.configure(background='#111111')
            urlalternativa_5 = urllib.request.urlopen('https://i.postimg.cc/NMSmYyDL/ex3-un-2.png')
            imgal1 = ImageTk.PhotoImage(file=urlalternativa_5, master=janelaultima)
            imagemalternativa5 = Button(janelaultima, image=imgal1)
            imagemalternativa5.configure(background='purple', border=3)
            textoquestao = Label(janelaultima,
                                 text='Descreva qual transformação geométrica foi realizada nessa figura:',
                                 background='#111111',
                                 foreground='white',
                                 font=('Bebas Neue', 20)
                                 )
            resposta1 = tk.Entry(janelaultima, bd=3)
            buttonenter_5 = tk.Button(janelaultima, text='Verificar',
                                      background='#111111',
                                      foreground='white',
                                      font=('Bebas Neue', 16),
                                      command=answer, bg='purple', bd=5
                                      )
            buttonenter = tk.Button(janelaultima, text='Verificar',
                                    background='#111111',
                                    foreground='white',
                                    font=('Bebas Neue', 16),
                                    command=answer
                                    )
            textoquestao.pack()
            imagemalternativa5.pack()
            resposta1.pack()
            resposta1.place(x=618, y=500)
            buttonenter_5.pack()
            buttonenter_5.place(x=632, y=533)
            buttonenter.pack()
            buttonenter.place(x=634, y=535)
            janelaultima.mainloop()

        else:
            janela5 = tk.Tk()
            janela5.title('Pergunta 5')
            janela5.geometry('1366x768')
            janela5.configure(background='#111111')
            urlalternativa_5 = urllib.request.urlopen('https://i.postimg.cc/NMSmYyDL/ex3-un-2.png')
            imgal1 = ImageTk.PhotoImage(file=urlalternativa_5, master=janela5)
            imagemalternativa5 = Button(janela5, image=imgal1)
            imagemalternativa5.configure(background='purple', border=3)

            textoquestao = Label(janela5, text='Descreva qual transformação geométrica foi realizada nessa figura:',
                                 background='#111111',
                                 foreground='white',
                                 font=('Bebas Neue', 20)
                                 )
            resposta1 = tk.Entry(janela5, bd=3)
            buttonenter_5 = tk.Button(janela5, text='Verificar',
                                      background='#111111',
                                      foreground='white',
                                      font=('Bebas Neue', 16),
                                      command=answer, bg='purple', bd=5
                                      )
            buttonenter = tk.Button(janela5, text='Verificar',
                                    background='#111111',
                                    foreground='white',
                                    font=('Bebas Neue', 16),
                                    command=answer
                                    )
            textoquestao.pack()
            imagemalternativa5.pack()
            resposta1.pack()
            resposta1.place(x=618, y=500)
            buttonenter_5.pack()
            buttonenter_5.place(x=632, y=533)
            buttonenter.pack()
            buttonenter.place(x=634, y=535)
            janela5.mainloop()

    if questao == 6:

        def perguntaacerto6():

            jogador.pontos = jogador.pontos + 100

            if questao == ultimoitem:
                janelaultima.destroy()
            elif questao == 6:
                janela6.destroy()

        def correcao():

            janelaerro6.destroy()
            if questao == ultimoitem:
                janelaultima.destroy()
            elif questao == 6:
                janela6.destroy()

            janelacorrecao = tk.Tk()
            janelacorrecao.title('Correção')
            janelacorrecao.geometry('430x600')
            janelacorrecao.configure(background='#111111')
            urlimagemcorrecao = urllib.request.urlopen(
                'https://i.postimg.cc/52Gt796y/corre-rota-o-redimensionada.png')
            imgcorrecao = ImageTk.PhotoImage(file=urlimagemcorrecao, master=janelacorrecao)
            imagemcorrecao = Label(janelacorrecao, image=imgcorrecao)
            imagemcorrecao.pack()
            janelacorrecao.mainloop()


        def perguntaerrada6():

            jogador.vidas = jogador.vidas - 1

            if jogador.vidas == 0:
                gameover()
            else:
                pass

            if jogador.pontos == 0:
                pass
            else:
                jogador.pontos = jogador.pontos - 100

            if questao == ultimoitem:
                janelaultima.destroy()
            elif questao == 6:
                janela6.destroy()

            global janelaerro6
            janelaerro6 = tk.Tk()
            janelaerro6.title('Você errou!')
            janelaerro6.geometry('200x200')
            janelaerro6.configure(background='#111111')
            textoerro = Label(janelaerro6, text='Sinto muito, você errou!',
                              background='#111111',
                              foreground='white',
                              font=('Bebas Neue', 12)
                              )
            button = tk.Button(janelaerro6, text='Saiba o porquê.', command=correcao,
                               background='#111111',
                               foreground='white',
                               font=('Bebas Neue', 12)
                               )
            textoerro.pack()
            button.pack()
            janelaerro6.mainloop()


        def answer():
            getresposta = resposta.get()
            if getresposta == 'Rotação' or getresposta == 'rotação':
                perguntaacerto6()
            else:
                perguntaerrada6()


        if questao == ultimoitem:
            janelaultima = tk.Tk()
            janelaultima.title('Última questão')
            janelaultima.geometry('1366x768')
            janelaultima.configure(background='#111111')
            textoquestao = Label(janelaultima,
                                 text='Descreva qual transformação geométrica foi realizada nessa figura.',
                                 background='#111111',
                                 foreground='white',
                                 font=('Bebas Neue', 20)
                                 )
            urlimagemenunciado = urllib.request.urlopen('https://i.postimg.cc/R04qbdgV/ex3-un-3.png')
            imgenunciado = ImageTk.PhotoImage(file=urlimagemenunciado, master=janelaultima)
            imagemenunciado = Button(janelaultima, image=imgenunciado)
            imagemenunciado.configure(background="red", border=5)
            resposta = tk.Entry(janelaultima, bd=3)
            buttonenter_1 = tk.Button(janelaultima, text='Verificar',
                                      background='red',
                                      foreground='white',
                                      font=('Bebas Neue', 16),
                                      command=answer, bd=5)
            buttonenter = tk.Button(janelaultima, text='Verificar',
                                    background='#111111',
                                    foreground='white',
                                    font=('Bebas Neue', 16),
                                    command=answer)
            textoquestao.pack()
            imagemenunciado.pack()
            resposta.pack()
            resposta.place(x=618, y=500)
            buttonenter.pack()
            buttonenter.place(x=634, y=535)
            buttonenter_1.pack()
            buttonenter_1.place(x=632, y=533)
            janelaultima.mainloop()
        else:
            janela6 = tk.Tk()
            janela6.title('Pergunta 6')
            janela6.geometry('1366x768')
            janela6.configure(background='#111111')
            textoquestao = Label(janela6, text='Descreva qual transformação geométrica foi realizada nessa figura.',
                                 background='#111111',
                                 foreground='white',
                                 font=('Bebas Neue', 20)
                                 )
            urlimagemenunciado = urllib.request.urlopen('https://i.postimg.cc/R04qbdgV/ex3-un-3.png')
            imgenunciado = ImageTk.PhotoImage(file=urlimagemenunciado, master=janela6)
            imagemenunciado = Button(janela6, image=imgenunciado)
            imagemenunciado.configure(background="red", border=5)
            resposta = tk.Entry(janela6, bd=3)
            buttonenter_1 = tk.Button(janela6, text='Verificar',
                                      background='red',
                                      foreground='white',
                                      font=('Bebas Neue', 16),
                                      command=answer, bd=5)
            buttonenter = tk.Button(janela6, text='Verificar',
                                    background='#111111',
                                    foreground='white',
                                    font=('Bebas Neue', 16),
                                    command=answer)
            textoquestao.pack()
            imagemenunciado.pack()
            resposta.pack()
            resposta.place(x=618, y=500)
            buttonenter_1.pack()
            buttonenter_1.place(x=632, y=533)
            buttonenter.pack()
            buttonenter.place(x=634, y=535)
            janela6.mainloop()

    if questao == 7:

        def perguntaacerto7():

            jogador.pontos = jogador.pontos + 100

            if questao == ultimoitem:
                janelaultima.destroy()
            elif questao == 7:
                janela7.destroy()

        def correcao():

            janelaerro7.destroy()
            if questao == ultimoitem:
                janelaultima.destroy()
            elif questao == 7:
                janela7.destroy()
            janelacorrecao = tk.Tk()
            janelacorrecao.title('Correção')
            janelacorrecao.geometry('430x600')
            janelacorrecao.configure(background='#111111')
            urlimagemcorrecao = urllib.request.urlopen(
                'https://i.postimg.cc/MKC1wdJm/corre-reflex-o-redimensionada.png')
            imgcorrecao = ImageTk.PhotoImage(file=urlimagemcorrecao, master=janelacorrecao)
            imagemcorrecao = Label(janelacorrecao, image=imgcorrecao)
            imagemcorrecao.pack()
            janelacorrecao.mainloop()


        def perguntaerrada7():

            jogador.vidas = jogador.vidas - 1

            if jogador.vidas == 0:
                gameover()
            else:
                pass

            if jogador.pontos == 0:
                pass
            else:
                jogador.pontos = jogador.pontos - 100

            if questao == ultimoitem:
                janelaultima.destroy()
            elif questao == 7:
                janela7.destroy()

            global janelaerro7
            janelaerro7 = tk.Tk()
            janelaerro7.title('Você errou!')
            janelaerro7.geometry('200x200')
            janelaerro7.configure(background='#111111')
            textoerro = Label(janelaerro7, text='Sinto muito, você errou!',
                              background='#111111',
                              foreground='white',
                              font=('Bebas Neue', 12)
                              )
            button = tk.Button(janelaerro7, text='Saiba o porquê.', command=correcao,
                               background='#111111',
                               foreground='white',
                               font=('Bebas Neue', 12)
                               )
            textoerro.pack()
            button.pack()
            janelaerro7.mainloop()


        if questao == ultimoitem:
            janelaultima = tk.Tk()
            janelaultima.geometry('1366x768')
            janelaultima.title('Última questão')
            janelaultima.configure(background='#111111')
            urlimagemenunciado = urllib.request.urlopen('https://i.postimg.cc/J0QVR10Q/quest-exer7.png')
            imgenunciado = ImageTk.PhotoImage(file=urlimagemenunciado, master=janelaultima)
            imagemenunciado = Button(janelaultima, image=imgenunciado)
            imagemenunciado.configure(bg='orange', bd=5)
            button_1_7 = tk.Button(janelaultima, text='A) Sofrer uma reflexão no eixo x.',
                                   background='orange',
                                   foreground='white',
                                   font=('Bebas Neue', 18),
                                   command=perguntaerrada7,
                                   bd=7)
            button_1 = tk.Button(janelaultima, text='A) Sofrer uma reflexão no eixo x.',
                                 background='#111111',
                                 foreground='white',
                                 font=('Bebas Neue', 18),
                                 command=perguntaerrada7)
            button_2_7 = tk.Button(janelaultima, text='B) Sofrer uma rotação no eixo y.',
                                   background='orange',
                                   foreground='white',
                                   font=('Bebas Neue', 18),
                                   command=perguntaerrada7,
                                   bd=7)
            button_2 = tk.Button(janelaultima, text='B) Sofrer uma rotação no eixo y.',
                                 background='#111111',
                                 foreground='white',
                                 font=('Bebas Neue', 18),
                                 command=perguntaerrada7)
            button_3_7 = tk.Button(janelaultima, text='C) Sofrer uma rotação no eixo x.',
                                   background='orange',
                                   foreground='white',
                                   font=('Bebas Neue', 18),
                                   command=perguntaerrada7,
                                   bd=7)
            button_3 = tk.Button(janelaultima, text='C) Sofrer uma rotação no eixo x.',
                                 background='#111111',
                                 foreground='white',
                                 font=('Bebas Neue', 18),
                                 command=perguntaerrada7)
            button_4_7 = tk.Button(janelaultima, text='D) Sofrer uma reflexão no eixo y.',
                                   background='orange',
                                   foreground='white',
                                   font=('Bebas Neue', 18),
                                   command=perguntaacerto7,
                                   bd=7)
            button_4 = tk.Button(janelaultima, text='D) Sofrer uma reflexão no eixo y.',
                                 background='#111111',
                                 foreground='white',
                                 font=('Bebas Neue', 18),
                                 command=perguntaacerto7)
            imagemenunciado.pack()
            button_1.pack()
            button_1_7.pack()
            button_1.place(x=274, y=504)
            button_1_7.place(x=270, y=500)
            button_2.pack()
            button_2_7.pack()
            button_2.place(x=274, y=604)
            button_2_7.place(x=270, y=600)
            button_3.pack()
            button_3_7.pack()
            button_3.place(x=804, y=504)
            button_3_7.place(x=800, y=500)
            button_4.pack()
            button_4_7.pack()
            button_4.place(x=804, y=604)
            button_4_7.place(x=800, y=600)
            janelaultima.mainloop()
        else:
            janela7 = tk.Tk()
            janela7.geometry('1366x768')
            janela7.title('Pergunta 7')
            janela7.configure(background='#111111')
            urlimagemenunciado = urllib.request.urlopen('https://i.postimg.cc/J0QVR10Q/quest-exer7.png')
            imgenunciado = ImageTk.PhotoImage(file=urlimagemenunciado, master=janela7)
            imagemenunciado = Button(janela7, image=imgenunciado)
            imagemenunciado.configure(bg='orange', bd=5)
            button_1_7 = tk.Button(janela7, text='A) Sofrer uma reflexão no eixo x.',
                                   background='orange',
                                   foreground='white',
                                   font=('Bebas Neue', 18),
                                   command=perguntaerrada7,
                                   bd=7)
            button_1 = tk.Button(janela7, text='A) Sofrer uma reflexão no eixo x.',
                                 background='#111111',
                                 foreground='white',
                                 font=('Bebas Neue', 18),
                                 command=perguntaerrada7)
            button_2_7 = tk.Button(janela7, text='B) Sofrer uma rotação no eixo y.',
                                   background='orange',
                                   foreground='white',
                                   font=('Bebas Neue', 18),
                                   command=perguntaerrada7,
                                   bd=7)
            button_2 = tk.Button(janela7, text='B) Sofrer uma rotação no eixo y.',
                                 background='#111111',
                                 foreground='white',
                                 font=('Bebas Neue', 18),
                                 command=perguntaerrada7)
            button_3_7 = tk.Button(janela7, text='C) Sofrer uma rotação no eixo x.',
                                   background='orange',
                                   foreground='white',
                                   font=('Bebas Neue', 18),
                                   command=perguntaerrada7,
                                   bd=7)
            button_3 = tk.Button(janela7, text='C) Sofrer uma rotação no eixo x.',
                                 background='#111111',
                                 foreground='white',
                                 font=('Bebas Neue', 18),
                                 command=perguntaerrada7)
            button_4_7 = tk.Button(janela7, text='D) Sofrer uma reflexão no eixo y.',
                                   background='orange',
                                   foreground='white',
                                   font=('Bebas Neue', 18),
                                   command=perguntaacerto7,
                                   bd=7)
            button_4 = tk.Button(janela7, text='D) Sofrer uma reflexão no eixo y.',
                                 background='#111111',
                                 foreground='white',
                                 font=('Bebas Neue', 18),
                                 command=perguntaacerto7)
            imagemenunciado.pack()
            button_1.pack()
            button_1_7.pack()
            button_1.place(x=274, y=504)
            button_1_7.place(x=270, y=500)
            button_2.pack()
            button_2_7.pack()
            button_2.place(x=274, y=604)
            button_2_7.place(x=270, y=600)
            button_3.pack()
            button_3_7.pack()
            button_3.place(x=804, y=504)
            button_3_7.place(x=800, y=500)
            button_4.pack()
            button_4_7.pack()
            button_4.place(x=804, y=604)
            button_4_7.place(x=800, y=600)
            janela7.mainloop()

    if questao == 8:

        def perguntaacerto8():

            jogador.pontos = jogador.pontos + 100

            if questao == ultimoitem:
                janelaultima.destroy()
            elif questao == 8:
                janela8.destroy()

        def correcao():

            janelaerro8.destroy()
            if questao == ultimoitem:
                janelaultima.destroy()
            elif questao == 8:
                janela8.destroy()
            janelacorrecao = tk.Tk()
            janelacorrecao.title('Correção 1')
            janelacorrecao.geometry('430x600')
            janelacorrecao.configure(background='#111111')
            urlimagemcorrecao1 = urllib.request.urlopen('https://i.postimg.cc/52Gt796y/corre-rota-o-redimensionada.png')
            imgcorrecao1 = ImageTk.PhotoImage(file=urlimagemcorrecao1, master=janelacorrecao)
            imagemcorrecao1 = Label(janelacorrecao, image=imgcorrecao1)
            imagemcorrecao1.pack()
            janelacorrecao.mainloop()


        def perguntaerrada8():

            jogador.vidas = jogador.vidas - 1

            if jogador.vidas == 0:
                gameover()
            else:
                pass

            if jogador.pontos == 0:
                pass
            else:
                jogador.pontos = jogador.pontos - 100

            if questao == ultimoitem:
                janelaultima.destroy()
            elif questao == 8:
                janela8.destroy()

            global janelaerro8
            janelaerro8 = tk.Tk()
            janelaerro8.title('Você errou!')
            janelaerro8.geometry('200x200')
            janelaerro8.configure(background='#111111')
            textoerro = Label(janelaerro8, text='Sinto muito, você errou!',
                              background='#111111',
                              foreground='white',
                              font=('Bebas Neue', 12)
                              )
            button = tk.Button(janelaerro8, text='Saiba o porquê.', command=correcao,
                               background='#111111',
                               foreground='white',
                               font=('Bebas Neue', 12)
                               )
            textoerro.pack()
            button.pack()
            janelaerro8.mainloop()


        if questao == ultimoitem:
            janelaultima = tk.Tk()
            janelaultima.title('Última questão')
            janelaultima.geometry('1366x768')
            janelaultima.configure(background='#111111')
            urlimagem_quest8 = urllib.request.urlopen('https://i.postimg.cc/m2SZV9YD/quest-exer8.png')
            img_8 = ImageTk.PhotoImage(file=urlimagem_quest8, master=janelaultima)
            imagem_8 = Button(janelaultima, image=img_8)
            imagem_8.configure(background='blue', border='7')
            imagem_8.pack()

            button_8_1_1 = tk.Button(janelaultima, text='A) Sentido Anti-horário e 90°', command=perguntaerrada8,
                                     background='blue',
                                     foreground='white',
                                     font=('Bebas Neue', 16),
                                     border='7'
                                     )
            button_8_1 = tk.Button(janelaultima, text='A) Sentido Anti-horário e 90°', command=perguntaerrada8,
                                   background='#111111',
                                   foreground='white',
                                   font=('Bebas Neue', 16)
                                   )
            button_8_2_1 = tk.Button(janelaultima, text='B) Sentido Horário e 100°', command=perguntaerrada8,
                                     background='blue',
                                     foreground='white',
                                     font=('Bebas Neue', 16),
                                     border='7'
                                     )
            button_8_2 = tk.Button(janelaultima, text='B) Sentido Horário e 100°', command=perguntaerrada8,
                                   background='#111111',
                                   foreground='white',
                                   font=('Bebas Neue', 16)
                                   )
            button_8_3_1 = tk.Button(janelaultima, text='C) Sentido Horário e 45°', command=perguntaacerto8,
                                     background='blue',
                                     foreground='white',
                                     font=('Bebas Neue', 16),
                                     border='7'
                                     )
            button_8_3 = tk.Button(janelaultima, text='C) Sentido Horário e 45°', command=perguntaacerto8,
                                   background='#111111',
                                   foreground='white',
                                   font=('Bebas Neue', 16)
                                   )
            button_8_4_1 = tk.Button(janelaultima, text='D) Sentido Anti-horário e 60°', command=perguntaerrada8,
                                     background='blue',
                                     foreground='white',
                                     font=('Bebas Neue', 16),
                                     border='7'
                                     )
            button_8_4 = tk.Button(janelaultima, text='D) Sentido Anti-horário e 60°', command=perguntaerrada8,
                                   background='#111111',
                                   foreground='white',
                                   font=('Bebas Neue', 16)
                                   )
            button_8_1_1.pack()
            button_8_1_1.place(x=10, y=550)
            button_8_1.pack()
            button_8_1.place(x=14, y=554)
            button_8_2_1.pack()
            button_8_2_1.place(x=383, y=550)
            button_8_2.pack()
            button_8_2.place(x=387, y=554)
            button_8_3_1.pack()
            button_8_3_1.place(x=770, y=550)
            button_8_3.pack()
            button_8_3.place(x=774, y=554)
            button_8_4_1.pack()
            button_8_4_1.place(x=1065, y=550)
            button_8_4.pack()
            button_8_4.place(x=1069, y=554)
            janelaultima.mainloop()
        else:
            janela8 = tk.Tk()
            janela8.title('Pergunta 8')
            janela8.geometry('1366x768')
            janela8.configure(background='#111111')
            urlimagem_quest8 = urllib.request.urlopen('https://i.postimg.cc/m2SZV9YD/quest-exer8.png')
            img_8 = ImageTk.PhotoImage(file=urlimagem_quest8, master=janela8)
            imagem_8 = Button(janela8, image=img_8)
            imagem_8.configure(background='blue', border='7')
            imagem_8.pack()

            button_8_1_1 = tk.Button(janela8, text='A) Sentido Anti-horário e 90°', command=perguntaerrada8,
                                     background='blue',
                                     foreground='white',
                                     font=('Bebas Neue', 16),
                                     border='7'
                                     )
            button_8_1 = tk.Button(janela8, text='A) Sentido Anti-horário e 90°', command=perguntaerrada8,
                                   background='#111111',
                                   foreground='white',
                                   font=('Bebas Neue', 16)
                                   )
            button_8_2_1 = tk.Button(janela8, text='B) Sentido Horário e 100°', command=perguntaerrada8,
                                     background='blue',
                                     foreground='white',
                                     font=('Bebas Neue', 16),
                                     border='7'
                                     )
            button_8_2 = tk.Button(janela8, text='B) Sentido Horário e 100°', command=perguntaerrada8,
                                   background='#111111',
                                   foreground='white',
                                   font=('Bebas Neue', 16)
                                   )
            button_8_3_1 = tk.Button(janela8, text='C) Sentido Horário e 45°', command=perguntaacerto8,
                                     background='blue',
                                     foreground='white',
                                     font=('Bebas Neue', 16),
                                     border='7'
                                     )
            button_8_3 = tk.Button(janela8, text='C) Sentido Horário e 45°', command=perguntaacerto8,
                                   background='#111111',
                                   foreground='white',
                                   font=('Bebas Neue', 16)
                                   )
            button_8_4_1 = tk.Button(janela8, text='D) Sentido Anti-horário e 60°', command=perguntaerrada8,
                                     background='blue',
                                     foreground='white',
                                     font=('Bebas Neue', 16),
                                     border='7'
                                     )
            button_8_4 = tk.Button(janela8, text='D) Sentido Anti-horário e 60°', command=perguntaerrada8,
                                   background='#111111',
                                   foreground='white',
                                   font=('Bebas Neue', 16)
                                   )
            button_8_1_1.pack()
            button_8_1_1.place(x=40, y=550)
            button_8_1.pack()
            button_8_1.place(x=44, y=558)
            button_8_2_1.pack()
            button_8_2_1.place(x=383, y=550)
            button_8_2.pack()
            button_8_2.place(x=387, y=558)
            button_8_3_1.pack()
            button_8_3_1.place(x=790, y=550)
            button_8_3.pack()
            button_8_3.place(x=794, y=558)
            button_8_4_1.pack()
            button_8_4_1.place(x=1100, y=550)
            button_8_4.pack()
            button_8_4.place(x=1104, y=558)
            janela8.mainloop()

    if questao == 9:

        def perguntaacerto9():

            jogador.pontos = jogador.pontos + 100

            if questao == ultimoitem:
                janelaultima.destroy()
            elif questao == 9:
                janela9.destroy()

        def correcao():

            janelaerro9.destroy()
            if questao == ultimoitem:
                janelaultima.destroy()
            elif questao == 9:
                janela9.destroy()
            janelacorrecao = tk.Tk()
            janelacorrecao2 = tk.Tk()
            janelacorrecao.title('Correção 1')
            janelacorrecao2.title('Correção 2')
            janelacorrecao.geometry('430x600')
            janelacorrecao2.geometry('430x600')
            janelacorrecao.configure(background='#111111')
            janelacorrecao2.configure(background='#111111')
            urlimagemcorrecao1 = urllib.request.urlopen('https://i.postimg.cc/52Gt796y/corre-rota-o-redimensionada.png')
            urlimagemcorrecao2 = urllib.request.urlopen(
                'https://i.postimg.cc/MKC1wdJm/corre-reflex-o-redimensionada.png')
            imgcorrecao1 = ImageTk.PhotoImage(file=urlimagemcorrecao1, master=janelacorrecao)
            imgcorrecao2 = ImageTk.PhotoImage(file=urlimagemcorrecao2, master=janelacorrecao2)
            imagemcorrecao1 = Label(janelacorrecao, image=imgcorrecao1)
            imagemcorrecao2 = Label(janelacorrecao2, image=imgcorrecao2)
            imagemcorrecao1.pack()
            imagemcorrecao2.pack()
            janelacorrecao.mainloop()
            janelacorrecao2.mainloop()


        def perguntaerrada9():

            jogador.vidas = jogador.vidas - 1

            if jogador.vidas == 0:
                gameover()
            else:
                pass

            if jogador.pontos == 0:
                pass
            else:
                jogador.pontos = jogador.pontos - 100

            if questao == ultimoitem:
                janelaultima.destroy()
            elif questao == 9:
                janela9.destroy()

            global janelaerro9
            janelaerro9 = tk.Tk()
            janelaerro9.title('Você errou!')
            janelaerro9.geometry('200x200')
            janelaerro9.configure(background='#111111')
            textoerro = Label(janelaerro9, text='Sinto muito, você errou!',
                              background='#111111',
                              foreground='white',
                              font=('Bebas Neue', 12)
                              )
            button = tk.Button(janelaerro9, text='Saiba o porquê.', command=correcao,
                               background='#111111',
                               foreground='white',
                               font=('Bebas Neue', 12)
                               )
            textoerro.pack()
            button.pack()
            janelaerro9.mainloop()


        if questao == ultimoitem:
            janelaultima = tk.Tk()
            janelaultima.title('Última questão')
            janelaultima.geometry('1366x768')
            janelaultima.configure(background='#111111')
            frame10 = tk.Frame(master=janelaultima, highlightbackground="purple", highlightthickness=8, height=458
                               , width=610)
            frame10.pack(padx=10, pady=10)
            frame10.place(x=379, y=0)
            urlimagem_1 = urllib.request.urlopen('https://i.postimg.cc/cCSZB16w/quest-exer9.png')
            frame1 = tk.Frame(master=janelaultima, highlightbackground="purple", highlightthickness=8, height=45
                              , width=259)
            frame1.pack(padx=10, pady=10)
            frame1.place(x=48, y=598)

            frame2 = tk.Frame(master=janelaultima, highlightbackground="purple", highlightthickness=8, height=45
                              , width=200)
            frame2.pack(padx=10, pady=10)
            frame2.place(x=48, y=538)

            frame3 = tk.Frame(master=janelaultima, highlightbackground="purple", highlightthickness=8, height=45
                              , width=403)
            frame3.pack(padx=10, pady=10)
            frame3.place(x=927, y=538)

            frame4 = tk.Frame(master=janelaultima, highlightbackground="purple", highlightthickness=8, height=45
                              , width=250)
            frame4.pack(padx=10, pady=10)
            frame4.place(x=1081, y=598)

            button_1 = tk.Button(janelaultima, text='A) Uma translação.', command=perguntaerrada9,
                                 background='#111111',
                                 foreground='white',
                                 font=('Bebas Neue', 16)
                                 )
            button_2 = tk.Button(janelaultima, text='B) Uma rotação em 180°.', command=perguntaacerto9,
                                 background='#111111',
                                 foreground='white',
                                 font=('Bebas Neue', 16)
                                 )
            button_3 = tk.Button(janelaultima, text='C) Reflexão no eixo X e rotação em 90°.', command=perguntaerrada9,
                                 background='#111111',
                                 foreground='white',
                                 font=('Bebas Neue', 16)
                                 )
            button_4 = tk.Button(janelaultima, text='D) Uma rotação em 45°.', command=perguntaerrada9,
                                 background='#111111',
                                 foreground='white',
                                 font=('Bebas Neue', 16)
                                 )

            img_1 = ImageTk.PhotoImage(file=urlimagem_1, master=janelaultima)
            imagem_1 = Label(janelaultima, image=img_1)
            imagem_1.pack()
            button_1.pack()
            button_1.place(x=50, y=540)
            button_2.pack()
            button_2.place(x=50, y=600)
            button_3.pack()
            button_3.place(x=930, y=540)
            button_4.pack()
            button_4.place(x=1084, y=600)
            janelaultima.mainloop()

        else:
            janela9 = tk.Tk()
            janela9.title('Pergunta 9')
            janela9.geometry('1366x768')
            janela9.configure(background='#111111')
            frame10 = tk.Frame(master=janela9, highlightbackground="purple", highlightthickness=8, height=458
                               , width=610)
            frame10.pack(padx=10, pady=10)
            frame10.place(x=379, y=0)
            urlimagem_1 = urllib.request.urlopen('https://i.postimg.cc/cCSZB16w/quest-exer9.png')
            frame1 = tk.Frame(master=janela9, highlightbackground="purple", highlightthickness=8, height=45
                              , width=259)
            frame1.pack(padx=10, pady=10)
            frame1.place(x=48, y=598)

            frame2 = tk.Frame(master=janela9, highlightbackground="purple", highlightthickness=8, height=45
                              , width=200)
            frame2.pack(padx=10, pady=10)
            frame2.place(x=48, y=538)

            frame3 = tk.Frame(master=janela9, highlightbackground="purple", highlightthickness=8, height=45
                              , width=403)
            frame3.pack(padx=10, pady=10)
            frame3.place(x=927, y=538)

            frame4 = tk.Frame(master=janela9, highlightbackground="purple", highlightthickness=8, height=45
                              , width=250)
            frame4.pack(padx=10, pady=10)
            frame4.place(x=1081, y=598)

            button_1 = tk.Button(janela9, text='A) Uma translação.', command=perguntaerrada9,
                                 background='#111111',
                                 foreground='white',
                                 font=('Bebas Neue', 16)
                                 )
            button_2 = tk.Button(janela9, text='B) Uma rotação em 180°.', command=perguntaacerto9,
                                 background='#111111',
                                 foreground='white',
                                 font=('Bebas Neue', 16)
                                 )
            button_3 = tk.Button(janela9, text='C) Reflexão no eixo X e rotação em 90°.', command=perguntaerrada9,
                                 background='#111111',
                                 foreground='white',
                                 font=('Bebas Neue', 16)
                                 )
            button_4 = tk.Button(janela9, text='D) Uma rotação em 45°.', command=perguntaerrada9,
                                 background='#111111',
                                 foreground='white',
                                 font=('Bebas Neue', 16)
                                 )

            img_1 = ImageTk.PhotoImage(file=urlimagem_1, master=janela9)
            imagem_1 = Label(janela9, image=img_1)
            imagem_1.pack()
            button_1.pack()
            button_1.place(x=50, y=540)
            button_2.pack()
            button_2.place(x=50, y=600)
            button_3.pack()
            button_3.place(x=930, y=540)
            button_4.pack()
            button_4.place(x=1084, y=600)
            janela9.mainloop()

    if questao == 10:

        def perguntaacerto10():

            jogador.pontos = jogador.pontos + 100

            if questao == ultimoitem:
                janelaultima.destroy()
            elif questao == 10:
                janela10.destroy()

        def correcao():

            janelaerro10.destroy()
            if questao == ultimoitem:
                janelaultima.destroy()
            elif questao == 10:
                janela10.destroy()
            janelacorrecao = tk.Tk()
            janelacorrecao.title('Correção 1')
            janelacorrecao.geometry('430x600')
            janelacorrecao.configure(background='#111111')
            urlimagemcorrecao1 = urllib.request.urlopen(
                'https://i.postimg.cc/fR6w7Hr0/corre-transla-o-redimensionada.png')
            imgcorrecao1 = ImageTk.PhotoImage(file=urlimagemcorrecao1, master=janelacorrecao)
            imagemcorrecao1 = Label(janelacorrecao, image=imgcorrecao1)
            imagemcorrecao1.pack()
            janelacorrecao.mainloop()


        def perguntaerrada10():

            jogador.vidas = jogador.vidas - 1

            if jogador.vidas == 0:
                gameover()
            else:
                pass

            if jogador.pontos == 0:
                pass
            else:
                jogador.pontos = jogador.pontos - 100

            if questao == ultimoitem:
                janelaultima.destroy()
            elif questao == 10:
                janela10.destroy()

            global janelaerro10
            janelaerro10 = tk.Tk()
            janelaerro10.title('Você errou!')
            janelaerro10.geometry('200x200')
            janelaerro10.configure(background='#111111')
            textoerro = Label(janelaerro10, text='Sinto muito, você errou!',
                              background='#111111',
                              foreground='white',
                              font=('Bebas Neue', 12)
                              )
            button = tk.Button(janelaerro10, text='Saiba o porquê.', command=correcao,
                               background='#111111',
                               foreground='white',
                               font=('Bebas Neue', 12)
                               )
            textoerro.pack()
            button.pack()
            janelaerro10.mainloop()


        if questao == ultimoitem:
            janelaultima = tk.Tk()
            janelaultima.title('Última questão')
            janelaultima.geometry('1366x768')
            janelaultima.configure(background='#111111')

            urlimagem_10 = urllib.request.urlopen('https://i.postimg.cc/9FXHmn9m/quest-exer10.png')
            urlalternativa10_1 = urllib.request.urlopen('https://i.postimg.cc/rmpG8HWr/ex10-1.png')
            urlalternativa10_2 = urllib.request.urlopen('https://i.postimg.cc/tg42Bkk2/ex10-2.png')
            urlalternativa10_3 = urllib.request.urlopen('https://i.postimg.cc/7LJTPTZq/ex10-3.png')
            urlalternativa10_4 = urllib.request.urlopen('https://i.postimg.cc/vH8ggKZq/ex10-4.png')
            img_10 = ImageTk.PhotoImage(file=urlimagem_10, master=janelaultima)
            imgal1 = ImageTk.PhotoImage(file=urlalternativa10_1, master=janelaultima)
            imgal2 = ImageTk.PhotoImage(file=urlalternativa10_2, master=janelaultima)
            imgal3 = ImageTk.PhotoImage(file=urlalternativa10_3, master=janelaultima)
            imgal4 = ImageTk.PhotoImage(file=urlalternativa10_4, master=janelaultima)

            frame_10 = tk.Frame(master=janelaultima, highlightbackground="red", highlightthickness=8, height=457,
                                width=610)
            frame_10.pack(padx=10, pady=10)
            frame_10.place(x=379, y=0)
            imagem_10 = Label(janelaultima, image=img_10)
            imagem_10.pack()

            frame_10_1 = tk.Frame(master=janelaultima, highlightbackground="red", highlightthickness=8, height=160,
                                  width=260)
            frame_10_1.pack(padx=10, pady=10)
            frame_10_1.place(x=8, y=498)
            frame_10_2 = tk.Frame(master=janelaultima, highlightbackground="red", highlightthickness=8, height=160,
                                  width=260)
            frame_10_2.pack(padx=10, pady=10)
            frame_10_2.place(x=298, y=498)
            frame_10_3 = tk.Frame(master=janelaultima, highlightbackground="red", highlightthickness=8, height=160,
                                  width=260)
            frame_10_3.pack(padx=10, pady=10)
            frame_10_3.place(x=788, y=498)
            frame_10_4 = tk.Frame(master=janelaultima, highlightbackground="red", highlightthickness=8, height=160,
                                  width=260)
            frame_10_4.pack(padx=10, pady=10)
            frame_10_4.place(x=1088, y=498)

            button_10_1 = tk.Button(janelaultima, image=imgal1, command=perguntaerrada10)
            button_10_2 = tk.Button(janelaultima, image=imgal2, command=perguntaacerto10)
            button_10_3 = tk.Button(janelaultima, image=imgal3, command=perguntaerrada10)
            button_10_4 = tk.Button(janelaultima, image=imgal4, command=perguntaerrada10)
            button_10_1.pack()
            button_10_1.place(x=10, y=500)
            button_10_2.pack()
            button_10_2.place(x=300, y=500)
            button_10_3.pack()
            button_10_3.place(x=790, y=500)
            button_10_4.pack()
            button_10_4.place(x=1090, y=500)
            janelaultima.mainloop()
        else:
            janela10 = tk.Tk()
            janela10.title('Pergunta 10')
            janela10.geometry('1366x768')
            janela10.configure(background='#111111')

            urlimagem_10 = urllib.request.urlopen('https://i.postimg.cc/9FXHmn9m/quest-exer10.png')
            urlalternativa10_1 = urllib.request.urlopen('https://i.postimg.cc/rmpG8HWr/ex10-1.png')
            urlalternativa10_2 = urllib.request.urlopen('https://i.postimg.cc/tg42Bkk2/ex10-2.png')
            urlalternativa10_3 = urllib.request.urlopen('https://i.postimg.cc/7LJTPTZq/ex10-3.png')
            urlalternativa10_4 = urllib.request.urlopen('https://i.postimg.cc/vH8ggKZq/ex10-4.png')
            img_10 = ImageTk.PhotoImage(file=urlimagem_10, master=janela10)
            imgal1 = ImageTk.PhotoImage(file=urlalternativa10_1, master=janela10)
            imgal2 = ImageTk.PhotoImage(file=urlalternativa10_2, master=janela10)
            imgal3 = ImageTk.PhotoImage(file=urlalternativa10_3, master=janela10)
            imgal4 = ImageTk.PhotoImage(file=urlalternativa10_4, master=janela10)

            frame_10 = tk.Frame(master=janela10, highlightbackground="red", highlightthickness=8, height=457, width=610)
            frame_10.pack(padx=10, pady=10)
            frame_10.place(x=379, y=0)
            imagem_10 = Label(janela10, image=img_10)
            imagem_10.pack()

            frame_10_1 = tk.Frame(master=janela10, highlightbackground="red", highlightthickness=8, height=160,
                                  width=260)
            frame_10_1.pack(padx=10, pady=10)
            frame_10_1.place(x=8, y=498)
            frame_10_2 = tk.Frame(master=janela10, highlightbackground="red", highlightthickness=8, height=160,
                                  width=260)
            frame_10_2.pack(padx=10, pady=10)
            frame_10_2.place(x=298, y=498)
            frame_10_3 = tk.Frame(master=janela10, highlightbackground="red", highlightthickness=8, height=160,
                                  width=260)
            frame_10_3.pack(padx=10, pady=10)
            frame_10_3.place(x=788, y=498)
            frame_10_4 = tk.Frame(master=janela10, highlightbackground="red", highlightthickness=8, height=160,
                                  width=260)
            frame_10_4.pack(padx=10, pady=10)
            frame_10_4.place(x=1088, y=498)

            button_10_1 = tk.Button(janela10, image=imgal1, command=perguntaerrada10)
            button_10_2 = tk.Button(janela10, image=imgal2, command=perguntaacerto10)
            button_10_3 = tk.Button(janela10, image=imgal3, command=perguntaerrada10)
            button_10_4 = tk.Button(janela10, image=imgal4, command=perguntaerrada10)
            button_10_1.pack()
            button_10_1.place(x=10, y=500)
            button_10_2.pack()
            button_10_2.place(x=300, y=500)
            button_10_3.pack()
            button_10_3.place(x=790, y=500)
            button_10_4.pack()
            button_10_4.place(x=1090, y=500)
            janela10.mainloop()


def gabarito():
    janelagabarito = tk.Tk()
    janelagabarito.geometry('800x800')
    janelagabarito.title('Gabarito')
    janelagabarito.configure(background='#111111')


def perguntagabarito():
    janelapergunta = tk.Tk()
    janelapergunta.title('Gabarito')
    janelapergunta.geometry('200x200')
    janelapergunta.configure(background='#111111')
    textopergunta = Label(janelapergunta, text='Quer ver o gabarito?',
                          background='#111111',
                          foreground='white',
                          font=('Bebas Neue', 12)
                          )
    buttonsim = tk.Button(janelapergunta, text='SIM',
                          background='#111111',
                          foreground='white',
                          font=('Bebas Neue', 12),
                          command=gabarito)
    buttonnao = tk.Button(janelapergunta, text='NÃO',
                          background='#111111',
                          foreground='white',
                          font=('Bebas Neue', 12),
                          command=janelapergunta.destroy)
    textopergunta.pack()
    buttonsim.pack()
    buttonsim.place(x=50, y=100)
    buttonnao.pack()
    buttonnao.place(x=150, y=100)
    janelapergunta.mainloop()


perguntagabarito()

#Verificando se os dados dos objetos são salvos corretamente!
print("O jogador {} fez {} pontos com {} vida(s)!".format(jogador.nome,jogador.pontos,jogador.vidas))

def saveinfo():
    qsave.destroy()
    with open('playerdata.json', 'r') as file:
        maindata = json.load(file)

    infojogador.update({jogador.nome : ['Pontos: {}, Vidas: {}'.format(jogador.pontos,jogador.vidas)]})
    maindata.update(infojogador)
    with open('playerdata.json','w') as file:
        json.dump(maindata,file,indent=1)


def scoreboard():
    qload.destroy()
    with open('playerdata.json','r') as file:
        data = json.load(file)

        ## Função utilizada para desligar o teclado enquanto se vê o placar de pontuação,
        ## para evitar fraudes.

        keyboarddisable = pynput.keyboard.Listener(suppress=True)
        keyboarddisable.start()

        scorewindow = tk.Tk()
        scorewindow.geometry('1366x768')
        scorewindow.title('SCOREBOARD')
        scorewindow.configure(background="#111111")
        scrollbar = tk.Scrollbar(scorewindow)
        scrollbar.pack(side=RIGHT,fill=Y)
        maintext = tk.Text(scorewindow,width=1366,height=768,bg="#111111",fg='white',font=('Bebas Neue',15),yscrollcommand=scrollbar.set)
        maintext.tag_configure("center",justify='center')
        for item in data.items():
            maintext.insert(tk.END, str(item) + '\n',"center")
        maintext.pack()
        scrollbar.config(command=maintext.yview)
        scorewindow.mainloop()



#Janela perguntando se o usuário quer salvar sua pontuação.

qsave = tk.Tk()
qsave.title('Salvar informações')
qsave.geometry('400x300')
qsave.configure(background='#111111')
text = Label(qsave,text='Quer salvar sua pontuação?',background='#111111',
             foreground='white',font=('Bebas Neue',15))
confirm = tk.Button(qsave,text='Sim',background='#111111',foreground='white',
                   font=('Bebas Neue',15),command=saveinfo)
decline = tk.Button(qsave,text='Não',background='#111111',foreground='white',
                    font=('Bebas Neue',15),command=qsave.destroy)
text.pack()
confirm.pack()
decline.pack()
qsave.mainloop()

#Janela perguntando se o usuário quer abrir o placar de pontuação:

qload = tk.Tk()
qload.title('Ver placar de pontuações')
qload.geometry('400x300')
qload.configure(background="#111111")
text = Label(qload,text='Quer ver o placar de pontuação?',background='#111111',
             foreground='white',font=('Bebas Neue',15))
confirm = tk.Button(qload,text='Sim',background='#111111',foreground='white',
                   font=('Bebas Neue',15),command=scoreboard)
decline = tk.Button(qload,text='Não',background='#111111',foreground='white',
                    font=('Bebas Neue',15),command=qload.destroy)
text.pack()
confirm.pack()
decline.pack()
qload.mainloop()





# Última função a serem executada no programa:
# Função encerramento: Agradecendo aos participantes do questionário:
def encerramento():
    janelaagradecimentos = tk.Tk()
    janelaagradecimentos.title('Obrigado!')
    janelaagradecimentos.geometry('300x300')
    janelaagradecimentos.configure(background='#111111')

    textoagradecimento = Label(janelaagradecimentos, text='Obrigado por participar deste questionário!',
                               background='#111111',
                               foreground='white',
                               font=('Bebas Neue', 12))
    botaoencerramento = tk.Button(janelaagradecimentos, text='Clique para encerrar o questionário!', command=exit,
                                  background='#111111',
                                  foreground='white',
                                  font=('Bebas Neue', 12))
    textoagradecimento.pack()
    botaoencerramento.pack()
    janelaagradecimentos.mainloop()

encerramento()
