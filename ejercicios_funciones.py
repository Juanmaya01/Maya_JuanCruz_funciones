# 1 Crear una función que le solicite al usuario el ingreso de un número entero y lo retorne. Punto 13 incluido.

def numero_entero():
    numero = int(input("Ingrese un numero entero: "))
    return numero

# 2 Crear una función que le solicite al usuario el ingreso de un número flotante y lo retorne. Punto 13 incluido.

def numero_flotante():
    numero = float(input("Ingrese un numero flotante: "))
    return numero

# 3 Crear una función que le solicite al usuario el ingreso de una cadena y la retorne. Punto 13 incluido.

def cadena():
    texto = input("Ingrese una cadena de texto: ")
    return texto

# 4 Escribir una función que calcule el área de un rectángulo. La función recibe la base y la altura y retorna el área.

def area_rectangulo(base, altura):
    area = base * altura
    return area

# 5 Escribe una función que calcule el área de un círculo. La función debe recibir el radio como parámetro y devolver el área.

def area_circulo(radio):
    import math
    area = math.pi * radio ** 2
    return area

# 6 Crea una función que verifique si un número dado es par o impar. La función debe imprimir un mensaje indicando si el número es par o impar.

def es_par_o_impar(numero):
    return numero % 2 == 0

# 7 Crea una función que verifique si un número dado es par o impar. La función retorna True si el número es par, False en caso contrario.

def es_par(numero):
    return numero % 2 == 0

# 8 Define una función que encuentre el máximo de tres números. La función debe aceptar tres argumentos y devolver el número más grande.

def maximo_de_tres(num1, num2, num3):
    return max(num1, num2, num3)

# 9 Diseña una función que calcule la potencia de un número. La función debe recibir la base y el exponente como argumentos y devolver el resultado.

def potencia(base, exponente):
    return base ** exponente

# 10 Crear una función que reciba un número y retorne True si el número es primo, False en caso contrario.

def es_primo(numero):
    if numero < 2:
        return False
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            return False
    return True

# 11 Crear una función que (utilizando el algoritmo del ejercicio de la guia de for), muestre todos los números primos comprendidos entre entre la unidad y un número ingresado como parámetro. La función retorna la cantidad de números primos encontrados. Modularizar todo lo posible.

# Verifica si un número es primo usando el algoritmo de la guía
def es_primo(numero):
    if numero < 2:
        return False
    for divisor in range(2, (numero // 2) + 1):
        if numero % divisor == 0:
            return False
    return True

# Muestra los primos y retorna la cantidad
def mostrar_primos(hasta):
    cantidad = 0
    for i in range(1, hasta + 1):
        if es_primo(i):
            print(i, end=' ')
            cantidad += 1
    print(f"Cantidad de números primos encontrados: {cantidad}")
    return cantidad

# 12 Crear una función que imprima la tabla de multiplicar de un número recibido como parámetro. La función debe aceptar parámetros opcionales (inicio y fin) para definir el rango de multiplicación. Por defecto es del 1 al 10.

def tabla_multiplicar(numero: int, inicio: int = 1, fin: int = 10) -> None:
    for i in range(inicio, fin + 1):
        print(f"{numero} x {i} = {numero * i}")
        return
tabla_multiplicar(5 , 1)

# 13 a




