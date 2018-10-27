allQuardents = []

while True:
    quardents = str(input())
    split = quardents.split()
    inInt = list(map(int, split))
    if inInt[0] == 0 or inInt[1] == 0:
        break
    allQuardents.append(inInt)    

def check_quardent(q1, q2):
        if q1 > 0 and q2 > 0:
            print('primeiro')
        elif q1 > 0 and q2 < 0:
            print('quarto')
        elif q1 < 0 and q2 < 0:
            print('terceiro')
        elif q1 < 0 and q2 > 0:
            print('segundo')

for i in range(len(allQuardents)):
    q1 = allQuardents[i][0]
    q2 = allQuardents[i][1]
    check_quardent(q1, q2)
    
