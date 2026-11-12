# SOLUCIÓN · RETO 2: PIEDRA, PAPEL O TIJERA
import random

OPCIONES = ["piedra", "papel", "tijera"]
GANA_A = {"piedra": "tijera", "papel": "piedra", "tijera": "papel"}

puntos_usuario = 0
puntos_pc = 0

print("=== PIEDRA, PAPEL O TIJERA (gana quien llegue a 3) ===")

while puntos_usuario < 3 and puntos_pc < 3:
    jugada = input("\nTu jugada (piedra/papel/tijera): ").strip().lower()
    if jugada not in OPCIONES:
        print("Jugada no válida.")
        continue

    jugada_pc = random.choice(OPCIONES)
    print("El computador eligió:", jugada_pc)

    if jugada == jugada_pc:
        print("Empate.")
    elif GANA_A[jugada] == jugada_pc:
        print("¡Ganaste la ronda!")
        puntos_usuario += 1
    else:
        print("Perdiste la ronda.")
        puntos_pc += 1

    print(f"Marcador → Tú: {puntos_usuario} | Computador: {puntos_pc}")

print("\n¡Ganaste la partida!" if puntos_usuario == 3 else "\nEl computador ganó la partida.")
