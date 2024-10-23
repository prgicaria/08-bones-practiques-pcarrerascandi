#!/usr/bin/env python
'''Divisió entera. Aquest programa fa una divisió entera de dos números
Institut Icaria
Programació - 1r Batxillerat - Curs 2023-2024
Aquest programa demana dos números: un divident i un divisor, 
fa una divisió entera dels dos nombres i mostra per pantalla la divisió, 
el quocient i el residu.
'''
__author__ = ""
__authors__ = ""
__email__ = "pcarreras-candi@instituticaria.cat"
__date__ = 2024/10/23

divident = int(input("Introdueix el divident:"))
divisor = int(input("Introdueix el divisor:"))
quocient = divident//divisor
residu = divident % divisor

print(f"Divisió: {divident}/{divisor}")
print(f"Quocient: {quocient}")
print(f"Residu: {residu}")