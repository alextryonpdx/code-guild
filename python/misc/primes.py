def prime(n):
    for n in range(2, (n - 1)):
        z = True
        for x in range(2, (n - 1)):
            if n % x == 0:
                z = False
        if z == True:
            print n


prime(30)

