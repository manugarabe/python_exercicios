preco = int(input("Insira o preço do produto: "))

notas100 = 0
notas50 = 0
notas20 = 0
notas10 = 0
notas5 = 0
notas2 = 0
notas1 = 0

if preco >= 100:
    notas100 = preco // 100
    preco = preco % 100

if preco >= 50:
    notas50 = preco // 50
    preco = preco % 50

if preco >= 20:
    notas20 = preco // 20
    preco = preco % 20

if preco >= 10:
    notas10 = preco // 10
    preco = preco % 10

if preco >= 5:
    notas5 = preco // 5
    preco = preco % 5

if preco >= 2:
    notas2 = preco // 2
    preco = preco % 2

if preco >= 1:
    notas1 = preco // 1
    preco = preco % 1

print("Notas de 100:", notas100)
print("Notas de 50:", notas50)
print("Notas de 20:", notas20)
print("Notas de 10:", notas10)
print("Notas de 5:", notas5)
print("Notas de 2:", notas2)
print("Notas de 1:", notas1)