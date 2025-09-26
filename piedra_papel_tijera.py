import random

def verificar_ganador_ronda(jugador,maquina) -> str:

    if (jugador == 1 and maquina == 3) or (jugador == 2 and maquina == 1) or (jugador == 3 and maquina == 2):
        return "jugador"
    
    elif (maquina == 1 and jugador == 3) or (maquina == 2 and jugador == 1) or (maquina == 3 and jugador == 2):
        return "maquina"
    
    else:
        return "empate"
    

def verificar_estado_partida(aciertos_jugador, aciertos_maquina, ronda_actual) -> bool:

    if aciertos_jugador == 2 or aciertos_maquina == 2:
        return False
    
    if ronda_actual >= 3:
        if aciertos_jugador != aciertos_maquina:
            return False
        return True
    return True

def verificar_ganador_partida(aciertos_jugador, aciertos_maquina) -> str:

    if aciertos_jugador > aciertos_maquina:
        return "jugador"
    elif aciertos_maquina > aciertos_jugador:
        return "maquina"
    else:
        return "empate"

def mostrar_elemento(eleccion) -> str:
    if eleccion == 1:
        return "Piedra"
    elif eleccion == 2:
        return "Papel"
    else:
        return "Tijera"

def jugar_piedra_papel_tijera() -> str:
    estado_partida = True
    aciertos_jugador = 0
    aciertos_maquina = 0
    ronda_actual = 0

    while estado_partida:
        jugador = int(input("Piedra = 1 - Papel = 2 - Tijera = 3: "))

        if jugador != 1 and jugador != 2 and jugador != 3:
            print("Numero invalido, ingrese nuevamente [1][2][3]")
            continue

        opciones = [1, 2, 3]
        maquina = random.choice(opciones)
        ronda_actual += 1

        ganador_ronda = verificar_ganador_ronda(jugador, maquina)

        print(f"\nRonda {ronda_actual}: ")
        print("___________________________")
        print(f"\nTu elegiste: {mostrar_elemento(jugador)}")
        print(f"La maquina eligio: {mostrar_elemento(maquina)}")
        print("___________________________")
        print(f"\nGanador de la ronda: {ganador_ronda}")

        if ganador_ronda == "jugador":
            aciertos_jugador += 1
        elif ganador_ronda == "maquina":
            aciertos_maquina += 1
        
        estado_partida = verificar_estado_partida(aciertos_jugador, aciertos_maquina, ronda_actual)

    ganador_partida = verificar_ganador_partida(aciertos_jugador, aciertos_maquina)
    print(f"Ganador de la partida: {ganador_partida}")

jugar_piedra_papel_tijera()











