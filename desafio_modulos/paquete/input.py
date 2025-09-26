from .validate import *

def get_int(mensaje:str, mensaje_error:str, minimo:int, maximo:int, reintentos:int) -> int | None:
    """
    mensaje: es el mensaje que se va a imprimir antes de pedirle al usuario el dato por consola.
    mensaje_error: mensaje de error en el caso de que el dato ingresado sea invalido.
    mínimo: valor mínimo admitido (inclusive)
    máximo: valor máximo admitido (inclusive)
    reintentos: cantidad de veces que se volverá a pedir el dato en caso de error.

    En caso de que la función no haya podido conseguir un número válido, la misma retorna None.

    """

    print(mensaje)

    entero = int(input("Ingresá un número: "))

    x = 1

    while x < reintentos:

        x += 1

        if minimo <= entero and maximo >= entero:
            print("Su número está dentro del rango.")
            break
        else:
            print(mensaje_error)
            entero = int(input("Ingresá un número: "))

        if x == reintentos:

            print("Llegaste al límite de reintentos.")


def get_float(mensaje:str, mensaje_error:str, minimo:float, maximo:float, reintentos:int) -> float|None:

    '''
    

    '''

    print(mensaje)

    flotante = float(input("Ingresá un número: "))

    x = 1

    while x < reintentos:

        x += 1

        if minimo <= flotante and maximo >= flotante:
            print("Su número está dentro del rango.")
            break
        else:
            print(mensaje_error)
            flotante = float(input("Ingresá un número: "))

    if x == reintentos:

        print("Llegaste al límite de reintentos.")

def get_string(longitud:int) -> str|None:
    '''
    
    '''
    cadena = input("Ingresá una cadena de texto: ")

    if len(cadena) == longitud:
        print("La cadena es correcta.")
    else:
        print("La cadena es incorrecta.")
    return cadena












