# -*- coding: utf-8 -*-
"""
Created on Wed Oct 26 10:31:26 2022

@author: Baldeon
"""

import os
#Crear archivo
def crear_archivo(archivo_tecnologia, contenido):
    archivo = open(archivo_tecnologia,"at")
    archivo.write(contenido)
    archivo.close()
    
def eliminar_archivo(archivo_tecnologia):
    os.remove(archivo_tecnologia)
    
def agregar_archivo_contenido(archivo_tecnologia, contenido):
    with open(archivo_tecnologia, 'a') as noticia:
        noticia.write(contenido)
    
def leer_archivo(archivo_tecnologia):
    noticia = open(archivo_tecnologia)
    datos_noticia = noticia.read()
    print(datos_noticia)