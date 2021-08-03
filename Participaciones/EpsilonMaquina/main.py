eps = 1.0
while eps + 1 > 1:
    eps /= 2
eps *= 2
print("The machine epsilon is:", eps)
