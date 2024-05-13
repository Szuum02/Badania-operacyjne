import sys

sys.path.append("genetic")
sys.path.append("selections")


from target_function import *
from selections import *
from crossbreeding import *
from mutation import *



def make_evolution(teams, k, selection, cross, mutation):
    # take k teams to selection
    selected_teams = selection(teams, k)
    for i in range(0, len(selected_teams) - 1, 2):
        # make crossbreeding
        cross(selected_teams[i], selected_teams[i+1])

        # make mutation
        mutation(teams, selected_teams[i], selected_teams[i+1])


gamers_matrix = make_gamers_matrix()

for i in range(1000):
    make_evolution(gamers_matrix,2,ranking_selection,lowest_pref_cross,lucky_mutation)



# res = calculate_teams_cost(gamers_matrix)