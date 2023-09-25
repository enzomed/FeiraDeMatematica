import tkinter as tk
from tkinter import *
import cv2
import tkinter.ttk
import PIL
import os
from PIL import Image,ImageTk
import urllib
import urllib.request
from tkinter.ttk import Label
import random
from random import shuffle

def creditospropaganda():
    creditos_propaganda = tk.Tk()
    creditos_propaganda.title('Créditos')
    creditos_propaganda.geometry('1366x768')
    creditos_propaganda.configure(background='#111111')
    textocreditos = Label(creditos_propaganda,text='Equipe responsável pela propaganda da feira:')
    botaoencerrar = tk.Button(creditos_propaganda,text='Sair',command=creditos_propaganda.destroy)
    textocreditos.pack()
    botaoencerrar.pack()


def creditosperguntas():
    creditos_perguntas = tk.Tk()
    creditos_perguntas.title('Créditos das perguntas')
    creditos_perguntas.geometry('1366x768')
    creditos_perguntas.configure(background='#111111')
    textocreditos = Label(creditos_perguntas,text='Equipe responsável pela criação das perguntas: Vitórias, Patrine, Rafael, Maisa, Pedro, Arthur, Sarah ',
                          background = '#111111',
                          foreground = 'white',
                          font = ('Bebas Neue',16)
                          )
    botaoproxcred = tk.Button(creditos_perguntas,text='Próxima equipe',command=creditospropaganda,
                              background='#111111',
                              foreground= 'white',
                              font=('Bebas Neue',16)
                              )
    textocreditos.pack()
    botaoproxcred.pack()




def creditosimagens():
    creditos_imagens = tk.Tk()
    creditos_imagens.title('Créditos das imagens')
    creditos_imagens.geometry('1366x768')
    creditos_imagens.configure(background='#111111')
    textocreditos = Label(creditos_imagens,text='Equipe das imagens: Juliana, Yasmin, Matheus, Nicolas, Miguel',
                          background = '#111111',
                          foreground = 'white',
                          font = ('Bebas Neue',16)
                          )
    botaoproxcred = tk.Button(creditos_imagens,text='Próxima equipe',command=creditosperguntas,
                              background='#111111',
                              foreground='white',
                              font = ('Bebas Neue',16)
                              )
    textocreditos.pack()
    botaoproxcred.pack()

def creditosprogramadores():
    creditos_programadores = tk.Tk()
    creditos_programadores.title('Equipe responsável pela modelagem e criação do código para o programa.')
    creditos_programadores.geometry('1366x768')
    creditos_programadores.configure(background='#111111')
    textocreditos = Label(creditos_programadores,text='Equipe de programação: Enzo Fernandes, Kleber Rogério, Gabryel Pereira, Leandro Kenji, Paulo Roberto,',
                          background='#111111',
                          foreground='white',
                          font=('Bebas Neue',16)
                          )
    botaoproxcred = tk.Button(creditos_programadores,text='Próxima equipe',command=creditosimagens,
                              background='#111111',
                              foreground='white',
                              font=('Bebas Neue',16),
                              )
    textocreditos.pack()
    botaoproxcred.pack()





## Janela principal:

janela_principal = tk.Tk()
janela_principal.title('Menu principal')
janela_principal.geometry('1366x768')
urlimagem = urllib.request.urlopen('https://i.pinimg.com/originals/43/d6/82/43d682282bc59ed8c21b448a6120277f.png')
img = ImageTk.PhotoImage(file=urlimagem,master=janela_principal)
imagemtitulo = Label(janela_principal,image=img)
botaocreditos = tk.Button(janela_principal,text='Ver créditos',background='#111111',foreground='white',font=('Bebas Neue',16),command=creditosprogramadores)
botaoinicio = tk.Button(janela_principal,
                        text='Clique para iniciar!',
                        background= "#111111",
                        foreground= "white",
                        font=("Bebas Neue", 16),
                        command=janela_principal.destroy)
botaoencerrar = tk.Button(janela_principal,text='Clique para encerrar o programa!',
                        background= "#111111",
                        foreground= "white",
                        font=("Bebas Neue", 16),
                        command=exit)
textointro = Label(janela_principal,text='Bem vindo ao Projeto da Feira de Matemática!',
                        background= "#111111",
                        foreground= "white",
                        font=("Bebas Neue", 16))
textosubintro = Label(janela_principal,text='Um projeto realizado pela turma do 3°B!',
                        background= "#111111",
                        foreground= "white",
                        font=("Bebas Neue", 16))
