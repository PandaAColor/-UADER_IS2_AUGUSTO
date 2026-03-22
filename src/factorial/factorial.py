#!/usr/bin/python
#*-------------------------------------------------------------------------*
#* factorial.py                                                            *
#* calcula el factorial de un número                                       *
#* Dr.P.E.Colla (c) 2022                                                   *
#* Creative commons                                                        *
#*-------------------------------------------------------------------------*
import sys
def factorial(num): 
    if num < 0: 
        print("Factorial de un número negativo no existe")
        return 0
    elif num == 0: 
        return 1
        
    else: 
        fact = 1
        while(num > 1): 
            fact *= num 
            num -= 1
        return fact 

if len(sys.argv) < 2: #si el usuario no ingresa nada le pide el rango explícitamente
   rango=input('Introduzca el rango')
   
else: #si al ejecutarlo ya agrega el rango se lo toma
    rango=sys.argv[1]
    
if rango.startswith('-'): #caso en que no se introduzca min pero si max
    min =1
    max = int(rango.replace('-', ''))

elif rango.endswith('-'): #se introduce min pero no max
    min = int(rango.replace('-', ''))
    max = 60

else: #tamto max como min fueron introducidos
    rango_lista = rango.split('-') #separa cada parte del rango y la pone en una lista
    min = int(rango_lista[0])
    max = int(rango_lista[1])

if min >max:
    a = max
    max = min
    min = a

for i in range(min, max+1): #imprime el factorial desde el min hasta el max incluido
    print("Factorial ",i,"! es ", factorial(i))

