# -*- coding: utf-8 -*-
"""
Created on Wed Apr 17 16:05:32 2019

@author: Alumno
"""

#Ejercio 3
x=int(input("Ingrese el ángulo1: "))
y=int(input("Ingrese el ángulo2: "))
z=180-(x+y)
if  x== 90 or y==90 or z==90:
    print("Es un triángulo rectángulo")
elif z<90 or x<90 or y<90:
    print("Es un triángulo acutángulo")
elif z>90 or x>90 or y>90:
    print("Es un triángulo obtusángulo")
      



