import tkinter as tk
from tkinter import messagebox
import time
from threading import Thread
import threading
import sys

def timer():

    global timerwindow
    timerwindow = tk.Tk()
    timerwindow.title('Tempo restante')
    timerwindow.geometry('200x150')
    timerwindow.configure(background="#111111")
    timerwindow.resizable(False, False)

    alert = tk.Label(timerwindow, text='Tempo restante:', font=("Bebas Neue", 15), background="#111111",
                     foreground='white')
    minutes = tk.Entry(timerwindow, width=3, background="#111111", font=("Bebas Neue", 20),
                       fg="#D0312D")
    sep = tk.Label(timerwindow, text=":", font=('Bebas Neue', 20), background="#111111", fg="#FFFFFF")
    seconds = tk.Entry(timerwindow, width=3, background="#111111", font=("Bebas Neue", 20),
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

    for variableminutes in reversed(range(0,2)):
        
        print(variableminutes)

        if variableminutes <= 10:

            textminute = minutes.insert(tk.END,str('0'+str(variableminutes)))
            timerwindow.update()
            variableminutes = variableminutes - 1

        if variableminutes > 10:

            textminute = minutes.insert(tk.END,str(variableminutes))
            timerwindow.update()
            variableminutes = variableminutes - 1




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

                    seconds.delete(0,tk.END)
                    minutes.delete(0,tk.END)

                    if variableminutes == -1:
                        minutes.delete(0,tk.END)
                        print('timer event is cleared.')
                        timerevent.clear()
                        time.sleep(2)
                        sys.exit()


            else:
                varseconds = second
                textsecond = seconds.insert(tk.END, varseconds)
                timerwindow.update()
                time.sleep(1)
                seconds.delete(0, tk.END)
                timerwindow.update()
                second = second - 1


    timerwindow.mainloop()

timerthread = threading.Thread(target=timer)
timerevent = threading.Event()

timerevent.set()
print('timer event is set!')
if timerevent.is_set():
    timerthread.start()
if timerevent.clear() == True:
    sys.exit()
