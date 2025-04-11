# ai-hex-2025

## Estrategia: Minimax con heuristicas

### EV(B,X)

Definimos la evaluacion de un posible tablero B bajo la perspectiva de un jugador X -> Ev(B, X) como el resultado del siguiente algoritmo:

1 - Tomar 1 camino ganador de tamaño minimo(donde las casillas ya marcadas por ese jugador aportan 0 a la "longitud" de dicho camino).

2 - suponer que el contrario juega aleatoriamente y tiene una probabilidad de interrumpir ese camino, bajo esta supocion bloquear una casilla random del camino actual.

3 - Repetir pasos 1 y 2 hasta tener 4 caminos distintos y sus longitudes.

4 - Decimos que la probabilidad de que el contrario que juega aleatorio no interrumpa un camino es 
$(total\_casillas - tamaño\_camino)/total\_casillas $ y la probabilidad de que si lo haga $(tamaño\_camino)/total\_casillas$. 

5 - Siendo L la lista de las longitudes de los 4 caminos seleccionados y $tot$ el total de casillas la formula de Ev(B,X) seria $P[0]$ donde:
    $$ P[i]=(tot-L[i])/tot + (L[i]/tot)*P[i+1]$$
    $$ P[4]=0 $$


### Score de una jugada
Definimos el score de una jugada del jugador X, como $max(Ev(B,X), 1-Ev(B,Y))$ donde B es el estado del tablero luego de que X hace la jugada(Y es el otro jugador). Aqui suponemos que una jugada muy buena para el jugador Y es mala para el jugador X y viceversa, por eso nos quedamos con el maximo entre lo buena que sea esta jugada para X y lo mala que sea para Y.

### Encontrando las casillas que vamos a explorar
Exploraremos solo un conjunto reducido de jugadas en el Minimax, empezamos con las 8 que tengan mejor score y vamos reduciendo el ancho de exploracion de 2 en 2 a medida que descendemos hasta llegar a 0, donde no se explora más simplemente se devuelve la jugada de mayor score como resultado. El jugador para el cual queremos hallar la mejor jugada busca maximizar este score, mientras el otro busca minimizarlo, al tener altura impar(5) el ärbol de Minimax se garantiza que en el último nivel juegue el mismo jugador para el cual queremos hallar la mejor jugada.
