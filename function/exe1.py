def absolute(x):
    if x > 0:
        return x
    elif x < 0:
        return -x

abs = absolute(-5)
print(abs)
abs = absolute(5)
print(abs)