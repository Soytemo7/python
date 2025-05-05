 # booleanos

a = True
b = False

print(5>3)

### structuras que devuelven verdadero

string = bool("No se olviden")
print(string)

num = bool(2025)
print(num)


lista = bool(["Naranja","Manzana"])
print(lista)

dictionario = bool({"nombre":"Sergio"})
print(dictionario)

### estructura que devuelve falso

string2 = bool("")
print(string2)

num2 = bool(0)
print(num2)

lista2=bool([])
print(lista2)

dict2 = bool({})
print(dict2)

none = bool(None)           # llamado null en otros lenguajes
print(none)


# OPERADORES

# Aritmeticos  + - * / % ** // 

a = 10
b = 5

print(a+b)
print(a-b)
print(a*b)
print(a/b)      # devuelve flotante
print(a%b)
print(a//b)
print(a**b)

# OPERADORES DE ASIGNACION

x = 10
print(x)

x += 3
print(x)

x -=2
print(x)

x *= 2
print(x)

x /=2
print(x)

# OPERADORES DE COMPARACION

num1 = 5
num2 = 5

igualdad = num1 == num2
print(igualdad)

distintos=num1 != num2
print(distintos)

mayor = num1 > num2
print(mayor)

menor = num1 < num2
print(menor)

mayor2 = num1 >= num2
print(mayor2)

menor2 = num1 <= num2
print(menor2)

# OPERADORES LOGICOS and, or, not

edad = 17
tramite = edad >= 18 and edad<=65
print(tramite)

semaforo = "Verde"
cruzar = semaforo == "Verde" or semaforo == "Amarillo"
print(cruzar)

verdad = True
mentira = False
print(not verdad)
print(not mentira)

# OPERADORES DE IDENTIDAD is, is not

nombre = "Manuel"
profesor = "Manuel"
son_el_mismo = nombre is profesor
print(son_el_mismo)

alumno = "Pedro"
print(profesor is not alumno)

# OPERADORES DE PERTENENCIA in, not in 

palabra = "Mundo"
texto = "Hola Mundo"
palabra2 = "Mercurio"

pertenece = palabra in texto
print(pertenece)

no_pertenece = palabra2 not in texto
print(no_pertenece)

# CONDICIONALES if (obligatorio), elif(opcional), else(opcional)

aa = 5
bb = 10
cc = 7

if aa>bb:
    print(f"{aa} es mayor que {bb}")
elif cc>bb:
    print(f"{cc} es mayor que {bb}")
else:
    print(f"{aa} es menor que {bb} y {cc} es menor que {bb}")


edad2 = 65

if edad2 >= 18 and edad2<=60:
    print("Puedes entrar al boliche")
else:
    if edad2 < 18:    
        print("No tienes edad para entrar al boliche")
    else:
        print("Este boliche solo admite persona hasta 60 años")

### SHORTHANDS

a = 5
b = 10
c = 7

if a > b : print(f"{a} es mayor que {b}")       # if solo
print("B es mayor que A") if b > a else print("A es mayor que B")       ## if + else

### BUCLE WHILE         

x = 1

while x<=10:
    print(f"Hola a todos, estoy en un bucle y x vale {x}")     
    if x == 5:  
        break
    x += 1

x=0
while x<10:
    x += 1
    if x == 5:  
        continue
    print(f"Hola a todos, estoy en un bucle y x vale {x}")     

x = 1

while x<=10:
    print(f"Hola a todos, estoy en un bucle y x vale {x}")         
    x += 1
else:
    print(f"Ya no se imprimio el numero {x} por no cumplir la condicion")


while True:    
    respuesta = input("¿Desea salir? (s/n)").strip().lower()
    if respuesta == 's':
        break

# BUCLE FOR

lenguajes = ["Python","JS","Java","C#","Angular","React","Django"]

for lenguaje in lenguajes:
    if lenguaje == "React":
        break    
    if lenguaje == "C#":
        continue
    print(lenguaje)

texto = "No te olvides de mi"

for caracter in texto:
    print(caracter)
else:
    print("FUE TODO...")

for x in range(5):
    print (x)

for x in range(2,10):
    print(x)

for x in range(2,11,2):
    print(x)

impares = [1,3,5,7,9]
pares = [2,4,6,8,10]

for impar in impares:
    for par in pares:
        print(impar,par)

# LISTAS (ordenada y mutable)

frutas = ['Naranja','Manzana','Pera']
print(frutas)
print(frutas[1])

longitud=len(frutas)
print(longitud)

listaStrings = ['a','b','c']
listaNumber = [1,2,3]
listaBooleans = [True,False]
listaMixta = ['a',1,False]
listaDesdeContructuor = list(('a',2,False))

print(listaStrings)
print(listaNumber)
print(listaBooleans)
print(listaMixta)
print(listaDesdeContructuor)

naranja = frutas[0]
parteLista = frutas[1:3]
print(naranja)
print(parteLista)
print(frutas[:2])
print(frutas[1:])
print(frutas[-1])
print(frutas[:-2])

if "Manzana" in frutas:
    print("Si, esta incluido la Manzana")

tecnologias = ["Python","JS","Java","C#","Angular","React","Django"]
print(tecnologias)
tecnologias[3]="Tensorflow"
print(tecnologias)
tecnologias[2:4] = ['C++','C#']
print(tecnologias)
tecnologias.insert(2,'Flask')
print(tecnologias)
tecnologias.append("Go")
print(tecnologias)

fronted = ["Angular","VUE","React"]
frontedTuple = ("Angular","VUE","React")

tecnologias.extend(fronted)
print(tecnologias)
tecnologias.extend(frontedTuple)
print(tecnologias)

tecnologias.remove('VUE')
print(tecnologias)
tecnologias.pop()
print(tecnologias)
tecnologias.pop(2)
print(tecnologias)
del tecnologias[2]
print(tecnologias)

listaaBorrar =  ["Python","JS","Java","C#","Angular","React","Django"]
print(listaaBorrar)
listaaBorrar.clear()
print(listaaBorrar)
print(tecnologias)

for tecnologia in tecnologias:
    print(tecnologia)

for i in range(len(tecnologias)):
    print(i)
    print(tecnologias[i])

for i in range(len(tecnologias)):
    print(f"{i+1}. {tecnologias[i]}")
    
for i in range(len(tecnologias)):
    print(i)
    print(tecnologias[i])

[print(tecnologia) for tecnologia in tecnologias]

listaconY=[]
for tecnologia in tecnologias:
    if "y" in tecnologia:
        listaconY.append(tecnologia)
    
print("Lista con Y")
print(listaconY)

lista2conY = [tecnologia.upper() for tecnologia in tecnologias if "y" in tecnologia]
print("Lista 2 con Y")
print(lista2conY)

print(tecnologias)

tecnologias.sort()
print(tecnologias)

numeros = [9,7,4,5,8]
print(numeros)
numeros.sort()
print(numeros)
numeros.sort(reverse=True)
print(numeros)

print(tecnologias)
tecnologias.reverse()
print(tecnologias)

meses = ["enero","Febrero"]
meses2 = ["marzo","abril"]

copiaMeses = meses.copy()
print(copiaMeses)

copiaMeses2 = list(meses)
print(copiaMeses2)

joinmeses=meses+meses2
print(joinmeses)

meses.extend(meses2)
print(meses)

# TUPLAS    ordenada e inmutable

tupla2 = ("a","b","c","c")
vehiculos = ("Bicicleta","Moto","Auto","Camioneta","Avion","Barco")

print(tupla2)
print(vehiculos)

longitud2 = len(vehiculos)
print(longitud2)

tipovehiculos = type(vehiculos)
print(tipovehiculos)

tupla3 = (2,True,"Suscribete")
print(tupla3)

tuplaContructor = tuple(("Esta","es","una","tupla"))
print(tuplaContructor)
print(type(tuplaContructor))

elemento1 = vehiculos[1]
print(elemento1)

elemento2 = vehiculos[-1]
print(elemento2)

rango2 = vehiculos[2:4]
print(rango2)

desdeelinicio = vehiculos[:3]
hastaelfinal = vehiculos[3:]
print(desdeelinicio)
print(hastaelfinal)

# otra tupla

listaVehiculos = list(vehiculos)
print(listaVehiculos)
listaVehiculos[3]="Camion"
listaVehiculos.append("Crucero")
print(listaVehiculos)
print(type(listaVehiculos))

vehiculos = tuple(listaVehiculos)
print(vehiculos)
print(type(vehiculos))

#Desempaquetamiento

(a,b,c,d,e,f,g) = vehiculos
print(a)
print(b)

(bici,moto,*cuadroruedas,avion,barco,crucero) = vehiculos
print(bici)
print(cuadroruedas)
print(type(cuadroruedas))

for vehiculo in vehiculos:
    print(vehiculo)

for i in range(len(vehiculos)):
    print(f"{i+1}. {vehiculos[i]}")

[print(vehiculo) for vehiculo in vehiculos]

citricos = ("naranja","limon","pomelo")
tropical = ("papaya","coco")

frutas  = citricos + tropical
print(frutas)
print(type(frutas))

doblecitrico = citricos * 2
print(doblecitrico)

