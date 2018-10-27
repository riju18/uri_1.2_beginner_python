testcase = int(input('number of testcase: '))
allIntNumbers = []
for i in range(testcase):
    numbers = str(input())
    split = numbers.split()
    inInt = list(map(int, split))
    allIntNumbers.append(inInt)

print('total odds between these numbers:')

def allOdd(n1, n2):
    odds = 0
    if n1 < n2:
        for i in range(n1 + 1, n2):
            if i % 2 != 0:
                odds += i
        print(odds)
    elif n1 == n2:
        for i in range(n1 + 1, n2):
            if i % 2 != 0:
                odds += i
        print(odds)
    elif n1 > n2:
        for i in range(n2 + 1, n1):
            if i % 2 != 0:
                odds += i
        print(odds)

for i in range(len(allIntNumbers)):
    num1 = allIntNumbers[i][0]
    num2 = allIntNumbers[i][1]
    allOdd(num1, num2)
