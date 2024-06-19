import csv

contactos=[]

def opcion_1():
    print("agregar contacto")
    nombre=input("ingrese nombre: ")
    telefono=int(input("ingrese telefono: "))
    correo =input("ingrese correo")
    contacto={"nombre":nombre,"telefono":telefono,"correo":correo}
    contactos.append(contacto)
    print("Contacto agregado")
    

def opcion_2():
    if not contactos:
        print("No existen contactos, registre uno en la opcion 1")
    else:
        print("\tlista de contactos")
        for c in contactos:
            print(f"NOMBRE: {c['nombres']}")
            print(f"TELEFONO: {c['telefono']}")
            print(f"CORREO: {c['correo']}\n")
 


def opcion_3():
    if not contactos:
        print("No existen contactos, registre uno en la opcion 1")
    else:
        nombre_arachivo = input("ingrese nombre del archivo: ")+".csv"
        with open(nombre_arachivo,"w",newline="") as archivo:
            escritor=csv.DictWriter(archivo, ["nombre","telefono","correo"])
            escritor.writerows(contactos)


def opcion_4():
    print("Gracias, a dios")
    exit()