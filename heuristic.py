def memoize(f):
    memo = {}
    def helper(state, player):
        pair = tuple(state.board.items())
        if pair not in memo:
            memo[pair] = f(state, player)
        return memo[pair]
    return helper

def Potenciales_4(state, move, jugador,(delta_x, delta_y)):
    if jugador=='X':
        contrario='O'
    else:  contrario='X'
    x, y = move
    jn_consecutivos=0
    heuristica_alineadas=0
    while (x<8 and x>0) and (y<7 and y>0):
        if state.board.get((x, y))==jugador:
            jn_consecutivos+=1
            heuristica_alineadas+=10
        if state.board.get((x,y))==None:
            jn_consecutivos+=1
            heuristica_alineadas+=0.5
        if state.board.get((x, y)) == contrario: break
        x, y = x + delta_x, y + delta_y
    x, y = move
    x, y = x - delta_x, y - delta_y

    while (x<8 and x>0) and (y<7 and y>0):
        if state.board.get((x, y)) == jugador:
            jn_consecutivos += 1
            heuristica_alineadas+=10
        if state.board.get((x, y)) == None:
            heuristica_alineadas+=0.5
            jn_consecutivos += 1
        if state.board.get((x, y)) == contrario: break
        x, y = x - delta_x, y - delta_y
    if jn_consecutivos >= 4:
        return heuristica_alineadas
    else:
        return 0
@memoize
def h1(state, jugador):
    if jugador == 'X':
        adversario = 'O'
    else:  adversario = 'X'

    def legal_moves(state):
        return [(x, y) for (x, y) in state.moves
                if y == 1 or (x, y - 1) in state.board]

    if jugador == 'X' and state.utility != 0: return state.utility * 1000000
    if jugador == 'O' and state.utility!= 0: return state.utility * -1000000

    valor_heuristica = 0
    l_moves =legal_moves(state)
    for i in l_moves:
        x,y=i
        #Situacion jugador
        valor_heuristica += Potenciales_4(state, (x, y), jugador, (1,0))
        valor_heuristica += Potenciales_4(state, (x, y), jugador, (0,1))
        valor_heuristica += Potenciales_4(state, (x, y), jugador, (1,1))
        valor_heuristica += Potenciales_4(state, (x, y), jugador, (1,-1))
        #Situacion adversario
        valor_heuristica -= Potenciales_4(state, (x, y), adversario, (1,0))
        valor_heuristica -= Potenciales_4(state, (x, y), adversario, (0,1))
        valor_heuristica -= Potenciales_4(state, (x, y), adversario, (1,1))
        valor_heuristica -= Potenciales_4(state, (x, y), adversario, (1,-1))

    return valor_heuristica