allNum = []
while True:
    numbers = str(input())
    split = numbers.split()
    inInt = list(map(int, split))
    if inInt[0] <= 0 or inInt[1] <= 0:
        break
    allNum.append(inInt)

def sum_btn_numbrs(n1, n2):
    summ = 0
    for i in range(n2, n1 + 1):
        summ += i
        print(i, end=' ')
    print('Sum={} '.format(summ))

for i in range(len(allNum)):
    num1 = allNum[i][0]
    num2 = allNum[i][1]
    sum_btn_numbrs(num1, num2)
