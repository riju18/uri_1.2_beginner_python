testCase = int(input('test case: '))
print('enter numbers one by one: ')
allNum = []
for i in range(testCase):
    nums = int(input())
    allNum.append(nums)


print(max(allNum))
print(allNum.index(max(allNum)))
