# -*- coding: utf-8 -*-
"""
Created on Wed Oct 26 10:15:46 2022

@author: user
"""

archivo = open("archivo_de_prueba.txt","wt")
contenido = "Linea1 Hola amigos cómo están?\nLínea2 Bienvenido a la Untels."
archivo.write(contenido)
archivo.close()
