# M-quina-de-Galton
Este proyecto proporciona una comprensión visual de cómo las distribuciones binomiales pueden aproximarse a una distribución normal. Simulaciones como esta son útiles para visualizar y entender conceptos estadísticos y matemáticos de una manera intuitiva y práctica.

#  Simulación de la Máquina de Galton
Introducción
Este proyecto simula el funcionamiento de una máquina de Galton utilizando Python. La máquina de Galton, diseñada por Francis Galton en el siglo XIX, muestra cómo una distribución binomial se aproxima a una distribución normal con una muestra lo suficientemente grande.



![Figure_1](https://github.com/user-attachments/assets/9dc77156-5192-4383-aee8-4b6ddf0b20fb)

Descripción del Código
El programa se divide en dos funciones principales:

simular_maquina_galton(num_bolas, num_niveles):

Esta función simula la caída de las canicas a través de los niveles de obstáculos.

Utiliza np.random.choice([0, 1]) para decidir aleatoriamente si la canica va a la izquierda (0) o a la derecha (1) en cada nivel.

Guarda el número de canicas en cada contenedor en un array.

graficar_histograma(resultados):

Esta función toma los resultados de la simulación y grafica un histograma utilizando matplotlib.

Etiqueta los ejes y añade un título al gráfico para mayor claridad.

Ejecución del Programa
El programa simula la caída de 3000 canicas a través de 12 niveles de obstáculos y muestra un histograma que representa la cantidad de canicas en cada contenedor.

# Reflexiones sobre el Bootcamp
El bootcamp ha sido una experiencia extremadamente enriquecedora y transformadora. Durante este tiempo, he adquirido una sólida comprensión de los fundamentos de la programación en Python.
