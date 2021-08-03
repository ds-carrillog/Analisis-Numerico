def metodo_horner(coeficientes, x):
  rta = coeficientes[0]
  n = len(coeficientes)
  numMultiplicaciones = 0
  numSumas = 0

  for i in range(1, n):
    rta = coeficientes[i] + x * rta 
    if not coeficientes[i] == 0: 
      numSumas += 1
    numMultiplicaciones +=1
  
  print("Numero de operaciones (sumas y multiplicaciones): ", numSumas, " y ",numMultiplicaciones)
  return rta

coeficientes = [1, 1, 0] #grado 10. Se necesita ingresas todos los coeficientes, desde el que acompaña la x con mayor grado hasta la de menor grado
x = 1

print("El valor del polinomio es" , metodo_horner(coeficientes, x))
