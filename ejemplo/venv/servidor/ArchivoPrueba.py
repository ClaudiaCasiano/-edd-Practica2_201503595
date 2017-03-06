import sys

sys.path.append('./')
from Matriz import Matriz
from ColaPila import Pila
from ColaPila import Cola
from ClassNodo import ListaSimple

class Inicio(object):
	"""docstring for Inicio"""
	def __init__(self):
		print 'se inicio======================================================'
		self.comenzar = Matriz()
		self.lista = ListaSimple()
		self.Pla = Pila()
		self.cola = Cola()

	def nuevacosa(self):
		#comenzar = Matriz()
		#comenzar.insert(1,'a.com','ajulia')
		#print '=======se inserto a julia======='
		#comenzar.insert(1,'fs.com','anita')
		#print '=======se inserto a julia======='
		
		self.lista.insertar('palabra1')
		self.lista.insertar('palabra2')
		self.lista.insertar('palabra3')
		self.lista.insertar('palabra4')
		self.lista.imprimir()
		self.lista.eliminar(2)
		print self.lista.buscar('palabra2')
		self.lista.imprimir()
		print ''
		self.Pla.push(5)
		self.Pla.pop()
		self.Pla.pop()
		self.Pla.push(9)
		self.Pla.push(7)
		self.Pla.push(10)
		self.Pla.push(20)
		self.Pla.pop()
		print ''
		self.cola.queue(2)
		self.cola.queue(3)
		self.cola.queue(8)
		self.cola.queue(9)
		self.cola.dequeue()
		self.cola.dequeue()
		self.cola.dequeue()
		self.cola.dequeue()
		self.cola.dequeue()


