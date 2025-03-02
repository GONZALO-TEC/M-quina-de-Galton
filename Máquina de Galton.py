import numpy as np
import matplotlib.pyplot as plt

def simular_maquina_galton(num_bolas, num_niveles):
    resultados = np.zeros(num_niveles + 1)
    for _ in range(num_bolas):
        posicion = 0
        for _ in range(num_niveles):
            posicion += np.random.choice([0, 1])  # 0 para izquierda, 1 para derecha
        resultados[posicion] += 1
    return resultados

def graficar_histograma(resultados):
    plt.bar(range(len(resultados)), resultados, align='center', alpha=0.7)
    plt.xlabel('Contenedor')
    plt.ylabel('Número de canicas')
    plt.title('Simulación de la Máquina de Galton')
    plt.show()

# Parámetros de la simulación
num_bolas = 3000
num_niveles = 12

# Realizar la simulación
resultados = simular_maquina_galton(num_bolas, num_niveles)

# Graficar el histograma
graficar_histograma(resultados)
