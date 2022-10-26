# -*- coding: utf-8 -*-
"""
Created on Wed Oct 26 08:57:39 2022

@author: user
"""

#Dado el total, calcular el IGV y el subtotal

import financieros

total  = 1000.49
print(f"Subtotal: {financieros.obtenerSubtotalconTotal(total):.2f}")
print(f"IGV: {financieros.obtenerIGVconTotal(total): .2f}")
print(f"Total:{total}")