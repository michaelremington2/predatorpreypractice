#!/usr/bin/python
import json

data = {}
data['sim'] = []
data['sim'].append({
    "days_of_sim": 365,
    "landscape_size_x": 100,
    "landscape_size_y": 80,
    "microhabitat_open_bush_proportions": [0.5,0.5],
    "initial_snake_pop": 15,
    "initial_krat_pop": 100,
    "cell_energy_pool": 2200,
    "snake_initial_energy": 120,
    "krat_initial_energy": 30,
    "snake_energy_cost": 1,
    "krat_energy_cost": 1,
    "strike_success_probability": 0.1,
    "krat_energy_gain": 0.0015})

with open('data.txt', 'w') as outfile:
    json.dump(data, outfile)