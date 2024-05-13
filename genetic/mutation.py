import random
from genetic.target_function import calculate_target_function


def get_target(team_1, team_2):
    return calculate_target_function(team_1) + calculate_target_function(team_2)


# n - number of permutation
def try_permutation(teams, team_1, team_2, n=5):
    best_team_1 = team_1.copy()
    best_team_2 = team_2.copy()
    best_target = get_target(team_1, team_2)
    for i in range(n):
        id_1 = random.randint(0, len(team_1) - 1)
        id_2 = random.randint(0, len(team_2) - 1)
        team_1[id_1], team_2[id_2] = best_team_2[id_2], best_team_1[id_1]
        if get_target(team_1, team_2) < best_target:
            best_target = get_target(team_1, team_2)
            best_team_1 = team_1.copy()
            best_team_2 = team_2.copy()

    for i in range(len(team_1)):
        team_1[i] = best_team_1[i]
        team_2[i] = best_team_2[i]


def lucky_mutation(teams, team_1, team_2, mutation_chance=5):
    if random.randint(1, 100) <= mutation_chance:
        other_team_id = random.randint(0, len(teams) - 1)
        team_1_id = teams.index(team_1)
        teams[other_team_id], teams[team_1_id] = teams[team_1_id], teams[other_team_id]

    if random.randint(1, 100) <= mutation_chance:
        other_team_id = random.randint(0, len(teams) - 1)
        team_2_id = teams.index(team_2)
        teams[other_team_id], teams[team_2_id] = teams[team_2_id], teams[other_team_id]
