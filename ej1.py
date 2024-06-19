import os, time
from funciones import *


while True:
    os.system('cls')
    print("menu contactos")
    print("1.agregar contacto\n2.ver contactos\n3.exportar archivo CSV\n4.salir")
    opc = int(input("ingrese opcion: "))

    os.system("cls")
    if opc==1:
        opcion_1()
    elif opc==2:
        opcion_2()
    elif opc==3:
        opcion_3()
    else:
        opcion_4()