#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 24 17:29:29 2021

@author: dr.guillermo

Code for solving the differential equation
using Predictor-Corrector or Improved-Euler method
with initial conditions 
to find the aproximation to yfinal 

Algorithm taken from the book:
Numerical methods applied to engineering, page 549
"""
import numpy as np
import matplotlib.pyplot as plt

# solicitamos al usuario las condiones iniciales
x =  float(input('Da valor inicial de x: '))
xf = float(input('Da valor final de x: '))
y =  float(input('Da valor inicial de y: '))
# leemos n, para que quede más claro lo manejamos 
# como subintervalos o numero de iteraciones:
it = int(input('Da el número de subintervalos(iteraciones): '))

#inicializamos los vectores para registrar los valores x,y (xV,yV)
# llenamos el vector con ceros
xV = np.zeros(it+1)
# valor inicial x
xV[0] = x 

yV = np.zeros(it+1)
# valor inicial de y 
yV[0] = y

# Algoritmo tomado del libro:
# Métodos numéricos aplicados a la ingeniería, pag 549 

# Función en donde insertamos la ED a resolver
def f(x,y):
  return (x-y)

# Paso 1
# Calculamos el valor de h
h= (xf - x)/it
# Calculamos los valores de x+h
for i in range(it):
  xV[i+1] = xV[i] + h
  
# Paso 2 Y 3 
for i in range(0,it):
    # Paso 4 PREDICTOR valor temporal 
    ft = yV[i] + h*(f(xV[i],yV[i]))
    # Paso 5 CORRECTOR 
    yV[i+1] = yV[i] + h*( (f(xV[i],yV[i]) + f(xV[i+1],ft) )/ 2 )
    # Paso 6 y 7 - el incremento x+h ya esta en el vector x,
    # solamente tomamos el valor para la iteración siguiente
print() 
   
# paso 8 imprimir resultado
print('Resultado:')
#print(xV)
# Creamos una lista con el arreglo yV
nlist = list()
for i in yV:
  nlist.append(i)
for i in nlist:
  print(i)
#print(yV)

# Gráfica
plt.scatter(xV,yV).set_color("blue")
plt.title('ED - Método de Euler mejorado')
plt.xlabel('Intervalo x')
plt.ylabel('y')
plt.grid() 
