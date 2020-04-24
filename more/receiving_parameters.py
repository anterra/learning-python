def powersum(power, *args):
    """Return the sum of each argument raised to the specified power."""
    total = 0
    for i in args:
        total += pow(i, power)
    return total

print(powersum(2, 3, 4))
print(powersum(2, 10))

#using * or ** prefix allowes you to receive a variable number of parameters to a tuple or dictionary, respectively
