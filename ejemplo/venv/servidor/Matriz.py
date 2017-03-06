class Nodom:
	def __init__(self, letra, dominio, nombre):
		self.letra = letra
		self.dominio = dominio
		self.nombre = nombre
		self.down = None
		self.next = None
		self.up = None
		self.left = None
		self.atras = None


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
##------------ ----PARA INSERTAR UNA NUEVA FILA ---------------------
		##para incertar el primer nodo de la fila
		if self.prim.nombre == 'vacio':
			NLetra = Nodom(letra,None,nombre[0])
			self.prim.nombre = 'vaciodom'
			self.prim.down = NLetra
			NLetra.up = self.prim
			auxf = auxf.down
			print 'Insertar nueva fila se creo el primer nodo con ', auxf.letra, nombre
		##si ya existe al menos un nodo de la fila
		else:
			while auxf.down!=None:
				if letra>auxf.down.letra:
					auxf = auxf.down
				elif letra == auxf.down.letra:
					existeletra=True
					auxf = auxf.down
					print 'LETRA INCIAL YA EXISTE',auxf.letra, nombre
					break
				else: 
					break
			if existeletra==False:
			 	NuevaLetra = Nodom(letra,None,nombre[0])
			 	if auxf.down != None:
			 		NuevaLetra.down = auxf.down
					NuevaLetra.down.up = NuevaLetra
				auxf.down = NuevaLetra
				NuevaLetra.up = auxf
				auxf = auxf.down
				print 'SE INGRESO NUEVA LETRA', letra, nombre
			else:
				print '-'



