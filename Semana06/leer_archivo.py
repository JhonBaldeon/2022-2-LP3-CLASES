# -*- coding: utf-8 -*-
"""
Created on Wed Oct 26 10:12:07 2022

@author: user
"""

noticia = open("noticia.txt","rt",encoding='utf8')
datos_noticias = noticia.read()
print(datos_noticias)