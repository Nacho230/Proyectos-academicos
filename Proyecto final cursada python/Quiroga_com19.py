import sys

#Funciones
def mostrar_propiedades(lista):
	
	cont = 0
	print("La lista de propiedades es:")
	for i in lista:
		
		print("Propiedad " + str(cont+1)+":")
		print("-" * 50)
		print("Código:", i[0])
		print("Tipo:", i[1])
		print("Transacción:", i[2])
		print("Dirección:", i[3])
		print("Habitaciones:", i[4])
		print("Baños:", i[5])
		print("Precio:", str(i[6])+"$")
		print("Zona:", i[7])
		print("Inmobiliaria:", i[8])
		print("Datos del dueño:",i[9],i[10],i[11])
		print("Porcentaje de comisión:",str(i[12])+"%")
		print("Estado:", i[13])
		print("-" * 50)  # LINEA SEPARADORA
		cont += 1


def actualizar_precio(lista):
	
	aux_booleano = False
	cont = 0
	
	for i in lista:
		print("Propiedad" ,str(cont+1)+":", i)
		cont += 1
		
	print()
	
	while aux_booleano != True: # Bucle para validar que el codigo que se ingresa coincida
		codigo = int(input("Ingrese el codigo de la propiedad que desea actualizar: "))
		
		for i in lista: 
			if codigo == i[0]:
				aux_booleano = True
				
		if aux_booleano == False: #Si el codigo es falso, se vuelve a pedir el dato
			print("El codigo de la propiedad ingresado no existe en nuestra base de datos, intentelo nuevamente")
			
	for i in lista:
		if codigo == i[0]:
			print("Elegiste la propiedad:")
			print("Codigo:",i[0],"|","Dirección:",i[3],"|","Zona:",i[7],"|","Precio:",str(i[6])+"$")
			
			while aux_booleano != False: #Bucle para validar que el precio ingresado no sea 0 o menor
				precio = float(input("Ingrese el nuevo precio de la propiedad: "))
				if precio <= 0:
					print("El valor de la propiedad no puede ser menor o igual a 0")
				else:
					i[6] = precio
					print("El precio de la propiedad ha sido actualizado con exito!")
					print("Codigo:",i[0],"|","Dirección:",i[3],"|","Zona:",i[7],"|","Precio:",str(i[6])+"$")
					aux_booleano = False #Se pone el false para que se salga del bucle
			
	return lista
	

def precio_promedio(lista):
	
	rta = 0
	zona = ""
	tipo = ""
	suma = 0
	cont = 0
	aux_booleano = False
	
	
	print("Vamos a calcular el precio promedio de las propiedades")
	
	
	while aux_booleano != True: #Bucle para validar que se ingresen correctamente los valores
		rta= int(input("Ingrese 1 para calcular por zona o ingrese 2 para calcular por tipo de propiedad: "))
		
		if(rta != 1 and rta != 2):
			print("El numero elegido es incorrecto, por favor elija 1 o 2") #Si el numero elegido no es ni 1 ni 2 se vuelve a pedir
		else:
			if(rta == 1): #Si la respuesta es 1, se consulta la zona
				zona = input("Ingrese la zona que desea consultar: 'QUILMES,FLORENCIO VARELA,CABA,PALERMO': ").lower()
				
				if zona in ["quilmes","florencio varela","caba","palermo"]:
					print("Las propiedades en", zona, "son:")
				
				for i in lista: # Bucle para validar que la zona ingresada o tipo de propiedad exista
					if(zona == i[7].lower()):
						print("Codigo:",i[0],"|","Dirección:",i[3],"|","Zona:",i[7],"|","Precio:",str(i[6])+"$")
						cont += 1
						suma = suma + i[6]
			else: #Si la respuesta es 2, se consulta que tipo de transaccion
				tipo = input("Ingrese el tipo de transacción que desea consultar: 'Venta,Alquiler': ").lower()
				print("Las propiedades en", tipo, "son:")
				for i in lista:
					if(tipo == i[2].lower()):
						
						print("Codigo:",i[0],"|","Dirección:",i[3],"|","Zona:",i[7],"|","Precio:",str(i[6])+"$")
						cont += 1
						suma = suma + i[6]
						
		if(cont>0): #La variable contador se utiliza para mostrar el promedio por fuera del bucle, para evitar repeticiones
			aux_booleano = True
			print("El promedio de las propiedades es:", round(suma/cont,2),"$")
			
		else:
			print("El valor seleccionado es incorrecto, por favor intentelo de nuevo")


