def validate_number(valor: float | int, minimo: float | int, maximo: float | int) -> None:
    '''
    Valida si un numero esta dentro de un rango especifico.

    Parámetros:
    valor (float | int): El numero a validar.
    minimo (float | int): El valor mínimo del rango.
    maximo (float | int): El valor máximo del rango.

    Retorna:
    None: No retorna ningún valor, solo imprime si el número está dentro o fuera del rango.
    '''
    if minimo <= valor <= maximo:
        print("El número está dentro del rango.")
    else:
        print("El número está fuera del rango.")

def validate_length(cadena: str, longitud: int) -> None:
    '''
    Valida si la longitud de una cadena es menor o igual a un valor especifico.

    Parámetros:
    cadena (str): La cadena a validar.
    longitud (int): La longitud máxima permitida.

    Retorna:
    None: No retorna ningún valor, solo imprime si la cadena cumple o no con la longitud.
    '''
    if len(cadena) <= longitud:
        print("La cadena cumple con la longitud.")
    else:
        print("La cadena excede la longitud permitida.")

