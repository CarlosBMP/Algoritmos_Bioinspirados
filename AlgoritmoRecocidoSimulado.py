#Autor Mejia Padilla Carlos Benjamin
import random
import math

# Parámetros del recocido simulado
TEMPERATURA_INICIAL = 1000
TEMPERATURA_FINAL = 1
FACTOR_ENFRIAMIENTO = 0.99
NUMERO_CIUDADES = 5
ITERACIONES_POR_TEMPERATURA = 100

# Matriz de distancias entre ciudades (simulada como lista de listas)
distancias = [[random.randint(1, 10) for _ in range(NUMERO_CIUDADES)] for _ in range(NUMERO_CIUDADES)]

# Función para calcular la longitud total de una ruta
def calcular_longitud_ruta(ruta):
    longitud = 0
    for i in range(len(ruta) - 1):
        longitud += distancias[ruta[i]][ruta[i + 1]]
    longitud += distancias[ruta[-1]][ruta[0]]  # Volver a la ciudad inicial
    return longitud

# Función para generar una nueva solución (ruta) modificada a partir de una existente
def generar_nueva_ruta(ruta):
    nueva_ruta = ruta[:]
    i, j = random.sample(range(NUMERO_CIUDADES), 2)
    nueva_ruta[i], nueva_ruta[j] = nueva_ruta[j], nueva_ruta[i]  # Intercambia dos ciudades
    return nueva_ruta

# Función de probabilidad de aceptación de soluciones peores
def aceptar_peor_solucion(delta, temperatura):
    if delta < 0:
        return True
    else:
        return random.random() < math.exp(-delta / temperatura)

# Algoritmo de recocido simulado
def recocido_simulado():
    # Inicializar ruta aleatoria
    ruta_actual = list(range(NUMERO_CIUDADES))
    random.shuffle(ruta_actual)
    mejor_ruta = ruta_actual[:]
    mejor_longitud = calcular_longitud_ruta(ruta_actual)

    temperatura = TEMPERATURA_INICIAL

    while temperatura > TEMPERATURA_FINAL:
        for _ in range(ITERACIONES_POR_TEMPERATURA):
            # Generar una nueva ruta y calcular su longitud
            nueva_ruta = generar_nueva_ruta(ruta_actual)
            longitud_actual = calcular_longitud_ruta(ruta_actual)
            longitud_nueva = calcular_longitud_ruta(nueva_ruta)

            # Ver si aceptamos la nueva ruta
            delta = longitud_nueva - longitud_actual
            if aceptar_peor_solucion(delta, temperatura):
                ruta_actual = nueva_ruta[:]
                if longitud_nueva < mejor_longitud:
                    mejor_ruta = nueva_ruta[:]
                    mejor_longitud = longitud_nueva

        # Enfriar la temperatura
        temperatura *= FACTOR_ENFRIAMIENTO

        print(f"Temperatura: {temperatura:.2f}, Mejor longitud: {mejor_longitud}")

    return mejor_ruta, mejor_longitud

if __name__ == "__main__":
    print("Matriz de distancias entre ciudades:")
    for fila in distancias:
        print(fila)
    
    mejor_ruta, mejor_longitud = recocido_simulado()
    print(f"\nMejor ruta encontrada: {mejor_ruta} con longitud {mejor_longitud}")
