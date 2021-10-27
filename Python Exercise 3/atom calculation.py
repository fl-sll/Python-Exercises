def num_atoms(mass, weight=196.97):
    atoms = mass / weight #number of atoms
    return atoms * (6.022 * (10 ** 23)) #number of moles

x = num_atoms(10)
print(x)

x = num_atoms(10, 12.001)
print(x)

x = num_atoms(10, 1.008)
print(x)
