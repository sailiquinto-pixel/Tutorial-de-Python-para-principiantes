# SOLUCIÓN · RETO 5: GENERADOR DE CONTRASEÑAS
import random
import string

SIMBOLOS = "!@#$%&*"


def generar_contraseña(longitud, usar_simbolos=True):
    """Genera una contraseña con mayúscula, minúscula, número (y símbolo)."""
    obligatorios = [
        random.choice(string.ascii_uppercase),
        random.choice(string.ascii_lowercase),
        random.choice(string.digits),
    ]
    caracteres = string.ascii_letters + string.digits

    if usar_simbolos:
        obligatorios.append(random.choice(SIMBOLOS))
        caracteres += SIMBOLOS

    restantes = [random.choice(caracteres) for _ in range(longitud - len(obligatorios))]
    contraseña = obligatorios + restantes
    random.shuffle(contraseña)        # Mezcla para que los obligatorios no queden al inicio
    return "".join(contraseña)


while True:
    try:
        longitud = int(input("Longitud de la contraseña (mínimo 8): "))
        if longitud >= 8:
            break
        print("Debe tener al menos 8 caracteres.")
    except ValueError:
        print("Escribe un número entero.")

con_simbolos = input("¿Incluir símbolos? (s/n): ").strip().lower() == "s"

print("\nContraseñas sugeridas:")
for _ in range(3):
    print("  ", generar_contraseña(longitud, con_simbolos))
