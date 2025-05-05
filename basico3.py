 
# CONJUNTOS O SETS desordenada unicos inmutables, se puede agrega y eliminar, pero no cambiar algun elemento al no tener indice

conjunto = {1,1,2,2,3,4,True,"Suscribte"}

print(conjunto)
print(type(conjunto))


longitud = len(conjunto)
print(longitud)

constructor = set(("Este","es","un","conjunto"))
print(constructor)

if "conjunto" in constructor:
    print("Si esta la palabra conjunto")

if "Python" not in constructor:
    print("Python no esta en el conjjunto")

telefonos = {"xiaomi","Samsung","motorola","motorola"}
telefonos2 = {"Huawei",'Oneplus','Nokia','xiaomi'}
telefonos3 = ["Huawei",'Oneplus','Nokia','xiaomi']
print(telefonos)

telefonos.add("Iphone")
print(telefonos)

telefonos.update(telefonos2)
print(telefonos)
telefonos.update(telefonos3)
print(telefonos)
print(type(telefonos))

telefonos.remove("xiaomi")          # da error si no existe
print(telefonos)

telefonos.discard("Samsung")        # no da error si no existe
print(telefonos)

telefonos.pop()     #eliminara al azar
print(telefonos)
telefonos2.clear()
print(telefonos2)


vehiculos = {"auto","coche","avion"}

for vehiculo in vehiculos:
    print(vehiculo)

[print(vehiculo) for vehiculo in vehiculos]

#join de sets (teoria de conjuntos)

a = {1,2,3,4,5}
b = {1,3,5,7,9}

#union (update)

c = a.union(b)      # no modifica al original
print(a)
print(c)

a = {1,2,3,4,5}
b = {1,3,5,7,9}

d = a.update(b)     # modifica al original
print(a)
print(d)

a = {1,2,3,4,5}
b = {1,3,5,7,9}

e = a | b   # igual que usar union
print(e)

# interseccion, elementos en comun

i = a.intersection(b)
i2 = a & b          # mismo que intersection
print(i) 
print(i2)

a.intersection_update(b)    #modifica el conjunto original
print(a)

a = {1,2,3,4,5}
b = {1,3,5,7,9}
booleanos = {True,False,True}

booleanosUnion = a.union(booleanos)         # true y 1 es lo mismo, false y 0 es lo mismo
booleanosInterseccion = a.intersection(booleanos)
print(booleanosUnion)
print(booleanosInterseccion)

# diferencias  elementos del 1er conjunto no presentes en el 2do

d= a.difference(b)
d2 = b.difference(a)
d3 = b - a
print(d)
print(d2)
print(d3)

a.difference_update(b)      #modifica el conjutno original
print(a)


a = {1,2,3,4,5}
b = {1,3,5,7,9}

#diferencia simetrica: elementos no presentes en ambos conjutnos

ds1 = a.symmetric_difference(b)
ds2 = a ^ b
print(ds1)
print(ds2)

a.symmetric_difference_update(b)
print(a)

# DICCIONARIOS clave:valor, desordenada y mutable

diccionario = {
    "nombre":"Manuel",
    "youtube":"www.youtube.com",
    "edad":34,
    "tecnologias":['Python','js'],
    "direccion":{
        "calle":"Avenida Argentina",
        "numero":3,
        "ciudad":"Londres"
    }
}

print(diccionario)
print(type(diccionario))
print(len(diccionario))

constructor2 =dict(nombre='Manuel',apellido='parra')
print(constructor2)

nombre = diccionario["nombre"]
print(nombre)

youtube = diccionario.get("youtube")
print(youtube)

keys = diccionario.keys()
print(keys)
print(type(keys))

value = diccionario.values()
print(value)
print(type(value))

items = diccionario.items()         
print(items)
print(type(items))

if "tecnologias" in diccionario:
    print("Si existe la tecnologia")

diccionario["tecnologias"] = ['python','JS','node']
print(diccionario)

diccionario.update({"direccion":{
    "calle":"Avenida Argentina",
    "numero":3,
    "ciudad":"Liverpool"
},})
print(diccionario)

diccionario["profesion"]="programador"
print(diccionario)

diccionario.update({'Comida Favorita':'Milanesa'})
print(diccionario)

diccionario.pop("Comida Favorita")
print(diccionario)

diccionario.popitem()       # elimina la ultima caracteristica.
print(diccionario)

del diccionario["edad"]
print(diccionario)

diccionario.clear()
print(diccionario)

curso_python = {
    "nombre": "Python desde cero",
    "duracion":6,
    "dificultad":"media-baja"    
}

for x in curso_python:          #imprime las keys
    print(x)


for key in curso_python:          
    print(f"{key.capitalize()} : {curso_python[key]}")


for values in curso_python.values():
    print(values)

for x,y in curso_python.items():        #desempaqueta la tupla de los elementos de la lista que devuelve items
    print(x,y)


copia = curso_python.copy()
copia2 = dict(curso_python)
print(copia)
print(copia2)

hijo1 = {
    "nombre":"Pedro",
    "edad":5
}
hijo2 = {
    "nombre":"Gonzales",
    "edad":5
}
hijo3 = {
    "nombre":"Manuel",
    "edad":6
}

familia = {
    "hijo1": hijo1,
    "hijo2": hijo2,
    "hijo3": hijo3
}

print(familia["hijo1"]["nombre"])
print(familia["hijo2"]["nombre"])
print(familia["hijo3"]["nombre"])

for x,obj in familia.items():
    print(x)
    for y in obj:
        print(y.capitalize(),obj[y])
    




