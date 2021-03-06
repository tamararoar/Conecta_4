#Fundamentos de los sistemas de los sistemas inteligentes. 
##Conecta 4.
Para la realización de esta práctica se han modificado los ficheros run.py, games.py y además se ha añadido un nuevo fichero llamado heuristic.py.


El fichero __run.py__ se ha sido modificado para permitir al usuario elegir si desea empezar él la partida o no, para permitir enfrentar directamente a dos heurísticas entre sí y para poder seleccionar la dificultad en cada partida. En el caso de optar por la opción de enfrentar a dos heurísticas, ambas compiten al máximo nivel de dificultad por defecto.
En el fichero __games.py__ simplemente se ha modificado la función alphabeta_search, ahora recibe también el jugador que va a realizar la jugada en cada turno.


Por último, en el fichero __heuristic.py__ añadido se encuentra la heurística de la máquina.
Con la heurística comprobamos por una parte, para cada movimiento inmediato realizable, el valor de su utilidad para saber si se trata de uno de los posibles estados objetivo o si nos puede llevar directamente a perder la partida. De no encontrarnos en ninguno de estos dos estados comprobamos la situación del tablero para ambos jugadores. Lo recorremos sumando 10 cada vez que encontramos una de nuestras fichas y 0.5 cuando encontramos un hueco vacío. Si encontramos una pieza de nuestro oponente dejamos de sumar. Cuando la suma consecutiva de las piezas del jugador más huecos suman cuatro o más devolvemos la suma de los pesos de estas. Este cálculo se realiza tanto para el jugador como para su oponente y la heurística devuelve la diferencia entre jugador y adversario.


Finalmente, en heuristic.py también se ha añadido el patrón de diseño memoize cuya función es mejorar la velocidad de respuesta de la máquina almacenando los resultados devueltos por la función encargada de calcular la heurística, reduciendo así el número de futuras invocaciones.
