#Autor: Mejia Padilla Carlos Benjamin

import random

# Parámetros del algoritmo genético
TAMANO_POBLACION = 10
TAMANO_CROMOSOMA = 8
GENERACIONES = 100
TASA_MUTACION = 0.01

# Función de aptitud (fitness): cuenta cuántos '1' tiene el cromosoma
def calcular_aptitud(individuo):
    return sum(individuo)

# Crear un individuo aleatorio
def crear_individuo():
    return [random.randint(0, 1) for _ in range(TAMANO_CROMOSOMA)]

# Crear una población inicial
def crear_poblacion():
    return [crear_individuo() for _ in range(TAMANO_POBLACION)]

# Selección por torneo: elige el mejor entre dos individuos aleatorios
def seleccion(poblacion):
    individuo1 = random.choice(poblacion)
    individuo2 = random.choice(poblacion)
    return individuo1 if calcular_aptitud(individuo1) > calcular_aptitud(individuo2) else individuo2

# Cruce entre dos individuos (crossover de un punto)
def cruzar(individuo1, individuo2):
    punto_corte = random.randint(1, TAMANO_CROMOSOMA - 1)
    hijo1 = individuo1[:punto_corte] + individuo2[punto_corte:]
    hijo2 = individuo2[:punto_corte] + individuo1[punto_corte:]
    return hijo1, hijo2

# Mutación: cambia aleatoriamente un bit del cromosoma
def mutar(individuo):
    for i in range(TAMANO_CROMOSOMA):
        if random.random() < TASA_MUTACION:
            individuo[i] = 1 - individuo[i]

# Algoritmo genético
def algoritmo_genetico():
    poblacion = crear_poblacion()

    for generacion in range(GENERACIONES):
        nueva_poblacion = []
        while len(nueva_poblacion) < TAMANO_POBLACION:
            # Selección de padres
            padre1 = seleccion(poblacion)
            padre2 = seleccion(poblacion)
            # Cruce
            hijo1, hijo2 = cruzar(padre1, padre2)
            # Mutación
            mutar(hijo1)
            mutar(hijo2)
            # Añadir a la nueva población
            nueva_poblacion.extend([hijo1, hijo2])

        poblacion = nueva_poblacion[:TAMANO_POBLACION]

        # Evaluar la aptitud promedio de la generación actual
        mejor_individuo = max(poblacion, key=calcular_aptitud)
        print(f"Generación {generacion+1}: Mejor aptitud = {calcular_aptitud(mejor_individuo)}")

        # Si encontramos el objetivo, terminamos
        if calcular_aptitud(mejor_individuo) == TAMANO_CROMOSOMA:
            print(f"Solución encontrada en la generación {generacion+1}: {mejor_individuo}")
            break

if __name__ == "__main__":
    algoritmo_genetico()
