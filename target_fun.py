import numpy as np
import pandas as pd
import random
import itertools


def make_gamers_matrix(path_stats='data/player_stats.csv', path_teams='data/teams.csv'):
    player_stats = pd.read_csv(path_stats)
    player_stats.set_index('player_id', inplace=True)

    teams = pd.read_csv(path_teams)

    n_teams = teams.shape[0]

    n_gamers = 5
    gamers_matrix = np.empty((n_teams, n_gamers), dtype=object)

    for i, row in teams.iterrows():
        for j in range(n_gamers):
            player_id = row[f'Player{j + 1}']
            player_info = player_stats.loc[player_id]
            mmr = player_info['mmr']
            wants = player_info[['pos1', 'pos2', 'pos3', 'pos4', 'pos5']].values
            gamers_matrix[i, j] = (player_id, mmr, *wants)

    return gamers_matrix

def calculate_target_function(gamers_matrix, a=1, b=1):
    n_teams = gamers_matrix.shape[0]
    res = []

    for i in range(n_teams):
        team = gamers_matrix[i]
        mmr_team = np.array([player[1] for player in team])
        std_mmr = np.std(mmr_team)

        best_value = float('inf')
        best_permutation = None

        for permutation in itertools.permutations(team):
            sum_wants = sum(1 - permutation[j][j] for j in range(5))
            value = a * std_mmr + b * sum_wants
            if value < best_value:
                best_value = value
                best_permutation = permutation

        res.append((best_value, best_permutation))

    return res


# gamers_matrix = make_gamers_matrix()
# res = calculate_target_function(gamers_matrix)

# # print(gamers_matrix)
# # print('-------')

# for i, (value, permutation) in enumerate(res):
#     print(f"Drużyna {i}: Wartość funkcji celu = {value:.2f}")
#     print("Skład drużyny:")
#     for gamer in permutation:
#         print(f"  ID: {gamer[0]}, MMR: {gamer[1]}, Chęci: {gamer[2:]}")
#     print()
