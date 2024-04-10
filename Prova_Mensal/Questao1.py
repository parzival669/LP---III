def pi ():
    den = -1
    pi = 0
    for i in range (100000):
        den += 2 
        pi += 4 / den
        ##print (f'{pi} : pi')
        den += 2
        pi -= 4/den
        ##print (f'{pi} : pi')

    return pi


if __name__ == '__main__':
    
    pi = pi()
    print (pi)