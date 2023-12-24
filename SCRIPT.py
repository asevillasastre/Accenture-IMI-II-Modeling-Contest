# -*- coding: utf-8 -*-
"""
Created on Fri Oct 11 15:17:57 2019

@author: migue
"""

import time
import datetime

prime_list = [1, 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47,
            53, 59, 61, 67, 71, 73, 79, 83, 89, 97]

"""En algunas funciones hay varios 'returns' y 'breaks' dentro de bucles.
Aunque no es lo corrrecto, lo hemos programado así con el onjetivo de reducir
el tiempo del algoritmo.
"""

depth = 4

class factores:
    """Estas clases serán productos, cada producto tendrá 3 atributos:
        'long' nos indica el número de primos utilizados hasta el momento.
        'prod' es el producto de los elementos de inside.
        'inside' son los factores de nuestro producto.
    """
    def __init__(self, lista):
        """Tenemos distintas formas de crear esta clase, la más típica es con
        una lista, sin embargo, también podemos crearlas usando enteros u
        objetos 'sumandos'
        """
        if type(lista) == list:
            self.long = lista[0]
            self.prod = lista[1]
            self.inside = lista[2]
        elif type(lista) == int:
            self.long = 1
            self.prod = lista
            self.inside = [sumandos(lista)]
        elif type(lista) == sumandos:
            self.long = lista.long
            self.prod = lista.sum
            self.inside = [lista]
        else:
            self.long = lista.long
            self.prod = lista.prod
            self.inside = lista.inside

    def __mul__(self, factor):
        """Con esta función podemos multiplicar objetos 'factores', en el caso
        de que intentemos multiplicar 'self' por algo que no sea un objeto
        'factores', creamos el objeto y después multiplicamos.
        """
        if type(factor) == factores:
            result = factores([
                    self.long+factor.long, self.prod*factor.prod,
                    [self, factor]
                    ])
        elif factor == 1:
            result = self
        else:
            result = self*factores(factor)
        return result

    def __add__(self, factor):
        """Con esta función podemos sumar objetos 'factores'."""
        if type(factor) == sumandos:
            result = sumandos(self)+factor
        elif factor == 0:
            result = self
        else:
            result = sumandos(self)+sumandos(factor)
        return result

    def __sub__(self, sumando):
        """Con esta función podemos restar objetos 'factores'."""
        return self+ sumando*(-1)

    def __str__(self):
        """Aquí conseguimos 'imprimir' correctamente los 'factores'."""
        if type(self.inside[0]) == sumandos:
            if self.inside[0].long == 1 and self.inside[0].inside[0]>0:
                result = str(self.inside[0])
            else:
                result = "("+str(self.inside[0])+")"
        else:
            result = str(self.inside[0])
        for i in range(len(self.inside)-1):
            if type(self.inside[i+1]) == sumandos:
                if self.inside[i+1].long == 1 and self.inside[i+1].inside[0]>0:
                    result = "*"+str(self.inside[i+1])
                else:
                    result += "*("+str(self.inside[i+1])+")"
            else:
                result += "*"+str(self.inside[i+1])
        return result

class sumandos:
    """Estas clases serán sumas, cada suma tendrá 3 atributos:
        'long' nos indica el número de primos utilizados hasta el momento.
        'sum' es el producto de los elementos de inside.
        'inside' son los sumandos de nuestra suma.
    """
    def __init__(self, lista):
        """Tenemos distintas formas de crear esta clase, la más típica es con
        una lista, sin embargo, también podemos crearlas usando enteros u
        objetos 'factores'
        """
        if type(lista) == list:
            self.long = lista[0]
            self.sum = lista[1]
            self.inside = lista[2]

        elif type(lista) == int:
            self.long = 1
            self.sum = lista
            self.inside = [lista]
        elif type(lista) == factores:
            self.long = lista.long
            self.sum = lista.prod
            self.inside = [lista]
        else:
            self.long = lista.long
            self.sum = lista.sum
            self.inside = lista.inside

    def __add__(self, sumando):
        """Con esta función podemos sumar objetos 'sumandos', en el caso
        de que intentemos sumar 'self' por algo que no sea un objeto
        'sumandos', creamos el objeto y después sumamos.
        """
        if type(sumando) == sumandos:
            result = sumandos([
                    self.long+sumando.long, self.sum+sumando.sum,
                    [self,sumando]
                    ])
        elif sumando == 0:
            result = self
        else:
            result = self+sumandos(sumando)
        return result
    def __sub__(self, sumando):
        """Con esta función podemos restar objetos 'sumandos'."""
        return self+ sumando*(-1)

    def __mul__(self, sumando):
        """Con esta función podemos multiplicar objetos 'sumandos'."""
        if type(sumando) == factores:
            result = factores(self)*sumando
        elif sumando == 1:
            result = self
        else:
            result = factores(self)*factores(sumando)
        return result

    def __str__(self):
        """Aquí conseguimos 'imprimir' correctamente los 'sumandos'."""
        result = str(self.inside[0])
        for i in range(len(self.inside)-1):
            if type(self.inside[i+1]) == int and self.inside[i+1] < 0:
                result += str(self.inside[i+1])
            elif ((type(self.inside[i+1]) == sumandos and
                type(self.inside[i+1].inside[0]) == int and
                self.inside[i+1].inside[0]) < 0):
                result += str(self.inside[i+1])
            else:
                result += "+"+str(self.inside[i+1])
        return result

