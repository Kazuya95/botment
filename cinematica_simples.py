# GUI para simular
import numpy as np                           # funcoes trigonometricas
import matplotlib.pyplot as plt              # parte grafica
from tkinter import *


# captar o comprimento dos links e os angulos
def dots_coordenate(L1,L2,angulo1,angulo2):
    theta1,theta2 = angulo1*np.pi/180,angulo2*np.pi/180 # em radiano
    dots = {'p0':[0,0],
            'p1':[round(L1*np.cos(theta1),2),round(L1*np.sin(theta1),2)],
            'p2':[round(L1*np.cos(theta1),2)+round(L2*np.cos(theta1+theta2),2),
                  round(L1*np.sin(theta1),2)+round(L2*np.sin(theta1+theta2),2)]}
    return dots

def interface():
    window = Tk()
    window.title('2D arm robot')
    window.geometry('300x180')
    
    # frame for screen and control
    noname_frame = Frame()
    noname_frame.grid(row=0,column=1)
    
    # frame for screen
    screen_frame=Frame(noname_frame,width=50,height=20)
    screen_frame.grid(row=0,column=1)
    
    # frame for control
    control_frame=Frame(noname_frame)
    control_frame.grid(row=1,column=1)

    screen_message = Label(screen_frame,width=40,height=5,text='',bg='orange',bd=9)
    screen_message.grid(row=1,column=0)
    screen_message['text']='''For L1 and L2, write in 'cm',\nfor angles, use degree.'''

    # texto para indicar onde colocar os dados e a recepcao de dados
    link1 = Label(control_frame,text = 'L1')
    link1.grid(row=0,column=0)
    link1_receber = Entry(control_frame,width=8)
    link1_receber.grid(row=0,column=1)
    
    link2 = Label(control_frame,text = 'L2')
    link2.grid(row=1,column=0)
    link2_receber = Entry(control_frame,width=8)
    link2_receber.grid(row=1,column=1)
    
    theta1 = Label(control_frame,text = 'Theta1')
    theta1.grid(row=0,column=2)
    theta1_receber = Entry(control_frame,width=8)
    theta1_receber.grid(row=0,column=3)
    
    theta2 = Label(control_frame,text = 'Theta2')
    theta2.grid(row=1,column=2)
    theta2_receber = Entry(control_frame,width=8)
    theta2_receber.grid(row=1,column=3)
    
    def _quit():
        plt.close()
        window.destroy()  # this is necessary on Windows to prevent
                          # Fatal Python Error: PyEval_RestoreThread: NULL tstate
    def msg():
        screen_message['text'] = '''Testing this orange rectangle.\n It's look ok'''

    def update():
        plt.clf()
        try:
            L1 = float(link1_receber.get())
            L2 = float(link2_receber.get())
            angulo1 = float(theta1_receber.get())
            angulo2 = float(theta2_receber.get())
            screen_message['text'] = 'L1: {}, L2: {}\nT1: {}, T2: {}'.format(L1,L2,angulo1,angulo2)
            dots = dots_coordenate(L1,L2,angulo1,angulo2)
            x,y=[],[]
            for key,values in dots.items():
                x.append(dots[key][0])
                y.append(dots[key][1])
            limites = [-50, 50, -50, 50] # xmin,xmax,ymin,ymax
            plt.axis(limites)
            plt.plot(x,y,marker='o')
            plt.show()
        except:
            screen_message['text'] = 'Lacunas vazias, por favor preenchê-las.'
        

    button = Button(master=control_frame, text="Quit", command=_quit)
    button.grid(row=9,column=0)
    
    testing_screen = Button(control_frame, text="Testing",command=msg)
    testing_screen.grid(row=9,column=1)

    reload_graph = Button(control_frame, text="Reload",command=update)
    reload_graph.grid(row=9,column=2)

    window.mainloop()

interface()
