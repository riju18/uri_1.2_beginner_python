def ij(i):
    for j in range(7, 4, -1):
        print('I={} J={}'.format(i, j))

def repitation(i):
    while i <= 9:
        ij(i)
        i += 2

repitation(1)
