def good(guess, x):
    dis = abs(guess**2 - x)
    acu = 1e-5
    if dis <= acu:
        return guess
    else:
        return 0

def better(guess, x):
    return ((guess + x/guess) / 2)

def test(guess, x):
    if good(guess, x):
        return good(guess, x)
    else:
        return test(better(guess, x), x)

def sqrt(x):
    return test(10, x)

print(sqrt(876))