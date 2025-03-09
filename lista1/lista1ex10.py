nome = input('Insira o nome do funcionário: ')
idade = int(input('Insira a idade do funcionário: '))
cargo = input('Insira o cargo do funcionário: ')
sb = float(input('Insira o salário bruto: '))
rsb = sb + (sb*0.38)
grat = 0.2*rsb
sl = (rsb + grat)*0.85
print('Nome: ', nome, ', Idade: ', idade, ', Cargo: ', cargo)
print('Salário bruto: ', rsb)
print('Salário líquido: ', sl)