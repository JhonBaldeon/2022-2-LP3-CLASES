# -*- coding: utf-8 -*-
"""
Created on Wed Oct 26 08:51:04 2022

@author: user
"""

#Dado el subtotal, calcular el IGV y el total

import financieros
subtotal = 800.77
print(f"Subtotal: {subtotal}")
print(f"IGV: {financieros.obtenerIGVconSubtotal(subtotal):.2f}")
print(f"Total:{financieros.obtenerTotalconSubtotal(subtotal):.2f}")