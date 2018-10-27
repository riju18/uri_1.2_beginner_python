def get_input():
    inp = float(input())
    if inp > 10 or inp < 0:
        print("nota invalida")
        return get_input()
    else:
        return inp


def calculate():
    a = get_input()
    b = get_input()
    return (a + b)/2


def redo():
    X = float(input())
    if X < 1 or X > 2:
        print("novo calculo (1-sim 2-nao)")
        redo()
    elif int(X) == 2:
        return False
    elif int(X) == 1:
        print("novo calculo (1-sim 2-nao)")
        return True


while True:
    print("media = {0:.2f}".format(calculate()))
    x = redo()
    if not x:
        break
