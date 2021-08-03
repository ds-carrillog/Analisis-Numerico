def suma(matriz, tamanio, triangulo):
  suma = 0
  operaciones = 0
  for i in range(0, tamanio):
    for j in range(0, tamanio):
      if triangulo == 1:
        if (i <= j):
          suma += matriz[i][j]
          operaciones += 1
      elif triangulo == 2:
        if (i >= j):
          suma += matriz[i][j]
          operaciones += 1
      else:
          suma += matriz[i][j]
          operaciones += 1

  print("\nLa suma toma: ",operaciones, " operaciones.")
  return suma

tamanio = 4
matriz = [[1, 2, 3, 4], [4, 5, 6, 4], [7, 8, 9, 4], [4, 4, 4, 4]]

#triangulo 1 para el triangulo superior, 2 para el inferior y cualquier otro numero para la matriz completa
print("La suma del triangulo superior de la matriz es: ", suma(matriz, tamanio, 1))

print("La suma del triangulo inferior de la matriz es: ", suma(matriz, tamanio, 2))

print("La suma de toda la matriz es: ", suma(matriz, tamanio, 3))