def agregar_propiedad(lista):
    dato = []
    aux_booleano = False
    
    print("Vamos a agregar propiedades a la lista, para frenar el procedimiento, ingrese '0'")
    
    codigo = int(input("Ingrese el codigo de la propiedad: "))
    
    while codigo != 0:
        
        while aux_booleano != True: # Se utiliza un bucle para cada valor que se ingresa para asegurarnos de que el usuario lo ingrese correctamente.
			
            tipo_propiedad = input("Ingrese el tipo de la propiedad 'Casa o Departamento': ").lower() #--> Convertimos en minuscula el valor que se ingresa
            if tipo_propiedad not in ["casa", "departamento"]: #--> Comparamos si el valor ingresado coincide con el valor esperado
                print("El tipo de propiedad ingresado es incorrecto, intentelo nuevamente")
            else:
                aux_booleano = True
        
        aux_booleano = False # Se reinicia el valor del booleano para comparar la siguiente entrada
        
        while aux_booleano != True:
            tipo_transaccion = input("Ingrese el tipo de transacción de la propiedad 'Venta o Alquiler': ").lower()
            if tipo_transaccion not in ["venta", "alquiler"]: # Se valida que se ingresen de forma correcta los valores
                print("El tipo de transacción ingresado es incorrecto, intentelo nuevamente")
            else:
                aux_booleano = True
        
        aux_booleano = False
        
        direccion = input("Ingrese la dirección de la propiedad: ")
        
        while aux_booleano != True:
            habitacion = int(input("Ingrese la cantidad de dormitorios de la propiedad: "))
            if habitacion <= 0: # Se valida que se ingresen de forma correcta los valores
                print("La cantidad de dormitorios no puede ser negativa o igual a 0, intentelo nuevamente")
            else:
                aux_booleano = True
        
        aux_booleano = False
        
        while aux_booleano != True:
            baño = int(input("Ingrese la cantidad de baños de la propiedad: "))
            if baño <=  0: # Se valida que se ingresen de forma correcta los valores
                print("La cantidad de baños no puede ser negativa o igual a cero, intentelo nuevamente")
            else:
                aux_booleano = True
        
        aux_booleano = False
        
        while aux_booleano != True:
            precio = float(input("Ingrese el precio de la propiedad: "))
            if precio < 0: # Se valida que se ingresen de forma correcta los valores
                print("El precio debe ser mayor a 0, intentelo nuevamente")
            else:
                aux_booleano = True
        
        aux_booleano = False
        
        while aux_booleano != True:
            zona = input("Ingrese la zona de la propiedad 'Quilmes, Florencio Varela, CABA, Palermo': ").lower()
            if zona not in ["quilmes", "florencio varela", "caba", "palermo"]: # Se valida que se ingresen de forma correcta los valores
                print("La zona ingresada es incorrecta, intentelo nuevamente")
            else:
                aux_booleano = True
        
        aux_booleano = False
        
        while aux_booleano != True:
            inmobiliaria = input("Ingrese el nombre de la inmobiliaria que administra la propiedad 'Parra, Lavalle, Feijo': ").lower()
            if inmobiliaria not in ["parra", "lavalle", "feijo"]: # Se valida que se ingresen de forma correcta los valores
                print("El nombre de la inmobiliaria ingresada es incorrecta, intentelo nuevamente")
            else:
                aux_booleano = True
        
        aux_booleano = False
        
        nombre_dueño = input("Ingrese el nombre del dueño de la propiedad: ")
        apellido_dueño = input("Ingrese el apellido del dueño de la propiedad: ")
        
        while aux_booleano != True:
            dni = int(input("Ingrese el dni del dueño de la propiedad: "))
            if dni <= 0: # Se valida que se ingresen de forma correcta los valores
                print("El DNI no puede ser negativo 0 igual a cero, intentelo nuevamente")
            else:
                aux_booleano = True
        
        aux_booleano = False
        
        while aux_booleano != True:
            porcentaje = int(input("Ingrese el porcentaje de ganancia que se lleva la inmobiliaria: "))
            if porcentaje <= 0: # Se valida que se ingresen de forma correcta los valores
                print("El porcentaje no puede ser negativo o igual a cero, intentelo nuevamente")
            else:
                aux_booleano = True
        
        aux_booleano = False
        
        while aux_booleano != True:
            estado = input("Ingrese el estado de la propiedad 'Vendido, Alquilado, Disponible': ").lower()
            if estado not in ["alquilado", "vendido", "disponible"]: # Se valida que se ingresen de forma correcta los valores
                print("El estado ingresado es incorrecto, intentelo nuevamente")
            else:
                aux_booleano = True
        
        dato = [codigo, tipo_propiedad, tipo_transaccion, direccion, habitacion, baño, precio, zona, inmobiliaria, nombre_dueño, apellido_dueño, dni, porcentaje, estado]
        
        if validar_duplicados(lista, dato):
            print("Uno de los datos ingresados está duplicado, por favor corrobore ingresar datos nuevos.")
        else:
            print("Propiedad agregada con éxito!")
            lista.append(dato)
        
        codigo = int(input("Ingrese el codigo de la propiedad: "))
    
    return lista
		

