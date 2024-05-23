import random

import numpy as np

from genetic.target_function import make_gamers_matrix, calculate_teams_cost
from genetic.selections import roulette_wheel, ranking_selection
from genetic.crossbreeding import lowest_pref_cross, mask_cross
from genetic.mutation import try_permutation, lucky_mutation
import matplotlib.pyplot as plt


def make_evolution(teams, k, selection, cross, mutation):
    # take k teams to selection
    selected_teams = selection(teams, k)
    for i in range(0, len(selected_teams) - 1, 2):
        # make crossbreeding
        cross(selected_teams[i], selected_teams[i + 1])

        # make mutation
        mutation(teams, selected_teams[i], selected_teams[i + 1])


if __name__ == "__main__":
    # input: 8 teams (40 players), 8 teams selected to evolution in each iteration
    teams = make_gamers_matrix(path_stats='data/player_stats.csv', path_teams='data/teams.csv')
    n = 1000
    k = 4
    selection = ranking_selection
    cross = mask_cross
    mutation = try_permutation
    teams_cost = []
    best_cost = float("inf")
    res = teams.copy()
    for i in range(n):
        make_evolution(teams, k, selection, cross, mutation)
        teams_cost.append(sum(calculate_teams_cost(teams)))
        if best_cost > sum(calculate_teams_cost(teams)):
            res = teams.copy()
            best_cost = sum(calculate_teams_cost(teams))
        # print(i, sum(calculate_teams_cost(teams)))

    plt.plot(teams_cost, linestyle='-')
    plt.title('Koszt zespołów')
    plt.xlabel('Numer iteracji')
    plt.ylabel('Koszt')
    plt.grid(True)
    # plt.show()
    print(res)
    print(best_cost)
    plt.show()
