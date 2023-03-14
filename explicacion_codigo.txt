Este es un programa de Python que solicita un inicio de sesión a los usuarios y les permite ingresar datos de 
los estudiantes para crear una base de datos. A continuación se explica el código paso por paso:

1- Primero, el programa importa las bibliotecas necesarias para su funcionamiento. La biblioteca "termcolor" 
se utiliza para imprimir texto con colores en la terminal. "datetime" se utiliza para obtener la fecha y hora 
actuales, y "time" se utiliza para pausar el programa durante unos segundos.

2- Luego, el programa imprime un mensaje de bienvenida en la terminal. 

3- El programa utiliza la función "datetime.now()" para obtener la fecha y hora actuales del sistema. 
Luego, utiliza la función "strftime()" para dar formato a la hora actual y el día actual como una cadena. 
Los formatos utilizados son '%H:%M:%S' para la hora y '%d/%m/%Y' para el día. Estas cadenas formateadas se 
almacenan en las variables "hora_actual" y "dia_actual".

4- El programa crea una matriz llamada "profesores" que contiene los nombres de usuario y contraseñas de los 
profesores. En este ejemplo, la matriz contiene solo una entrada, "admin" y "1234". Además, establece una 
variable "op_logico" en "False".

5- El programa utiliza un bucle "while" para solicitar al usuario que ingrese su nombre de usuario y 
contraseña. El programa verifica si el nombre de usuario y la contraseña están en la matriz "profesores".
Si se encuentra una coincidencia, el programa imprime un mensaje de "Iniciando sesión!" y cambia la variable 
"op_logico" a "True" para permitir al usuario introducir datos de los alumnos. Si no se encuentra una 
coincidencia, el programa pregunta al usuario si desea registrarse como nuevo profesor.

6- Si el usuario elige registrarse, el programa solicita un nuevo nombre de usuario y contraseña y los agrega 
a la matriz "profesores". Si el usuario no desea registrarse, el programa termina con un mensaje de "Vuelva 
pronto".

7- Si el inicio de sesión es exitoso, el programa utiliza otro bucle "while" para solicitar al usuario que 
ingrese datos de los estudiantes. El programa imprime un mensaje para pedir al usuario que introduzca datos 
del alumnado.

8- El programa utiliza otro bucle "while" para solicitar al usuario que ingrese la cantidad de alumnos que 
desea ingresar. El programa verifica si se introduce un valor numérico y si es así, almacena el valor en la 
variable "num1". Si no se introduce un valor numérico, el programa muestra un mensaje de error y solicita al 
usuario que vuelva a intentarlo.

9- Si se ha ingresado una cantidad válida de estudiantes, el programa solicita al usuario que ingrese los 
datos de cada estudiante. El usuario debe ingresar el nombre, apellido, edad y género de cada estudiante. 
Los datos se almacenan en una matriz llamada "alumnos".

10- El programa muestra los datos ingresados por el usuario y le pregunta si desea ingresar más datos de los 
estudiantes. Si el usuario elige continuar, el programa solicita los datos para otro estudiante. Si el usuario
elige no continuar, el programa muestra un mensaje de "Fin del programa" y finaliza.