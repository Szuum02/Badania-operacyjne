import random
import numpy as np
from genetic.target_function import calculate_target_function


def swap(team, id_1, id_2):
    tmp = team[id_1]
    team[id_1] = team[id_2]
    team[id_2] = tmp
    pass


# n - number of permutation
def make_permutation(team, n):
    best_team = team.copy()
    best_target = calculate_target_function(team)
    for i in range(n):
        id_1 = random.randint(0, len(team) - 1)
        id_2 = random.randint(0, len(team) - 1)

        swap(team, id_1, id_2)
        if calculate_target_function(team) < best_target:
            best_target = calculate_target_function(team)
            best_team = team.copy()

    for i in range(len(team)):
        team[i] = best_team[i]

def try_permutation(teams, team_1, team_2, n=5):
    make_permutation(team_1, n)
    make_permutation(team_2, n)

def make_lucky_mutation(teams, team_1):
    team_2_id = random.randint(0, len(teams) - 1)
    team_1_id = np.where(teams == team_1)[0][0]
    player_1_id = random.randint(0, 4)
    player_2_id = random.randint(0, 4)
    tmp = teams[team_2_id][player_1_id]
    teams[team_2_id][player_1_id] = teams[team_1_id][player_2_id]
    teams[team_1_id][player_2_id] = tmp

def lucky_mutation(teams, team_1, team_2, mutation_chance=1):
    if random.randint(1, 100) <= mutation_chance:
        make_lucky_mutation(teams, team_1)

    if random.randint(1, 100) <= mutation_chance:
        make_lucky_mutation(teams, team_2)
