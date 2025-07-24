# Ejecución
Para ejecutar el código solo debe correrse main.py. Los valores de las variables deben ser seteadas en el mismo archivo y llevan el mismo nombre que en el enunciado (a, b, x, y)

# Solución

## Lógica general
Luego de analizar el problema por un tiempo, me di cuenta de que toda configuración optima puede ser generalizada en una solución con 4 sectores: superior izquierda, paneles 'parados' (parte más corta del panel está paralela al eje x del techo); superior derecha, paneles 'acostados' (parte más larga del panel está paralela al eje x del techo); inferior izquierda, paneles 'acostados'; e inferior derecha, paneles 'parados'.

Esta solución parte de una configuración donde el techo está cubierto de izuierda a derecha por paneles 'parados'. Por simplicidad, se cubre el techo hacia abajo de paneles de la misma orientación. Luego, siempre mirando la primera fila de paneles, se itera quitando el panel parado de más a la derecha y todos los paneles bajo ese mismo. Se chequea si hay espacio para añadir un panel acostado en el extremo derecho. Si lo hay, se añade y se repiten hacia abajo la máxima cantidad de paneles en esta orientación. Por último, se compara esta nueva cantidad de paneles con la máxima cantidad de paneles totales. Si es mayor, se guardará como solución.

Esto se repite hasta recorrer todas las combinaciones posibles de paneles parados y acostados en el eje x. Se garantiza entonces que se encontrará la mejor solución para "esta orientación" del techo. Como esto no cubre todos los casos, ya que en el eje y no tenemos combinaciones distintas de paneles, se repite todo el proceso, pero se dan vueltas las coordenadas del techo (equivalente a girar el techo en 90 grados). Con esto si podemos encontrar la solución optima al problema para la mayoría de los casos, si es que no todos.

## Chequeos iniciales
* Si un lado del panel es más grande que ambos lados del techo, no cabe ningún panel en el techo, por lo que devuelvo 0. De la misma forma, si un lado del techo es más pequeño que ambos lados del panel, tampoco cabrán los paneles, devuelvo 0.
* Para poder orientar la solución, defino el 'lado corto' y el 'lado largo' del panel
```
if panel_a <= panel_b:
    panel_corto = panel_a
    panel_largo = panel_b
else:
    panel_corto = panel_b
    panel_largo = panel_a
```
* Defino una heurística que sabemos que se cumplirá: La cantidad máxima de paneles debe ser menor o igual al area del techo dividido por el area de los paneles. Esto se cumple por la simple razón de que, evidentemente, la cantidad máxima de paneles cubrirá como máximo el area del techo, no más, de otra forma habrán paneles que quedan 'volando': `max_paneles = (techo_x*techo_y)//(panel_a*panel_b)`

## Configuración inicial
Para facilitar el código, defino las siguientes variables:
```
n_parados_x = Número de paneles parados en el techo (solo considerando la primera fila)
n_acostados_x = Número de paneles acostados en el techo (solo considerando la primera fila)

max_parados_y = Número máximo de paneles parados que caben hacia abajo (lado y)
max_acostados_y = Número máximo de paneles acostados que caben hacia abajo (lado y)
```

Los valores iniciales definen entonces la configuración inicial, donde solo hay paneles parados en la primera fila `n_parados_x = techo_x//panel_corto`, y hacia abajo se repiten estos mismos `n_paneles = n_parados_x * max_parados_y`

## Loop principal
Como se explicó, en cada iteración se 'quita' un panel parado de la primera fila `n_parados_x -= 1` y se chequea si cabe un panel acostado `if techo_x - techo_ocupado >= panel_largo`. En el caso de caber, se añade y se actualiza la cantidad de paneles presentes en el techo en esta configuración:
```
n_acostados_x += 1
n_paneles = n_parados_x*max_parados_y + n_acostados_x*max_acostados_y

if n_paneles == max_paneles:
    return n_paneles
if n_paneles > mayor_paneles_logrado:
    mayor_paneles_logrado = n_paneles
```

Se itera hasta que no queden paneles parados, habiendo recorrido todas las combinaciones posibles.
Este loop se repite cambiando la orientación del techo para cubrir todos los casos:

```
orientación_1 = max_paneles(a, b, x, y)
orientación_2 = max_paneles(a, b, y, x)
```

## Otras soluciones
Otra forma que se me ocurrió para solucionar este desafío fue usar un arbol, basado en la idea de los 4 cuadrantes, donde se parte con el nodo raíz siendo el techo vacío, luego cada nodo hijo sería añadir un panel a cada cuadrante (siempre 4 nodos hijos). Sin embargo, me pareció que esta solución podría ser más engorrosa de programar y entender, además de que parte de una configuración con el techo vacío, lo cual no tiene mucho sentido. Por simplicidad y tiempo, preferí ir con la solución que presenté aquí.

## Consideraciones
* Es importante notar que dentro de la iteración, siempre chequeo si la heurística se cumple. Si logramos encontrar una solución que cubre completamente el area del techo, no tenemos que seguir intentando soluciones.
* Pensando en el modelamiento inicial de cuatro sectores, reconozco que existe la posibilidad donde esta solución no encuentre la combinación optima para algún caso. Esto es porque no se probaron combinaciones de los cuatro cuadrantes al mismo tiempo, solo entre dos (cuadrante 1 y 2 en la orientación inicial del techo y luego cuadrante 1 y 3 en la segunda pasada). Sin embargo, para no alargar la solución y considerando el tiempo invertido en este desafío, consideré que es una buena solución de todas formas. Además, cubre los casos de prueba perfectamente, y también existe la posibilidad que mi modelo de 4 cuadrantes se pueda simplificar a uno con 2, como se codeó aquí.
* En el enunciado pedían seguir un template, pero el link me manda a una página 404, por lo que lo hice sin este.
