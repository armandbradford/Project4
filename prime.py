def is_prime(x):

    prime = True
    if x < 2:
        prime = False
    else:
        for n in range(2, x):
            if x % n == 0:
                prime = False
                break
            else:
                prime = True
    return prime

print(is_prime(6))
