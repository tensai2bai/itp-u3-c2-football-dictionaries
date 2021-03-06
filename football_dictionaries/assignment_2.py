def players_by_position(squads_list):
    result = {}
    for player in squads_list:
        player_dict = {
        'number': player[0],
        'position': player[1],
        'name': player[2],
        'date_of_birth': player[3],
        'caps': player[4],
        'club': player[5],
        'country': player[6],
        'club_country': player[7],
        'year': player[8]
        }
        if player[1] in result :
            result[player[1]].append(player_dict)
        else:
            result[player[1]] = [player_dict]
    
    return result
    
    
    