def sumar_naturales(numero: int)-> int:
    if numero == 0:
        return 0
    else:
        return numero + sumar_naturales(numero - 1)
print(sumar_naturales(5)) # 15

def calcular_potencia(base: int, exponente: int) -> int:
    if exponente == 0:
        return 1
    else:
        return base * calcular_potencia(base, exponente - 1)
    
print(calcular_potencia(2, 3)) # 8

def sumar_digitos(numero: int) -> int:
    numero = str(numero)
    suma = 0
    for digito in numero:
        suma += int(digito)
    return suma

print(sumar_digitos(1234)) # 10

def calcular_fibonacci(numero: int) -> int:
    if numero == 0:
        return 0
    elif numero == 1:
        return 1
    else:
        return calcular_fibonacci(numero - 1) + calcular_fibonacci(numero - 2)
print(calcular_fibonacci(50)) # 8