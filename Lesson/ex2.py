# orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]


# max_orbit = max([i[0] * i[1] for i in orbits if i[0] != i[1]])
# print(*[i for i in orbits if max_orbit == i[0] * i[1]])

def find_farthest_orbit():
    dict_orbits = {val[0] * val[1]: val for val in orbits if val[0] != val[1]}
    return max(dict_orbits.items())[1]


orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]

print(*find_farthest_orbit())