def corroborar_inmobiliaria(lista):
	
	aux_booleano = False
	cont = 0
	
	# for i in lista:
		# print("Propiedad" ,str(cont+1)+":", i)
		# cont += 1

	while aux_booleano != True:
		inmobiliaria = input("Ingrese el nombre de la inmobiliaria a consultar 'Parra, Lavalle, Feijo': ").lower()
		
		for i in lista: # BUCLE PARA VALIDAR LA INMOBILIARIA QUE SE INGRESA
			if inmobiliaria == i[8].lower():
				aux_booleano = True
				
		if aux_booleano == False: #Si la inmobiliaria no existe, se retorna la lista
			print("El nombre ingresado es incorrecto o no poseemos alguna propiedad de esa inmobiliaria")
				
	
	if aux_booleano == True:
		print("Estas son las propiedades de",inmobiliaria+":")
		for i in lista:
			if inmobiliaria.lower() == i[8].lower():
				print("Codigo:",i[0],"|","Dirección:",i[3],"|","Zona:",i[7],"|","Precio:",str(i[6])+"$")


def propiedad_mas_cara_barata(lista):
    propiedad1 = []
    propiedad2 = []
    maximo = 0
    minimo = 9999999999
    rta = 0
    opc = 0
    tipo = ""
    aux_booleano = False
    
    print("Vamos a calcular la propiedad mas cara o mas barata")
    
    while aux_booleano != True:  # Bucle para validar que se ingresen correctamente los valores
        rta = int(input("Ingrese 1 para calcular la propiedad de tipo 'casa' o ingrese 2 para calcular la propiedad de tipo 'departamento': "))
        
        if rta != 1 and rta != 2:
            print("El numero elegido es incorrecto, por favor elija 1 o 2")
            
        else:
            if rta == 1:  # 1 ES PARA PROPIEDAD TIPO CASA
                tipo = input("Ingrese el tipo de transacción que desea consultar: 'Venta, Alquiler': ").lower()
                
                if tipo in ["venta", "alquiler"]:
                    opc = int(input("Ingrese 1 para el valor mas barato o 2 para el valor mas caro: "))
                    
                    if opc == 1: #Casa en venta o alquiler mas barato
                        for i in lista:
							
                            if i[6] < minimo and i[1].lower() == "casa" and i[2].lower() == tipo:
                                minimo = i[6]
                                propiedad2 = i
                        print("La propiedad mas barata de tipo Casa y en", tipo, "es:")
                        print("Codigo:", propiedad2[0], "|", "Dirección:", propiedad2[3], "|", "Zona:", propiedad2[7], "|", "Precio:", str(propiedad2[6]) + "$")
                        aux_booleano = True
                        
                    elif opc == 2: #Casa en venta o alquiler mas caro
                        for i in lista:
							
                            if i[6] > maximo and i[1].lower() == "casa" and i[2].lower() == tipo:
                                maximo = i[6]
                                propiedad1 = i
                        print("La propiedad mas cara de tipo Casa y en", tipo, "es:")
                        print("Codigo:", propiedad1[0], "|", "Dirección:", propiedad1[3], "|", "Zona:", propiedad1[7], "|", "Precio:", str(propiedad1[6]) + "$")
                        aux_booleano = True
                        
                    else:
                        print("La opción elegida es incorrecta, intentelo otra vez")
                        
                else:
                    print("La opción elegida es incorrecta, intentelo otra vez")
                    
            elif rta == 2:  # 2 ES PARA PROPIEDAD TIPO DEPARTAMENTO
                tipo = input("Ingrese el tipo de transacción que desea consultar: 'Venta, Alquiler': ").lower()
                
                if tipo in ["venta", "alquiler"]:
                    opc = int(input("Ingrese 1 para el valor mas barato o 2 para el valor mas caro: "))
                    
                    if opc == 1: #Departamento en venta o alquiler mas barato
                        for i in lista:
							
                            if i[6] < minimo and i[1].lower() == "departamento" and i[2].lower() == tipo:
                                minimo = i[6]
                                propiedad2 = i
                        print("La propiedad mas barata de tipo Departamento y en", tipo, "es:")
                        print("Codigo:", propiedad2[0], "|", "Dirección:", propiedad2[3], "|", "Zona:", propiedad2[7], "|", "Precio:", str(propiedad2[6]) + "$")
                        aux_booleano = True
                        
                    elif opc == 2: #Departamento en venta o alquiler mas caro
                        for i in lista:
							
                            if i[6] > maximo and i[1].lower() == "departamento" and i[2].lower() == tipo:
                                maximo = i[6]
                                propiedad1 = i
                        print("La propiedad mas cara de tipo Departamento y en", tipo, "es:")
                        print("Codigo:", propiedad1[0], "|", "Dirección:", propiedad1[3], "|", "Zona:", propiedad1[7], "|", "Precio:", str(propiedad1[6]) + "$")
                        aux_booleano = True
                        
                    else:
                        print("La opción elegida es incorrecta, intentelo otra vez")
                        
                else:
                    print("La opción elegida es incorrecta, intentelo otra vez")
  
    
