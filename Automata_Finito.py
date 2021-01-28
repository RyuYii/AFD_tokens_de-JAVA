class AFND:
	def __init__(self, grafo):
		self.alfabeto = grafo['alfabeto']
		self.estados = grafo['estados']
		self.transiciones = grafo['transiciones']
		self.estado_inicial = grafo['estado_inical']
		self.estado_final = grafo['estado_final']

	def checkLetter(self, actualState, letter):
		for value in self.transiciones[actualState].keys():
			if letter in self.transiciones[actualState][value]:
				return value
		else:
			return ''

	def checkword(self, word):
		actualState = self.estado_inicial
		for letter in word:
			NextState = self.checkLetter(actualState, letter)
			if not NextState == '':
				 actualState = NextState
			else:
				actualState = self.estado_inicial
				break
		if actualState in self.estado_final.keys():
			print(f'Palabra: \t{word} es un numero {self.estado_final[actualState]}')
		else:
			print(f'Palabra: \t{word} no aceptada')
		

	def isAccept(self, cadena=''):
		if(type(cadena) == str):
			cadena = cadena.split(' ')
		if cadena == '':
			print('No data')
		for word in cadena:	
			self.checkword(word)
			


	def __str__(self):
		return f' ====== DATOS ========\
		\nAlfabeto:\n{self.alfabeto}\
	\n\nEstados:\n{self.estados}\
	\n\nTransiciones:\n{self.transiciones}\
	\n\nEstado Inicial:\n{self.estado_inicial}\
	\n\nEstados Finales:\n{self.estado_final}'