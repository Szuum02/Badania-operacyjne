def make_evolution(teams, k, selection, cross, mutation):
    # take k teams to selection
    selected_teams = selection(teams, k)
    for i in range(0, len(selected_teams) - 1, 2):
        # make crossbreeding
        cross(selected_teams[i], selected_teams[i+1])

        # make mutation
        mutation(teams, selected_teams[i], selected_teams[i+1])
