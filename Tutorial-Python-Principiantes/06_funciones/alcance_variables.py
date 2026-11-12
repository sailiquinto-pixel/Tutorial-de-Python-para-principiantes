# CAPÍTULO 6. ALCANCE DE LAS VARIABLES

# --- Variable global: existe en todo el archivo ---
saludo = "Hola"


def mostrar():
    # Una función puede LEER una variable global
    print(saludo, "desde la función")


mostrar()


# --- Variable local: solo existe dentro de la función ---
def calcular():
    resultado = 100      # local
    print("Dentro de la función:", resultado)


calcular()
# print(resultado)   # ← Descomenta: provoca NameError (la variable es local)


# --- Una local con el mismo nombre NO cambia la global ---
contador = 0


def intentar_cambiar():
    contador = 99        # Crea una variable LOCAL nueva
    print("Dentro:", contador)


intentar_cambiar()
print("Fuera:", contador)    # Sigue valiendo 0


# --- Forma recomendada: recibir por parámetro y devolver el resultado ---
def incrementar(valor):
    return valor + 1


contador = incrementar(contador)
print("Después de incrementar:", contador)


# --- La palabra global (úsala con moderación) ---
total = 0


def sumar_al_total(cantidad):
    global total
    total += cantidad


sumar_al_total(10)
sumar_al_total(5)
print("Total global:", total)

# EJERCICIO:
# Crea una función que cuente cuántas veces ha sido llamada
# (primero con `global`, luego intenta hacerlo sin variables globales).