def actualizar_porcentaje(lista):
	
	aux_booleano = False
	codigo_valido = True
	cont = 0
	cont_aux = 0
	porcentaje = 0
	
	print("Vamos a actualizar el porcentaje de una propiedad")

	while aux_booleano != True:
		inmobiliaria = input("Ingrese el nombre de la inmobiliaria a consultar 'Parra, Lavalle, Feijo': ").lower()
		
		for i in lista: # BUCLE PARA VALIDAR LA INMOBILIARIA QUE SE INGRESA
			
			if inmobiliaria == i[8].lower():
				aux_booleano = True
				
				
		if aux_booleano == False: #Si la inmobiliaria no existe
			print("El nombre ingresado es incorrecto o no poseemos alguna propiedad de esa inmobiliaria")
			
			
	
	
	if aux_booleano == True : #Se leen los valores por fuera del bucle WHILE para evitar los valores que se repiten
		print("Estas son las propiedades de",inmobiliaria+":")
		for i in lista:
			if(inmobiliaria == i[8].lower()):
				print("Codigo:",i[0],"|","Dirección:",i[3],"|","Zona:",i[7],"|","Precio:",str(i[6])+"$","|","Porcentaje:",str(i[12])+"%")
		
		codigo_valido = False	#Declaramos otro booleano para poder recorrer el otro bucle de la lista sin problemas
	
	

	
	while codigo_valido != True: 
            codigo = int(input("Ingrese el codigo de la propiedad que desea actualizar: "))
            
            for i in lista:
                if inmobiliaria == i[8].lower() and codigo == i[0]:
                    porcentaje = int(input("Ingrese el porcentaje que se lleva la inmobiliaria: "))
                    i[12] = porcentaje
                    print("Porcentaje actualizado con éxito!")
                    print("Codigo:", i[0], "|", "Dirección:", i[3], "|", "Zona:", i[7], "|", "Precio:", str(i[6]) + "$", "Porcentaje:",str(i[12])+"%")
                    codigo_valido = True
                   
            if codigo_valido == False:
                print("El código ingresado no coincide con ninguna propiedad de la inmobiliaria:", inmobiliaria)
                
	return lista


