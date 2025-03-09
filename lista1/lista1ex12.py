nome = input(('Insira o nome:'))
hora = float(input('Insira o número de horas trabalhadas: '))
dep = int(input('Insira o número de dependentes: '))
salario = 12*hora + 40*dep
inss = 0.085*salario
ir = 0.05*salario
sl = salario - (inss + ir)
print('Nome:', nome)
print('Salário bruto:', salario)
print('INSS e IR:', inss, ir)
print('Salário líquido:', sl)