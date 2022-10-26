# -*- coding: utf-8 -*-
"""
Created on Wed Oct 26 09:23:21 2022

@author: user
"""
import camelcase

nombre = "jhon percy baldeon figueroa"
print(nombre.upper())
print(nombre.title())

cam = camelcase.CamelCase()
print("Con camelcase")

#imprimimos el nombre en fromato titulo
#utilizamos camelcase
print(cam.hump(nombre))

#Para resolver el problema, ceramos otro objeto, incluimos los argumento
#'Jhon' y 'leon'

cam2=camelcase.CamelCase('jhon','baldeon')
print(cam2.hump(nombre))