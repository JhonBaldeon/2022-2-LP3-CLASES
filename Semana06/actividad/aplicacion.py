# -*- coding: utf-8 -*-
"""
Created on Wed Oct 26 21:03:55 2022

@author: Baldeon
"""

import os
import sys
from gestion_archivos import crear_archivo
from gestion_archivos import eliminar_archivo
from gestion_archivos import leer_archivo
from gestion_archivos import agregar_archivo_contenido



def crear():
    contenido = input("\nIngrese la noticia: ")
    crear_archivo("tecnologia.txt", contenido)

def eliminar():
    eliminar_archivo("tecnologia.txt")

def listar():
    leer_archivo("tecnologia.txt")

def agregar():
    contenido = input("\nIngrese el contenido: ")
    agregar_archivo_contenido("tecnologia.txt", contenido)
    
def salir():
    sys.exit()
    
def menu():
    opcion = input(" 1. Crear archivo \n 2. Eliminar archivo \n 3. Agregar contenido \n 4. Mostrar contenido de archivo \n 5. Salir \nIngrese su opcion:")  
    if opcion == "1":
        crear()
    elif opcion == "2":
        eliminar()
    elif opcion == "3":
        agregar()
    elif opcion == "4":
        listar()
    elif opcion == "5":
       salir()
       
menu()
