import sys

sys.path.append('./')
from Matriz import Matriz

class Inicio(object):
	"""docstring for Inicio"""
	def __init__(self):
		self.comenzar = Matriz()

	def nuevacosa(self):
		comenzar = Matriz()
		comenzar.insert(1,'a.com','ajulia')
		print '=======se inserto a julia======='
		comenzar.insert(1,'fs.com','anita')
		print '=======se inserto a julia======='
		comenzar.insert(12,'a.com','laura')
		print '=======se incerto a laura'
		comenzar.insert(5,'hss.com','eoco')
		print '=======se inserto a eoco'
		comenzar.insert(3,'bss.com','cob')
		print '=======se incerto a cob'
		comenzar.insert(5,'fs.com','ecob')
		print '=======se incerto a ecob'
		comenzar.insert(6,'ba.com','fob')
		print '=======se incerto a fob'
		comenzar.imprimir()



	nuevacosa(None)

