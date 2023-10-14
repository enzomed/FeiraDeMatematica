import cv2
import tkinter as tk
from tkinter import *
import random
import PIL
from PIL import Image,ImageTk
from tkinter import ttk
from tkinter.ttk import Label
import urllib
import urllib.request

##IMPORTANTE (LEIA POR FAVOR): AS IMAGENS NÃO SERÃO MOSTRADAS, POIS É NECESSÁRIO QUE MUDE O CAMINHO DELAS NO SEU
#COMPUTADOR.

##Não estive muito preocupado em fazer as 8 funções para as perguntas, pois é só a versão beta.

##Definição de variáveis:
pergunta = random.randint(1,3)
global_image_list = ['C:/Users/Nathaen/Downloads/mathchalkboard.webp','C:/Users/Nathaen/Downloads/Trollface.png']


## Janela principal do programa, introdução.
janelaprincipal = tk.Tk()
urlimagemprincipal = urllib.request.urlopen('https://i.pinimg.com/originals/43/d6/82/43d682282bc59ed8c21b448a6120277f.png')
imgtk = ImageTk.PhotoImage(file=urlimagemprincipal,master=janelaprincipal)
janelaprincipal.title('Projeto Feira (VERSÃO BETA)')
janelaprincipal.geometry('1366x768')

texto1 = Label(janelaprincipal, text='Bem vindo ao Projeto da Feira de Matemática!')
texto2 = Label(janelaprincipal, text='Um projeto realizado pela turma do 3°B!')

Label(janelaprincipal,image=imgtk).pack()
texto1.pack(ipadx=10,ipady=10)
texto2.pack(ipadx=10,ipady=20)

##Definição de funções:

##Função pergunta 1:
def pergunta1():
    perguntas0 =[pergunta2, pergunta3]
    janela1 = tk.Tk()
    janela1.title('Pergunta 1')
    janela1.geometry('1366x768')
    urlimagem1 = urllib.request.urlopen('https://images.educamaisbrasil.com.br/content/banco_de_imagens/eb-educacao/D/questoes-de-matematica-do-enem.JPG')
    img1 = ImageTk.PhotoImage(file=urlimagem1,master=janela1)
    imagem1 = Label(janela1, image=img1)
    imagem1.pack()
    button2 = tk.Button(janela1,text='Clique para ver a próxima pergunta.',command=random.choice(perguntas0))
    button2.pack()
    janela1.mainloop()
##Função pergunta 2:
def pergunta2():
    perguntas1 =[pergunta1, pergunta3]
    janela2 = tk.Tk()
    janela2.title('Pergunta 2')
    janela2.geometry('1366x768')
    urlimagem2 = urllib.request.urlopen('https://images.educamaisbrasil.com.br/content/banco_de_imagens/eb-educacao/D/enemmatematica.jpg')
    img2 = ImageTk.PhotoImage(file=urlimagem2,master=janela2)
    imagem2 = Label(janela2, image=img2)
    imagem2.pack()
    button3 = tk.Button(janela2,text='Clique para ver a próxima pergunta.',command=random.choice(perguntas1))
    button3.pack()
    janela2.mainloop()
##Função pergunta 3:
def pergunta3():
    perguntas2 = [pergunta1, pergunta2]
    janela3 = tk.Tk()
    janela3.title('Pergunta 3')
    janela3.geometry('1366x768')
    urlimagem3 = urllib.request.urlopen('https://images.educamaisbrasil.com.br/content/banco_de_imagens/eb-educacao/D/questoes-de-matematica-do-enem-e-o-que-mais-cai-nessa-disciplina.JPG')
    img3 = ImageTk.PhotoImage(file=urlimagem3, master=janela3)
    imagem3 = Label(janela3,image=img3)
    imagem3.pack()
    button4 = tk.Button(janela3,text='Clique para ver a próxima pergunta.',command=random.choice(perguntas2))
    button4.pack()
    janela3.mainloop()


##Função do botão de início (tela inicial):
def firstbuttoncallback():
    pergunta = random.randint(1,3)
    if pergunta == 1:
        pergunta1()
    elif pergunta == 2:
        pergunta2()
    elif pergunta == 3:
        pergunta3()

def creditos():
    janelacreditos = tk.Tk()
    janelacreditos.title('Créditos')
    janelacreditos.geometry('1366x768')
    textocreditos = Label(janelacreditos,text='Criação do modelo do código feita por Enzo F.')
    textocreditos1 = Label(janelacreditos,text="Equipe de programação: Enzo Fernandes, Kleber Rogério, Paulo Roberto, Gabryel Pereira, Leandro Kenji")
    urlimagemgrupo = urllib.request.urlopen('https://s3.dualstack.us-east-2.amazonaws.com/pythondotorg-assets/media/community/logos/python-logo-only.png')
    imagemgr = ImageTk.PhotoImage(file=urlimagemgrupo,master=janelacreditos)
    imagemgrupo = Label(janelacreditos, image=imagemgr)
    textocreditos.pack()
    textocreditos1.pack()
    imagemgrupo.pack()
    janelacreditos.mainloop()



#Modelo a seguir:
#elif pergunta == 8:
#janela8 = tk.Tk()
#janela8.title("Pergunta 2")
#janela8.geometry('1366x768')
#imagem2 = ImageTk.PhotoImage(file='C:/Users/Nathaen/Downloads/memeface1.png', master=janela8)
#lbimagem1 = Label(janela8, image=imagem2)
#lbimagem1.pack()
#janela8.mainloop()


##Botão de início

button1 = tk.Button(janelaprincipal,text="Clique para começar!",command=firstbuttoncallback)
button1.pack(ipadx=0,ipady=10)

buttoncredits = tk.Button(janelaprincipal,text='Créditos',command=creditos)
buttoncredits.pack(ipadx=600,ipady=10)









janelaprincipal.mainloop()
