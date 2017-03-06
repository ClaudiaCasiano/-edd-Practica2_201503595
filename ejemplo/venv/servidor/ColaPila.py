class Nodo(object):
	
	def __init__(self, dato):
		self.dato = dato 
		self.siguiente = None

	def getDato(self):
		return self.dato

class Pila(object):
	def __init__(self):
		print 'entor a pila'

		self.arriba = None
		self.abajo = None

	def push(self,dato):
		nuevo = Nodo(dato)
		if self.arriba == None:
			self.arriba = nuevo
		else:
			nuevo.siguiente = self.arriba
			self.arriba = nuevo
		print 'se inserto' ,nuevo.dato
		return "se inserto " + str(nuevo.dato)

	def pop(self):
		if self.arriba == None:
			print 'pila vacia'
			return 'pila vacia'
		print 'se saco', self.arriba.dato

		if self.arriba == self.abajo:
			self.abajo = None
			self.arriba = None
			print 'se vacio pila'
			return 'se vacio pila'
		self.arriba = self.arriba.siguiente
		if self.arriba != None:
			return "ahora el de arriba es"+ str( self.arriba.dato)
		else:
			return "no hay ni mais :v"
		

	def imprimir(self):

		if self.arriba != None:
			aux = self.arriba
			ann = str(self.arriba.dato)+ ";"

		while aux.siguiente != None:
			ann = ann + str(aux.siguiente.dato)+";"
			ann = ann + str(aux.dato)+ " -> " + str(aux.siguiente.dato) + ";"
			aux = aux.siguiente

		return str(ann)


class Cola(object):
	def __init__(self):
		print 'entor a Cola '

		self.first = None
		self.last = None

	def queue(self,dato):
		nuevo = Nodo(dato)
		if self.first == None:
			self.first = nuevo
			self.last = self.first
			self.first.siguiente = self.last
		else:
			self.last.siguiente = nuevo
			self.last = nuevo
		print 'se inserto', self.last.dato
		return "se inserto " + str(nuevo.dato)

	def dequeue(self):
		if self.first == None:
			print 'cola vacia'
			return 'cola vacia'
		print 'se saco', self.first.dato
		if self.first == self.last:
			self.first = None
			self.last = None
			print 'se vacio cola'
			return 'se vacio cola'
		self.first = self.first.siguiente
		print 'ahora el primero es', self.first.dato
		return "ahora el primero ess "+  str(self.first.dato)

	def imprimir(self):
		if self.first != None:
			aux = self.first
			ann = str(self.first.dato)+ ";"

		while aux.siguiente != None:
			print 'quee'
			ann = ann + str(aux.siguiente.dato)+";"
			ann = ann + str(aux.dato)+ " -> " + str(aux.siguiente.dato) + ";"
			aux = aux.siguiente
		print ann

		return str(ann)

