# Crear un login de profesores con contraseña, solo podran entrar si tienen los datos guardados en la matriz
# Si no tienen su usuario guardado daremos la opcion de loguearse creando una cuenta (introduciendo los datos
# dentro de la matriz)
# (Introduciran datos de alumnos) Pedir una matriz de tres nombres con su edad y nota global y separarlo en 
# pantalla ordenandolos por orden alfabetico o por orden de mejor nota

# Importamos colored para dar color a diferentes print en la terminal
from termcolor import colored
# Obtenemos dia y hora exactos
from datetime import datetime
# obtenemos la hora actual
ahora = datetime.now()
hora_actual = ahora.strftime('%H:%M:%S')
# obtenemos el dia
dia = datetime.now()
dia_actual = dia.strftime('%d/%m/%Y')
# Importamos tiempo
import time

# Damos bienvenida al programa
print (colored('\nBienvenido al programa de la base de datos del alumnado\n', 'green'))

# Damos la hora y dia 
print (colored('La hora actual del sistemas es: ','grey') , colored(hora_actual, 'yellow'))
print (colored('Fecha:', 'blue') , colored(dia_actual, 'yellow'))

# Matriz que almacena los nombres de usuario y contraseñas de los profesores
profesores = [["admin", "1234"]]
# Variable de tipo logico que nos dara paso a introducir los datos de los alumnos
op_logico = False

# Empieza el login
while True:
    # Pedimos al usuario que ingrese su nombre de usuario y contraseña
    nombre_usuario = input('\nIngrese su nombre de usuario:\n')
    contraseña = input('Ingrese su contraseña:\n')

    # Verificamos si el nombre de usuario y la contraseña existen en la matriz de profesores
    for profesor in profesores:

        # Si existen en la matriz entramos al programa saliendo de este bucle con break
        if nombre_usuario == profesor[0] and contraseña == profesor[1]:
            print (colored('Iniciando sesión!', 'yellow'))
            # Sacamos el dia y la hora del login
            dia = datetime.now()
            dia_actual = dia.strftime('%d/%m/%Y')
            # Cambiamos el op_logico a true para el siguiente while (introducir datos alumnos)
            op_logico = True
            time.sleep(2)
            break
    else:
        # Metodo try_except
        # Si no existen en la matriz damos la opciona a crear un usuario 
        while True:

            try: # Controlamos que la respuesta sea solo 1 o 2 para comprovar si quieren crear un usuario o no
                
                # Damos print por pantalla como si estubiera correcto todo para simularlo
                print (colored('Iniciando sesión!', 'yellow'))

                # Sacamos el dia y la hora del login
                dia = datetime.now()
                dia_actual = dia.strftime('%d/%m/%Y')

                # Cambiamos el op_logico a true para el siguiente while (introducir datos alumnos)
                op_logico = True
                time.sleep(2)

                print ('\n- Su usuario y contraseña no estan registrados')
                registro_opcion = int(input('¿Desea registrarse? (Introduzca 1 para si y 2 para no):\n'))
                if registro_opcion < 1 or registro_opcion > 2: 
                    raise ValueError ('\nPor favor, elija 1 o 2, solamente')
                else:
                    # Si la respuesta és válida, damos salida
                    break 

            # Capturamos el error y lo mostramos por pantalla
            except ValueError as error: 
                print(colored(error, 'red'))
                time.sleep(1)

        # Si no existen en la matriz, se pregunta al usuario si desea registrarse
        if registro_opcion == 1:
            # Si elige hacerlo, se piden los nuevos datos de inicio de sesión y se agregan a la matriz 
            # de profesores
            nuevo_nombre_usuario = input('Ingrese un nuevo nombre de usuario:\n')
            nueva_contraseña = input('Ingrese una nueva contraseña:\n')
            profesores.append([nuevo_nombre_usuario, nueva_contraseña])
            time.sleep(2)
            print (colored('Registro con exito! Por favor inicie sesión.', 'yellow'))
            # Volvemos al inicio de sesion del while con el continue
            continue
        else:
            print (colored('Vuelva pronto', 'yellow'))
            op_logico = False
            # Si no elige registrarse, se sale del bucle y se termina el programa
            break
    break

