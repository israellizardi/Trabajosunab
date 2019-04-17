# -*- coding: utf-8 -*-
"""
Editor de Spyder

Este es un archivo temporal.
"""
''
#Ejercicio 1
def rut():
    s=[2,3,4,5,6,7,2,3,4,5,6,7]
    r=input("Ingrese RUT sin codigo verificador: ")
    r=r[::-1]
    c=0
    d=0
    dv=0
    suma=0
    
    while c<len(r):
        d=int(r[c])*int(s[c])
        suma=suma+d
        c=c+1
    print (suma)
    v=11-(suma%11)
     
    if 0<v<10:
         dv=v
    elif v==11:
         dv=0
    elif v==10:
         str(dv)
         dv= "K"
    print("El digito verificador es: ",dv)
rut() 
    







