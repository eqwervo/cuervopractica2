from src import roundsdb



# Funcion iniciardora de estadisticas por jugador. 
# Comtempla a todos los jugadores que participaron en una partida aunque no haya jugado todas las rondas

def stats_init(players, rounds):
    '''Esta funcion recorre cada ronda del la base de datos de todas las rondas.
        el segundo recorrido es por nombre de jugador, asignandole a cada un sus estadisticas iniciales.'''
    
    for round in rounds:
        for name in round:
            players[name] = {'kills': 0, 'assists': 0, 'deaths': 0, 'mvp_counter': 0, 'points': 0}
    return players

    
def process_round(round, players, round_score, score_max):
    '''Funcion que recorre una ronda, asignando valores de puntaje y estadísticas. Incluye MVP'''
    
    # Recorre por clave valor los items de round y asigna puntajes y estadisticas
    for player, value in round.items():
            # print(f'player x ronda{player}')
            players[player]['kills'] += value['kills']
            players[player]['assists'] += value['assists']
            round_score = value['kills'] * 3 + value['assists']
            # Evalua el valor 'deaths' y agrega a puntajes y estadisticas
            if value['deaths'] == True:
                players[player]['deaths'] += 1
                round_score -= 1      
            players[player]['points'] += round_score
            # Evalua el score del jugador con el score max y obtiene el mvp de la ronda
            if round_score > score_max:
                score_max = round_score
                mvp = player
            
    return mvp

def order_print(mvp_round, players, i):
    '''Funcion que ordena la informacion por ronda e imprime'''
    
    print((f'Marcador al finalizar ronda {i+1}').center(60))
    print(f'MVP de la ronda: {mvp_round}'.center(60))
    print()
    final_score = sorted(players.items(), key=lambda x: x[1]['points'], reverse=True)
    print(f'''Jugador     Kills       Assists     Deaths      MVPs        Totales''')
    for player, stats in final_score:
        print(f'''{player:8} {stats['kills']:>6}{stats['assists']:>13}{stats['deaths']:>12}{stats['mvp_counter']:>11}{stats['points']:>13}''')
    print() 
            
        
# for anidado por rondas, luego itera por items de cada ronda 
# almacenando key y value que finalmente permite acceder a los valores 
# y hacer las operaciones
def main():
    rounds = roundsdb.rounds
    players = {}
    # Funcion iniciardora de estadisticas por jugador
    stats_init(players, rounds)
    for i,round in enumerate(rounds):
        #Reinicio scores y mvp por ronda
        score_max = 0
        round_score = 0
        mvp_round = process_round(round, players, round_score, score_max)
        #finalizada la ronda se registra el mvp
        players[mvp_round]['mvp_counter'] += 1
        order_print(mvp_round, players, i)

if __name__ == '__main__':
    main()