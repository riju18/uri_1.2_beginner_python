# salary = float(input('input salary: '))
salary = float(input())
salaryRound = float("{0:.2f}".format(salary))
if salaryRound >= 0.00 and salaryRound <= 400.00:
    Reajuste_ganho = (salaryRound * 15) / 100
    Novo_salario = Reajuste_ganho + salaryRound
    Em_percentual = 15
    print('Novo salario: {0:.2f}'.format(Novo_salario))
    print('Reajuste ganho: {0:.2f}'.format(Reajuste_ganho))
    print('Em percentual: {} %'.format(Em_percentual))
elif salaryRound >= 400.01 and salaryRound <= 800:
    Reajuste_ganho = (salaryRound * 12) / 100
    Novo_salario = Reajuste_ganho + salaryRound
    Em_percentual = 12
    print('Novo salario: {0:.2f}'.format(Novo_salario))
    print('Reajuste ganho: {0:.2f}'.format(Reajuste_ganho))
    print('Em percentual: {} %'.format(Em_percentual))
elif 800.01 <= salaryRound <= 1200:
    Reajuste_ganho = (salaryRound * 10) / 100
    Novo_salario = Reajuste_ganho + salaryRound
    Em_percentual = 10
    print('Novo salario: {0:.2f}'.format(Novo_salario))
    print('Reajuste ganho: {0:.2f}'.format(Reajuste_ganho))
    print('Em percentual: {} %'.format(Em_percentual))
elif salaryRound >= 1200.01 and salaryRound <= 2000:
    Reajuste_ganho = (salaryRound * 7) / 100
    Novo_salario = Reajuste_ganho + salaryRound
    Em_percentual = 7
    print('Novo salario: {0:.2f}'.format(Novo_salario))
    print('Reajuste ganho: {0:.2f}'.format(Reajuste_ganho))
    print('Em percentual: {} %'.format(Em_percentual))
elif salaryRound > 2000:
    Reajuste_ganho = (salaryRound * 4) / 100
    Novo_salario = Reajuste_ganho + salaryRound
    Em_percentual = 4
    print('Novo salario: {0:.2f}'.format(Novo_salario))
    print('Reajuste ganho: {0:.2f}'.format(Reajuste_ganho))
    print('Em percentual: {} %'.format(Em_percentual))

