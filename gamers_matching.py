import pandas as pd
import numpy as np


def assign_positions(filename):
    # Wczytanie danych
    data = pd.read_csv(filename)

    # Pobranie ID graczy
    player_ids = data['player_id'].values

    # Przetasowanie ID
    np.random.shuffle(player_ids)

    # Podział na 2000 piątek
    teams = player_ids[:10000].reshape(2000, 5)  # Zakładamy, że mamy dokładnie 10000 graczy

    return teams


# Użycie funkcji
filename = 'data/player_stats.csv'
teams = assign_positions(filename)
print(teams)
