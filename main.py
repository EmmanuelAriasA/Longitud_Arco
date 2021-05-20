# Arias Aguilar Emmanuel
''' 
Escribe un programa que lea un polinomio de grado n > 1 y encuentre su longitud de arco en un intervalo cerrado [a,b].

El programa tendrá las entradas:

    * Grado del polinomio
    * Coeficientes del polinomio
    * Intervalo cerrado [a,b].
    * Cantidad de cifras significativas.
    * Elección entre la regla de trapecios o de Simpson.

Y entregará como resultado:

    * El resultado de la integral de longitud de arco del polinomio en el intervalo, 
    por medio de la regla de trapecios o bien, la regla de Simpson.
    *La cantidad de subintervalos utilizados.
'''

# -----------------------------------------------------------------------------------------------------
from math import sqrt

# -----------------------------------------------------------------------------------------------------

def deriva(coef):
    derivada = []
    k = 1
    if((len(coef)) == 1):
        derivada.append(0)
    else:
        while(len(coef) > k):
            derivada.append(coef[k]*k)
            k = k+1
    return derivada

# -----------------------------------------------------------------------------------------------------

def horner(grdo, derivada, x):
    polinomio = 0
    for i in range(grdo):
        polinomio = polinomio + (derivada[i] * pow(x, i))

    #Una vez que termina de evaluar la función, para poder sacar la longitud de arco
    #Debemos seguir la formula que es: raiz(1+f'(x)^2)
    polinomio = sqrt(1+pow(polinomio, 2))

    return polinomio

# -----------------------------------------------------------------------------------------------------

def MetodTrapecio(a, b, n, tol, ValorAnt, derivada):
    sumatoria = resIntegral = 0
    deltaX = (b-a)/n  # delta x

    # procederemos a hacer la suma de riemmann
    for i in range(1, n):  # inicia en 1 y termina en n
        sumatoria += horner(grdo, derivada, (a+(i*deltaX)))

    # formula de la regla del trapecio
    resIntegral = (deltaX/2)*(horner(grdo, derivada, a) + 2*sumatoria + horner(grdo, derivada, b))

    #Calculamos el error
    err = ((resIntegral - ValorAnt)/resIntegral)*10

    #Imprimimos nuestros valores de cada iteración
    print("La aproximacion de la resIntegral es: " + str(resIntegral) + " obtenida con n = "+str(n))

    if(abs(err) >= tol):
        n += 10
        ValorAnt = resIntegral
        return MetodTrapecio(a, b, n, tol, ValorAnt, derivada)

    #Imprmimios nuestro valor final, junto con la cantidad de particiones que se hicieron
    print("El resultado de la resIntegral es: "+str(resIntegral))
    print("Calculado con "+str(n)+" particiones")

# -----------------------------------------------------------------------------------------------------

def MetodSimspon(a, b, n, tol, ValorAnt, derivada):
    sumatoria1 = sumatoria2 = resIntegral = 0
    deltaX = (b-a)/n

    # procederemos a hacer la suma de riemmann
    for i in range(1, n):
        if i % 2 == 0:
            sumatoria2 += horner(grdo, derivada, (a+(i*deltaX)))
        else:
            sumatoria1 += horner(grdo, derivada, (a+(i*deltaX)))

    # formula de la regla de simpson
    resIntegral = (deltaX/3)*(horner(grdo, derivada, a) + 4 * sumatoria1 + 2*sumatoria2 + horner(grdo, derivada, b))

    #Calculamos el error
    err = ((resIntegral - ValorAnt)/resIntegral)*100

    #Imprimimos nuestros valores de cada iteración
    print("La aproximacion de la resIntegral es: "+str(resIntegral) + " obtenida con n = "+str(n)+". El error es: "+str(err))

    if(abs(err) >= tol):
        n += 10
        ValorAnt = resIntegral
        return MetodSimspon(a, b, n, tol, ValorAnt, derivada)

    #Imprmimios nuestro valor final, junto con la cantidad de particiones que se hicieron
    print("Valor de la longitud de arco: "+str(resIntegral))
    print("Calculado con "+str(n)+" particiones")

# -----------------------------------------------------------------------------------------------------

def longitudArco():
    # Obtenemos la derivada de nuestro polinomio (Ya que con esa derivada)
    # Obtenemos la longitud de arco
    derivada = deriva(coef)

    # Y mandamos a algun metodo según haya tecleado el usuario
    if opc == 1:
        MetodTrapecio(a, b, n, tol, ValorAnt, derivada)
    elif opc == 2:
        MetodSimspon(a, b, n, tol, ValorAnt, derivada)
    else:
        print("Ingrese una opcion valida")


# ------------------------------------------------------------------------------------------------------
# Pedimos el grado del polinomio y este debe ser mayor a 1
grdo = int(input("Ingrese el grado del polinomio (debe ser mayor a 1): "))

# Array donde se guardaran los coeficientes de nuestro polinomio
coef = []
x = []

if grdo > 1:
    # Ingresamos los coeficientes del polinomio comenzando con el termino de mayor grado y terminando
    print("Ingresa los coeficientes empezando por el de mayor grado, y terminando con el de menor grado ")
    for i in range(grdo+1):
        coeficientes = float(input("Ingresa el coeficiente: "))
        coef.append(coeficientes)
    coef.reverse()

    a = b = 0
    # a y b no pueden ser iguales
    while a == b:
        a = float(input("Limite inferior: "))
        b = float(input("Limite superior: "))
        n = 6
        # Mientras sean diferentes los limites
        if(a != b):
            # Pedimos las cifras significativas
            csig = int(input("Cifras significativas: "))
            tol = 0.5*(10**(2-csig))
            ValorAnt = 0

            # E imprimimos el menú en pantalla
            print("\n1.- Metodo Trapecio\n2.- Metodo Simpson")
            opc = int(input("Ingresa el metodo que desea utilizar: "))
            # Y mandamos al metodo de longitud de arco
            longitudArco()

        #Si los limites son iguales, mandamos el mensaje
        else:
            print("El limite inferior no puede ser igual al superior")

#Si el grado del polinomio no es mayor a 1, mandamos el mensaje correspondiente
else:
    print("El grado debe ser mayor a 1")
