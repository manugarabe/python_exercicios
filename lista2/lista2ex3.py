nome = input('Insira o nome completo: ')
cdd = input('Insira a cidade natal: ')
ano = int(input('Insira o ano de ingresso no curso: '))

print(nome, 'é natural de', cdd, 'e ingressou no curso em', ano) #primeiraopção

info = ('{} é natural de {} e ingressou no curso em {}'.format(nome, cdd, ano))
print(info)