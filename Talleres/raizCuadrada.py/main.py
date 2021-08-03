import math

def metodo_babilonico(n, e):

    decimales = "."+str(e)+"f"
    e = pow(10, -e)
    x = n
    y = (1 / 2) * (x+(n / x))
    valorReal = math.sqrt(n)
    iteraciones = 0

    print("\nValores de 'y' en las iteraciones:")
    while abs(x - y) > e:

        x = y
        y = (1 / 2) * (x+(n / x))
        print(format(y, decimales))
        errorRelativo = abs((valorReal-y)/valorReal)
        print(" Error relativo: ", errorRelativo )
        iteraciones += 1

    print('Numero de iteraciones: ', iteraciones)
    return y


n = 7
e = 8
decimales ="."+str(e)+"f"

print(
    "\nLa raiz cuadrada de",
    n,
    ", con el metodo de la biblioteca math, es",
    math.sqrt(n))

print(
    "La raiz cuadrada de",
    n,
    ", con tolerancia 10 a la -",e,", es",
    format(metodo_babilonico(n, e), decimales),
)

e = 16
decimales ="."+str(e)+"f"

print(
    "La raiz cuadrada de",
    n,
    ", con tolerancia 10 a la -",e,", es",
    format(metodo_babilonico(n, e), decimales),
)
