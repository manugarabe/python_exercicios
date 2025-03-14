preco = float(input('Insira o preço do carro: '))
ano = int(input('Insira o ano do carro: '))

if ano < 1990:
    taxa = 0.01 * preco
    print(f'O imposto a ser pago é: {taxa:,.2f}')
else:
    taxa = 0.015 * preco
    print(f'O imposto a ser pago é: {taxa:,.2f}')