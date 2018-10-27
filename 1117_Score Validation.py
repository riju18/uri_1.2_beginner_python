count = 0
allmarks = []
summ = 0
count1 = 0

while True:
    marks = float(input())
    if marks < 0 or marks > 10:
        print('nota invalida')
    if marks >= 0 and marks <= 10:
        allmarks.append(marks)
        count += 1 
    if count == 2:
        break
for i in allmarks:
    summ += i
    count1 += 1
    
print('media = {0:.2f} '.format(summ / count1))
