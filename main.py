# -*- coding: utf-8 -*-
from Automata_Finito import AFD
from tkinter import *
from tkinter import ttk
from tkinter import scrolledtext
import time
# La clase 'Aplicacion' ha crecido. En el ejemplo se incluyen
# nuevos widgets en el método constructor __init__(): Uno de
# ellos es el botón 'Info'  que cuando sea presionado llamará 
# al método 'verinfo' para mostrar información en el otro 
# widget, una caja de texto: un evento ejecuta una acción: 

class Aplicacion():
    def __init__(self):
        
        self.raiz = Tk()
        self.raiz.geometry('600x500')
        self.cont = 0
        #self.raiz.resizable(width=False,height=False)
        self.raiz.title('Ver info')
        self.grafo = ''



        Label(self.raiz, 
            text="Validador de sintaxis").grid(row=0)
        Label(self.raiz, 
            text="code:      ").grid(row=1)
        Label(self.raiz, 
            text="status:    ").grid(row=2)


        #input para cadenas
        self.e1 = Entry(self.raiz) 
        self.e1.grid(row=1, column=1)
        self.e1['width']=40
        
        
        self.tinfo = scrolledtext.ScrolledText(self.raiz)
        self.tinfo.grid(row=2, column=1) 
        self.tinfo['width']=40
        self.tinfo['height']=5 
        '''    
        self.btnshow = Button(self.raiz, 
                                text='Quit', 
                                command=self.raiz.quit).grid(row=3, 
                                                            column=0, 
                                                            sticky=W, 
                                                            pady=4)
        '''
        self.btn = Button(self.raiz)
        self.btn['text'] = "Iniciar"
        self.btn.grid(row=4,column=0)
        self.btn['command'] = self.show

        self.btnQ = Button(self.raiz)
        self.btnQ['text'] = "Salir"
        self.btnQ.grid(row=4,column=1)
        self.btnQ['command'] = self.raiz.quit

        '''
        self.btnquit = Button(self.raiz, 
                                text='Show',
                                command=self.show).grid(row=3, 
                                                                    column=1, 
                                                                    sticky=W, 
                                                                    pady=4)
        '''
        
    
    def show(self):
        #self.tinfo.delete('1.0')

        cad = f'Test #{self.cont}\n\n'
        cad += f'entrada: {self.e1.get()}\n\n'
        cad += 'salida: '+self.grafo.isAccept(self.e1.get())
        self.tinfo.insert('1.0',f'{cad}\n\n')
        print(self.grafo.isAccept('if'))
        self.e1.delete('0', END)
        self.cont+=1

    def add_grafo(self, grafo):
        self.grafo = grafo
    
        


def main():
    ejemplo = {
        'alfabeto':['i','f','t','h','e','n','l','s'],
        'estados':['q0','q1','q2','q3','q4','q5','q6','q7','qf'],
        'transiciones':{
            'q0'	:{'i':'q1','e':'q2','t':'q3'},
            'q1'	:{'f':'qf'},
            'q2'	:{'l':'q4'},
            'q4'	:{'s':'q5'},
            'q5'	:{'e':'qf'},
            'q3'	:{'h':'q6'},
            'q6'	:{'e':'q7'},
            'q7'	:{'n':'qf'}
        },
        'estado_inical':'q0',
        'estado_final':['qf']
    }
    grafo =  AFD(ejemplo)
    app = Aplicacion()
    app.add_grafo(grafo)
    app.raiz.mainloop()
    return 0

if __name__ == '__main__':
    main()