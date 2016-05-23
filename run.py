import games
import heuristic
game = games.ConnectFour()
state = game.initial
aux=0
dificultad=3
def quienEmpieza(state,player):
    while not game.terminal_test(state):
        if player=='X':
            print "Jugador a mover:", game.to_move(state)
        else: print "Jugador a mover:", game.to_move(state)
        game.display(state)
        if player == 'O':
            col_str = raw_input("Movimiento: ")
            coor = int(str(col_str).strip())
            x = coor
            y = -1
            legal_moves = game.legal_moves(state)
            for lm in legal_moves:
                if lm[0] == x:
                    y = lm[1]
            state = game.make_move((x, y), state)
            player = 'X'
        else:
            print "Thinking..."
            move = games.alphabeta_search(state, game, eval_fn=heuristic.h1,d=dificultad)
            state = game.make_move(move, state)
            player = 'O'
        print "-------------------"
    game.display(state)
    print "Final de la partida"

def maquinaVSmaquina(state):
    while not game.terminal_test(state):
        game.display(state)
        print "Thinking X...\n"
        move = games.alphabeta_search(state, game, eval_fn=heuristic.h1,player='X', d=4)
        state = game.make_move(move, state)
        print "-------------------"
        game.display(state)
        print chr(27)+"[0;36m"+"Thinking O...\n"+chr(27)+"[0m"
        move = games.alphabeta_search(state, game, eval_fn=heuristic.h1,player='O', d=4)
        state = game.make_move(move, state)
        print "-------------------"
    game.display(state)
    print "Final de la partida"

while aux==0:
    n = int(input("Introduzca 1 si quiere jugar o 0 para enfrentar a dos heuristicas:\n"))
    if n != 1 and n != 0:
        print chr(27)+"[0;31m"+"No ha introducido una opcion valida, vuelva a intentarlo\n"+chr(27)+"[0m"
    if n ==0:
        aux=1
        maquinaVSmaquina(state)
    if n == 1:
        h = int(input(
            "Ha decidido jugar contra la maquina: Introduzca 1 si quiere comenzar la partida o 0 en caso contrario\n"))
        if h == 1:
            state.to_move = 'O'
            print "Ha decidido comenzar la partida, elija el nivel de dificultad\n"
            g = int(input("Seleccione: 0 para nivel facil, 1 para intermedio o 2 para nivel avanzado\n"))
            if g!=0 and g!=1 and g!=2:
                print chr(27) + "[0;31m" + "No ha introducido una opcion valida, jugara con nivel intermedio\n" + chr(27) + "[0m"
                dificultad=3
            elif g==0: dificultad=1
            elif g==1: dificultad=3
            elif g==2: dificultad=4
            aux=1
            quienEmpieza(state,player='O')
        elif h == 0:
            print "Ha decidido comenzar la partida, elija el nivel de dificultad\n"
            g = int(input("Seleccione: 0 para nivel facil, 1 para intermedio o 2 para nivel avanzado\n"))
            if g != 0 and g != 1 and g != 2:
                print chr(27) + "[0;31m" + "No ha introducido una opcion valida, jugara con nivel intermedio\n" + chr(
                    27) + "[0m"
                difiultad=3
            elif g == 0: dificultad = 1
            elif g == 1: dificultad = 3
            elif g == 2: dificultad = 4
            aux=1
            state.to_move = 'X'
            quienEmpieza(state,player='X')
        else:
            print chr(27) + "[0;31m" + "No ha introducido una opcion valida\n" + chr(27) + "[0m"
