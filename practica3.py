 
def mostrar_menu():
    print("\nAgenda de Cotnactos")
    print("1.-Agregar nuevo contacto")
    print("2.-Eliminar contacto")
    print("3.-Buscar contacto")
    print("4.Lista de contactos")
    print("5.-Salir del programa")
    print("\n")

def agregar_contacto(agenda):
    nombre = input("Introduzca el nombre completo del contacto: ")
    telefono = input("Introduzca el telefono del contacto: ")
    email = input("Introduzca el email del contacto: ")

    agenda[nombre] = {"telefono":telefono,"email":email}
    print(f"Se ha agregado el contacto {nombre} exitosamente")

def eliminar_contacto(agenda):
    nombre=input("Ingrese el nombre de la agenda a eliminar")
    if nombre in agenda:
        del agenda[nombre]
        print(f"El contacto de {nombre} ha sido eliminado correctamente")
    else:
        print(f"No se ha encontrado el contacto {nombre}")

def buscar_contacto(agenda):
    nombre = input("Ingrese el nombre del contacto a buscar: ")
    if nombre in agenda:
        print(f"Nombre: {nombre}")
        print(f"Telefono: {agenda[nombre]['telefono']}")
        print(f"Email: {agenda[nombre]['email']}")
    else:
        print(f"El contacto {nombre} no ha sido encontrado en la agenda")

def listar_contactos(agenda):
    if agenda:
        print("\nLista de contactos:")
        for nombre,info in agenda.items():
            print(f"Nombre: {nombre}")
            print(f"Telefono: {info["telefono"]}")
            print(f"Email: {info["email"]}")
            print("-" * 20)
    else:
        print("La agenda aún esta vacia")

def agenda_contacto():
    agenda = {}

    while True:
        mostrar_menu()
        opcion = input("Elija una opcion: ")
        print("\n")

        if opcion=="1":
            agregar_contacto(agenda)
        elif opcion=="2":
            eliminar_contacto(agenda)
        elif opcion=="3":
            buscar_contacto(agenda)
        elif opcion=="4":
            listar_contactos(agenda)
        elif opcion=="5":
            print("Saliendo de la agenda de contactos")
            break
        else:
            print("Por favor seleccione una opcion valida (1 al 5)")

agenda_contacto()