import numpy as np

def get_weights(teams, cost_function):
    teams_cost = np.array([cost_function(team) for team in teams])
    total_cost = np.sum(teams_cost)
    return teams_cost / total_cost


# k - ilość drużyn do selekcji
def roulette_wheel(teams, cost_function, k):
    weights = get_weights(teams, cost_function)
    teams_idx = np.arange(len(teams))
    selected_teams = np.random.choice(teams_idx, size=k, replace=False, p=weights)
    return [teams[idx] for idx in selected_teams]


def ranking_selection(teams, cost_function, k):
    teams = sorted(teams, key=lambda team: cost_function(team), reverse=True)
    return teams[:k]
