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
