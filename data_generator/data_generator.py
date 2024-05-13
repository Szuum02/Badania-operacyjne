import numpy as np
import random
import csv

n = 40
stats = [dict() for _ in range(n)]
for i in range(n):
    position_preferences = np.random.dirichlet(np.ones(5), size=1)
    mmr = random.randint(0, 3000)
    player_stats = {"player_id": i + 1, "mmr": mmr}
    for j, preference in enumerate(position_preferences[0]):
        player_stats.update({"pos" + str(j + 1): preference})
    stats[i] = player_stats

fields = ["player_id", "mmr", "pos1", "pos2", "pos3", "pos4", "pos5"]
filename = "../data/player_stats.csv"

with open(filename, 'w') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=fields)
    writer.writeheader()
    writer.writerows(stats)
