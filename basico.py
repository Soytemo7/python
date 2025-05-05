# https://github.com/sergiecode/bibliotecas-populares-python
# https://gist.github.com/sergiecode/835b3f990142ad9cc232b30af0106fdf

# Git Graph INSTALAR.

# en powershell
# New-Item -ItemType Directory --Name nombre_carpeta
# New-Item -ItemType File --Name nombre_archivo

# linux
# mkdir nombre_carpeta
# touch nombre_archivo.txt

# ms-dos

# para hacer un archivo desde consola msdos:
# echo. > prueba.txt
# para que lo cree pero no se sobreescriba si existe:
# type nul > prueba2.txt
# mkdir nombre_carpeta
# md nombre_carpeta

# mac
# mkdir nombre_carpeta
# touch nombre_archivo

# CONSOLA.
# phyton
# exit()

# ALT+ SHIFT +F         se formate
print("Hola mundo")

if 5>3:
    if 5>4:
        print("5 es Mayor que 4 y 3")


# forma de comentar con hash
""" 
comentario
multilinea
"""

# VARIABLES (caseSensitive).
# inician con una letra (caracter alfanumerico o guiones bajos) o guion bajo, no puede iniciar con un numero, es creada cuando se asigna un valor.
# No se puede utilizar palabras reservadas.

x=5
X=6
mivariable="Esto es un texto"
_mivariable = 'otro texto'
_mivariable2='otro texto mas'

print(x)
print(X)
print(mivariable)

# CONVENCIONES
# Camel Case        

camelCase = 'Comienza con minuscula, y la otra con mayuscula'
PascalCase = 'Comienza con mayuscula, y la otra con mayuscula'
snake_case = 'Son minuscula y son separadas con guiones bajos.' 

w,y,z = 6,7,9

print(w)
print(y)
print(z)

a = b = c = 'Manuel Parra'
print(a)
print(b)
print(c)

b = 'soy un cacahuate'
print(a)
print(b)
print(c)

# COLECCIONES
frutas = ["banana","naranja","mandarina"]
m,n,o = frutas
print(m)
print(n)
print(o)

texto1="Curso"
texto2="de"
texto3="Python"
print(texto1,texto2,texto3)
print(texto1+texto2+texto3)

num1=2
num2=4
num3=6
print(num1+num2+num3)
print(num1,num2,num3)

print(texto1,num1)

# VARIABLES GLOBALES VS VARIABLES Scope (alcance de una variable)

variableGlobal = 'Disponible para todo el programa'
print(variableGlobal)

def funcion():
    variableDeScope = 'Solo disponible en la funcion'
    global variableDeScope2
    variableDeScope2 = 'Variable de Scope transformada a global'
    variableGlobal = "Valor especial dentro de la funcion"
    print(variableGlobal)
    print(variableDeScope)
    print(variableDeScope2)

funcion()

print(variableGlobal)
print(variableDeScope2)


# TIPOS DE DATOS

variablestring = 'hola'
numero_entero = 13
numero_decimal = 1.25
numero_complejo = 5 + 2j
lista_lista = [0,1,2,3,4,5]     # ordenada y mutable
tupla = (0,1,2,3,4,5)       #inmutable y ordenada
tupla = ("a","b","c")
range_range = range(1,10)           
dictionary = {                      # clave-valor desordenad y mutable
    "nombre":"Sergie Code",         
    "edad":5,
    "diccionario":{
        "nombre":"cuautemoc parra"
    }
}

set_set = {1,1,2,3,4,4}             # desordenada y mutabñle
frozen_set = frozenset([1,2,3,3,3])     # desordenada e inmutable
booleano = True
bool_falso = False

print(numero_decimal)
print(type(numero_decimal))

print(numero_entero)
print(type(numero_entero))

print(numero_complejo)
print(type(numero_complejo))

# CAST

decimal_desde_entero = float(numero_entero)
entero_desde_decimal = int(numero_decimal)
complejo_desde_decimal = complex(numero_decimal)
complejo_desde_entero = complex(numero_entero)

# RANDOM

import random 

aleatorio = random.randrange(1,10)      # imprime del 1 al 9, el de stop no se incluye
print(aleatorio)

aleatorio_par = random.randrange(2,11,2)        # numero par
print(aleatorio_par)

aleatorio_impar = random.randrange(1,10,2)      # numero impar
print(aleatorio_impar)


#STRINGS

print(variablestring)
print(type(variablestring))

texto_string = "Este es un curso de manuel"
caracter = texto_string[2]
print(caracter)

amplitud = len(texto_string)
print(amplitud)

print("manuel" in texto_string)         # devuelve true o false
print("Manuel" in texto_string)
print("Manuel".lower() in texto_string.lower())

print("francisco" not in texto_string)

print(texto_string[11:16])
print(texto_string[:5])
print(texto_string[11:])
print(texto_string[-6:])
print(texto_string[:-15])

# MODIFICADORES

mayusculas = texto_string.upper()
print(mayusculas)

minusculas = texto_string.lower()
print(minusculas)

texto_con_espacios="           hola mundo            "
texto_sin_espacios= texto_con_espacios.strip()
print(texto_con_espacios)
print(texto_sin_espacios)

reemplazo = texto_con_espacios.replace("mundo","universo")
print(reemplazo)
reemplazo = texto_con_espacios.replace("mundo","universo").strip()
print(reemplazo)

texto_con_comas = "No, se, olviden, de, suscribirse"
separar_por_comas = texto_con_comas.split(",")
print(separar_por_comas)        # devuelde un array

texto_a = "Hola"
texto_b = "Mundo"
texto_c = texto_a+" "+texto_b
print(texto_c)

# F-strins o Templete Strings

nums1 = 5
nombre = "Pedro"
edad1 = "edad"
txt1 = f"La {edad1} de {nombre} es de {nums1:.2f}" 
print(txt1)

resultado1 = f"El resultado de 69 x 75 es {69-75}" 
print(resultado1)

#Escapes \ backlash - barra invertida

escape = "Mi pais favorito es \"México\" porque nací ahí"
directorio = "El directorio donde está almacenado mi mayor secreto es c:\\secreto\\archivo.txt"
salto_de_linea = "Quiero hacer un \nsalto de linea"
print(escape)
print(directorio)
print(salto_de_linea)

# METODOS MAS USADOS

texto_a_modificar = "este es UN texto A MODIFICAR"
capitalizado = texto_a_modificar.capitalize()
print(capitalizado)
esta_comenzando = texto_a_modificar.startswith("este")
print(esta_comenzando)
esta_finalizando = texto_a_modificar.endswith("MODIFICAR")
print(esta_finalizando)
titulo = texto_a_modificar.title()          # mayuscula cada palabra
print(titulo)

contador = texto_a_modificar.count("e")
print(contador)

encontrador = texto_a_modificar.find("texto")
print(encontrador)