def actualizar_estado(lista):
	
	aux_booleano = False
	codigo_valido = False #Utilizo otro booleano para el 2do bucle while
	cont = 0
	
	for i in lista:
		print("Propiedad" ,str(cont+1)+":", i)
		cont += 1
		
	print()
	
	print("Vamos a actualizar el estado de una propiedad")
	
	while aux_booleano != True:
		codigo = int(input("Ingrese el codigo de la propiedad que desea actualizar: "))
		
		for i in lista: # BUCLE PARA VALIDAR EL CODIGO QUE SE INGRESA
			if codigo == i[0]:
				print("Elegiste la propiedad:")
				print("Codigo:",i[0],"|","Dirección:",i[3],"|","Zona:",i[7],"|","Precio:",str(i[6])+"$","|","Estado:",i[13])
				aux_booleano = True
				
		if aux_booleano == False: #Si el codigo es falso, se vuelve a pedir el dato
			print("El codigo de la propiedad ingresado no existe en nuestra base de datos, intentelo nuevamente")
			
	
	while codigo_valido != True:
		for i in lista:
			if codigo == i[0]:
				estado = (input("Ingrese el estado de la propiedad 'Vendido, Alquilado, Disponible' : ")).lower()
				if estado in ["alquilado", "vendido", "disponible"]:
					i[13] = estado
					print("El estado de la propiedad ha sido actualizado con exito!")
					print("Codigo:",i[0],"|","Dirección:",i[3],"|","Zona:",i[7],"|","Precio:",str(i[6])+"$","|","Estado:",i[13])
					codigo_valido = True
				else:
					print("El estado ingresado es incorrecto, intentelo nuevamente")
					
	return lista
	
	
def buscar_propiedades(lista):
	
	aux_booleano = False
	booleano = False
	
	print("Vamos a buscar propiedades según el criterio que tú elijas")
	print("1= Buscar por cant. habitaciones")
	print("2= Buscar por cant. baños")
	print("3= Buscar por tipo de transacción")
	print("4= Buscar por zona")
	
	
	while aux_booleano != True:
		opc = int(input("Ingrese una opción '1,2,3,4': "))
		if(opc == 1):
			habitacion = int(input("Ingrese la cantidad de habitaciones a consultar: "))
			for i in lista:
				if (habitacion == i[4]):
					print("Dirección:",i[3],"|","Zona:",i[7],"|","Precio:",str(i[6])+"$","|","Habitaciones:",i[4])
					aux_booleano = True
					booleano = True # Este booleano se utiliza para mostrar un mensaje por consola luego
				else:
					aux_booleano = True #Se poné en verdadero para que a pesar del valor ingresado, se salga del bucle
					
					
		elif(opc == 2):
			baño = int(input("Ingrese la cantidad de baños a consultar: "))
			for i in lista:
				if (baño == i[5]):
					print("Dirección:",i[3],"|","Zona:",i[7],"|","Precio:",str(i[6])+"$","|","Baños:",i[5])
					aux_booleano = True
					booleano = True
				else:
					aux_booleano = True #Se poné en verdadero para que a pesar del valor ingresado, se salga del bucle
					
			
		
		elif(opc == 3):
			tipo = input("Ingrese el tipo de transacción que desea buscar 'Venta, Alquiler': ").lower()
			if tipo in ["venta","alquiler"]:
				for i in lista:
					if(tipo == i[2].lower()):
						print("Tipo de propiedad:",i[1],"|","Dirección:",i[3],"|","Zona:",i[7],"|","Precio:",str(i[6])+"$","|","Tipo de transacción:",i[2])	
						aux_booleano = True	
						booleano = True
					else:
						aux_booleano = True #Se poné en verdadero para que a pesar del valor ingresado, se salga del bucle
					
				
		elif(opc == 4):
			zona = input("Ingrese la zona a buscar 'Quilmes,Florencio Varela, CABA, Palermo': ").lower()
			if zona in ["quilmes","florencio varela","caba","palermo"]:
				for i in lista:
					if(zona == i[7].lower()):
						print("Dirección:",i[3],"|","Zona:",i[7],"|","Precio:",str(i[6])+"$")
						aux_booleano = True
						booleano = True
					else:
						aux_booleano = True #Se poné en verdadero para que a pesar del valor ingresado, se salga del bucle
					
						
		else:
			print("Por favor, ingrese una opción correcta")		
						
	if booleano == False:
		print("Lo sentimos, no contamos con ninguna propiedad que cumpla con esos requisitos")	
		
	
def validar_duplicados(lista, dato):
    # Verificar duplicados de código, dirección, nombre_dueño, apellido_dueño, dni_dueño
    for i in lista:
        if (i[0] == dato[0]) or (i[3] == dato[3]) or (i[9] == dato[9]) or (i[10] == dato[10]) or (i[11] == dato[11]):
            return True
    

    return False


#Programa principal
print("Bienvenidos a la Inmobiliaria Integral Javac")
print()