##====================PARA INSERTAR UNA NUEVA COLUMNA============			
		##si no existe nada despues del primero	
		if self.prim.nombre == 'vaciodom':
			self.prim.nombre ='alv'
			NDominio = Nodom(None,dominio,None)
			auxc.next = NDominio
			NDominio.left = auxc
			auxc = auxc.next
		else:
			letdom = ord(dominio[0])
			inauxc = ord('n') 
			while auxc.next != None:
				temp = auxc.next.dominio[0]
				inauxc = ord(temp)
				#print 'insert columna, el codigo ascii es',inauxc,auxc.next.dominio ##toma la primera letra del dominio del nodo actual.next
				if letdom == inauxc :
					print 'EMPIEZA CON LA MISMA LETRA'
					if auxc.next.dominio == dominio:
						print 'EL DOMINIO YA EXISTE'
						auxc = auxc.next
						existedom = True
						break
					else:
						auxc = self.verificar(auxc,dominio)
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
					Nuevodom.next.left = Nuevodom
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
			if auxc.down!= None:
				Nuevo.down = auxc.down
				Nuevo.down.up = Nuevo
			auxc.down = Nuevo
			Nuevo.up = auxc
		else:
			print 'insertar atras es true D:'
			auxc = auxc.down
			auxc.atras = Nuevo



			#para conectarlo con el siguiente
		#print auxf.letra ,'esta es el indice de la letra a agregar'
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
					auxf = self.verificar(auxf,dominio)
					print 'el codigo de letra',letdom,'es igual al aux',inauxf
					break
			elif letdom > inauxf:
				auxf = auxf.next
			else:
				break


		if insetarAtras != True:
			Nuevo.next = auxf.next
			Nuevo.left = auxf
			if Nuevo.next != None:
				Nuevo.next.left = Nuevo
			auxf.next = Nuevo
		else:
			print 'ya esta ligado a un siguiente'
			#auxc.down = Nuevo


		#print 'abajo de',auxc.nombre,auxc.dominio,'esta',auxc.down.nombre,'@',auxc.down.dominio,'derecha de ',auxf.letra,auxf.nombre,auxf.dominio,'esta',auxf.next.nombre,'@',auxf.next.dominio
		#if Nuevo.next != None and Nuevo.down != None:
		#	print 'abajo de', Nuevo.nombre, Nuevo.dominio,'esta',Nuevo.down.nombre,'@',Nuevo.down.dominio, 'a  la dereca de', Nuevo.nombre,Nuevo.dominio,'esta',Nuevo.next.nombre, '@',Nuevo.next.dominio
		#elif Nuevo.next != None:
		#	print 'abajo de', Nuevo.nombre, Nuevo.dominio,'No hay nada a  la derecha de', Nuevo.nombre,Nuevo.dominio,'esta',Nuevo.next.nombre, '@',Nuevo.next.dominio
		#elif Nuevo.down != None:
		#	print 'abajo de', Nuevo.nombre, Nuevo.dominio,'esta',Nuevo.down.nombre,'@',Nuevo.down.dominio, 'a  la dereca de', Nuevo.nombre,Nuevo.dominio,'NO HAY NADA'
		#else:
		#	print 'No hay nada debajo ni a su derecha'

		return "se inserto " + str(Nuevo.nombre) + "@" + str(Nuevo.dominio)

	def verificar(self,auxc ,dominio):#manda el nodo y la palabra dominio
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
		print ''
		print '------------------'
		print ' vamo a imprimir'
		grafico = str(self.prim.dominio) + ";"
		ac = self.prim
		af = self.prim

		while(af.next!= None):
			grafico = grafico + af.next.dominio + ";"
			grafico = grafico + af.dominio + " -> "+ af.next.dominio+';'
			grafico = grafico + af.next.dominio + " -> "+ af.dominio+';'
			af = af.next

		print 'por la puchis'

		af = self.prim.down
		grafico = grafico + af.nombre+ ";"
		grafico =grafico + self.prim.dominio +" -> "+ af.nombre + ';'
		grafico =grafico + af.nombre +" -> "+ self.prim.dominio + ';'
		


		while af.down != None:
			grafico = grafico + af.down.nombre + ";"
			grafico = grafico + af.nombre + " -> "+ af.down.nombre+';'
			grafico = grafico + af.down.nombre + " -> "+ af.nombre+';'
			af = af.down

		af = self.prim
		while af.down !=None:
			ac = af.down
			af = af.down
			grafico = grafico + ac.nombre + " -> "+ ac.next.nombre+ ";"
			grafico = grafico + ac.next.nombre + " -> "+ ac.nombre+ ";"
			ac = ac.next
			while ac.next!= None:
				grafico = grafico + ac.next.nombre+";"
				grafico = grafico + ac.nombre+' -> ' + ac.next.nombre + ';'
				grafico = grafico + ac.next.nombre+' -> ' + ac.nombre + ';'
				ac = ac.next

		af = self.prim
		while af.next !=None:
			ac = af.next
			af = af.next
			grafico = grafico + ac.dominio + " -> "+ ac.down.nombre+ ";"
			grafico = grafico + ac.down.nombre + " -> "+ ac.dominio+ ";"
			ac = ac.down
			while ac.down!= None:
				grafico = grafico + ac.nombre+' -> ' + ac.down.nombre + ';'
				grafico = grafico + ac.down.nombre+' -> ' + ac.nombre + ';'

				if ac.atras != None:
					grafico = grafico + ac.nombre+' -> ' + ac.atras.nombre + ';'
					grafico = grafico + ac.atras.nombre+' -> ' + ac.nombre + ';'

				ac = ac.down
			

		print grafico + "por la pushix"
		return str(grafico)
		#hile(af.down!=None):

	def eliminar(self,letra,dominio,nombre):
		busqueda = self.prim.next
		while busqueda != None:
			if busqueda.dominio == dominio:
				break
			else:
				busqueda = busqueda.next

		busqueda = busqueda.down

		while busqueda != None:
			if busqueda.letra ==letra:
				break
			else:
				busqueda = busqueda.down
		if busqueda != None:
			while busqueda != None:
				if busqueda.nombre == nombre:
					break
				else:
					nombre = nombre.left
				pass

		if busqueda!= None:
			if busqueda.left!= None:
				busqueda = busqueda.left
				return "se elimino el nodo" 
			else:
				n = busqueda.left
				n.next = busqueda.next
				n.next.left = n 
				a = busqueda.down
				a.up = busqueda.up
				a.up.down = a
				return "se elimino el nodo" 


	def letra(self,letra):
		lista = ''
		af = self.prim.down
		while af != None:
			if af.letra == letra:
				break
			else:
				af= af.down
		if af!= None:
			af = af.next
			while af != None:
				lista = lista+ ' - ' + af.nombre
				if af.atras != None:
					while af.atras!= None:
						lista = lista +' - ' + af.nombre
					
				af = af.next


		return str(lista)


	def dominio(self, dominio):
		lista = ''
		ac = self.prim.next
		while ac!= None:
			if ac.dominio == dominio:
				break
			else:
				ac = ac.next
		if ac != None:
			ac = ac.down 
			while ac != None:
				lista = lista + ' - ' + ac.nombre
				if ac.atras != None:
					while ac.atras!= None:
						lista = lista +' - ' + ac.nombre
				ac = ac.down
		return str(lista)


		#while(ac != None):=
		#	print ac.letra
		#	while(af.next!= None):
		#		grafico = grafico + af.next.
		#		print af.next.nombre, af.next.dominio
		#		af = af.next
		#	ac = ac.down
		#	af = ac


		
