class Nodom:
	def __init__(self, letra, dominio, nombre):
		self.letra = letra
		self.dominio = dominio
		self.nombre = nombre
		self.down = None
		self.next = None


class Matriz(object):
	def __init__(self):
		print 'inicializo matriz'
		print ''
		print '------------------------------------------------------------------------------------------------------------------------'
		self.prim = Nodom(None,'inicio','vacio')

	

	def insert(self,letra, dominio, nombre):
		auxf = self.prim
		auxc = self.prim
		Nuevo = Nodom(letra, dominio, nombre)
		existeletra= False
		existedom = False
##----------------PARA INSERTAR UNA NUEVA FILA ---------------------
		##para incertar el primer nodo de la fila
		if self.prim.nombre == 'vacio':
			self.prim.nombre = 'vaciodom'
			self.prim.down = Nodom(letra,None,nombre[0])
			auxf = auxf.down
			print 'Insertar nueva fila se creo el primer nodo con ', auxf.letra, nombre
		##si ya existe al menos un nodo de la fila
		else:
			print 'el abajo no esta vacio', auxf.down.letra
			while auxf.down!=None:
				if letra>auxf.down.letra:
					auxf = auxf.down
					print 'letra',letra,' es mayor que auxfletra', auxf.letra
				##si la letra ya existe
				elif letra == auxf.down.letra:
					existeletra=True
					auxf = auxf.down
					print 'Insertar nueva fila esta letra YA EXISTE',auxf.letra, nombre
					break
				else: #va a salir hasta que letra sea menor que aux.down.letra
				##si la letra no existe y ya es menor que el siguiente
					break
			#si no existe la letra	
			if existeletra==False:
			 	NuevaLetra = Nodom(letra,None,nombre[0])
				NuevaLetra.down = auxf.down
				auxf.down = NuevaLetra
				auxf = auxf.down
				print 'se ingreso la letra', letra, nombre
			else:
				print 'insertar nueva fila: No incerto nada porque ya existe'



##====================PARA INSERTAR UNA NUEVA COLUMNA============			
		##si no existe nada despues del primero	
		if self.prim.nombre == 'vaciodom':
			self.prim.nombre ='alv'
			auxc.next = Nodom(None,dominio,None)
			auxc = auxc.next
			print 'Insertar nueva fila se creo el primer nodo con ', auxf.letra, nombre
			#prim.letra = 'lleno'
			#auxc.next = Nodom(None,dominio,None)
			#auxc = auxc.next
	    #si ya existe un dominio
		else:
			letdom = ord(dominio[0])
			print 'insertar nueva columna la letra del dominio es',letdom,dominio
			inauxc = ord('n')# es el valor ancii 
			while auxc.next != None:
				temp = auxc.next.dominio[0]
				print 'insertar columna, la letra del temp es',temp
				inauxc = ord(temp)
				print 'insert columna, el codigo ascii es',inauxc,auxc.next.dominio ##toma la primera letra del dominio del nodo actual.next
				if letdom == inauxc :
					print 'EMPIEZA CON LA MISMA LETRA'
					if auxc.next.dominio == dominio:
						print 'EL DOMINIO YA EXISTE'
						auxc = auxc.next
						existedom = True
						break
					else:
						auxc = verificar(auxc,dominio)
						print 'el codigo de letra',letdom,'es igual al aux',inauxc
						break
				elif letdom > inauxc:
					auxc = auxc.next
					print 'es mayor'
				else:
					print 'insertar columna se deberia insertar here'
		    		break


		    #si no existe el dominio
			print 'ha salido del fking while',existedom	
			if existedom == False:
				Nuevodom = Nodom(None,dominio,None)
				if auxc.next!= None:
					Nuevodom.next = auxc.next
				auxc.next = Nuevodom
				auxc = auxc.next
			else:
				print 'nojoda'
				print auxc.dominio





