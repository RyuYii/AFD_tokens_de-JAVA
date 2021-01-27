class AFD:
	"""docstring for AFD"""
	def __init__(self, grafo):
		self.alfabeto = grafo['alfabeto']
		self.estados = grafo['estados']
		self.transiciones = grafo['transiciones']
		self.estado_inicial = grafo['estado_inical']
		self.estado_final = grafo['estado_final']

	def isAccept(self, cadena=''):
		if cadena == '':
			print('No data')
			return False
		estadoActual = self.estado_inicial
		print(list(self.transiciones[estadoActual].keys()))
		for letter in cadena:
			try:
				if letter in list(self.transiciones[estadoActual].keys()):
					estadoActual = self.transiciones[estadoActual][letter]
				else:
					return False
			except KeyError:
				print('transicion incorrecta')
				return False

		else:
			if estadoActual in self.estado_final:
				return True
			else:
				print(f'Estado {estadoActual} no aceptado, cadena aceptada')
				return False

	def __str__(self):
		return f' ====== DATOS ========\
		\nAlfabeto:\n{self.alfabeto}\
	\n\nEstados:\n{self.estados}\
	\n\nTransiciones:\n{self.transiciones}\
	\n\nEstado Inicial:\n{self.estado_inicial}\
	\n\nEstados Finales:\n{self.estado_final}'



