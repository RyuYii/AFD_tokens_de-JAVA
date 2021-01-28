class AFND:
	def __init__(self, grafo):
		self.alfabeto = grafo['alfabeto']
		self.estados = grafo['estados']
		self.transiciones = grafo['transiciones']
		self.estado_inicial = grafo['estado_inical']
		self.estado_final = grafo['estado_final']

	def checkLetter(self, actualState, letter):
		print('-'*50)
		states = []
		try:
			for value in self.transiciones[actualState].keys():
				if letter in self.transiciones[actualState][value]:
					print('\t'+value)
					states.append(value)
			return states
		except KeyError:
			return states

	def efe(self, pila, word):
		if not pila :
			return False, ''
		else:
			#print(pila)
			#print('-'*50)
			actualState = pila.pop()
			for letter in range(len(word)):
				NextState = self.checkLetter(actualState, word[letter])
				#print(NextState)
				if len(NextState) >= 2:
					try:
						return self.efe(NextState, word[letter+1:])
					except:
						return False, ''
				elif len(NextState) == 1:
					actualState = NextState[0]
				elif len(NextState) == 0 and len(pila) != 0 : 
					return self.efe(pila, word)
				else:
					actualState = self.estado_inicial
					break
			if actualState in self.estado_final.keys():
				return True, actualState
			else:
				return False, ''

	def checkword(self, word):
		actualState = self.estado_inicial
		val, NextState = self.efe(self.checkLetter(actualState, word[0]),word[1:])

		print(f'ultimo {NextState}')
		if val:
			return(f'Palabra: \t{word} es un {self.estado_final[NextState]}\n')
		else:
			return(f'Palabra: \t{word} no aceptada\n')
		

	def isAccept(self, cadena=''):
		cad = ''
		if(type(cadena) == str):
			cadena = cadena.rstrip().split()
			print(cadena)
		if cadena == '':
			print('No data')
		for word in cadena:	
			cad += self.checkword(word)
		return cad	


	def __str__(self):
		return f' ====== DATOS ========\
		\nAlfabeto:\n{self.alfabeto}\
	\n\nEstados:\n{self.estados}\
	\n\nTransiciones:\n{self.transiciones}\
	\n\nEstado Inicial:\n{self.estado_inicial}\
	\n\nEstados Finales:\n{self.estado_final}'