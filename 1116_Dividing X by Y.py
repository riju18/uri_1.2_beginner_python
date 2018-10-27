testcase = int(input())
for i in range(testcase):
    numbers = str(input())
    split = numbers.split()
    inInt = list(map(int, split))
    if inInt[1] == 0:
        print('divisao impossivel')
    else:
        x = inInt[0]
        y = inInt[1]
        result = x / y
        print('{0:.1f}'.format(result))    
