import pandas as pd
import numpy as np
import csv

def assign_positions(filename):
    # Wczytanie danych
    data = pd.read_csv(filename)

    # Pobranie ID graczy
    player_ids = data['player_id'].values

    # Przetasowanie ID
    np.random.shuffle(player_ids)

    # Podział na 2000 piątek
    teams = player_ids[:n].reshape(n // 5, 5)  # Zakładamy, że mamy dokładnie 10000 graczy

    return teams

n = 200
# Użycie funkcji
filename = 'data/player_stats.csv'
teams = assign_positions(filename)


output_filename = "data/teams.csv"

teams_with_id = np.hstack((np.arange(1, len(teams)+1).reshape(-1, 1), teams))

with open(output_filename, 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['ID', 'Player1', 'Player2', 'Player3', 'Player4', 'Player5'])
    
    for team in teams_with_id:
        writer.writerow(team)