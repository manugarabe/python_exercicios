v1 = int(input('Insira o primeiro valor: '))
v2 = int(input('Insira o segundo valor: '))

div1 = v1 / v2
div2 = v1 // v2

print(f'A divisão do valor 1 pelo valor 2 é: {div1:,.2f}')
print('A divisão truncada do valor 1 pelo valor 2 é:', div2)