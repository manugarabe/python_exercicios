peso = float(input('Insira o peso: '))
altura = float(input('Insira a altura: '))

imc = peso/(altura*altura)

print(f'O IMC é: {imc:,.2f}')