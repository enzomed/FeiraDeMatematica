import tkinter as tk
from tkinter import messagebox
import time
from threading import Thread

def timer():

    global timerwindow
    timerwindow = tk.Tk()
    timerwindow.title('Tempo restante')
    timerwindow.geometry('200x150')
    timerwindow.configure(background="#111111")
    timerwindow.resizable(False, False)

    varminutes = tk.StringVar()
    varseconds = tk.StringVar()

    alert = tk.Label(timerwindow, text='Tempo restante:', font=("Bebas Neue", 15), background="#111111",
                     foreground='white')
    minutes = tk.Entry(timerwindow, textvariable=varminutes, width=3, background="#111111", font=("Bebas Neue", 20),
                       fg="#D0312D")
    sep = tk.Label(timerwindow, text=":", font=('Bebas Neue', 20), background="#111111", fg="#FFFFFF")
    seconds = tk.Entry(timerwindow, textvariable=varseconds, width=3, background="#111111", font=("Bebas Neue", 20),
                       fg="#D0312D")

    alert.pack()

    minutes.pack()
    minutes.place(x=60, y=75)
    sep.pack()
    sep.place(x=102, y=75)
    seconds.pack()
    seconds.place(x=120, y=75)

    ## Main for loop:

    loop = 0

    '''A variável loop é incrementada (acresida de uma unidade) toda vez que 1 minuto se passa.
       É a variável responsável por ajustar o ponteiro dos minutos.'''

    while loop <= 3:

        if loop == 0:
            minute = 2
            varminutes = minute
            textminute = minutes.insert(tk.END, str('0' + str(varminutes)))
            timerwindow.update()

        elif loop == 1:
            minutes.delete(0, tk.END)
            minute = 1
            varminutes = minute
            textminute = minutes.insert(tk.END, str('0' + str(varminutes)))
            timerwindow.update()

        elif loop == 2:
            minutes.delete(0, tk.END)
            minute = 0
            varminutes = minute
            textminute = minutes.insert(tk.END, str('0' + str(varminutes)))
            timerwindow.update()

        elif loop == 3:
            minutes.delete(varminutes, tk.END)
            seconds.delete(varseconds, tk.END)
            timerwindow.update()
            timesup = tk.messagebox.showinfo('Fim de jogo!', 'O tempo acabou!')
            time.sleep(3)
            timerwindow.destroy()




        for second in reversed(range(1, 60)):

            '''Se o display dos segundos estiver no intervalo (0 < x < 10), o display mostrará "0x".
            Caso contrário, o display mostrará "xy", onde x e y são números naturais nesse intervalo descrito
             anteriormente.'''

            if second in reversed(range(-1, 10)):
                varseconds = second
                textsecond = seconds.insert(tk.END, str('0' + str(varseconds)))
                timerwindow.update()
                time.sleep(1)
                seconds.delete(0, tk.END)
                timerwindow.update()
                second = second - 1

                '''Quando o ponteiro dos segundos der 0, o loop será incrementado.'''

                if second == 0:
                    print('before loop update: {}'.format(loop))
                    loop = loop + 1
                    print('after loop update: {}'.format(loop))


            else:
                varseconds = second
                textsecond = seconds.insert(tk.END, varseconds)
                timerwindow.update()
                time.sleep(1)
                seconds.delete(0, tk.END)
                timerwindow.update()
                second = second - 1


    timerwindow.mainloop()

timer()
