import random

import numpy as np
from itertools import product

from genetic.target_function import make_gamers_matrix, calculate_teams_cost
from genetic.selections import roulette_wheel, ranking_selection
from genetic.crossbreeding import lowest_pref_cross, mask_cross
from genetic.mutation import try_permutation, lucky_mutation
import matplotlib.pyplot as plt


def make_evolution(teams, k, selection, cross, mutation, a, b):
    # take k teams to selection
    selected_teams = selection(teams, k)
    for i in range(0, len(selected_teams) - 1, 2):
        # make crossbreeding
        cross(selected_teams[i], selected_teams[i + 1])

        # make mutation
        mutation(teams, selected_teams[i], selected_teams[i + 1], a, b)

def run_test(n):
    k_parameters=[2,5,10,25,50]
    for k in k_parameters:
        title=f"k{k}test"
        test_unit(n,k,0.001,1,title)

    title=f"a=0test"
    test_unit(n,25,0,1,title)

    title=f"b=0test"
    test_unit(n,25,0.001,0,title)

    compare_methods(n, 25, 0.001, 1)

def test_unit(n, k, a, b, title, num_of_tests=8):
    selection = ranking_selection
    cross = mask_cross
    mutation = try_permutation
    teams_graphs=[]
    legend_names = [f"Test {i+1}" for i in range(num_of_tests)]
    for j in range(num_of_tests):
        teams = make_gamers_matrix(
        path_stats='data/player_stats.csv', path_teams='data/teams.csv')
        teams_cost = []
        for i in range(n):
            make_evolution(teams, k, selection, cross, mutation, a, b)
            teams_cost.append(sum(calculate_teams_cost(teams, a, b)))
        teams_graphs.append(teams_cost)

    save_graph(title, teams_graphs, legend_names, k, a, b)

def compare_methods(n, k, a, b):
    selections = [roulette_wheel, ranking_selection]
    crossbreeding = [lowest_pref_cross, mask_cross]
    mutations = [try_permutation, lucky_mutation]
    teams_graphs=[]
    legend_names = [f"Test {i+1}" for i in range(8)]
    for selection, cross, mutation in product(selections, crossbreeding, mutations):
        teams = make_gamers_matrix(
            path_stats='data/player_stats.csv', path_teams='data/teams.csv')
        teams_cost = []
        for i in range(n):
            make_evolution(teams, k, selection, cross, mutation, a, b)
            teams_cost.append(sum(calculate_teams_cost(teams, a, b)))
        teams_graphs.append(teams_cost)

    save_graph("comparison", teams_graphs, legend_names, k, a, b)

def save_graph(title, teams_graphs, legend_names, k, a, b):
    for i, team_data in enumerate(teams_graphs, start=1):
        plt.plot(team_data, linestyle='-', label=legend_names[i - 1])
    title_graph = f'Wartość funkcji kosztu od iteracji dla różnych metod [k={k}][a={a}][b={b}]'
    plt.title(title_graph)
    plt.xlabel('Numer iteracji')
    plt.ylabel('Koszt')
    plt.grid(True)
    plt.legend(legend_names)
    plt.savefig(f"graphs/{title}.jpg")
    plt.clf()
    print(f"Saved graph {title}")

def run_algorithm(teams,n,k,a,b):
    selection = ranking_selection
    cross = mask_cross
    mutation = try_permutation
    best_cost = float("inf")
    res = teams.copy()
    for i in range(n):
        make_evolution(teams, k, selection, cross, mutation, a, b)
        if best_cost > sum(calculate_teams_cost(teams, a, b)):
            res = teams.copy()
            best_cost = sum(calculate_teams_cost(teams, a, b))
        with open("results/results.txt", "w") as outfile:
            outfile.write(f"COST FUNCTION: {best_cost} \n")
            for i,team in enumerate(res,start=1):
                outfile.write(str(str(i)+":").rjust(5))
                for player in team:
                    outfile.write(str(player[0]).rjust(4))
                outfile.write("\n")

if __name__ == "__main__":
    teams = make_gamers_matrix(
        path_stats='data/player_stats.csv', path_teams='data/teams.csv')
    plt.figure(figsize=(10, 6))
    # run_algorithm(teams,100,10,0.001,1) # running clear algorithm
    run_test(700) # running tests

    

