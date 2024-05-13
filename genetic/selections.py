import numpy as np
from target_fun import calculate_target_function, make_gamers_matrix
from crossbreeding import lowest_pref_cross, mask_cross


def get_weights(teams, cost_function, a, b):
    teams_cost = np.array([cost_function(team, a, b) for team in teams])
    total_cost = np.sum(teams_cost)
    return teams_cost / total_cost


# k - ilość drużyn do selekcji
def roulette_wheel(teams, k, cost_function=calculate_target_function, a=1, b=1):
    weights = get_weights(teams, cost_function, a, b)
    teams_idx = np.arange(len(teams))
    selected_teams = np.random.choice(
        teams_idx, size=k, replace=False, p=weights)
    return [teams[idx] for idx in selected_teams]


def ranking_selection(teams, k, cost_function=calculate_target_function, a=1, b=1):
    teams = sorted(teams, key=lambda team: cost_function(
        team, a, b), reverse=True)
    return teams[:k]


# if __name__ == '__main__':
#     gamers_matrix = make_gamers_matrix()
#     k = 2
#     print("SELECTED TEAMS\n")

#     roulette_teams = roulette_wheel(gamers_matrix, k)
#     print("Roulette wheel:")
#     print(*roulette_teams, sep="\n")

#     # ranking_teams = ranking_selection(gamers_matrix, k)
#     # print("\nRanking selection:")
#     # print(*ranking_teams, sep="\n")

#     lowest_pref_cross(roulette_teams[0], roulette_teams[1])

#     print("Roulette wheel after crossbreeding:")
#     print(*roulette_teams, sep="\n")