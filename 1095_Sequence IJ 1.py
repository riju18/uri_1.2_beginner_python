def seq(x, y):
    while not y < 0:
        print('I={} J={}'.format(x,y))
        if y == 0:
            break
        x += 3
        y -= 5            
seq(1, 60)
