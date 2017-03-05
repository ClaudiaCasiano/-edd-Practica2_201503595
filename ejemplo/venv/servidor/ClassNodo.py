from flask import Flash, request, Response
import Nodo
app = flask("E")



Nod = Nodo
class ListaSimple(object):
	def__init__(self):
		self.__primero = None
		self.__ultimo = None
		self.__con = 0

	def esVacio(self):
		if self.__primero== None:
			return True

 	def insertar(self,dato):
 		nuevo = Nod.Nodo(dato)
 		if self.esVacio:
 			self.__primero= self.__ultimo= nuevo
 			self.__con = self.__con+1
 		else
 			self.__ultimo.siguiente= nuevo 
 			self.__ultimo= nuevo
 			self.__con = self.__con+1

 	def eliminar(self, num):
 		temp = self.__primero
 		if self.esVacio:
 			return "Lista vacia"

 	    else if num == 0
 	    	eliminado = self.__primero.getDato
 	    	self.__primero= self.__primero.siguiente
 	    	return "se elimino " + eliminado

 	    else:
 	    	for x in xrange(0,num-1):
 	    		temp = temp.siguiente
 	    	temp.siguiente= temp.siguiente.siguiente

 	    		



	
class Nodo(object):
	
	def__init__(self, dato)
		self.dato = dato 
		self.siguiente = None

	def getDato(self):
		return self.dato