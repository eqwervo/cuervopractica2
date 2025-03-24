import roundsdb

# Marcadores iniciales
players = {}
for round in roundsdb.rounds:
    for name in round:
        players[name] = {'kills': 0, 'assists': 0, 'deaths': 0, 'mvp': 0, 'points': 0}

        



# for anidado por rondas, luego itera por items de cada ronda 
# almacenando key y value que finalmente permite accede a los valores 
# y hacer las operaciones
for i,round in enumerate(roundsdb.rounds):
    score_max = 0
    round_score = int(0)
    mvp = None
    round = roundsdb.rounds[i]
    for player, value in round.items():
        players[player]['kills'] += value['kills']
        players[player]['assists'] += value['assists']
        round_score = value['kills'] * 3 + value['assists']
        if value['deaths'] == True:
            players[player]['deaths'] += 1
            round_score -= 1      
        players[player]['points'] += round_score
        if round_score > score_max:
            score_max = round_score
            mvp = player
    players[mvp]['mvp'] += 1
    print(f'Marcador al finalizar ronda {i+1}')
    print(f'MVP de la ronda: {mvp}')
    final_score = sorted(players.items(), key=lambda x: x[1]['points'], reverse=True)
    print(f'''Jugador     Kills       Assists     Deaths      MVPs        Totales''')
    for player, stats in final_score:
        print(f'''{player:8} {stats['kills']:>6}{stats['assists']:>13}{stats['deaths']:>12}{stats['mvp']:>11}{stats['points']:>13}''')
    print() 