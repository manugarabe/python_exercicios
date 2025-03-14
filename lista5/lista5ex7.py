estado = input('Insira o estado: ')
valor = float(input('Insira o valor: '))

mg = (valor * 0.07) + valor
sp = (valor * 0.12) + valor
rj = (valor * 0.15) + valor
ms = (valor * 0.08) + valor

if estado == 'mg':
    print(f'o preço final é de: {mg:,.2f}')
elif estado == 'sp':
    print(f'O preço final é de: {sp:,.2f}')
elif estado == 'rj':
    print(f'O preço final é de: {rj:,.2f}')
elif estado == 'ms':
    print(f'O preço final é de: {ms:,.2f}')
else:
    print('Erro')