#=================PARA METER EL NUEVO NODO ===================
		insetarAtras = False
		print auxc.letra, auxc.nombre
		while auxc.down!= None:
			if letra > auxc.down.letra: #si la letra del nodo nuevo es mayor a  la del nodo actual
				auxc = auxc.down
			elif letra == auxc.down.letra:##si es igual, debe insertar el nodo atras de esa
				auxc.down.atras = Nuevo
				insetarAtras = True
				break
				print 'Debe insertar el nodo atras'
			else:#sale del ciclo y pasa al insertar
				insetarAtras= False
				print 'LO INSERTARA ANTES DEL ACTUAL.DOWN'
				break
		if insetarAtras != True: #si no hay que incertar atras, se incerta el nodo al abajo del auxcdown
			print 'insertar atras no es true'

			if auxc.down!= None:
				Nuevo.down = auxc.down
				print auxc.down.nombre,'este es el nombre que va abajo'
				auxc.down = Nuevo
			else:
				auxc.down = Nuevo
		else:
			print 'insertar atras es true D:'
			auxc = auxc.down
			auxc.atras = Nuevo


			#para conectarlo con el siguiente
		print auxf.letra ,'esta es el indice de la letra a agregar'
		letdom = ord(dominio[0])
		print 'insertar nueva columna la letra del dominio es',letdom,dominio
		inauxf = ord('n')# es el valor ancii 
		while auxf.next != None:
			temp = auxf.next.dominio[0]
			print 'insertar columna, la letra del temp es',temp
			inauxf = ord(temp)
			if letdom == inauxf :
				print 'ya existe uno con la misma letra'
				if auxf.next.dominio == dominio:
					print 'EL DOMINIO YA EXISTE'
					auxf = auxf.next
					break
				else:
					auxf = verificar(auxf,dominio)
					print 'el codigo de letra',letdom,'es igual al aux',inauxf
					break
			elif letdom > inauxf:
				auxf = auxf.next
			else:
				break


		if insetarAtras != True:
			Nuevo.next = auxf.next
			auxf.next = Nuevo
		else:
			print 'ya esta ligado a un siguiente'
			#auxc.down = Nuevo


		print 'abajo de',auxc.nombre,auxc.dominio,'esta',auxc.down.nombre,'@',auxc.down.dominio,'derecha de ',auxf.letra,auxf.nombre,auxf.dominio,'esta',auxf.next.nombre,'@',auxf.next.dominio
		if Nuevo.next != None and Nuevo.down != None:
			print 'abajo de', Nuevo.nombre, Nuevo.dominio,'esta',Nuevo.down.nombre,'@',Nuevo.down.dominio, 'a  la dereca de', Nuevo.nombre,Nuevo.dominio,'esta',Nuevo.next.nombre, '@',Nuevo.next.dominio
		elif Nuevo.next != None:
			print 'abajo de', Nuevo.nombre, Nuevo.dominio,'No hay nada a  la derecha de', Nuevo.nombre,Nuevo.dominio,'esta',Nuevo.next.nombre, '@',Nuevo.next.dominio
		elif Nuevo.down != None:
			print 'abajo de', Nuevo.nombre, Nuevo.dominio,'esta',Nuevo.down.nombre,'@',Nuevo.down.dominio, 'a  la dereca de', Nuevo.nombre,Nuevo.dominio,'NO HAY NADA'
		else:
			print 'No hay nada debajo ni a su derecha'



	def verificar(self,auxc,dominio):#manda el nodo y la palabra dominio
		i = 1
		print 'entro a verificar'

		if auxc.dominio != None:	
			l1 = len(dominio)  #largo de la palabra dominio
			l2 = len(auxc.next.dominio)#largo del dominio del nodo
			print 'el largo del dominio es ', l1
			print 'el largo del dominio de auxc es ',l2
			cont =0#contador auxicliar
			if l1 <l2:
				cont = l1
			else:
				cont = l2
			while (i<cont):
				if ord(dominio[i])< ord(auxc.next.dominio[i]):
					break
				elif ord(dominio[i])> ord(auxc.next.dominio[i]):
					auxc = auxc.next
					break
				else:
					i=i+1
			return auxc

		else:
			print 'que puchis pasa D'
			return auxc


	def imprimir(self):
		grafico =self.prim.dominio+';'
		ac = self.prim
		af = ac

		while(af.next!= None):
			grafico = grafico + af.next.dominio + ';'
			grafico = grafico + af.dominio + " -> "+ af.next.dominio+';'
			af = af.next

		af = self.prim.down
		grafico =grafico + self.prim.dominio +' -> '+ af.nombre + ';'

		while af.down != None:
			grafico = grafico + af.down.nombre + ';'
			grafico = grafico + af.nombre + ' -> '+ af.down.nombre+';'
			af = af.down

		af = self.prim
		print af.nombre
		print af.down.nombre
		ac = self.prim.down
		while af.down !=None:
			af = af.down
			while ac.next!= None:
				grafico = grafico + ac.nombre+' -> ' + ac.next.nombre + ';'
				ac = ac.next
			

		print grafico
		return grafico
		#hile(af.down!=None):

	def eliminar(self):
		return 'deberia eliminar'




		#while(ac != None):
		#	print ac.letra
		#	while(af.next!= None):
		#		grafico = grafico + af.next.
		#		print af.next.nombre, af.next.dominio
		#		af = af.next
		#	ac = ac.down
		#	af = ac


		
