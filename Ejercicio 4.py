# -*- coding: utf-8 -*-
"""
Created on Wed Apr 17 16:05:59 2019

@author: Alumno
"""

#Ejercio 4
nombre=input("Nombre del clavadista: ")
d=float(input("Intruduzca el grado de dificultad: "))
jueces=7
x=0
i=0
I=0
puntajes=[]
for i in range(0,jueces) :
    x=float(input("Ingrese puntaje del juez: "))
    x=x+I
    puntajes.append(x)
    if I==0:
        I=1/2
puntajes.sort()

puntajes.pop(-1)

puntajes.pop(0)

r=(puntajes[0]+puntajes[1]+puntajes[2]+puntajes[3]+puntajes[4])*(3/5)
r=r*d
print("El puntaje del clavista es: ", r)