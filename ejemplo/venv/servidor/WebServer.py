

#Si mientras trabajan en Python alguna vez les arroja un "IndentationError" es porque en alguna linea, los tabs al inicio de la sentencia estan erroneos, por ejemplo:
#Esto es valido:
#class Usuario():
#	def __init__(self, nombre):
#		self.nombre = nombre
#		self.password = password
#Esto NO es valido y arroja un "IndentationError":
#class Usuario():
#	def __init__(self, nombre):
#		self.nombre = nombre
#	   self.password = password
#	   ^
#	   Esto no deberia  de estar ahi, sino que tiene que estar igual de indentado que las demas sentencias.
#
#
#Recomiendo Sublime Text como IDE
#



from flask import Flask, request, Response
from Inicializar import Inicializar
from ClassNodo import ListaSimple
from ColaPila import Pila
from ColaPila import Cola
from Matriz import Matriz
app = Flask("EDD practica2")


accion = Inicializar()
cola = Cola()
pila = Pila()
lista = ListaSimple()
matriz = Matriz()

#Ejemplo de una clase, todos los metodos de las clases deben de tener como parametro el "self", que es como el .this en Java
class Usuario():
    def __init__(self):
    	print 'ha entrado al server'
        self.accion = Inicializar()


#HACER LOS METODOS :V

#=============METODO PILA============
@app.route('/push',methods=['POST']) 
def hellos():
	accion = Inicializar()
	dato = str(request.form['dato'])
	mns = pila.push(dato)
	return mns

@app.route('/pop',methods=['POST']) 
def pop():
	mns = pila.pop()
	return mns

@app.route('/printpila',methods=['POST']) 
def pp():
	mns = pila.imprimir()
	return mns


#=================METODOS COLA============
@app.route('/queue',methods=['POST']) 
def queue():
	dato = str(request.form['dato'])
	mns = cola.queue(dato)
	return mns

@app.route('/dequeue',methods=['POST']) 
def dequeue():
	mns = cola.dequeue()
	return mns

@app.route('/printcola',methods=['POST']) 
def pca():
	mns = cola.imprimir()
	return mns

#================MMETODO LISTA==============
@app.route('/printlista',methods=['POST']) 
def printl():
	mns = lista.imprimir()
	return mns

@app.route('/addlista',methods=['POST']) 
def addL():
	dato = str(request.form['dato'])
	mns = lista.insertar(dato)
	return mns

@app.route('/delelista',methods=['POST']) 
def delL():
	dato = str(request.form['num'])
	mns = lista.eliminar(dato)
	return mns

@app.route('/buscarLi',methods=['POST'])
def busl():
	dato = str(request.form['dato'])
	msn = lista.buscar(dato)
	return msn
#==============METODO MATRIZ==============


@app.route("/insertM", methods = ['POST'])
def instM():
	letra = request.form['letra']
	dominio = str(request.form['dominio'])
	nombre = str(request.form['nombre'])
	N = str(matriz.insert(letra,dominio,nombre))
	return N

@app.route("/printM", methods = ['POST'])
def printM():
	N = str(matriz.imprimir())
	return N

@app.route('/eliminarM', methods = ['POST'])
def eliminarM():
	print 'va a eliminar'
	letra = request.form['letra']
	dominio = str(request.form['dominio'])
	nombre = str(request.form['nombre'])
	n = matriz.eliminar(letra,dominio,nombre)
	return str(n)

@app.route('/buscarl', methods = ['POST'])
def buscarl():
	letra = request.form['letra']
	n = matriz.letra(letra)
	return str(n)

@app.route('/BuscarDominio', methods = ['POST'])
def buscarn():
	letra = request.form['dominio']
	n = matriz.dominio(letra)
	return str(n)


@app.route("/inicializar",methods=['POST'])
def hellof():
	n = Usuario()
	return "Hello World2!"




if __name__ == "__main__":
  app.run(debug=True, host='0.0.0.0')