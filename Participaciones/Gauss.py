# -*- coding: utf-8 -*-
"""
Created on Sat Aug 28 18:47:31 2021

@author: Diana Sofía Carrillo
"""
import numpy as np
import time
#Función que resuelve un sistema de ecuaciones con Gauss-Jordan
# a es la matríz con los coeficientes y b el vector con las constantes
def gauss(a, b):
  n = len(b) #Cantidad de ecuaciones
  c = np.zeros([n, n+1]) #Genera matriz de n * n+1 llena de ceros
  print("rango: ", np.ptp(a))
  for i in range (n):
    for j in range (n):
      c[i][j] = a[i][j] #Se crea la matriz aumentada
    c[i][n] = b[i]
  for k in range(n): #Se empieza con el proceso de normalización y reducción
    t = c[k][k] 
    for j in range (k, n+1):
      c[k][j] = c[k][j]/t #Se normaliza la fila k
    for i in range(k+1, n): #Se reducen las filas debajo
      t = c[i][k]
      for j in range (k, n+1):
        c[i][j] = c[i][j]-t*c[k][j]
  x = np.zeros([n, 1]) #Se genera la matriz llena de ceros para el vector solución
  x[n-1] = c[n-1][n] #Se llena la última posición del arreglo con la solución 
                     #de la última ecuación (la que no necesita despeje)
  for i in range(n-2, -1, -1): #Sistema triangular
      s = 0
      for j in range(i+1, n):
          s += c[i][j]*x[j]
      x[i] = c[i][n] - s
  
  return x

def gaussPivote(a, b):
    n = len(b)
    c = np.zeros([n, n+1])
    for i in range(n):
        for j in range(n):
            c[i][j] = a[i][j] #Matriz aumentada
        c[i][n] = b[i]
    for k in range(n): 
        p = k
        for i in range(k+1, n): #Selección del pivote
            if (abs(c[i][k])>abs(c[p][k])):
                p = i
        for j in range(k, n+1): #Intercambio de filas
            t = c[k][j]
            c[k][j] = c[p][j]
            c[p][j] = t
        t = c[k][k]
        if abs(t) < 1e-10: #Verificar que el sistema es singular
            return []
        for j in range(k, n+1): #Normalizar fila e
            c[k][j] = c[k][j]/t
        for i in range(k+1, n): #Reducir filas debajo
            t = c[i][k]
            for j in range(k, n+1):
                c[i][j] = c[i][j] - t*c[k][j]
    x = np.zeros([n,1]) #Celdas para el vector solución
    x[n-1] = c[n-1][n]
    for i in range (n-2, -1, -1): #Resolver el sistema triangular
        s = 0
        for j in range(i+1, n):
            s = s + c[i][j]*x[j]
        x[i] = c[i][n] - s
    return x
            
    
def conteoOperacionesGauss(n):
    operaciones = 0
    for i in range(n):
        for j in range (i + 1, n):
            for k in range (i, n + 1):
                operaciones += 1
    return operaciones

def error_relativo(v_obtenido, a, b):
    v_real = np.linalg.solve(a, b)
    rta = np.linalg.norm(v_obtenido - v_real) / np.linalg.norm(v_real)
    return rta

#np.set_printoptions(precision=9)
a = [[2, 3, 7], [-2, 5, 6], [8, 9, 4]]
b = [3, 5, 8]

#t1 = time.time()
x = gauss(a, b)
#print("--- %s seconds ---" % (time.time() - t1))
print ("\n--Resultado--")
print(x)

print("\nError Relativo:")
e = error_relativo(x, a, b)
print (e)


x2 = gaussPivote(a, b)
print(error_relativo(x2, a, b))

#Probar el alcance del error.
a = [[2.1, 3, 7], [-2, 5, 6], [8, 9, 4]]
x1 = gauss(a, b)
