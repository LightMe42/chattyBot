def closest_higher_mod_5(x):
    if x % 5 == 0:
        return x
    y = x + 1
    while y % 5 != 0:
        y += 1
    return y
closest_higher_mod_5(5, 3)
