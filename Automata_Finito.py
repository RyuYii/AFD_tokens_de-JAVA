class AFND:
	def __init__(self, grafo):
		self.alfabeto = grafo['alfabeto']
		self.estados = grafo['estados']
		self.transiciones = grafo['transiciones']
		self.estado_inicial = grafo['estado_inical']
		self.estado_final = grafo['estado_final']

	def checkLetter(self, actualState, letter):
		print(self.transiciones[actualState].keys())
		print('-'*50)
		for value in self.transiciones[actualState].keys():
			print(self.transiciones[actualState][value])
			print()
			if letter in self.transiciones[actualState][value]:
				print('\t'+value)
				return value
		else:
			return ''

	def checkword(self, word):
		actualState = self.estado_inicial
		for letter in word:
			NextState = self.checkLetter(actualState, letter)
			#print(NextState)
			if not NextState == '':
				 actualState = NextState
				 #print(actualState)
			else:
				actualState = self.estado_inicial
				break
		print(self.estado_final.keys())
		if actualState in self.estado_final.keys():
			return(f'Palabra: \t{word} es un numero {self.estado_final[actualState]}\n')
		else:
			return(f'Palabra: \t{word} no aceptada\n')
		

	def isAccept(self, cadena=''):
		cad = ''
		if(type(cadena) == str):
			cadena = cadena.split(' ')
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