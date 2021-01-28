#!/usr/bin/python3
# -*- coding: utf-8 -*-
from Automata_Finito import AFND
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
        #self.raiz.geometry('600x500')
        self.cont = 0
        #self.raiz.resizable(width=False,height=False)
        self.raiz.title('AFND')
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
        self.e1['width']=61
        
        
        self.tinfo = scrolledtext.ScrolledText(self.raiz)
        self.tinfo.grid(row=2, column=1) 
        self.tinfo['width']=60
        self.tinfo['height']=15 
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
        cad += 'salida: \n'+self.grafo.isAccept(self.e1.get())
        self.tinfo.insert('1.0',f'{cad}\n\n')
        #print(self.grafo.isAccept('if'))
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
    # Ejemplo de Entrada 

    ejemplo_RealEntero = {
        'alfabeto':['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','$','_','0','1','2','3','4','5','6','7','8','9','!','@','#','$','%','^','&'],
        'estados':['q0','q1','q2','q3','q4','q5','q6','q7','q8','q9','q10','q11','q12','q13','q14','q15','q16','q17','q18','q19','q20','q21','q22','q23','q24','q25','q26','q27','q28','q29','q30','q31','q32','q33','q34','q35','q36','q37','q38','q39','q40','q41','q42','q43','q44','q45','q46','q47','q48','q49','q50','q51','q52','q53','q54','q55','q56','q57','q58','q59','q60','q61','q62','q63','q64','q65','q66','q67','q68','q69','q70','q71','q72','q73','q74','q75','q76','q77','q78','q79','q80','q81','q82','q83','q84','q85','q86','q87'],
        'transiciones':{
            'q0':{'q1':['/','+','*','-','|','&','^'],
                'q2':['>'],
                'q3':['<'],
                'q4':['>'],
                'q69':['e'],
                'q6':['='],
                'q7':['0','1','2','3','4','5','6','7','8','9','-'],
                'q9':['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','$','_'],
                'q12':['t'],
                'q19':['f'],
                'q24':['m'],
                'q28':['e'],
                'q35':['d'],
                'q41':['S'],
                'q47':['b'],
                'q54':['s'],
                'q59':['i'],
                'q62':['c'],
                'q66':['n'],
                'q84':['+'],
                'q11':['-'],
                },
            'q1':{'q6':['=']},
            'q2':{'q1':['>']},
            'q3':{'q1':['<']},
            'q4':{'q5':['>']},
            'q5':{'q1':['>']},
            'q6':{'q10':['_']},
            'q7':{'q8':['.'],
                'q7':['0','1','2','3','4','5','6','7','8','9']
                },
            'q8':{'q69':['0','1','2','3','4','5','6','7','8','9']},
            'q9':{'q9':['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','$','_','0','1','2','3','4','5','6','7','8','9','!','@','#','$','%','^','&'],
                'q70':['_']
                },
            'q11':{'q83':['-']},
            'q12':{'q13':['r'],
                'q16':['h']},
            'q13':{'q14':['u']},
            'q14':{'q15':['e']},
            'q15':{'q71':['_']},
            'q16':{'q17':['i']},
            'q17':{'q18':['s']},
            'q18':{'q72':['_']},
            'q19':{'q20':['a']},
            'q20':{'q21':['l']},
            'q21':{'q22':['s']},
            'q22':{'q23':['e']},
            'q23':{'q73':['_']},
            'q24':{'q25':['a']},
            'q25':{'q26':['i']},
            'q26':{'q27':['n']},
            'q27':{'q74':['_']},
            'q28':{'q29':['x']},
            'q29':{'q30':['t']},
            'q30':{'q31':['e']},
            'q31':{'q32':['n']},
            'q32':{'q33':['d']},
            'q33':{'q34':['s']},
            'q34':{'q75':['_']},
            'q35':{'q36':['o']},
            'q36':{'q37':['u']},
            'q37':{'q38':['b']},
            'q38':{'q39':['l']},
            'q39':{'q40':['e']},
            'q40':{'q76':['_']},
            'q41':{'q42':['t']},
            'q42':{'q43':['r']},
            'q43':{'q44':['i']},
            'q44':{'q45':['n']},
            'q45':{'q46':['g']},
            'q46':{'q77':['_']},
            'q47':{'q48':['o']},
            'q48':{'q49':['o']},
            'q49':{'q50':['l']},
            'q50':{'q51':['e']},
            'q51':{'q52':['a']},
            'q52':{'q53':['n']},
            'q53':{'q78':['_']},
            'q54':{'q55':['w']},
            'q55':{'q56':['i']},
            'q56':{'q57':['t']},
            'q57':{'q58':['c']},
            'q58':{'q79':['h']},
            'q79':{'q88':['_']},
            'q59':{'q60':['n']},
            'q60':{'q61':['t']},
            'q61':{'q80':['_']},
            'q62':{'q63':['a']},
            'q63':{'q64':['s']},
            'q64':{'q65':['e']},
            'q65':{'q81':['_']},
            'q66':{'q67':['e']},
            'q67':{'q68':['w']},
            'q68':{'q82':['_']},
            'q83':{'q87':['_']}, 
            'q84':{'q85':['+']},
            'q85':{'q86':['_']},
            'q69':{'q69':['0','1','2','3','4','5','6','7','8','9']},
        },
        'estado_inical':'q0',
        'estado_final':{
            'q7':'Numero Entero',
            'q10':'Operador de Asignacion',
            'q69':'Numero Real',
            'q70':'Identificador',
            'q71':'true_',
            'q72':'this_',
            'q73':'false_',
            'q74':'main_',
            'q75':'extends_',
            'q76':'double_',
            'q77':'String_',
            'q78':'boolean_',
            'q79':'switch',
            'q80':'int',
            'q81':'case_',
            'q82':'new_',
            'q86':'incremento',
            'q87':'decremento'

        }
    }
    
    grafo =  AFND(ejemplo_RealEntero)

    app = Aplicacion()
    app.add_grafo(grafo)
    app.raiz.mainloop()
    return 0

if __name__ == '__main__':
    main()
    