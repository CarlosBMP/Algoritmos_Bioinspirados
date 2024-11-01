#Autor Mejia Padilla Carlos Benjamin
import random

# Parámetros del algoritmo
CANTIDAD_HORMIGAS = 10
NUMERO_CIUDADES = 5
ALFA = 1.0  # Importancia de las feromonas
BETA = 2.0  # Importancia de la distancia
EVAPORACION = 0.5  # Tasa de evaporación de feromonas
ITERACIONES = 100
FEROMONA_INICIAL = 1.0

# Distancias entre las ciudades (simulado como una lista de listas)
distancias = [[random.randint(1, 10) for _ in range(NUMERO_CIUDADES)] for _ in range(NUMERO_CIUDADES)]

# Inicializa las feromonas como una lista de listas
feromonas = [[FEROMONA_INICIAL for _ in range(NUMERO_CIUDADES)] for _ in range(NUMERO_CIUDADES)]

# Función para calcular la probabilidad de moverse de una ciudad a otra
def calcular_probabilidades(ciudad_actual, visitadas):
    probabilidades = []
    for ciudad in range(NUMERO_CIUDADES):
        if ciudad not in visitadas:
            tau = feromonas[ciudad_actual][ciudad] ** ALFA  # Influencia de feromonas
            eta = (1.0 / distancias[ciudad_actual][ciudad]) ** BETA  # Inverso de la distancia
            probabilidades.append(tau * eta)
        else:
            probabilidades.append(0)  # Ciudad ya visitada
    total_probabilidades = sum(probabilidades)
    return [p / total_probabilidades if total_probabilidades > 0 else 0 for p in probabilidades]

# Función para que una hormiga construya una solución (ruta)
def construir_ruta():
    ruta = []
    ciudad_actual = random.randint(0, NUMERO_CIUDADES - 1)
    ruta.append(ciudad_actual)

    for _ in range(NUMERO_CIUDADES - 1):
        probabilidades = calcular_probabilidades(ciudad_actual, ruta)
        ciudad_siguiente = random.choices(range(NUMERO_CIUDADES), probabilidades)[0]
        ruta.append(ciudad_siguiente)
        ciudad_actual = ciudad_siguiente

    return ruta

# Función para calcular la longitud total de una ruta
def calcular_longitud_ruta(ruta):
    longitud = 0
    for i in range(len(ruta) - 1):
        longitud += distancias[ruta[i]][ruta[i + 1]]
    longitud += distancias[ruta[-1]][ruta[0]]  # Volver a la ciudad inicial
    return longitud

# Actualización de las feromonas basada en las rutas construidas
def actualizar_feromonas(rutas):
    global feromonas
    # Evaporación de feromonas
    for i in range(NUMERO_CIUDADES):
        for j in range(NUMERO_CIUDADES):
            feromonas[i][j] *= (1 - EVAPORACION)
    
    # Añadir feromonas nuevas basadas en la calidad de las rutas
    for ruta, longitud in rutas:
        feromona_depositada = 1.0 / longitud
        for i in range(len(ruta) - 1):
            feromonas[ruta[i]][ruta[i + 1]] += feromona_depositada
            feromonas[ruta[i + 1]][ruta[i]] += feromona_depositada  # Bidireccional

# Algoritmo de colonia de hormigas
def colonia_hormigas():
    mejor_ruta = None
    mejor_longitud = float('inf')

    for iteracion in range(ITERACIONES):
        rutas = []
        for _ in range(CANTIDAD_HORMIGAS):
            ruta = construir_ruta()
            longitud_ruta = calcular_longitud_ruta(ruta)
            rutas.append((ruta, longitud_ruta))

            # Guardar la mejor ruta encontrada
            if longitud_ruta < mejor_longitud:
                mejor_ruta = ruta
                mejor_longitud = longitud_ruta

        # Actualizar feromonas
        actualizar_feromonas(rutas)

        print(f"Iteración {iteracion + 1}: Mejor longitud = {mejor_longitud}")

    print(f"\nMejor ruta encontrada: {mejor_ruta} con longitud {mejor_longitud}")

if __name__ == "__main__":
    print("Matriz de distancias entre ciudades:")
    for fila in distancias:
        print(fila)
    colonia_hormigas()
