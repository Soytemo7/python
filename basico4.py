 
# FUNCIONES

# parametros, lista de variables de los parentesis
# argumentos, valores que le enviamos a la funcion cuando es llamada

                # parametros = varibales
def funcion(profesor,curso,femenino):    
    articulo = "el profesor"
    if femenino:
        articulo="la profesora"
    print(f"El curso de {curso} lo dará {articulo} {profesor}")

            # argumentos
funcion("Manuel","Python",False)
funcion("Pedro","Cocina",False)
funcion("Marina","Manejo",True)

#argumentos arbitrarios

def llamar_alumnos(*alumnos):
    print(f"Mi mejor alumno es {alumnos[0]}")
    print(f"Mi alumno mas divertido es {alumnos[2]}")

llamar_alumnos("Ricardo","Manuel","Beatriz","Pepe")

#agumentos clave / key arguments

def cursos(curso1,curso2,curso3):
    print(f"el primer curso que dare es {curso1}, el siguiente es {curso2}, y por ultimo el curso {curso3}")

cursos("java","CSS","HTML")
cursos(curso3="Java",curso2="CSS",curso1="HTML")

# argumentos claves arbitrarios

def llamar_alumno(**alumno):
    print(f"el apellido del alumno es {alumno["apellido"]} y su nombre es {alumno["nombre"]}")

llamar_alumno(apellido="perez",nombre="Manuel",edad=34)

# Varibales por defecto

def decir_pais(pais="Argentina"):
    print(f"el nombre de mi pais es {pais}")

decir_pais("Mexico")
decir_pais()

# otros tipos de datos

lista = ['Javascript',True,35]
number = 33

def usar_tipos_de_datos(lista,number):
    print(lista)
    print(number)

usar_tipos_de_datos(['Hawai','Jamaica',1],100)
usar_tipos_de_datos(lista,number)

# retornar valores

def suma(a,b):
    return a+b

resultado=suma(3,2)

print(suma(1,2))
print(resultado)

# Recursividad - recursion (como un bucle)

#factorial ejemplo
# 0! = 1
# n! = n * (n-1) para n > 0

def factorial(n):
    if n==0:
        return 1
    else:
        return n * factorial(n-1)

numero = 3
print(f"El factorial de {numero} es {factorial(numero)}")

# LAMBDA: FUNCIONES anonimas y cortas 1 sola linea
# sintaxis: lambda arg1,arg2 : retorno

suma_lambda = lambda a,b : a+b
resta_lambda = lambda a,b : a-b
mul_lambda = lambda a,b : a*b
div_lambda = lambda a,b : a/b

print(suma_lambda(6,2))


# CONTRUCTOR DE FUNCIONES

def creador_funciones_multiplicacion(n):
    return lambda a : a*n

duplicador = creador_funciones_multiplicacion(2)
triplicador = creador_funciones_multiplicacion(3)
cuadriplicador = creador_funciones_multiplicacion(4)

print(duplicador(5))
print(triplicador(5))
print(cuadriplicador(4))

# LAMBDA EN FILTER

numeros = [1,2,3,4,5,6,7,8,9,10]
pares = list(filter(lambda x: x%2 ==0,numeros))

print(pares)



