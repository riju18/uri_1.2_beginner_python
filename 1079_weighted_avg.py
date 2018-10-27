import numpy as np

number = int(input('test case number: '))
nums = []

print('enter 3 numbers: ')

for i in range(number):
    values = str(input())
    split = values.split()
    inInt = list(map(float, split))
    nums.append(inInt)

for i in range(len(nums)):
    num1 = nums[i][0]
    num2 = nums[i][1]
    num3 = nums[i][2]
    print(round(((num1 / 10) * 2) + ((num2 / 10) * 3) + ((num3 / 10) * 5), 1))
    

# print(np.array(nums).flatten())  # matrix to 1D array
