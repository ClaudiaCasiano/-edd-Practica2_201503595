
class ListaSimple(object):
	def __init__(self):
		print 'entro a la lista simple'
		self.__primero= None
		self.__con = 0
		self.__ultimo= None

	def esVacio(self):
		if self.__primero== None:
			return True
		else:
			return false

 	def insertar(self,dato):
 		nuevo = Nodo(dato)
 		if self.__primero == None:
 			self.__primero= self.__ultimo= nuevo
 			self.__con = self.__con+1
 			print "se inserto" , str(self.__primero.dato)
 		else:
 			self.__ultimo.siguiente= nuevo 
 			self.__ultimo= nuevo
 			self.__con = self.__con+1
 			print " se inserto "+str(self.__ultimo.dato)
		return " se inserto "+str(self.__ultimo.dato)

 	def eliminar(self, num):
 		no = int(num)
 		temp = self.__primero
 		if self.__primero ==None:
 			return "Lista vacia"
		if no == 0:
			eliminado = self.__primero.getDato
			self.__primero= self.__primero.siguiente
			print 'se eliminio ', eliminado
			return "se elimino " + str(eliminado)
		else:
			for x in xrange(0,no-1):
				temp = temp.siguiente
				print 'se eliminio ',  temp.siguiente.dato
			temp.siguiente= temp.siguiente.siguiente

		return "indice excede el limite"


 	def imprimir(self):
 		if self.__primero==None:
 			print 'la lista esta vacia'
 			return "lista Vacia"
 		else:
 			a = str(self.__primero.dato) + ";"
 			aux = self.__primero.siguiente
 			
 			while aux.siguiente!= None:
 				a=a+ str(aux.dato)+";"
 				a=a+ str(aux.dato)+" -> "+ str(aux.siguiente.dato)+ ";"
 				print aux.dato
 				aux = aux.siguiente
			return str(a)

	def buscar(self, palabra):
		cont = 0
		if self.__primero ==None:
			return "Lista vacia"
		else:
			aux = self.__primero
			while aux!=None:
				if aux.dato == palabra:
					print 'Se encontro', palabra
					return "Se encontro "+str(palabra)+ " en el indice ",str(cont)
				else:
					aux = aux.siguiente
					cont = cont + 1

			return "no se encontro palabra "

 	    		



	
class Nodo(object):
	
	def __init__(self, dato):
		self.dato = dato 
		self.siguiente = None

	def getDato(self):
		return self.dato