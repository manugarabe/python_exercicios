valor_emprestimo = float(input('Insira o valor do empréstimo: '))
valor_salario = float(input('Insira o valor do salário: '))

if valor_emprestimo > valor_salario * 0.20:
    print('Empréstimo não será concedido.')
else:
    print('Empréstimo concedido.')