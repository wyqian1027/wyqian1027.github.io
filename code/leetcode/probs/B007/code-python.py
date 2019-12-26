# For example, given that,
# def BiasedRand():
#    return 1 if random.random() > 0.7 else 0

def UnBiasedRand():
    x = BiasedRand()
    y = BiasedRand()
    if x == y:
        return UnBiasedRand()
    else:
        return x
