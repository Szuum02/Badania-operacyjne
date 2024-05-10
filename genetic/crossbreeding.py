import random

import numpy as np


def get_min(team):
    min_1 = 1
    min_1_id = 0
    for i, x in enumerate(team):
        if min_1 > team[i][i + 2]:
            min_1 = min(min_1, team[i][i + 2])
            min_1_id = i
    return min_1_id


def get_mask():
    return [random.randint(0, 1) for _ in range(5)]


def lowest_pref_cross(team_1, team_2):
    # get position with lowest desire
    min_1_id = get_min(team_1)
    min_2_id = get_min(team_2)

    # swap them
    temp = team_1[min_1_id]
    team_1[min_1_id] = team_2[min_2_id]
    team_2[min_2_id] = temp


def mask_cross(team_1, team_2):
    mask = get_mask()
    for i in range(len(team_1)):
        if mask[i] == 1:
            team_1[i], team_2[i] = team_2[i], team_1[i]
