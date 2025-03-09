import math
custo = float(input('Custo do espetáculo teatral: '))
preco_convite = float(input('Preço do convite: '))
n_convite = custo/preco_convite
n_convite2 = custo/preco_convite * 1.23 
print('Número de convites para alcançar o custo do espetáculo: ', math.floor(n_convite))
print('Número de convites para alcançar 23% de lucro: ', math.floor(n_convite2))