class descomp:
    """El objetivo es que al imprimir uno de estos elementos nos salga escrito
    el resultado.
    """
    def __init__(self, lista):
        """La lista introducida es un par con el
        'ID' de la prueba y el resultado.
        """
        self.ID = lista[0]
        self.result = lista[1]

    def __str__(self):
        """Con esto conseguimos devolver los caracteres correctos."""
        ID, long, res = str(self.ID), str(self.result.long), str(self.result)
        return "REZZ|"+ID+"|"+long+"|"+res

def brain(n, lista, lista_no1, deep):
    """Esta función es recursiva, se encarga de sacar una lista con
    "factoizaciones" de 'n', después con otra función escogeremos la mejor
    factorización.
        'n' es el número objetivo.
        'lista' es una lista con los "primos" que podemos usar.
        'lista_no1' es una lista con los primos que podemos usar.
        'deep' es un natural, señala las ramificaciones que se irán sacando.
    'deep' crea ramificaciones.
    El objetivo, recordemos, es obtener buenas "factorizaciones" en poco
    tiempo.
    La función devuelve una lista de factorizaciones, para escoger
    la mejor usaremos la función selector.
    """
    result, save = [], [[0,0]]*deep
    if n <= 10**3:
        return [n_menor_1000(n, lista, lista_no1)] #Si el número es pequeño usamos otra función.
    elif n <= 10**4:
        save = [[0, 0], [[0, 0]]*(deep+10)]
    elif n <= 10**5:
        save = [[0, 0], [[0, 0]]*(deep+7)]
    elif n <= 10**8:
        save = [[0, 0], [[0, 0]]*(deep+5)]
    else:
        save = [[0, 0], [[0, 0]]*deep]
    """Básicamente, cuando más pequeño sea el número, más ramificaciones habrá.
    
    """
    divid = factorio(n, lista_no1)
    if divid != []:
        save[0] = [divid[-1], 0]
        """En esta parte, vamos a ver si renta dividir por primos,
        si dividimos por primos pequeños (por ejemplo 5 veces por 2),
        es probable que podamos expresar 32 como 31+1 ahorrando pasos.
        """
        if len(divid) >= 3:
            for i in range(len(divid)-2):
                product = prod_list(divid[i:])
                if product != n and product > 20:
                    possible_reduction = selector(brain(
                            product, lista, lista_no1, deep
                            ))
                    if possible_reduction.long < len(divid):
                        results = selector(
                                brain(n//product, lista, lista_no1, deep
                                      ))
                        result.append(factores(possible_reduction)*results)
    """Aquí intentamos movernos a otro número cercano que sea divisible
    por un primo alto.
    """
    for i in lista:
        divida = dividamos(n+i, lista_no1)
        divido = dividamos(n-i, lista_no1)
        if divida[0]:
            save[1] = save_worker(save[1], [divida[1][-1], -i])
        if divido[0]:
            save[1] = save_worker(save[1], [divido[1][-1], i])
    if save[0] != [0,0] and save[0][0] > 10:
        results = selector(brain(n//save[0][0], lista, lista_no1, deep))
        result.append(factores(save[0][0])*results)
    for i in save[1]:
        if i != [0,0]:
            results = selector(brain((n-i[1])//i[0], lista, lista_no1, deep))
            result.append(factores(i[0])*results+i[1])
    if result == []:
        save = [0]
        for i in lista:
            for j in lista:
                divida = dividamos(n+i+j, prime_list)
                if divida[0] and divida[1][-1] >= save[0]:
                    save = [divida[1][-1], -i, -j]
                else:
                    divido = dividamos(n-i+j, prime_list)
                    if divido[0] and divido[1][-1] >= save[0]:
                        save = [divido[1][-1],i, -j]
            for j in lista:
                divida = dividamos(n+i-j, prime_list)
                if divida[0] and divida[1][-1] >= save[0]:
                    save = [divida[1][-1], -i, j]
                else:
                    divido = dividamos(n-i-j, prime_list)
                    if divido[0] and divido[1][-1] >= save[0]:
                        save = [divido[1][-1], i, j]
        results = selector(brain(
                (n-save[1])//save[0], lista, lista_no1, deep
                ))
        result.append(factores(save[0])*results+save[1]+save[2])
    return result

def prod_list(lista):
    """Esta función multiplica los elementos de una lista"""
    result = 1
    for i in lista:
        result *= i
    return result

def save_worker(tuplas, candidate):
    """Con esta función actualizamos nuestra lista de mejores candidatos:
        'tuplas' es una lista de pares de números, guarda la información
        de las posibles mejores vías para llegar a la solución.
        'candidate' es un candidato a vía para obtener la solución.
    Generamos una nueva lista con pares de las posibles mejores vías.
    """
    for i in range(len(tuplas)):
        if candidate[0] > tuplas[i][0]:
            tuplas[i], candidate = candidate, tuplas[i]
    return tuplas

def selector(lista):
    """Una vez obtenidas todas las posibles buenas soluciones, seleccionamos
    una que use el menor número de 'primos' necesarios para llegar al número
    objetivo.
        'lista' es una lista con las soluciones obtenidas.
    Esta función devuelve un objeto 'descomp', el cuál al imprimirse nos dará
    una "factorización".
    """
    result = lista[0]
    for i in lista:
        if i.long < result.long:
            result = i
    return result

def dividamos(n, lista):
    """Con esta función vemos por qué 'primos' que podamos usar es divisible un
    número dado.
        'n' es un entero.
        'lista' es una lista con una primos.
    La función devuelve un par con una variable booleana que es 'False'
    si no encontramos ningún 'primo' que divida a 'n'. En cambio, si
    encontramos alguno devolverá 'True' y una lista con los primos encontrados.
    """
    result = [False,[]]
    for i in lista:
        if n%i == 0:
            result[0] = True
            result[1].append(i)
    return result

def closest_primes(n, lista):
    """Con esta función recursiva, dado un entero 'n' y una lista de valores
    ordenada de menor a mayor, conseguiremos el elemento de la lista más
    cercano a 'n'.
        'n' es un número real.
        'lista' es una lista.
    La función devuelve un elemento de la lista, es decir, un entero.
    """
    if len(lista) == 1:
        result = lista[0]
    else:
        long = len(lista)
        k = long//2
        if long%2 == 0:
            if abs(n-lista[k-1]) <= abs(n-lista[k]):
                result = closest_primes(n, lista[:k])
            else:
                result = closest_primes(n, lista[k:])
        else:
            if n > lista[k]:
                result = closest_primes(n, lista[k:])
            else:
                result = closest_primes(n, lista[:k])
    return result

def n_menor_1000(n, lista, lista_no1):
    """Con esta función podemos calcular factorizaciones óptimas para números
    menores o iguales a '1000'.
        'n' es entero a factorizar.
        'lista' es una lista con los 'primos' que podemos usar.
        'lista_no1' es una lista con los 'primos' que podamos usar sin el '1'.
    La función devuelve un objeto 'factores' o 'sumandos'.
    Básicamente, vamos probando distintas técnicas para obtener las
    descomposiciones óptimas de números menores o iguales a 1000.
    """
    result = []
    if n in lista:
        result = factores(n)
    else:
        fact, gold = factorio(n, lista_no1), goldbach(n, lista)
        if len(fact) == 2 and fact[0]*fact[1] == n:
            result = factores(fact[0])*fact[1]
        elif len(gold) == 2:
            result = sumandos(gold[0])+gold[1]
        else:
            trigold = trigoldbach(n, lista)
            if len(fact) == 3 and fact[0]*fact[1]*fact[2] == n:
                result = factores(fact[0])*fact[1]*fact[2]
            elif len(trigold) == 3:
                result = sumandos(trigold[0])+trigold[1]+trigold[2]
            else:
                for i in lista_no1:
                    if n%i == 0:
                        reduced = n_menor_1000(n//i, lista, lista_no1)
                        if reduced != [] and reduced.long == 2:
                            result = reduced*i
                    else:
                        for j in lista:
                            for i in lista_no1:
                                redu1, redu2 = (n+j)//i, (n-j)//i
                                if (n+j)%i == 0 and redu1 in lista_no1:
                                    return sumandos(i)*redu1-j
                                elif (n-j)%i == 0 and redu2 in lista_no1:
                                    return sumandos(i)*redu2+j
    if result == []:
        k = closest_primes(n**(1/2), lista)
        a, b = n-k**2, k**2-n
        golda, goldb = goldbach(a, lista), goldbach(b, lista)
        if len(golda) == 2:
            result = factores(k)*k+golda[0]+golda[1]
        elif len(goldb) == 2:
            result = factores(k)*k-goldb[0]-goldb[1]
        else:
            k1 = closest_primes(n**(1/3), lista)
            k2 = closest_primes(n**(2/3), lista)
            a, b = n-k1*k2, k1*k2-n
            golda, goldb = goldbach(a, lista), goldbach(b, lista)
            if len(golda) == 2:
                result = factores(k1)*k2+golda[0]+golda[1]
            elif len(goldb) == 2:
                result = factores(k1)*k2-goldb[0]-goldb[1]
    if result == []:
        for i in lista:
            fact1 = factorio(n+i, lista_no1)
            fact2 = factorio(n-i, lista_no1)
            if len(fact1) == 3 and fact1[0]*fact1[1]*fact1[2] == n+i:
                result = factores(fact1[0])*fact1[1]*fact1[2]-i
                break
            elif len(fact2) == 3 and fact2[0]*fact2[1]*fact2[2] == n-i:
                result = factores(fact2[0])*fact2[1]*fact2[2]+i
                break
    return result

def goldbach(n, lista):
    """Aquí metemos un entero 'n' y vemos si lo podemos obtener como suma o
    resta de dos primos que se puedan usar.
        'n' es un entero.
        'lista' es una lista con los primos quepodemos usar.
    La función puede devolver un par de números si estos sumados o restados
    dan 'n' o una lista vacía si no es posibel expresar 'n' así.
    """
    for i in lista:
        if n-i in lista:
            return [n-i, i]
        elif n+i in lista:
            return [n+i, -i]
    return []

def trigoldbach(n ,lista):
    """Aquí metemos un entero 'n' y vemos si lo podemos obtener como suma o
    resta de tres primos que se puedan usar.
        'n' es un entero.
        'lista' es una lista con los primos quepodemos usar.
    La función puede devolver una terna de números, si estos usando sumas y
    restas de alguna forma, dan 'n' o una lista vacía si no es posibel expresar
    'n' así.
    """
    for i in lista:
        for j in lista:
            if n-i-j in lista:
                return [i, j, n-i-j]
            elif n+i-j in lista:
                return [-i, j, n+i-j]
            elif n-i+j in lista:
                return [i, -j, n-i+j]
            elif n+i+j in lista:
                return [-i, -j, n+i+j]
    return []

def factorio(n, lista_no1):
    """Con esta función generamos una lista con todos los factores que haya en
    nuestra lista (pueden estar repetidos).
        'n' es un entero.
        'lista_no1' es una lista de primos usables sin el '1'.
    La función devuelve una lista con los factores de 'n' que estén en
    'lista_no1'. Si no encuentra ninguno, dicha lista será vacía.
    """
    factores, i, m = [], 0, n
    tope = m**(1/2)
    while i < len(lista_no1):
        if m in lista_no1:
            factores += [int(m)]
            i += 100
        elif lista_no1[i] <= tope:
            while m % lista_no1[i] == 0:
                factores += [lista_no1[i]]
                m /= lista_no1[i]
            i += 1
        else:
            i += 100
    return factores


data = open("TEST.txt", "r")
file = open("SCORE.txt", "w")
ts = time.time()
st = str(datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d-%H:%M:%S.%f'))
file.write(st+'\n')
media = 0
for line in data.readlines():
    test = line.split('|')
    if test[0] != 'ID':
        test[0], test[1], test[2] = int(test[0]), int(test[1]), int(test[2])
        A, B = [], []
        for j in prime_list:
            if j != test[2]:
                A.append(j)
                if j != 1:
                    B.append(j)
        result = descomp([test[0], selector(brain(test[1], A, B, depth))])
        file.write(str(result)+'\n')
        media += result.result.long
ts = time.time()
st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d-%H:%M:%S.%f')
file.write(str(st))
file.close()
data.close()
    

