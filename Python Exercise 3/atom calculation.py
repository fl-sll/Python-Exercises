def num_atoms(mass, weight=196.97):
    atoms = mass / weight
    return atoms * (6.022 * (10 ** 23))

x = num_atoms(10)
print(x)

x = num_atoms(10, 12.001)
print(x)

x = num_atoms(10, 1.008)
print(x)
