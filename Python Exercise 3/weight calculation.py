def calc_weight_on_planet(weight, gravity = 23.1):
    mass = weight/9.8

    return mass * gravity

x = calc_weight_on_planet(120,9.8)
print(x)

x = calc_weight_on_planet(120)
print(x)

x = calc_weight_on_planet(120,23.1)
print(x)
