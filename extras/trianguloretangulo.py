print('Descubra se é um triângulo retângulo!')
b = int(input('Insira o valor do primeiro cateto: '))
c = int(input('Insira o valor do segundo cateto: '))
a = int(input('Insira o valor da hipotenusa: '))
calculo = b**2 + c**2
if calculo == a**2:
 print('É um triângulo retângulo')
else:
 print('Não é um triângulo retângulo')