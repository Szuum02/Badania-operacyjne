import random
import numpy as np
from genetic.target_function import calculate_target_function


# def get_target(team_1, team_2):
#     return calculate_target_function(team_1) + calculate_target_function(team_2)

def swap(team, id_1, id_2):
    tmp = team[id_1]
    team[id_1] = team[id_2]
    team[id_2] = tmp
    pass


# n - number of permutation
def try_permutation(teams, team_1, team_2, n=5):
    best_team_1 = team_1.copy()
    best_team_2 = team_2.copy()
    best_target_1 = calculate_target_function(team_1)
    best_target_2 = calculate_target_function(team_2)
    for i in range(n):
        id_1 = random.randint(0, len(team_1) - 1)
        id_2 = random.randint(0, len(team_2) - 1)

        swap(team_1, id_1, id_2)
        if calculate_target_function(team_1) < best_target_1:
            best_target_1 = calculate_target_function(team_1)
            best_team_1 = team_1.copy()

        swap(team_2, id_1, id_2)
        if calculate_target_function(team_2) < best_target_2:
            best_target_2 = calculate_target_function(team_2)
            best_team_2 = team_2.copy()

    for i in range(len(team_1)):
        team_1[i] = best_team_1[i]
        team_2[i] = best_team_2[i]


def lucky_mutation(teams, team_1, team_2, mutation_chance=1):
    if random.randint(1, 100) <= mutation_chance:
        other_team_id = random.randint(0, len(teams) - 1)
        team_1_id = np.where(teams == team_1)[0][0]
        player_1_id = random.randint(0, 4)
        player_2_id = random.randint(0, 4)
        tmp = teams[other_team_id][player_1_id]
        teams[other_team_id][player_1_id] = teams[team_1_id][player_2_id]
        teams[team_1_id][player_2_id] = tmp
        # teams[other_team_id], teams[team_1_id] = teams[team_1_id], teams[other_team_id]
        pass

    if random.randint(1, 100) <= mutation_chance:
        other_team_id = random.randint(0, len(teams) - 1)
        team_2_id = np.where(teams == team_2)[0][0]
        player_1_id = random.randint(0, 4)
        player_2_id = random.randint(0, 4)
        tmp = teams[other_team_id][player_1_id]
        teams[other_team_id][player_1_id] = teams[team_2_id][player_2_id]
        teams[team_2_id][player_2_id] = tmp
        # teams[other_team_id], teams[team_2_id] = teams[team_2_id], teams[other_team_id]
        pass