propiedades = [ 
# Codigo, Tipo, Tipo de Transaccion, Dirección, Habitaciones, Baños, Precio, Zona, Inmobiliaria, Nombre, Apellido, DNI, Porcentaje, Estado 
[127, "Casa", "Venta", "Andres Baranda 35", 3, 2, 20000.0, "Quilmes", "Parra", "Juan", "Perez", 52653216, 20, "Disponible"],

[112, "Casa", "Alquiler", "Av. Santa Fe 21", 5, 3, 50000.0, "Palermo", "Parra", "Agustin", "Fernandez", 23673231, 40, "Alquilado"],

[652, "Casa", "Alquiler", "La Haya 6", 4, 1, 25000.0, "CABA", "Lavalle", "Facundo", "Figueroa", 35929451, 30, "Disponible"],

[921, "Departamento", "Alquiler", "Av. Rivadavia 685", 2, 1, 10000.0, "CABA", "Parra", "Simon", "Guzman", 25767233, 15, "Disponible"],

[731, "Departamento", "Alquiler", "Bartolome Mitre 67", 3, 3, 30000.0, "Florencio Varela", "Lavalle", "Ignacio", "Gutierrez", 39424122, 20, "Alquilado"],

[976, "Casa", "Venta", "Triunvirato 25", 6, 4, 100000.0, "Quilmes", "Parra", "Diego", "Gauna", 40242888, 50, "Disponible"],

[891, "Departamento", "Venta", "Dr. Nicolas Boccuzzi", 2, 1, 15000.0, "Florencio Varela", "Feijo", "Agustina", "Sanchez", 35863214, 25, "Disponible"],

[642, "Departamento", "Alquiler", "Guemes 742", 4, 2, 40000.0, "Palermo", "Feijo", "Fernanda", "Robles", 40422658, 25, "Alquilado"],

[197, "Casa", "Venta", "Av. Brasil 6", 10, 8, 1000000.0, "CABA", "Feijo", "Sabrina", "Gutierrez", 31654752, 25, "Disponible"],

[783, "Departamento", "Venta", "Av. Vicente Lopez", 1, 1, 8000.0, "Quilmes", "Feijo", "Raul", "Quiroga", 32567123, 25, "Vendido"]
] 
#0 = Codigo de la propiedad, 
#1 = Tipo de propiedad casa/departamento, 
#2 = Tipo de transaccion venta/alquiler,
#3= Dirección, 
#4 = Habitaciones, 
#5 = baños, 
#6 = Precio , 
#7 = Zona (Palermo,Quilmes,Varela, CABA), 
#8 = Nombre de la inmobiliaria
#9 = Nombre del propietario, 
#10 = Apellido del propietario, 
#11 = Dni del propietario, 
#12 = Porcentaje que se lleva la inmobiliaria  ,
#13 = Estado del inmueble (Vendido/alquilado) o Disponible.


menu = """1. Mostrar lista de propiedades
2. Actualizar precio de una propiedad
3. Calcular precio promedio de las propiedades de una determinada zona (Segun venta o tipo de propiedad)
4. Agregar una propiedad
5. Mostrar lista de propiedades segun dueño de inmobiliaria 
6. Mostrar la propiedad mas cara o mas barata de una determinada zona (Segun tipo de venta o tipo de propiedad)
7. Actualizar el porcentaje que se lleva la inmobiliaria de una determinada propiedad
8. Actualizar el estado de una propiedad
9. Buscar propiedades segun criterio (Cant. habitaciones, Cant. baños, tipo de transaccion o zona)
10. Salir
"""

print(menu)

opcion = int(input("Ingrese una opción: "))

while opcion !=10:
	
	if opcion == 1:
		mostrar_propiedades(propiedades)
	
	elif opcion == 2:
		propiedades = actualizar_precio(propiedades)
	
	elif opcion == 3:
		precio_promedio(propiedades)
		
	elif opcion == 4:
		propiedades = agregar_propiedad(propiedades)
	
	elif opcion == 5:
		corroborar_inmobiliaria(propiedades)
	
	elif opcion == 6:
		propiedad_mas_cara_barata(propiedades)
	
	elif opcion == 7:
		actualizar_porcentaje(propiedades)
	
	elif opcion == 8:
		actualizar_estado(propiedades)
	
	elif opcion == 9:
		buscar_propiedades(propiedades)
		
	else:
		print("Por favor ingrese una opción del menu")
	
	print()
	print(menu)	
	opcion = int(input("Ingrese una opcion: "))
	
	
	
print("Gracias por utilizar Inmobiliaria Integral Javac")
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
