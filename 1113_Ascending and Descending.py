allNum = []
while True:
    numbers = str(input())
    split = numbers.split()
    inInt = list(map(int, split))
    if inInt[0] == inInt[1]:
        break
    allNum.append(inInt)

def check(i):
    if sorted(i) == i:
        print('Crescente')
    elif sorted(i) != i:
        print('Decrescente')

for i in range(len(allNum)):
    check(allNum[i])