# Si se registro con exito pasamos a la introduccion de datos de los alumnos
while op_logico == True:
    
    # Empieza la creacion de base de datos de los alumnos
    print ('\nIntroduce datos del alumnado\n')

    # Iniciamos la variable a pedir con un espacio para que entre al bucle
    num1 = ' ' 

    # Bucle while para pedir numero de alumnos por pantalla
    while  str(num1).isdigit() == False:  # Cuando la condición sea True saldremos del bucle

        # Metodo try para controlar que introduzcan datos numericos
        try:
            num1 = input('Cuantos alumnos son: ') 
            
            # Si se introduce un espacio capturamos el error
            if ' ' in num1:  
                raise ValueError ('** No introduzca espacios')

            # Si se introducen letras, o punto o comas capturamos el error
            elif str(num1).isdigit() == False: 
                raise ValueError ('*** Introduzca solo números enteros..')
            
            # Una vez estamos seguros que lo introducido son numeros pasamos la variable a int.
            num1 = int(num1) 
        # Sacamos el error por pantalla  
        except ValueError as error:
            if '**' in str(error):
                print(colored(error, 'red'))


    # Creamos la matriz en blanco para que introduzcan los datos del alumno
    datos_alumnos = []

    # Si es mayor de 0 pediremos que introduzcan los datos
    if num1 > 0:
        for i in range (num1):
            print ('- DATOS DEL ALUMNO:')

            # Pedimos el nombre
            nombre = input ('· Nombre:\n')
            # Pasamos el nombre con el primer caracter en mayusculas
            nombre = nombre.title()

            # Preguntamos por la edad y con el metodo try y el while controlamos que lo introduzcan bien
            nota_1 = ''
            while  str(nota_1).isdigit() == False:  # Cuando la condición sea True saldremos del bucle
                try:
                    nota_1 = input('Pseudocodigo:\n') 

                    # Si se introduce un espacio capturamos el error
                    if ' ' in nota_1:  
                        raise ValueError ('** No introduzca espacios')

                    # Si se introducen letras, o punto o comas capturamos el error
                    elif str(nota_1).isdigit() == False: 
                        raise ValueError ('*** Introduzca solo números enteros..')
                    
                    # Una vez estamos seguros que lo introducido son numeros pasamos la variable a int.
                    nota_1 = int(nota_1)  
                
                
                except ValueError as error:
                    if '**' in str(error):
                        print(colored(error, 'red'))
            
            # Pedimos la nota
            nota_2 = ''
            # Cuando la condición sea True saldremos del bucle
            while  str(nota_2).isdigit() == False:  
                try:
                    nota_2 = input('Python:\n') 

                    # Si se introduce un espacio capturamos el error
                    if ' ' in nota_2:  
                        raise ValueError ('** No introduzca espacios')
                    
                    # Si se introducen letras, o punto o comas capturamos el error
                    elif str(nota_2).isdigit() == False: 
                        raise ValueError ('*** Introduzca solo números enteros..')
                    
                    # Una vez estamos seguros que lo introducido son numeros pasamos la variable a int.
                    nota_2 = int(nota_2)  
                
                # Sacamos el error por pantalla
                except ValueError as error:
                    if '**' in str(error):
                        print(colored(error, 'red'))
            
            # Sacamos la nota media de cada alumno
            nota_media = (nota_1 + nota_2) / 2

            # Añadimos los datos en la matriz
            datos_alumnos.append([nombre,nota_1,nota_2,float(nota_media)])

        # Ordenamos la matriz en orden alfabetico
        datos_alumnos.sort()

        # Sacamos la matriz por pantalla
        print (datos_alumnos)

        # Sacamos los datos de los alumnos por pantalla ya ordenados
        print ('\nDatos alumnos ordenados alfabeticamente:\n')

        # Con el for recorremos de nuevo la matriz dando todos los datos separados
        nota_media_alumnos = 0
        for i in range(len(datos_alumnos)):
            print('\n- Nombre:', datos_alumnos[i][0] , '- Pseudocodigo:', datos_alumnos[i][1] , '- Python:' , 
            datos_alumnos[i][2] , '- Nota mnedia:' , datos_alumnos [i][3])

            # Sumamos todas las notas medias de los alumnos
            nota_media_alumnos += datos_alumnos[i][3]
        
        # Dividimos la suma de las notas medias entre el numero de alumnos que hay
        nota_media_alumnos = nota_media_alumnos/num1

        # Imprimimos por pantalla el num de alumnos y la nota media    
        print(f"\n- La nota media de los {num1} alumnos es {nota_media_alumnos}")
        # Salimos ya del bucle para finalizar el programa
        op_logico = False

    # Como no tiene alumnos que a introducido 0 o menos salimos del programa dando un mensaje
    else:
        print ('Vuelva cuando tenga datos del alumnado')

        # Salimos ya del bucle para finalizar el programa
        op_logico = False