testcase = int(input('total testcase: '))
print('input all animal sample: ')
allcases = []
c = []
r = []
s = []
for i in range(testcase):
    allExperiments = str(input())
    split = allExperiments.split(' ')
    allcases.append(split)

for i in range(len(allcases)):
    animal = allcases[i][1]
    if animal == 'C':
        c.append(allcases[i][0])
    elif animal == 'R':
        r.append(allcases[i][0])
    elif animal == 'S':
        s.append(allcases[i][0])

c = list(map(int, c))
r = list(map(int, r))
s = list(map(int, s))

total = sum(c) + sum(r) + sum(s)

print('Total: {} cobaias'.format(total))
print('Total de coelhos: {}'.format(sum(c)))
print('Total de ratos: {}'.format(sum(r)))
print('Total de sapos: {}'.format(sum(s)))

print('Percentual de coelhos:{0:.2f} %'.format(total / sum(c)))
print('Percentual de ratos:{0:.2f} %'.format(total / sum(r)))
print('Percentual de sapos:{0:.2f} %'.format(total / sum(s)))
