from ClassNodo import ListaSimple
from ColaPila import Pila
from ColaPila import Cola
from Matriz import Matriz
class Inicializar(object):
	"""docstring for Inicializar """
	def __init__(self):
		self.matriz = Matriz()
		self.pila = Pila()
		self.cola = Cola()
		self.lista = ListaSimple()

	def insertarMatriz(self,letra,dominio,nombre):
		self.matriz.insert(letra,dominio,nombre)


	def eliminarMatriz(self,letra,dominio,nombre):
		self.matriz.eliminar(letra,dominio,nombre)


	def filaMatriz(self,letra):
		self.matriz.letra(letra)


	def columnaMatriz(self,dominio):
		self.matriz.dominio(dominio)


	def addLista(self,dato):
		self.lista.insertar(dato)


	def borrarLista(self,indice):
		self.lista.eliminar(indice)
		

	def findLista(self,dato):
		self.lista.buscar(dato)
	
	def push(self,dato):
		self.pila.push(dato)


	def pop(self):
		self.pila.pop()


	def queue(self,dato):
		self.cola.queue(dato)


	def dequeue(self):
		self.cola.pop()





		