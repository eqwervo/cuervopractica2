import roundsdb

players = []

for round in roundsdb.rounds:
    for name in round:
        players.append(name)
        
# Marcadores iniciales
players_points = {'Shadow': 0, 'Blaze': 0, 'Viper': 0, 'Frost': 0, 'Reaper': 0} 
players_mvp = {'Shadow': 0, 'Blaze': 0, 'Viper': 0, 'Frost': 0, 'Reaper': 0}
player_deaths = {'Shadow': 0, 'Blaze': 0, 'Viper': 0, 'Frost': 0, 'Reaper': 0}
player_kills = {'Shadow': 0, 'Blaze': 0, 'Viper': 0, 'Frost': 0, 'Reaper': 0}
player_assists = {'Shadow': 0, 'Blaze': 0, 'Viper': 0, 'Frost': 0, 'Reaper': 0}
    



# for anidado por rondas, luego itera por items de cada ronda 
# almacenando key y value que finalmente permite accede a los valores 
# y hacer las operaciones
for i,round in enumerate(roundsdb.rounds):
    round = roundsdb.rounds[i]
    for player, value in round.items():
        players_points[player] += value['kills'] * 3
        player_kills[player] += value['kills']
        players_points[player] += value['assists']
        player_assists[player] += value['assists']
        if value['deaths'] == True:
            players_points[player] -= 1
            player_deaths[player] += 1
    #print(f'Marcador al finalizar ronda {i+1} \n{players_points}')
    mvp = max(players_points, key=players_points.get)
    players_mvp[mvp] += 1
    print(f'''
    Jugador     Kills       Assists     Deaths      MVPs        Totales    
    {players[0]} {player_kills[players[0]]:>8}{player_assists[players[0]]:>13}{player_deaths[players[0]]:>11}{players_mvp[players[0]]:>11}{players_points[players[0]]:>14}
    {players[1]} {player_kills[players[1]]:>9}{player_assists[players[1]]:>13}{player_deaths[players[1]]:>11}{players_mvp[players[1]]:>11}{players_points[players[1]]:>14}   
    {players[2]} {player_kills[players[2]]:>9}{player_assists[players[2]]:>13}{player_deaths[players[2]]:>11}{players_mvp[players[2]]:>11}{players_points[players[2]]:>14}   
    {players[3]} {player_kills[players[3]]:>9}{player_assists[players[3]]:>13}{player_deaths[players[3]]:>11}{players_mvp[players[3]]:>11}{players_points[players[3]]:>14}
    {players[4]} {player_kills[players[4]]:>8}{player_assists[players[4]]:>13}{player_deaths[players[4]]:>11}{players_mvp[players[4]]:>11}{players_points[players[4]]:>14}  
    ''')

    
    
print(f'MVP ronda {i+1}: {mvp}')
print()

'''
print('Randking final')
print(f
Jugador     Kills       Assists     Deaths      MVPs        Totales    
{players[0]} {player_kills[players[0]]:>8}{player_assists[players[0]]:>13}{players_mvp[players[0]]:>8}{player_kills[players[0]]:>8}{players_points[players[0]]:>8}
{players[1]}    
{players[2]}    
{players[3]}
{players[4]}    
    '''

    
            

        