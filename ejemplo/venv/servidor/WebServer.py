

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
#	   Esto no deberia de estar ahi, sino que tiene que estar igual de indentado que las demas sentencias.
#
#
#Recomiendo Sublime Text como IDE
#



from flask import Flask, request, Response
from Matriz import Matriz
app = Flask("EDD_codigo_ejemplo")

#Ejemplo de una clase, todos los metodos de las clases deben de tener como parametro el "self", que es como el .this en Java
class Usuario():
    def __init__(self, password, correo, nombre):
        self.nombre = nombre
        self.password = password
        self.correo = correo
        self.matriz = Matriz()

@app.route("/insertar",methods=['POST']) 
def hello1():
	letra = str(request.form['letra'])
	dominio = str(request.form['dominio'])
	nombre = str(request.form['nombre'])

	return 'Se inserto',nombre,'@',dominio
	##insert(parametro, dato2)


@app.route("/dd",methods=['POST']) 
def hello2():
	letra = str(request.form['letra'])
	dominio = str(request.form['dominio'])
	nombre = str(request.form['nombre'])

	matriz.eliminar(letra,dominio,nombre)
	return "Hola " + str(parametro) + "!"
	##insert(parametro, dato2)

@app.route("/e",methods=['POST'])
def hellof():
	return "Hello World2!"


@app.route('/eliminar',methods=['POST']) 
def hello():
	parametro = str(request.form['dato'])
	dato2 = str(request.form['dato2'])
	daton = matriz.eliminar
	return "Hola " + str(parametro) + "!" + daton

if __name__ == "__main__":
  app.run(debug=True, host='0.0.0.0')