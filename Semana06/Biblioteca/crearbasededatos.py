# -*- coding: utf-8 -*-
"""
Created on Wed Oct 26 11:25:33 2022

@author: user
"""

import sqlite3

# Con el comando Connect buscara la base de datos que tenga ese nombre
# de lo contrario lo creara

conexion =sqlite3.connect("bdbiblioteca.db")
tabla_pais="""CREATE TABLE pais(
                idpais INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre TEXT UNIQUE,
                estado TEXT)
                """
tabla_editorial="""CREATE TABLE editorial(
                ideditorial INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre TEXT,
                estado TEXT
                )
                """
tabla_autor=""" CREATE TABLE autor(
                idautor INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre TEXT,
                f_nacimiento TEXT
                )
                """
tabla_libro="""CREATE TABLE libro(
               idlibro INTEGER PRIMARY KEY AUTOINCREMENT,
               titulo TEXT,
               cantidad INTEGER,
               anio INTEGER,
               precio REAL,
               estado TEXT,
               idpais INTEGER REFERENCE pais,
               ideditorial INTEGER REFERENCE editorial,
               idautor INTEGER REFERENCE autor
                )
            """
cursor = conexion.cursor()
cursor.execute(tabla_pais)
cursor.execute(tabla_editorial)
cursor.execute(tabla_autor)
cursor.execute(tabla_libro)

conexion.close()