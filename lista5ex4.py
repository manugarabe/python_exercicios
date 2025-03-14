alt = float(input('Insira a altura: '))
sexo = input('Insira o sexo, sendo m para masculino e f para feminino: ')

m = (72.7 * alt) - 58
f = (62.1 * alt) - 44.7

if m:
    print('O peso ideal é:', m)
else:
    print('O peso ideal é:', f)