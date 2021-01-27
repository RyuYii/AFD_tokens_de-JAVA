from Automata_Finito import AFD


Segundo_ejemplo = {
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
grafo =  AFD(Segundo_ejemplo)
print(grafo)
print(grafo.isAccept('if'))
#print(grafo.isAccept('elfse'))
#print(grafo.isAccept('elsefi'))
#print(grafo.isAccept('karmalanda'))
