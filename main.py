# -*- coding: utf-8 -*-
from Automata_Finito import AFD
from tkinter import *
from tkinter import ttk

# La clase 'Aplicacion' ha crecido. En el ejemplo se incluyen
# nuevos widgets en el método constructor __init__(): Uno de
# ellos es el botón 'Info'  que cuando sea presionado llamará 
# al método 'verinfo' para mostrar información en el otro 
# widget, una caja de texto: un evento ejecuta una acción: 

class Aplicacion():
    def __init__(self):
        
        self.raiz = Tk()
        self.raiz.geometry('600x500')
        
        #self.raiz.resizable(width=False,height=False)
        self.raiz.title('Ver info')
        



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
        

        self.tinfo = Text(self.raiz)
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
        self.raiz.mainloop()
    
    def show(self):
        self.tinfo.insert("1.0", f'{self.e1.get()}\n')
        print(f"First Name: {self.e1.get()}")

    def add_grafo(self, grafo):
        pass


def main():
    mi_app = Aplicacion()
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
    print(grafo)
    print(grafo.isAccept('if'))
    return 0

if __name__ == '__main__':
    main()