imagemtitulo.pack()
textointro.pack()
textosubintro.pack()
botaoinicio.pack()
botaocreditos.pack()
botaoencerrar.pack()
janela_principal.configure(bg='#111111')
janela_principal.mainloop()










## Definição das questões
lista = [3,2,1]
ultimoitem = lista[-1]
print(lista)

for questao in lista:
    if questao == 1:
        ##Definição das funções: ( EM PRIMEIRO LUGAR SE DEFINE A FUNÇÃO CORREÇÃO E DEPOIS A FUNÇÃO DA PERGUNTA ERRADA. )
        ## 1° def correcao()
        ## 2° def perguntaerrada()

        def correcao():
            janelacorrecao=tk.Tk()
            janelacorrecao.title('Correção')
            janelacorrecao.geometry('430x600')
            janelacorrecao.configure(background='#111111')
            urlimagemcorrecao = urllib.request.urlopen('https://i.postimg.cc/MKC1wdJm/corre-reflex-o-redimensionada.png')
            imgcorrecao = ImageTk.PhotoImage(file=urlimagemcorrecao,master=janelacorrecao)
            imagemcorrecao = Label(janelacorrecao,image=imgcorrecao)
            imagemcorrecao.pack()
            janelacorrecao.mainloop()

        def perguntaerrada():
            janelaerro = tk.Tk()
            janelaerro.title('Você errou!')
            janelaerro.geometry('200x200')
            janelaerro.configure(background='#111111')
            textoerro = Label(janelaerro,text='Sinto muito, você errou!',
                              background='#111111',
                              foreground='white',
                              font=('Bebas Neue',12))
            button = tk.Button(janelaerro,text='Saiba o porquê.',command=correcao,
                               background='#111111',
                               foreground='white',
                               font=('Bebas Neue',12))
            textoerro.pack()
            button.pack()
            janelaerro.mainloop()


        if questao == ultimoitem:
            janelaultima = tk.Tk()
            janelaultima.geometry('1366x768')
            janelaultima.title('ultima questao')
            janelaultima.configure(background='#111111')
            textoquestaoultima = Label(janelaultima, text='A que corresponde a uma reflexão axial?',
                         background='#111111',
                         foreground='white',
                         font=('Bebas Neue',20)
                         )
            urlimagem = urllib.request.urlopen('https://i.postimg.cc/wjXDFLRx/imagem-questao1.png')
            img = ImageTk.PhotoImage(file=urlimagem,master=janelaultima)
            imagem = Label(janelaultima,image=img)
            imagem.pack()
            textoquestaoultima.pack()
            button_1 = tk.Button(janelaultima, text='A) É a figura 3.', command=perguntaerrada,
                                 background='#111111',
                                 foreground='white',
                                 font=('Bebas Neue',16)
                                 )
            button_2 = tk.Button(janelaultima, text='B) É a figura 1.', command=perguntaerrada,
                                 background='#111111',
                                 foreground='white',
                                 font=('Bebas Neue',16)
                                 )
            button_3 = tk.Button(janelaultima, text='C) É a figura 4.', command=perguntaerrada,
                                 background='#111111',
                                 foreground='white',
                                 font=('Bebas Neue',16)
                                 )
            button_4 = tk.Button(janelaultima, text='D) É a figura 2.', command=janelaultima.destroy,
                                 background='#111111',
                                 foreground='white',
                                 font=('Bebas Neue',16)
                                 )
            button_1.pack()
            button_1.place(x=50,y=600)
            button_2.pack()
            button_2.place(x=200,y=600)
            button_3.pack()
            button_3.place(x=1050,y=600)
            button_4.pack()
            button_4.place(x=1200,y=600)
            janelaultima.mainloop()
        else:
            janela1 = tk.Tk()
            janela1.title('Pergunta 1')
            janela1.geometry('1366x768')
            janela1.configure(background='#111111')
            urlimagem_1 = urllib.request.urlopen('https://i.postimg.cc/wjXDFLRx/imagem-questao1.png')
            img_1 = ImageTk.PhotoImage(file=urlimagem_1, master=janela1)
            imagem_1 = Label(janela1, image=img_1)
            textoquestao = Label(janela1,text='A que corresponde a uma reflexão axial?',
                                 background='#111111',
                                 foreground='white',
                                 font=('Bebas Neue',20)
                                 )
            imagem_1.pack()
            button_1 = tk.Button(janela1, text='A) É a figura 3.', command=perguntaerrada,
                                 background='#111111',
                                 foreground='white',
                                 font=('Bebas Neue',16)
                                 )
            button_2 = tk.Button(janela1, text='B) É a figura 1.', command=perguntaerrada,
                                 background='#111111',
                                 foreground='white',
                                 font=('Bebas Neue',16)
                                 )
            button_3 = tk.Button(janela1, text='C) É a figura 4.', command=perguntaerrada,
                                 background='#111111',
                                 foreground='white',
                                 font=('Bebas Neue',16)
                                 )
            button_4 = tk.Button(janela1, text='D) É a figura 2.', command=janela1.destroy,
                                 background='#111111',
                                 foreground='white',
                                 font=('Bebas Neue',16)
                                 )
            textoquestao.pack()
            button_1.pack()
            button_1.place(x=50,y=600)
            button_2.pack()
            button_2.place(x=200,y=600)
            button_3.pack()
            button_3.place(x=1050,y=600)
            button_4.pack()
            button_4.place(x=1200,y=600)
            janela1.mainloop()

    if questao == 2:

        def correcao():
            janelacorrecao = tk.Tk()
            janelacorrecao.title('Correção')
            janelacorrecao.geometry('600x600')
            janelacorrecao.configure(background='#111111')
            textocorrecao = Label(janelacorrecao, text='Insira o texto aqui!',
                                  background='#111111',
                                  foreground='white',
                                  font=('Bebas Neue',12)
                                  )
            textocorrecao.pack()
            janelacorrecao.mainloop()


        def perguntaerrada():
            janelaerro = tk.Tk()
            janelaerro.title('Você errou!')
            janelaerro.geometry('200x200')
            janelaerro.configure(background='#111111')
            textoerro = Label(janelaerro, text='Sinto muito, você errou!',
                              background='#111111',
                              foreground='white',
                              font=('Bebas Neue',12)
                              )
            button = tk.Button(janelaerro, text='Saiba o porquê.', command=correcao,
                               background='#111111',
                               foreground='white',
                               font=('Bebas Neue',12)
                               )
            textoerro.pack()
            button.pack()
            janelaerro.mainloop()

        if questao == ultimoitem:
            janelaultima = tk.Tk()
            janelaultima.geometry('1366x768')
            janelaultima.title('ultima questao')
            text = Label(janelaultima, text='ultimaquestao')
            urlimagem = urllib.request.urlopen('https://upload.wikimedia.org/wikipedia/commons/thumb/c/c9/-Insert_image_here-.svg/320px--Insert_image_here-.svg.png')
            img = ImageTk.PhotoImage(file=urlimagem,master=janelaultima)
            imagem = Label(janelaultima,image=img)
            text.pack()
            imagem.pack()
            button_1 = tk.Button(janelaultima, text='A)  Alternativa A', command=janelaultima.destroy)
            button_2 = tk.Button(janelaultima, text='B)  Alternativa B', command=perguntaerrada)
            button_3 = tk.Button(janelaultima, text='C)  Alternativa C', command=perguntaerrada)
            button_4 = tk.Button(janelaultima, text='D)  Alternativa D', command=perguntaerrada)
            button_5 = tk.Button(janelaultima, text='E)  Alternativa E', command=perguntaerrada)
            button_1.pack()
            button_2.pack()
            button_3.pack()
            button_4.pack()
            button_5.pack()
            janelaultima.mainloop()
        else:
            janela2 = tk.Tk()
            janela2.title('Pergunta 2')
            janela2.geometry('1366x768')
            janela2.configure(background='#111111')
            urlimagem_1 = urllib.request.urlopen('https://i.postimg.cc/Pq9prXPc/imagem-questao2-pequeno.png')
            img_1 = ImageTk.PhotoImage(file=urlimagem_1, master=janela2)
            imagem_1 = Label(janela2, image=img_1)
            imagem_1.pack()
            button_1 = tk.Button(janela2, text='A)  Alternativa A', command=janela2.destroy)
            button_2 = tk.Button(janela2, text='B)  Alternativa B', command=perguntaerrada)
            button_3 = tk.Button(janela2, text='C)  Alternativa C', command=perguntaerrada)
            button_4 = tk.Button(janela2, text='D)  Alternativa D', command=perguntaerrada)
            button_5 = tk.Button(janela2, text='E)  Alternativa E', command=perguntaerrada)
            button_1.pack()
            button_2.pack()
            button_3.pack()
            button_4.pack()
            button_5.pack()
            janela2.mainloop()
    if questao == 3:

        def correcao():
            janelacorrecao = tk.Tk()
            janelacorrecao.title('Correção')
            janelacorrecao.geometry('600x600')
            janelacorrecao.configure(background='#111111')
            textocorrecao = Label(janelacorrecao, text='Insira o texto aqui!',
                                  background='#111111',
                                  foreground='white',
                                  font=('Bebas Neue',12))
            textocorrecao.pack()
            janelacorrecao.mainloop()


        def perguntaerrada():
            janelaerro = tk.Tk()
            janelaerro.title('Você errou!')
            janelaerro.geometry('200x200')
            janelaerro.configure(background='#111111')
            textoerro = Label(janelaerro, text='Sinto muito, você errou!',
                              background='#111111',
                              foreground='white',
                              font=('Bebas Neue',12)
                              )
            button = tk.Button(janelaerro, text='Saiba o porquê.', command=correcao,
                               background='#111111',
                               foreground='white',
                               font=('Bebas Neue',12)
                               )
            textoerro.pack()
            button.pack()
            janelaerro.mainloop()

        if questao == ultimoitem:
            janelaultima = tk.Tk()
            janelaultima.geometry('1366x768')
            janelaultima.title('ultima questao')
            text = Label(janelaultima, text='ultimaquestao')
            urlimagem = urllib.request.urlopen('https://upload.wikimedia.org/wikipedia/commons/thumb/c/c9/-Insert_image_here-.svg/320px--Insert_image_here-.svg.png')
            img = ImageTk.PhotoImage(file=urlimagem,master=janelaultima)
            imagem = Label(janelaultima,image=img)
            text.pack()
            imagem.pack()
            button_1 = tk.Button(janelaultima, text='A)  Alternativa A', command=janelaultima.destroy)
            button_2 = tk.Button(janelaultima, text='B)  Alternativa B', command=perguntaerrada)
            button_3 = tk.Button(janelaultima, text='C)  Alternativa C', command=perguntaerrada)
            button_4 = tk.Button(janelaultima, text='D)  Alternativa D', command=perguntaerrada)
            button_5 = tk.Button(janelaultima, text='E)  Alternativa E', command=perguntaerrada)
            button_1.pack()
            button_2.pack()
            button_3.pack()
            button_4.pack()
            button_5.pack()
            janelaultima.mainloop()
        else:
            janela3 = tk.Tk()
            janela3.title('Pergunta 3')
            janela3.geometry('1366x768')
            urlimagem_1 = urllib.request.urlopen('https://upload.wikimedia.org/wikipedia/commons/thumb/c/c9/-Insert_image_here-.svg/320px--Insert_image_here-.svg.png')
            img_1 = ImageTk.PhotoImage(file=urlimagem_1, master=janela3)
            imagem_1 = Label(janela3, image=img_1)
            imagem_1.pack()
            button_1 = tk.Button(janela3, text='A) Alternativa A', command=janela3.destroy)
            button_2 = tk.Button(janela3, text='B) Alternativa B', command=perguntaerrada)
            button_3 = tk.Button(janela3, text='C) Alternativa C', command=perguntaerrada)
            button_4 = tk.Button(janela3, text='D) Alternativa D', command=perguntaerrada)
            button_5 = tk.Button(janela3, text='E) Alternativa E', command=perguntaerrada)
            button_1.pack()
            button_2.pack()
            button_3.pack()
            button_4.pack()
            button_5.pack()
            janela3.mainloop()

# Função encerramento: Agradecendo aos participantes do questionário:
def encerramento():
    janelaagradecimentos = tk.Tk()
    janelaagradecimentos.title('Obrigado!')
    janelaagradecimentos.geometry('300x300')
    janelaagradecimentos.configure(background='#111111')

    textoagradecimento = Label(janelaagradecimentos,text='Obrigado por participar deste questionário!',
                               background='#111111',
                               foreground='white',
                               font=('Bebas Neue',12))
    botaoencerramento = tk.Button(janelaagradecimentos,text='Clique para encerrar o questionário!',command=exit,
                                  background='#111111',
                                  foreground='white',
                                  font=('Bebas Neue',12))
    textoagradecimento.pack()
    botaoencerramento.pack()
    janelaagradecimentos.mainloop()
encerramento()
